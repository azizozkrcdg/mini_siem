def read_log(file_path):
	with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
		return f.readlines()
