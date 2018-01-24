def max_of_3_num(*num):
    print('dupa')
    if len(num)!=3:
        print("You should put only 3 numbers.")
    else:
        print(max(num))
    for i in num:
        print(i)

max_of_3_num(1,2,3,4)