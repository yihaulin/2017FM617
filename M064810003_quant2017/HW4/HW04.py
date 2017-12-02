def multiplication_table(m, n):
    for i in range(1,10):
          for j in range(m,n+1):
                print(j, 'X', i, '=', i*j,'\t',sep='',end='')
          print()
    print('\n')

def pyramid(t):   
    for i in range(t+1):
        print(' '*(t-i)+("*"*((i)*2-1))) 