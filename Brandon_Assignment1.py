##################################################################################
# Aurthors: Amon Al-Khatib, Brandon Royal, Derek Goodwin, Eric Ly,
#           Steven Zielinski, Tyler VanHaren
# 
# Description: COT5405 Fall 2018, Assignment 1, Adding Two Random Numbers
# 
##################################################################################


import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from memory_profiler import memory_usage


def add(a, b):
    """Adds two numbers that are represented as Strings
  
    Takes two numbers, each represented as a string, and finds the sum. The numbers,
    as with the result, can be significantly large (above max integer size).

    Args:
        a: A string of digits that represents a valid whole number.
        b: A string of digits that represents a valid whole number.

    Returns:
        A string of digits that represents the sum of a and b.
    """

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
    """Generates a random number of size n.

    Generates a random number containing digits. This number is represented as a string
    to enable generating very large numbers.

    Args:
        n: The number of digits the random number will have.

    Returns:
        A string representing the random number. The length will always be n.
    """

    answer = str(random.randint(1,9))+ ''.join([str(random.randint(0,9)) for _ in range(1,n)])
    return answer

def memory_test(n):
    """Test method to be used by the memory profile.

    Test method that randomly generates two numbers of size n and then adds them.
    This method was specifically created to analyze memory usage with memory_profiler.

    Args:
        n: The number of digits each random number will have.

    Returns:
        result: The sum of the two random numbers.
    """
    x = generate(n)
    y = generate(n)
    result = add(x,y)
    return result


if __name__ == '__main__':
    length = []
    time = []
    memory = []
    needed = [4,8,16,32,64,128,256,512]

    for i in needed:

        numerator = 0
        denominator = 0
        totalMem = 0

        for iteration in range(0,1000):

            #Code to get the time of running our algorithm
            x = generate(i)
            y = generate(i)
            start = timer()
            add(x,y)
            end = timer()

            #Code for checking the memory usage of our code
            if(iteration == 0):
                memory_points = memory_usage((memory_test, (i,),), interval=0.000001)
                allPoints = sum(memory_points)
                curAvg = allPoints / len(memory_points)
                #print(curAvg)
                totalMem = totalMem + curAvg
                

            numerator = numerator + end-start
            denominator = denominator+1
        length.append(i)
        time.append(numerator/denominator)
        avgMem = totalMem / 1 #1 for now since we are only testing one iteration
        memory.append(avgMem)
        print("For " + str(i) + " average memory usage is: " + str(avgMem))
    plt.plot(length,time)
    plt.savefig('performance.png')