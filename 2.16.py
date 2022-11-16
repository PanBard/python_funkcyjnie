
class Matrix:

    def generate_new_two_dimension_list(self,size_of_2D_list):
        matrix = list([0 for i in range(size_of_2D_list)] for j in range(size_of_2D_list))
        return matrix

    def display_matrix(self,matrix):
        N=len(matrix)
        for i in range(N):
            for j in range(N):
                print(matrix[i][j]," ",end="")
            print()

    def insert_numbers_in_diagonal(self,matrix):
        N = len(matrix)
        for i in range(N):
            for j in range(N):
                if (N==i+j+1):
                    matrix[i][j] = 1


    def sum_diagonal_numbers(self,matrix):
        N = len(matrix)
        sum = 0

        for i in range(N):
            for j in range(N):
                if (N==i+j+1):
                    sum += matrix[i][j]

        return sum

            ##################### 2 sposob -poczatek- ###########################
    # def insert_numbers_in_diagonal(self,matrix):
    #     N = len(matrix)
    #     counter = 9
    #     for i in range(N):
    #         for j in range(N):
    #             if j==counter:
    #                 matrix[i][j] = 1
    #                 counter -=1
    #
    # def sum_diagonal_numbers(self,matrix):
    #     N = len(matrix)
    #     sum = 0
    #     counter = 9
    #     for i in range(N):
    #         for j in range(N):
    #             if j == counter:
    #                 sum += matrix[i][j]
    #                 counter -=1
    #     return sum
##################### 2 sposob -koniec- ###########################

def main():
    matrix = Matrix()
    new_2D_list = matrix.generate_new_two_dimension_list(10)
    matrix.insert_numbers_in_diagonal(new_2D_list)
    matrix.display_matrix(new_2D_list)
    print("Sum of diagonal numbers:",matrix.sum_diagonal_numbers(new_2D_list))

if __name__ == '__main__':
    main()
