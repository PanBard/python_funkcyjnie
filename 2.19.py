
class Matrix:

    def generate_new_two_dimension_list(self,size_of_2D_list, numbers_inside_matrix):
        matrix = list([numbers_inside_matrix for i in range(size_of_2D_list)] for j in range(size_of_2D_list))
        return matrix

    def display_matrix(self,matrix):
        N=len(matrix)
        for i in range(N):
            for j in range(N):
                print(matrix[i][j]," ",end="")
            print()
        print()

    def insert_numbers_in_diagonal(self,matrix):
        N = len(matrix)
        for i in range(N):
            for j in range(N):
                if (N==i+j+1):
                    matrix[i][j] = i

    def subtraction_matrix(self,matrix_1,matrix_2):
        N = len(matrix_1)
        for i in range(N):
            for j in range(N):
                summ = matrix_1[i][j] - matrix_2[i][j]
                matrix_1[i][j] = summ
        return matrix_1
    # def insert_numbers_in_diagonal(self,matrix):
    #     N = len(matrix)
    #     for i in range(N):
    #         for j in range(N):
    #             if (N==i+j+1):
    #                 matrix[i][j] = i

    def sum_diagonal_numbers(self,matrix):
        N = len(matrix)
        sum = 0

        for i in range(N):
            for j in range(N):
                if (N==i+j+1):
                    sum += matrix[i][j]
        return sum

def main():
    matrix = Matrix()
    new_2D_list_1 = matrix.generate_new_two_dimension_list(10,numbers_inside_matrix=1)
    new_2D_list_2 = matrix.generate_new_two_dimension_list(10,numbers_inside_matrix=2)

    matrix.display_matrix(new_2D_list_1)
    matrix.display_matrix(new_2D_list_2)
    sum_of_two_matrix = matrix.subtraction_matrix(new_2D_list_1, new_2D_list_2)
    print("Substraction of 2 matrix:")
    matrix.display_matrix(sum_of_two_matrix)

if __name__ == '__main__':
    main()
