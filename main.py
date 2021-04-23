from numpy import *












if __name__ == "__main__":

    
    # give matrix is a square matrix
    n_matrix, number_of_b = input().split(' ')
    n_matrix, number_of_b = int(n_matrix), int(number_of_b)



    # read matrix A
    A = []
    for _ in range(n_matrix):
        A.append([int(x) for x in input().split(' ')])


    
