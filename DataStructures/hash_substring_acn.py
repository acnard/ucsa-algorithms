# python3

x = 263
prime = 1000000007

def read_input():
    return (input().rstrip(), input().rstrip())


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
    # hash3 = c3*x^3 + c2*x^2 + c1*x
    #
    # and more generally you can iteratively do :
    #   hash(next) = hash(previous)*x + c(next)
    #
    # all mod prime
    #


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
    
    ## compute y = (x**p_len) mod prime
    ## multiply x by itself p_len times
    y = 1
    for _ in range(p_len):
        y = (y*x) % prime
    

    lastpos = len(text) - p_len  # last index pos where a substring can start
    ## work backwards from last substring position to zero
    for i in range(lastpos, -1, -1):
        hashes[i] = 
    
    

def test(pattern, text):
    result = get_occurrences(pattern, text)
    result_naive = get_occurrences_naive(pattern, text)

    print("result:", result)
    print("result naive:", result_naive)


if __name__ == '__main__':
   # print_occurrences(get_occurrences(*read_input()))

    (pattern, text) = (input().rstrip(), input().rstrip())
    test(pattern, text)
