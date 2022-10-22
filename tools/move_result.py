
import os
import shutil

# dirs = ['Car', 'Coffee', 'Easyship', 'Scar', 'Scarf']
dirs = ['Coffee']
test_back = 'B_'
cnt = 0
log_dir = '../logs_ref/'
for dir in dirs:
    dir_test = log_dir + dir + '/' + test_back + 'test'
    for f in os.listdir(dir_test):
        shutil.move(dir_test + '/' + f, log_dir + test_back + 'result/' + f)
        cnt += 1
print(f'move {cnt} files')
