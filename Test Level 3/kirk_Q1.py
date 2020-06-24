with open('file2.txt', 'r') as f:
    print('\n'.join(f.read().splitlines()[::-1]))

f.close()