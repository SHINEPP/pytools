import os
import shutil

if __name__ == '__main__':
    root = '/Users/zhouzhenliang/source/shine/'
    files = os.listdir(root)
    for f in files:
        path = root + os.path.join(f, 'app', 'build')
        if os.path.exists(path):
            shutil.rmtree(path)
            print(f'rm: {path}')
