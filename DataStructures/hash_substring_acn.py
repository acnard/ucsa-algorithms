# python3
"""
In this problem, your goal is to implement the Rabin–Karp’s algorithm.
for searching the given pattern in the given text.
Input Format. There are two strings in the input: the pattern 𝑃 and the text 𝑇.

Output Format. Print all the positions of the occurrences of 𝑃 in 𝑇 in ascending order. 
Use 0-based indexing of positions in the the text 𝑇.

"""

x = 263               # int between 1 and prime-1
prime = 1000000007    # must be big prime, prob of collision prop to 1/prime


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences_naive(pattern, text):
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]


def get_occurrences(pattern, text):
    result = []
    p_hash = polyhash(pattern)

    for i in range(len(text) - len(pattern) + 1):
        substring = text[i:i+len(pattern)]  # slice the substring

        # only check strings for equality if hashes match
        if polyhash(substring) == p_hash and substring == pattern:
            result.append(i)

    return result


def get_occurrences_opt(pattern, text): 
    """
    optimized version that uses precomputed hashes for the text
    """
    result = []
    p_hash = polyhash(pattern)   #hash of the pattern

    t_hashes = precompute_hashes(text, len(pattern))  #hashes of all text substrings


    for i in range(len(text) - len(pattern) + 1):
        substring = text[i:i+len(pattern)]  # slice the substring

        # only check strings for equality if hashes match
        if t_hashes[i] == p_hash and substring == pattern:
            result.append(i)

    return result

def polyhash(s):
    # The ord() function returns an integer c, representing the Unicode character.
    # Polynomial funciton is,
    #   SUM (from i=0 to last index in string) of (ith char)*x^i  modP
    # eg for a four-character string:
    #    c0x^0 + c1x^1 + c2x^2 +c3x^3
    #
    # if you start from i=0 but work backwards through the string,
    # hash0 = c3x^0 = c3
    # hash1 = c3*x +c2
    # hash2 = c3*x^2 +c2*x +c1
    # hash3 = c3*x^3 + c2*x^2 + c1*x + c0
    #
    # and more generally you can iteratively do :
    #   hash(next) = hash(previous)*x + c(next)
    #
    # all mod prime
    #
    # x and prime are global constants defined above

    tot = 0
    for c in reversed(s):
        tot = (tot*x + ord(c)) % prime

    return tot

def precompute_hashes(text, p_len):
    """
    text is a string, p_len is an int, the length of the pattern for which 
    we want to precompute hashes
    """
    
    num_substrings = len(text) - p_len + 1
    hashes = [None]*(num_substrings)

    lastpos = len(text) - p_len  # last index pos where a substring can start

    ## compute polyhash of last substring in text
    hashes[-1] = polyhash( text[lastpos:] )
    
    ## compute y = (x**p_len) mod prime
    ## multiply x by itself p_len times
    ## NB x and prime are global constants
    y = 1
    for _ in range(p_len):
        y = (y*x) % prime
    

    ## work backwards from penultimate substring position to zero
    for i in range(lastpos-1, -1, -1):
        
        ## we have to take val mod prime but val may be negative
        ## compute the next hash value, working backwards
        ## take mod prime at each stage of the calcuation
        val = (x * hashes[i+1]) % prime 
        val = ( val + ord(text[i]) )%prime   
        val = val - ( y*ord(text[i+p_len]) )%prime
        
        if val < 0:
            val = (val+prime) 
        hashes[i] = (val) % prime 

    
    return hashes

def test_precompute(text, p_len):
    """
    compares the precomputed hashes with the manually generated ones
    """

    precomputed = precompute_hashes(text, p_len)

    manual = []
    for i in range( len(text) - p_len + 1):
        substring = text[i:i+p_len]  # slice the substring
        manual.append( polyhash(substring) ) 

    print("manual hashes:", manual)
    print("prcomputed hashes", precomputed)

def test(pattern, text):
    result = get_occurrences(pattern, text)
    result_naive = get_occurrences_naive(pattern, text)
    result_optimized = get_occurrences_opt(pattern, text)

    print("result:", result)
    print("result naive:", result_naive)
    print("result optimized:", result_optimized)

if __name__ == '__main__':
   # print_occurrences(get_occurrences(*read_input()))

    (pattern, text) = (input().rstrip(), input().rstrip())

    #test(pattern, text)
    print_occurrences(get_occurrences_opt(pattern,text))
