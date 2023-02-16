from pathlib import Path
import os

ROOT_DIR  = os.path.dirname(os.path.abspath(__file__))

def create_file(folder_name,subfolder_name):
	try:
		files = ['file_a', 'file_b', 'file_c','file_d','file_c']
		for i, file in enumerate(files):
			file_name = file + str(i)
			myfile = Path(ROOT_DIR+'/'+folder_name+'/'+subfolder_name+'/'+file_name+'.txt')
			myfile.touch(exist_ok=True)
			open(myfile)
			print('Create a new file at path:', myfile)
	except Exception as e:
		print('Error:',e)
		raise
	else:
		print('Result sum of files:',len(files))
	finally:
		print('Executing sum of files:',myfile)


	
create_file('topic','subtopic')
