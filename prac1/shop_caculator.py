def main():
    list=[]
    total=0
    numOfItem=0
    numOfItem=int(input("Enter the number of item:"))
    for n in range(numOfItem):
      price=float(input("Enter the price:"))
      list.append(price)
    total=sum(list)
    if total>100:
      sum1=total-(total*0.1)
      print("Total price for",numOfItem,"items is $",sum1)
main()