
def make_matrix(size):
    matrix = []
    for i in range(size):
        matrix.append(make_list(size))
    print("List matrix: ",matrix)
    return matrix

def make_list(size):
    ist = []

    for x in range(size):
        ist.append(0)
    return ist


def enter_numbers_in_diagonal(matrix):
    number = 1
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            if j == i:
                matrix[i][j] = number
                number +=1
    return matrix

def print_matrix(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j]," ",end="")
        print()

def change_list_matrix_for_tuple_list(matrix_list):
    for i in range(len(matrix_list)):
        matrix_list[i] = tuple(matrix_list[i])
    matrix_list = tuple(matrix_list)
    print("Tuple matrix: ",matrix_list)
    return matrix_list

def main():
    matrix = make_matrix(10)
    matrix2 = enter_numbers_in_diagonal(matrix)
    print_matrix(matrix2)
    tuple_matrix = change_list_matrix_for_tuple_list(matrix2)
    print_matrix(tuple_matrix)
if __name__ == '__main__':
    main()
