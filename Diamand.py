def pyramid(rows):
    for i in range(rows):
        print(' '*(rows-i-1)+'* '*(1+i))
    for j in range(rows-1,0,-1):
        print(' '*(rows-j)+'* '*(j))
