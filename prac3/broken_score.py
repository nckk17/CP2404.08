def caculate_score(score):
    if score < 0:
        message =("Invalid score")
    elif score >100:
        message = ("Invalid score")
    elif score >50:
        message =("Passable")
    elif score >90:
        message =("Excellent")
    else:
        message =("Bad")
    return (message)

def main():
    userscore = int(input("Enter the user score:"))
    ans=caculate_score(userscore)
    print(ans)
main()