import subprocess

class SSH:
	"""SSH wrapper for server communication"""
	login: str

	def __init__(self, login: str):
		self.login = login

	def __call__(self, cmd: str, *args) -> subprocess.CompletedProcess:
		return subprocess.run(['ssh', self.login] + [arg for arg in args] + cmd.split(' '))
