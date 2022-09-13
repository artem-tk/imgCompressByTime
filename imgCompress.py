import os

path = 'C:\\test'
#logPath = 'C:\\test'
renamed = 0 # Renamed files counter

print('Starting script')

def recurseRename (path) :

    for i in os.listdir(path) :
        
        global renamed

        if ' ' in i : # Finding spaces and deleting them
            os.rename(path + '\\' + i, path + '\\' + i.replace(' ',''))
            i = i.replace(' ','')
            print(path + '\\' + i + ' was renamed')
            renamed += 1

        if (os.path.isdir(path + '\\' + i)) : # Recursive running all directorys in path
            print('Go to ', (path + '\\' + i))
            recurseRename(path +'\\' + i)
            print('Comeback to ', path)

print('Starting rename')

recurseRename(path)

print('Rename ended. Renamed: ', renamed)