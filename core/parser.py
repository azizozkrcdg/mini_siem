import re

def parse_auth_log(line):
    if "Failed password" in line:
        match = re.search(
            r'(?P<time>\w+ \d+ \d+:\d+:\d+).*Failed password for (?P<user>\w+) from (?P<ip>\d+\.\d+\.\d+\.\d+)',
            line
        )
        if match:
            return {
                "timestamp": match.group("time"),
                "event": "FAILED_LOGIN",
                "user": match.group("user"),
                "ip": match.group("ip")
            }
    return None
