from math import pow

def radixSort (int_vector):
    '''
    Sorts a vector of integers
    :param int_vector:  vector not sorted of integers
    :return: ordered_int_vector
    '''
    ordered_int_vector = int_vector[:]
    current_pos = 1
    completed = False

    while not completed:
        completed = True
        digit = pow (10, current_pos)
        digit_dict = {i: [] for i in range(10)}

        for index in ordered_int_vector:
            num = findNdigit(index, current_pos)
            #print (num, index, current_pos)
            digit_dict[int (num%digit)] += [index]
            completed &= (index//digit == 0)

        ordered_int_vector = []
        for index in list (digit_dict.keys()):
            ordered_int_vector += [i for i in digit_dict[index]]

        current_pos += 1

    return ordered_int_vector

def findNdigit (int_num, index):
   '''
   :param int_num: 
   :param index: 
   :return: 
   '''
   n_digit = int_num // pow (10, index - 1)
   return n_digit % 10