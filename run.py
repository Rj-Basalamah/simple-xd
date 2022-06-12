import os
python = 'py' 
cython = 'ct' 
java = 'jv' 
if __name__ == "__main__":
	try:
		__import__(python).key()
	except Exception as e:
		exit(str(e))
