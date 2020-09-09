import os.path
from solution import File

path_to_file = 'some_filename'
os.path.exists(path_to_file)
file_obj_1 = File(path_to_file + '_1')
file_obj_2 = File(path_to_file + '_2')
file_obj_1.write('line 1\n')
file_obj_2.write('line 2\n')
new_file_obj = file_obj_1 + file_obj_2
