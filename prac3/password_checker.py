def password_check(passwd):#process
    specialSymbol = ['$', '@', '#', '%']
    value = True

    if len(passwd) < 6 or len(passwd) >20:
        print('length should be at least 6 and between 20')
        value = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        value = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        value = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        value = False

    if not any(char in specialSymbol for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if value:
        return value


def main():
    passwd =input("Enter the password:")

    if (password_check(passwd)):
        print("Password is valid")
    else:
        print("Invalid Password !!")

main()