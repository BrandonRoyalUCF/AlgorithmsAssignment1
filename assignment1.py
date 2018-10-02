import random
from timeit import default_timer as timer
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

# This specifies the size of the randomly generated large numbers
needed = 8
# This should be the name of the file that you would like the program to
# generate that will have the performance data
plotFile1 = 'Nof8Time.png'
plotFile2 = 'Nof8Memory.png'
# The number of times the program should add numbers of length needed
numberOfIterations = 1000
# Title of the graph of time per run
graphTitle1 = 'N of 8 Time'
graphTitle2 = 'N of 8 Memory'


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
        carry = result//10
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
    result = add(x, y)
    return result


if __name__ == '__main__':
    length = []
    time = []
    mem_avg = []

    print('size of input numbers', needed)
    numerator = 0
    denominator = 0
    maxHeight = 0.0
    maxMemory = 0.0
    summationMemory = 0.0
    for iteration in range(0,numberOfIterations):
        x = generate(needed)
        y = generate(needed)
        start = timer()
        result = add(x,y)
        end = timer()
        print(iteration)
        print('x = ', x)
        print('y = ', y)
        print('x + y = ',  result)
        memory_points = memory_usage((memory_test, (needed,),), interval=0.0000000001)
        memorySum = sum(memory_points)
        avgMemory = memorySum / len(memory_points)
        mem_avg.append(avgMemory)
        time.append(end-start)
        maxHeight = max(maxHeight, end-start)
        numerator = numerator + end-start
        denominator = denominator+1
    for j in mem_avg:
        maxMemory = max(maxMemory, j)
        summationMemory = summationMemory + j
    text = 'Average = ', numerator/denominator
    memText = 'Average = ', summationMemory/len(mem_avg)
    plt.figure(0)
    plt.xlabel('Runs')
    plt.ylabel('Time')
    plt.title(graphTitle1)
    plt.plot(range(0, numberOfIterations), time)
    plt.text(0, maxHeight*0.98, text)
    plt.savefig(plotFile1)
    plt.figure(1)
    plt.xlabel('Runs')
    plt.ylabel('Memory Usage')
    plt.title(graphTitle2)
    plt.plot(range(0, numberOfIterations), mem_avg)
    print(maxMemory)
    plt.text(0, maxMemory*0.98, memText)
    plt.savefig(plotFile2)
    print(text)
    print(memText)