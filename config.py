from util.format import *
import os
import sys
import json
import re


def select_config(prefix: str) -> (str, dict):
	"""Select a JSON config file based on a search prefix"""
	# Search for config files starting with prefix
	config_dir = './config'
	config_files: list(str) = []
	for file in os.listdir(config_dir):
		if file.startswith(prefix) and file.endswith('.json'):
			config_files.append(file)
	# Don't prompt for selection if a single config file is found
	if len(config_files) == 1:
		config_name = ''.join(config_files[0].split('.')[:-1])
		with open(f'{config_dir}/{config_name}.json') as f:
			return (config_name, json.load(f))

	print('Select config file:')
	for i, config in enumerate(config_files):
		print_info(f'{" "*4}{i+1}. {config}')
	print_error(f'{" "*4}0. Exit')
	choice = int(input())
	if choice == 0:
		sys.exit(0)
	elif choice > len(config_files):
		raise ValueError('Invalid config selection')
	else:
		config_name = ''.join(config_files[choice-1].split('.')[:-1])
		with open(f'{config_dir}/{config_name}.json') as f:
			return (config_name, json.load(f))


def load_schema(name: str) -> dict:
	with open(f'config_examples/{name}.jsonc') as f:
		lines: list(str) = f.readlines()
		lines = filter(lambda line: not line.lstrip().startswith('//'), lines)
		return json.loads(''.join(lines))

def validate_config(config: dict, schema: dict):
	for k, v in schema.items():
		if not k in config:
			raise KeyError(f'Missing config key "{k}": {v}')
