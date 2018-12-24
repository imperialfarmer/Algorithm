# -*- using: utf-8 -*-

def partition(array, l, r):
    # pivot = l
    p = array[l]
    # i is the position where the number starts to > pivot
    i = j = l + 1
    while j < r:
        if array[j] < p:
            # swap array[j] and array[i]
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp
            i += 1
        j += 1
    return array, i


def main():
    test_array = [3,8,2,5,1,4,7,6]
    print('-- Before partition --')
    print(test_array)
    partitioned_array = partition(test_array,0,len(test_array)-1)
    print('-- After partition --')
    print(partitioned_array)


if __name__ == '__main__':
    main()
    
