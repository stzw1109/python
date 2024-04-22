num = [1,2,2,3]

def has_duplicates(nums):
    result = False
    for x in nums:
        if nums.count(x) > 1:
            result = True
    if result == True:
        print('There are duplicates in the list')
    else:
        print('There are no duplicates in the list')
        
has_duplicates(num) 