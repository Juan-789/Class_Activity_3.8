print("Give me three integers and I will tell you which is the smallest ")
firstInt =  int(input("Enter First Integer "))
secondInt = int (input("Enter Second Integer "))
thirdInt = int(input("Enter Third Integer "))
if firstInt < secondInt and firstInt < thirdInt:
  print(f"{firstInt} is the smallest value ")
elif firstInt > secondInt and secondInt < thirdInt:
  print(f"{secondInt} is the smallest value ")
elif thirdInt < secondInt and firstInt > thirdInt:
  print(f"{thirdInt} is the smallest value ")