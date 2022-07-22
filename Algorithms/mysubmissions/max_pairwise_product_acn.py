def max_pairwise_product(numbers):
    #find biggest number    
    biggest = max(numbers)
    numbers.remove(biggest)
    
    #find second biggest
    secondbiggest = max(numbers)

    #print( "{}*{}={}".format(biggest, secondbiggest, biggest*secondbiggest) )
    return biggest*secondbiggest


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
