import os

python = 'python ' 
python1 = 'py.' 
python2 = 'cpython-310' 
python3 = '.pyc'
python = python + python1 + python2 + python3
if __name__ == "__main__":
	try:
		os.system(python) 
	except Exception as e:
		exit(str(e))
