def oddoreven(num):
   if (num % 2) == 0:
      print("Number is Even")
   else:
      print("Number is Odd")

again= "yes"
while(again=="yes"):
   x = int(input("Enter a number: "))
   print (oddoreven(x))
   again = input("type yes or no to check again: ")
