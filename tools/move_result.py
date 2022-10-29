
import os
import shutil

dirs = ['Coffee', 'Easyship', 'Scar']
test_back = 'B_'
cnt = 0
logs_dir = '../logs_ref/'
for dir in dirs:
    dir_test = logs_dir + dir + '/' + test_back + 'test'
    for f in os.listdir(dir_test):
        shutil.move(dir_test + '/' + f, logs_dir + test_back + 'result/' + f)
        cnt += 1
print(f'move {cnt} files')
