import os

path = 'C:\\test'
#logPath = 'C:\\test'
renamed = 0 # Renamed files counter
compressed = 0 # Compressed files counter

def recursiveCompress (path) :

    global renamed
    global compressed

    for i in os.listdir(path) :

        if (' ' in i) & ~(os.path.exists(path + '\\' + i.replace(' ',''))) : # Finding spaces and deleting them
            os.rename(path + '\\' + i, path + '\\' + i.replace(' ',''))
            i = i.replace(' ','')
            print(path + '\\' + i + ' was renamed')
            renamed += 1
        elif (' ' in i) & (os.path.exists(path + '\\' + i.replace(' ',''))) : # If file without spaces already exist - add '1_'
            os.rename(path + '\\' + i, path + '\\1_' + i.replace(' ',''))
            i = '1_' + i.replace(' ','')
            print(path + '\\' + i + ' was renamed')
            renamed += 1

        if (os.path.isdir(path + '\\' + i)) : # Recursive running all directories in path
            print('Go to ', (path + '\\' + i))
            recursiveCompress(path +'\\' + i)
            print('Comeback to ', path)
        elif (os.path.isfile(path + '\\' + i)) & ~('compressed_' in i) : # Compess images by mozjpeg ignore files with 'compressed_' in name
            os.system("mozjpeg\\cjpeg -quant-table 2 -quality 75 -outfile {} {}".format(path + "\\" + "compressed_" + i, path + "\\" + i))

            if (os.path.exists(path + "\\" + "compressed_" + i)) : #Cheks for the existing compressed file and deleting original
                os.remove (path + '\\' + i)
            
            print(path + '\\' + i + ' was compressed')
            compressed += 1

print('Starting script')

recursiveCompress(path)

print('Script ended. Renamed: ', renamed, ' Compressed: ', compressed)