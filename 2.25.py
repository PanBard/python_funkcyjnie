
class PrimaryNumbers:

    # def generate_primary_numbers(self,start_range,close_range):
    #     F = start_range
    #     N = close_range
    #     primary_numbers_list = []
    #     for x in range(F, N + 1):
    #         if x > 1:
    #             for i in range(2, x):
    #                 if (x % i) == 0:
    #                     break
    #             else:
    #                 primary_numbers_list.append(x)
    #                 print(x, end=" ")
    #     print()
    #     return primary_numbers_list
    def filter_function(self,x):
        return x%2 != 0 and x%3 != 0




def main():
    primNum = PrimaryNumbers()
    # print("Program display prime numbers from range F to N ")
    # F = int(input("Enter F: "))
    # N = int(input("Enter N: "))
    F=10
    N=25
    print(f"\nPrime numbers from range [{F}-{N}]:")

    primary_numbers = list(filter(primNum.filter_function,range(F,N)))

    print(primary_numbers)



if __name__ == '__main__':
    main()