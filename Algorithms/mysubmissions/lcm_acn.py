# Uses python3
#import sys

def gcd(a,b):
    # ensure a>=b
    if a<b:
        a,b = b,a
    # base case
    if b==0:
      return a  
    a, b = b, a%b
    return gcd(a,b)


def lcm(a,b):
    
    ## find gcd
    gc_divisor = gcd(a,b)
    
    return gc_divisor * a//gc_divisor * b//gc_divisor
    
def test():
    for a in [20, 30, 25, 15, 100, 60, 12, 3, 6]:
        for b in [20, 30, 25, 15, 100, 60, 12, 3, 6]:
            assert lcm_naive(a,b) == lcm(a,b)
    print("testok")

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b



if __name__ == '__main__':
#    input = sys.stdin.read()
    a, b = map(int, input().split())
    print(lcm(a, b))

