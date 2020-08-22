def main():
    student={"lindsay.ward@jcu.edu.au":"Lindsay Ward","abe@gmail.com":"Abe","jimbo546@hotmail.com":"Jim Boh" }
    email = input("Email:")
    while True:
        if email in student and email != " ":
         a = email.split("@")
         print("Is your name ",a[0],"? (Y/n)")
         userchoice = input("")
         if userchoice == "n".lower():
            print("Name:",student[email])

        else:
         print("Invaild")

        email=input('Email:')



main()
