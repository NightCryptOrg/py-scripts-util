import subprocess

class SSH:
	"""SSH wrapper for server communication"""
	login: str

	def __init__(self, login: str):
		self.login = login

	def __call__(self, cmd: str, *args) -> subprocess.CompletedProcess:
		return subprocess.run(['ssh', self.login] + [arg for arg in args] + cmd.split(' '))

# Parse the hostname portion of an SSH login
def parse_hostname(login: str) -> str:
	hostname = login.split('@', 2)[1] if '@' in login else login
	hostname = hostname.split(':', 2)[0] # Trim port
	return hostname
