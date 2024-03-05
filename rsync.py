import subprocess

_rsync_flags = ['-h', '--info=progress2']


class Rsync:
	"""rsync wrapper for handling server file transfers"""
	login: str
	reverse: bool
	port: int|None

	def __init__(self, login: str, reverse=False):
		login_split = login.split(':', 2)
		self.login = login_split[0]
		self.port = login_split[1] if len(login_split) == 2 else None
		self.reverse = reverse

	def __call__(self, src: str, dst: str, *args) -> subprocess.CompletedProcess:
		rsync = 'rsync'
		ssh_args = ['-e', f'ssh -p {self.port}'] if self.port else []
		transfer_args = [f'{self.login}:{src}', dst] if self.reverse else [src, f'{self.login}:{dst}']
		return subprocess.run([rsync] + _rsync_flags + ssh_args + [arg for arg in args] + transfer_args)
