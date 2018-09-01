import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt

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
        carry = result/10
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
needed = [4,8,16,32,64,128,256,512]
for i in needed:
    print(i)
    numerator = 0
    denominator = 0
    for iteration in range(0,1000):
        x = generate(i)
        y = generate(i)
        start = timer()
        add(x,y)
        end = timer()
        numerator = numerator + end-start
        denominator = denominator+1
    length.append(i)
    time.append(numerator/denominator)
plt.plot(length,time)
plt.savefig('performance.png')
