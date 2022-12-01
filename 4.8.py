
def check_password(password):
    correct_lenght = False
    has_uppercase = False
    has_lowercase = False
    has_numbers = False

    if len(password)>=7:
        correct_lenght = True

    for char in password:
        if char.isupper():
            has_uppercase = True
        if char.islower():
            has_lowercase = True
        if char.isdigit():
            has_numbers = True
    if correct_lenght and has_numbers and has_lowercase and has_uppercase:
        check = True
    else:
        check = False

    return check

def main():
    password = input("Enter new password (minimum 7 characters, one capital letters, one lower letters, one digit):")

    if check_password(password):
        print("Ok, it is good password!")
    else:
        print("It isnt good ")

if __name__ == '__main__':
    main()