# Uses python3

def calc_fib(n):
    #print( "iterative find fibonacci N{}".format(n))
    
    numbers = [0,1]
    if n<=1:
        return n
    
    while len(numbers) <= n:
        numbers.append(numbers[-1]+numbers[-2])
    #print(numbers)       
    return numbers[-1]    
        


def calc_fib_recursive(n):
    if (n <= 1):
        return n

    return calc_fib_recursive(n - 1) + calc_fib_recursive(n - 2) 



def testfib():
    for i in range(13):
        assert calc_fib_recursive(i) == calc_fib(i)



n = int(input())
print(calc_fib(n))
