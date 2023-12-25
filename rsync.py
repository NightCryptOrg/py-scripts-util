import subprocess

_rsync_flags = ['-h', '--size-only', '--info=progress2']


def rsync(login: str, src: str, dst: str) -> subprocess.CompletedProcess:
    return subprocess.run(['/usr/bin/rsync'] + _rsync_flags +
                          [src, f'{login}:{dst}'])

class Rsync:
  """rsync wrapper for handling server file transfers"""
  login: str

	def __init__(self, login: str):
		self.login = login

  def __call__(self, src: str, dst: str, *args) -> subprocess.CompletedProcess:
		rsync = 'rsync'
		return subprocess.run([rsync] + _rsync_flags + [arg for arg in args] + [src, f'{self.login}:{dst}'])
