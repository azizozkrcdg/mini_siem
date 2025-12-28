import time

class AlertState:
	def __init__(self, cooldown_seconds=150):
		self.cooldown = cooldown_seconds
		self.last_alert = {}

	def should_alert(self, ip):
		now = time.time()

		if ip not in self.last_alert:
			self.last_alert[ip] = now
			return True

		if now - self.last_alert[ip] > self.cooldown:
			self.last_alert[ip] = now
			return True

		return False
