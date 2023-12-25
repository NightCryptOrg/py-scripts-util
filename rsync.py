import subprocess

_rsync_flags = ['-h', '--size-only', '--info=progress2']


class Rsync:
	"""rsync wrapper for handling server file transfers"""
	login: str
	reverse: bool

	def __init__(self, login: str, reverse: bool):
		self.login = login
		self.reverse = False if reverse is None else reverse

	def __call__(self, src: str, dst: str, *args) -> subprocess.CompletedProcess:
		rsync = 'rsync'
		transfer_args = [f'{self.login}:{src}', dst] if self.reverse else [src, f'{self.login}:dst']
		return subprocess.run([rsync] + _rsync_flags + [arg for arg in args] + transfer_args)
