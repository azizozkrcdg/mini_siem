import json

def save_alerts(alerts, file_path="reports/alerts.json"):
	with open(file_path, "w") as f:
		json.dump(alerts, f, indent=4)

def print_alerts(alerts):
	for alert in alerts:
		print(f"🚨 [{alert['severity']}] {alert['type']} - IP: {alert['ip']} ({alert['count']} deneme)")

