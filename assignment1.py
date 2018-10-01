import random
from timeit import default_timer as timer
from memory_profiler import profile
import matplotlib.pyplot as plt

# This specifies the size of the randomly generated large numbers
needed = 4
# This should be the name of the file that you would like the program to
# generate that will have the performance data
plotFile = 'performance.png'
# A value of 0 will give a plot based on runtime while a value of 1 will give
# a plot of the memory usage
memoryOrTime = 0;
# The number of times the program should add numbers of length needed
numberOfIterations = 1000;

def add(a, b):
    a = a[::-1]
    b = b[::-1]
    carry = 0
    numbers = []
    for i in range(0, max(len(a),len(b))):
        aa = 0 if len(a)<=i else int(a[i])
        bb = 0 if len(b)<=i else int(b[i])
        result = aa + bb + carry
        realresult = result%10
        carry = result//10
        numbers.append(realresult)
    if carry != 0:
        numbers.append(carry)
    numbers = numbers[::-1]
    answer = ''.join([str(digit) for digit in numbers])
    return answer

def generate(n):
    answer = str(random.randint(1,9))+ ''.join([str(random.randint(0,9)) for _ in range(1,n)])
    return answer
    
length = []
time = []

print('size of input numbers', needed)
numerator = 0
denominator = 0
for iteration in range(0,numberOfIterations):
    x = generate(needed)
    y = generate(needed)
    start = timer()
    result = add(x,y)
    end = timer()
    print('x = ', x)
    print('y = ', y)
    print('x + y = ',  result)
    time.append(end-start)
    numerator = numerator + end-start
    denominator = denominator+1
print('average = ', numerator/denominator)
plt.plot(range(0, numberOfIterations), time)
plt.savefig(plotFile)
