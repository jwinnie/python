def italic(x):
	return '\x1b[3m{}\x1b[23m'.format(x)
def underlined(x):
	return "\033[4m"+x+"\033[0m"
def bold(x):
	return "\033[1m"+x+"\033[0m"
