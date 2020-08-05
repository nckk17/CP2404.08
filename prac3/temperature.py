def convert_celius_to_F(celius_temp):
    fer=celius_temp * 1.8 + 32.0
    print(fer)
def main():
    f = float(input("Enter the celius temperature"))
    feri=convert_celius_to_F(f)
    return feri

main()