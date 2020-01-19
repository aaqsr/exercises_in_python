import time

'''
    calculate the factorial of a positive integer
    use while loop
'''
num = input("Number? \n")
num = int(num)

a = 1

# startTime = time.process_time()

while num > 0 :
    a = a * num
    num = num-1

# endTime = time.process_time()

print(a)
# print("That took about {}ms".format(endTime-startTime))