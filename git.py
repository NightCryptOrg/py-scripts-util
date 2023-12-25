import subprocess


def rev_parse(repo_path: str) -> str:
	"""Return a short git commit ID from the given repo path"""
	result = subprocess.run(
			['git', 'rev-parse', '--short', 'HEAD'], stdout=subprocess.PIPE, cwd=repo_path)
	return result.stdout.decode('utf-8')[:-1]
