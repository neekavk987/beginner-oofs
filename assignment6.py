for x in range (0,5):
 number1=input("Enter number here ")
 number2=input("Enter another number here ")
 if not number1.isnumeric(): 
  print("this is not valid")
  break
 if not number2.isnumeric():
     if number1.isnumeric():
      print("this is not valid") 
      break
     if not number1.isnumeric():
      break
 print("the sum of your two numbers is" +str(int(number1) + int(number2))) 
 print("the product of the two numbers is" +str(int(number1) * int(number2)))