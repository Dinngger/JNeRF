
import os
import shutil

dirs = ['Car', 'Coffee', 'Easyship', 'Scar', 'Scarf']

cnt = 0
for dir in dirs:
    for f in os.listdir('../logs/' + dir + '/test'):
        shutil.move('../logs/' + dir  + '/test/' + f, '../logs/result/' + f)
        cnt += 1
print(f'move {cnt} files')
