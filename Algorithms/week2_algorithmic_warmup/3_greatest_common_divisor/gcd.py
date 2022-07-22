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
    

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def test():
    for a in [1, 3333, 23, 711, 60, 54, 64]:
        for b in [1, 3333, 23, 711, 60, 54, 64]:
            assert gcd_naive(a,b) == gcd(a,b)
    print("testok")
            

if __name__ == "__main__":
#    input = sys.stdin.read()
    a, b = map(int, input().split())
    print(gcd_naive(a, b))
