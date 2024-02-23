def fibonacci(nums):
    a = 0
    b = 1
    next = 1
    count = 1
    lst = []
    while count<=nums:
        lst.append(next)
        a, b = b, next
        next = a+b
        count+=1
    return lst


# print(fibonacci(10))