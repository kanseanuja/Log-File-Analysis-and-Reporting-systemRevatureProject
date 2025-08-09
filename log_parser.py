import re
from datetime import datetime

class LogParser:
    LOG_PATTERN = re.compile(
        r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d{3}) (\d+|-) "(.*?)" "(.*?)"'
    )

    def parse_line(self, line):
        match = self.LOG_PATTERN.match(line)
        if match:
            ip, timestamp, request, status, bytes_sent, referrer, user_agent = match.groups()

            # Split request into method, path, protocol
            parts = request.split()
            method = parts[0] if len(parts) > 0 else None
            path = parts[1] if len(parts) > 1 else None
            protocol = parts[2] if len(parts) > 2 else None

            # Detect OS from user agent
            os_name = self.extract_os(user_agent) if user_agent else None

            # Return tuple with exactly 10 values
            return (
                ip,
                datetime.strptime(timestamp, '%d/%b/%Y:%H:%M:%S %z'),
                method,
                path,
                protocol,
                int(status),
                int(bytes_sent) if bytes_sent.isdigit() else 0,
                None if referrer == "-" else referrer,
                user_agent,
                os_name
            )
        return None

    def extract_os(self, user_agent):
        ua = user_agent.lower()
        if 'windows' in ua:
            return 'Windows'
        elif 'mac' in ua:
            return 'MacOS'
        elif 'linux' in ua:
            return 'Linux'
        elif 'android' in ua:
            return 'Android'
        elif 'iphone' in ua or 'ios' in ua:
            return 'iOS'
        return 'Other'
