import os
import abc123

def run(**args):

	print "[*] In dirlister module"
	files = os.listdir(".")

	return str(files)