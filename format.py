# Formatted logging functions

def _term_color(code: int) -> str:
	"""Terminal color escape codes, use 0 to reset"""
	return f'\x1b[{code}m'


def _print_color(text: str, code: int):
	"""Print a colored line of text"""
	print(f'{_term_color(code)}{text}{_term_color(0)}')


def print_warning(text: str):
	_print_color(text, 31)


def print_error(text: str):
	_print_color(text, 31)


def print_success(text: str):
	_print_color(text, 32)


def print_info(text: str):
	_print_color(text, 34)


def print_heading(text: str):
	print_info(f'[{text}]')


def print_subinfo(text: str):
	_print_color(f'\u2014 {text}', 35)
