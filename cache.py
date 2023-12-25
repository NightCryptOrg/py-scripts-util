import os
import shutil

def init(config_name: str) -> str:
	"""Initialize an empty cache directory and return its path"""
	path = f'.cache/{config_name}'
	shutil.rmtree(path)
	os.makedirs(path)
	return os.path.abspath(path)
