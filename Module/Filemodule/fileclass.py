import os

Folderpath = 'C:\\java_mylibrary'
for f in os.listdir(Folderpath):
    print(f)

'''folder = 'C:\python'
for g in os.listdir(folder):
    print(g)'''

'''def listdir(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        print('File Name: ' + filename)
        print('folder path: ' + os.path.abspath(os.path.join(dir,filename)), sep='\n')


        if __name__ == '__main__':
            listdir(Folderpath)'''