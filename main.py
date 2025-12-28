import time
from core.journal_reader import read_ssh_logs
from core.parser import parse_auth_log
from detectors.ssh_bruteforce import detect
from core.alert import print_alerts, save_alerts
from core.state import AlertState

INTERVAL = 5
TIME_WINDOW = 5
THRESHOLD = 5
COOLDOWN = 150  
state = AlertState(cooldown_seconds=COOLDOWN)

print("🛡️ Mini-SIEM başlatıldı (Ctrl+C ile durdur)")

try:
    while True:
        log_lines = read_ssh_logs(minutes=TIME_WINDOW)

        events = []
        for line in log_lines:
            parsed = parse_auth_log(line)
            if parsed:
                events.append(parsed)

        alerts = detect(events, threshold=THRESHOLD)

        final_alerts = []
        for alert in alerts:
            if state.should_alert(alert["ip"]):
                final_alerts.append(alert)

        if final_alerts:
            print_alerts(final_alerts)
            save_alerts(final_alerts)
        else:
            print("✅ Güvenlik olayı tespit edilmedi veya cooldown aktif.")

        print("-" * 50)
        time.sleep(INTERVAL)

except KeyboardInterrupt:
    print("\n🛑 Mini-SIEM durduruldu.")
