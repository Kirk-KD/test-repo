try:
    fileptr = open('file.txt', 'r')
except FileNotFoundError:
    print('file not found.')
else:
    print("The file opened successfully")  
    fileptr.close()