# Uses python3
#import sys

# The last digits of the fibonaccis repeat this 60-digit sequence: 
# repeat = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]

# The last digit of the sum of the first n fibonaccis is the same as 
# The last digit of the sum of the first n last digits
# The last digits of the sum repeat this 60-digit sequence: 
#[0, 1, 2, 4, 7, 2, 0, 3, 4, 8, 3, 2, 6, 9, 6, 6, 3, 0, 4, 5, 0, 6, 7, 4, 2, 7, 0, 8, 9, 8, 8, 7, 6, 4, 1, 6, 8, 5, 4, 0, 5, 6, 2, 9, 2, 2, 5, 8, 4, 3, 8, 2, 1, 4, 6, 1, 8, 0, 9, 0]


def gen_repeat_last_digits():
    """generate the sequence of 60 fibonacci last digits that repeaet
       these correspond to last digits of fibonacci numbers F0 --> F59
    """
    repeat= [0,1]
    for _ in range(2, 60):
        repeat.append( (repeat[-1] + repeat[-2])%10 )  #next last digit is units of sum of prev two last digits
    
    assert repeat == [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]

    return repeat


def gen_repeat_sum_last_digits():
    """ generate the sequence of 60 last digits of fibonacci sums that repeats
        these correspond to the last digits of fibonacci sums FS0 --> FS59
        where eg FS59 means the sum of the fibonacci numbers F0 through F59. 
    """
    repeat = gen_repeat_last_digits()  #get the last  digits that repeat
  
    # The last digit of the sum of the first n fibonaccis is the same as 
    # The last digit of the sum of the first n last digits in repeat
    
    sum_lastdigits = [0]

    for i in range( 1, len(repeat) ):
        sum_lastdigits.append( (repeat[i] + sum_lastdigits[-1])%10 )
    
    assert sum_lastdigits == [0, 1, 2, 4, 7, 2, 0, 3, 4, 8, 3, 2, 6, 9, 6, 6, 3, 0, 4, 5, 0, 6, 7, 4, 2, 7, 0, 8, 9, 8, 8, 7, 6, 4, 1, 6, 8, 5, 4, 0, 5, 6, 2, 9, 2, 2, 5, 8, 4, 3, 8, 2, 1, 4, 6, 1, 8, 0, 9, 0]
    return sum_lastdigits

def get_fibsum_lastdigit(n):
    """ returns the last digit of fibonacci sum n, which is the sum of the 
        first n fibonacci numbers (from f0 to fn inclusive) 
    """    
    #print("**call get_fibsum_lastdigit**")   

    # get repeat sequence of last-digits-of-sums 
    repeat = gen_repeat_sum_last_digits()
    if n<60:
        index = n
    else:
        index = n%60
    #print("last digit is", repeat[index])
    return repeat[index]
    
    


## BELOW FUNCTIONS INCLUDED FOR TESTING OR FOR COMPARISON ##

def gen_repeat_sum_last_digits_naive():
    # generate the sequence of 60 last digits of fibonacci sums that repeats
    # these correspond to the last digits of fibonacci sums FS0 --> FS59
    # where eg FS59 means the sum of the fibonacci numbers F0 through F59. 
    
    repeat = gen_repeat_last_digits()  #get the last  digits that repeat

    sums = [0]
    for i in range( 1, len(repeat) ):
        sums.append(repeat[i] + sums[-1])
    print("the sums of these last digits are \n{}".format(sums) )

    lastdigits = [s%10 for s in sums]
    print("the last digits of these sums are \n{}".format(lastdigits) )    
    
    assert lastdigits == [0, 1, 2, 4, 7, 2, 0, 3, 4, 8, 3, 2, 6, 9, 6, 6, 3, 0, 4, 5, 0, 6, 7, 4, 2, 7, 0, 8, 9, 8, 8, 7, 6, 4, 1, 6, 8, 5, 4, 0, 5, 6, 2, 9, 2, 2, 5, 8, 4, 3, 8, 2, 1, 4, 6, 1, 8, 0, 9, 0]
    return lastdigits

  
def calc_fib(n):
    #print( "iterative find fibonacci N{}".format(n))
    
    numbers = [0,1]
    if n<=1:
        return n
    
    while len(numbers) <= n:
        numbers.append(numbers[-1]+numbers[-2])
    #print(numbers)       
    #return numbers[-1]    #return nth fibonacci number
    return numbers         # return the entire list
    

def show_fib_sums(n):
    print("**call show_fib_sums**")   
    fiblist = calc_fib(n)
    ## show a list of the sum of fibonacci numbers up to n
    print("the fibonaccis from N0 to N{} are \n{}".format(n, fiblist) )
    
    sums = []
    for fib in fiblist:
        if fib==0:
            sums.append(0)   # first fib has no previous one
        else:
            sums.append(fib + sums[-1]) #otherwise sum fib to the previous sum
            
    lastdigits = [s%10 for s in sums]
     
    print("the sums of these fibonaccis are \n{}".format(sums) )
    print("the last digits of these sums are \n{}".format(lastdigits) )
    
    return lastdigits
        
    

def get_nth_fibonacci_last_digit(n):
    # generate the 60 last digits that repeaet
    # these correspond to fibonacci numbers F0 --> F59
    repeat = gen_repeat_last_digits()
    
    # get last digit of nth fibonacci number
    if n<60:
        index = n
    else:
        index = n%60
    return repeat[index]
    

def get_nth_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def test(n):
    
    ## test get last digit of nth fibonacci number
    # for n in [0, 1, 2, 59, 60, 61, 120, 327305, 999999]:
    #     assert get_nth_fibonacci_last_digit(n)==get_nth_fibonacci_last_digit_naive(n)
    # print("testsok")
    
    ## test that repeat sequences are generated correctly
    # show_fib_sums(60)  #shows the first 60 fibonaccis, first 60 fibonacci sums, and their last digits
    # print("\n output of gen_repeat_sum_last_digits is\n", gen_repeat_sum_last_digits())
    
    ## see if get_fibsum_last_digit(n) returns same as show_fib_sums
    assert get_fibsum_lastdigit(n) == show_fib_sums(n)[-1]
    print("test ok")
    


if __name__ == '__main__':
 #   input = sys.stdin.read()
    n = int(input())
    print(get_fibsum_lastdigit(n))
    pass
    

