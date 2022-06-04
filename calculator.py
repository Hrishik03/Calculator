import math
num_1 = float(input("Enter the first no:"))
num_2 = float(input("Enter the first no:"))
opt = input("Enter the operator:")

if opt == '+':
    print("ANS:", num_1 + num_2)
elif opt == '-':
    if (num_2 > num_1):
          print("ANS:", num_2 - num_1)
    else :
         print("ANS:", num_1 - num_2)
elif opt == '*':
    print("ANS:", num_1 * num_2)
elif opt == '/':
    if (num_2 > num_1):
          print("ANS:", num_2 / num_1)
    else :
         print("ANS:", num_1 / num_2)
else:
    print("Invlaid input")