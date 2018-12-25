import random as rd
import time

def generateTestVector (elements = 100, min = 0, max = 1000):
    '''
    :param elements: number of items of the test vector
    :param min: min value of each element
    :param max: max value of each element
    :return: test_vector: a random vector of elements vector
    '''
    test_vector = [rd.randint (min, max) for _ in range (elements)]
    return test_vector

def generateAllTestVectors ():
    '''
    Generate a matrix of test vector
    :return: all_vector: a matrix of test vector
    '''
    all_vector = [
        generateTestVector (elements=pow (10, i), min = 0, max = pow (10, j))
        for i in range (1, 5)
        for j in range (1, 5)
    ]
    return all_vector

def test (func):
    times = []
    all_vectors = generateAllTestVectors()

    for vec in all_vectors:
        t_start = time.time ()
        func (vec)
        times += [(time.time() - t_start, len (vec))]

    return times