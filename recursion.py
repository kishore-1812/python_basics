number=int(input("Enter a positive number: "))
def recur(number):
     if(number != 0):
         return number + recur(number-1)
     else:
         return number
print("The sum is : ",recur(number))
