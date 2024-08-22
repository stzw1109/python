def recursive_sum(sum,num):
    if num <= 10:
        sum+=num
        recursive_sum(sum,num+1)
    else:
        print(sum)

recursive_sum(0,0)
