for x in range(1,8):
    if x == 1:
        print(' *** ')
    elif x in range(2,4) or x in range(5,8):
        print('*   *')

    else:
        print('*****')
    