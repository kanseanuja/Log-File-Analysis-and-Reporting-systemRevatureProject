
# Log File Analysis & Reporting System

## 📌 Project Overview
The **Log File Analysis & Reporting System** is a Python-based CLI application designed to parse web server log files, store them in a database, and generate analytical reports with visualizations.  
It helps in identifying **top visitors, error patterns, peak traffic hours, and OS usage** for website performance monitoring and debugging.

---

## 🎯 Features
- **Log Parsing**: Extracts IP, timestamp, request method, URL, status codes, referrer, and OS.
- **Database Storage**: Saves parsed logs into a **MySQL/MariaDB** database.
- **Analytical Reports**:
  - Top N IP addresses visiting the site.
  - HTTP error type distribution.
  - Peak visiting hours.
  - Operating system usage statistics.
- **Visualization**: Generates **pie charts** for reports using Matplotlib.
- **Command-Line Interface (CLI)** for easy interaction.

---

## 🛠️ Tech Stack
- **Language**: Python 3.11+
- **Database**: MySQL / MariaDB
- **Libraries**:
  - `mysql-connector-python`
  - `tabulate`
  - `matplotlib`
  - `re` & `datetime` (for parsing)
- **OS**: Cross-platform (Windows, Linux, macOS)

---

## 📂 Project Structure
Project_Revature/
│
├── main.py # Entry point, CLI handling
├── log_parser.py # Parses log lines using regex
├── mysql_handler.py # Handles database connection & queries
├── create_tables.sql # SQL schema for 'logs' table
├── config.ini # Database configuration
├── requirements.txt # Python dependencies
├── sample_logs/ # Sample log files for testing
└── README.md # Documentation

yaml
Copy
Edit

---

## ⚙️ Installation & Setup

### 1️⃣ Install Python & MySQL
- Install **Python 3.11+**
- Install **MySQL/MariaDB** and note down host, user, password, and port.

### 2️⃣ Clone the Project
     clone this project here
cd Log-File-Analysis

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Database
Edit config.ini:
[mysql]
host = localhost
user = root
password = your_password
database = weblogs_db
port = 3307

5️⃣ Create Database
CREATE DATABASE weblogs_db;

🚀 Usage
Process Logs & Store in DB
python main.py process_logs sample_logs/access.log
Generate Reports
Top N IP Addresses
python main.py generate_report top_n_ips --n 5
HTTP Error Types
python main.py generate_report error_types
Peak Visiting Hours
python main.py generate_report peak_hours
Operating System Usage
python main.py generate_report os_usage

📊 Sample Output
CLI Output Example
+---------------+---------+
| IP Address    | Count   |
+---------------+---------+
| 192.168.0.10  | 150     |
| 10.0.0.5      | 120     |
| 172.16.5.2    | 110     |
+---------------+---------+
Pie Chart Example
Displays graphical representation of the report for better understanding.

🔮 Future Enhancements
Support for multiple log formats (Apache, Nginx).

Export reports to PDF/CSV.

Real-time log monitoring.

Web-based dashboard interface.

👨‍💻 Author
Anuja Kanse
Intern - Web Development | Revature Project
