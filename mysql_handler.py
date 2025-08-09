import mysql.connector

class MySQLHandler:
    def __init__(self, config):
        self.conn = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config.get('password', '') or None,
            database=config['database'],
            port=int(config.get('port', 3307)),
            charset='utf8mb4'  
        )
       
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                ip VARCHAR(45),
                timestamp DATETIME,
                method VARCHAR(10),
                url TEXT,
                protocol VARCHAR(10),
                status_code INT,
                size INT,
                referrer TEXT,
                user_agent TEXT,
                os VARCHAR(50)
            )
        """)
        self.conn.commit()

    def insert_log_entry(self, entry):
      sql = """
        INSERT INTO logs 
        (ip, timestamp, method, url, protocol, status_code, size, referrer, user_agent, os)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
       """
      if not isinstance(entry, tuple):
        entry = tuple(entry)

    # Debugging print
      if len(entry) != 10:
         print(f"[ERROR] Invalid entry length: {len(entry)} | Entry: {entry}")
         return  
      self.cursor.execute(sql, entry)
      self.conn.commit()
 


    def get_top_n_ips(self, n):
        self.cursor.execute("""
            SELECT ip, COUNT(*) as count FROM logs
            GROUP BY ip ORDER BY count DESC LIMIT %s
        """, (n,))
        return self.cursor.fetchall()

    def get_error_types(self):
        self.cursor.execute("""
            SELECT status_code, COUNT(*) FROM logs
            WHERE status_code >= 400
            GROUP BY status_code
        """)
        return self.cursor.fetchall()

    def get_peak_hours(self):
        self.cursor.execute("""
            SELECT HOUR(timestamp), COUNT(*) FROM logs
            GROUP BY HOUR(timestamp)
            ORDER BY COUNT(*) DESC
        """)
        return self.cursor.fetchall()

    def get_os_usage(self):
        self.cursor.execute("""
            SELECT os, COUNT(*) FROM logs
            GROUP BY os ORDER BY COUNT(*) DESC
        """)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
