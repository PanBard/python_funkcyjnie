def main():
    numbers = list(range(1,101))
    print("Our list: ",numbers)
    print("Sum of each element in our list:",sum(numbers))
    print("arithmetic mean of our list:", sum(numbers)/len(numbers))

if __name__ == '__main__':
    main()