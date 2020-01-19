import time

'''
    calculate the factorial of a positive integer
    use for loop
'''
num = input("Number? \n")
num = int(num)

a = 1

# startTime = time.process_time()

for i in range(1,num+1):
    a = a * i

# endTime = time.process_time()

print(a)
# print("That took about {}ms".format(endTime-startTime))