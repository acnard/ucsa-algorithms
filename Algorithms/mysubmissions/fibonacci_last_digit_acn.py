# Uses python3
#import sys

# The last digits repeat this 60-digit sequence: 
# repeat = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]


def get_fibonacci_last_digit(n):
    # generate the 60 last digits that repeaet
    # these correspond to fibonacci numbers F0 --> F59
    repeat= [0,1]
    for _ in range(2, 60):
        repeat.append( (repeat[-1] + repeat[-2])%10 )
#    print(repeat)    
    if n<60:
        index = n
    else:
        index = n%60
    return repeat[index]
    

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def test():
    for n in [0, 1, 2, 59, 60, 61, 120, 327305, 999999]:
        assert get_fibonacci_last_digit(n)==get_fibonacci_last_digit_naive(n)
    print("testsok")

if __name__ == '__main__':
 #   input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit(n))
