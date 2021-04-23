from numpy import *





def calculate_LU(matrix: list) -> tuple:

    n_matrix = len(matrix)

    U = matrix
    L = [[(1 if i == j else 0) for j in range(n_matrix)] for i in range(n_matrix)]

    
    current_pivot = 0
    for i in range(n_matrix):
        for j in range(i+1, n_matrix):

            operator = -1 * (matrix[j][current_pivot]/matrix[i][current_pivot])
            L[j][current_pivot] = -operator

            for x in range(current_pivot, n_matrix):
                U[j][x] += operator * U[i][x]

        current_pivot += 1                


    print(U)
    print('\n', L)

    return ()









if __name__ == "__main__":

    
    # give matrix is a square matrix
    n_matrix, number_of_b = input().split(' ')
    n_matrix, number_of_b = int(n_matrix), int(number_of_b)



    # read matrix A
    A = []
    for _ in range(n_matrix):
        A.append([int(x) for x in input().split(' ')])


    

