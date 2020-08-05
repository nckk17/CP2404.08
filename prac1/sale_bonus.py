def main():
 sales = float(input("Enter sales: $"))
 while sales <= 0:
  print("Sorry your saalary must be positive")
  sales = float(input("Enter sales: $"))
  #end loop
 if sales < 1000:
      sale_bonus = sales * 0.1
      print(sale_bonus)
 else:
        sale_bonus=sales*0.15
        print(sale_bonus)
main()