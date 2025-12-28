from collections import defaultdict

def detect(events, threshold=5):
	counter = defaultdict(int)

	for event in events:
		if event["event"] == "FAILED_LOGIN":
			counter[event["ip"]] += 1

	alerts = []
	for ip, count in counter.items():
		if count >= threshold:
			alerts.append({
				"type": "SSH_BRUTE_FORCE",
				"ip": ip,
				"count": count,
				"severity": "HIGH"
				})

	return alerts
