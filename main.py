import argparse
import configparser
from log_parser import LogParser
from mysql_handler import MySQLHandler
from tabulate import tabulate
import matplotlib.pyplot as plt

def plot_pie_chart(data, labels, title):
    counts = [item[1] for item in data]
    labels = [item[0] for item in data]
    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')
    plt.show()

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    #  Extract each value explicitly and convert port to int
    db_config = {
        'host': config['mysql']['host'],
        'user': config['mysql']['user'],
        'password': config['mysql']['password'],
        'database': config['mysql']['database'],
        'port': int(config['mysql']['port'])  # Important fix
    }

    db = MySQLHandler(db_config)
    db.create_tables()

    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='command')

    p = sub.add_parser('process_logs')
    p.add_argument('file_path')

    r = sub.add_parser('generate_report')
    r.add_argument('report_type')
    r.add_argument('--n', type=int, help='Top N IPs')

    args = parser.parse_args()

    if args.command == 'process_logs':
        parser = LogParser()
        with open(args.file_path, 'r', encoding='utf-8', errors='ignore') as f:

            for line in f:
                data = parser.parse_line(line)
                if data:
                    db.insert_log_entry(data)
        print("Log file processed and saved to DB.")

    elif args.command == 'generate_report':
        if args.report_type == 'top_n_ips':
            results = db.get_top_n_ips(args.n or 5)
            print(tabulate(results, headers=["IP Address", "Count"], tablefmt="grid"))
            plot_pie_chart(results, [row[0] for row in results], "Top IP Addresses")

        elif args.report_type == 'error_types':
            results = db.get_error_types()
            print(tabulate(results, headers=["Error Code", "Count"], tablefmt="grid"))
            plot_pie_chart(results, [str(row[0]) for row in results], "HTTP Error Types")

        elif args.report_type == 'peak_hours':
            results = db.get_peak_hours()
            print(tabulate(results, headers=["Hour", "Count"], tablefmt="grid"))
            plot_pie_chart(results, [f"{row[0]}h" for row in results], "Peak Visiting Hours")

        elif args.report_type == 'os_usage':
            results = db.get_os_usage()
            print(tabulate(results, headers=["Operating System", "Count"], tablefmt="grid"))
            plot_pie_chart(results, [row[0] for row in results], "Operating Systems Used")

        else:
            print("Invalid report_type. Try: top_n_ips, error_types, peak_hours, os_usage")

    db.close()

if __name__ == "__main__":
    main()