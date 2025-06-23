def input_number(num):
   return int(input("Enter a number: ")) * num 
input1 = input_number(10)
print(input1)

#multiple parameters
def input_numbers(num1, num2):
    return int(input("Enter a number: ")) * num1 - num2

#can explicitly name parameters
input2 = input_numbers(num2=5, num1=3)

#can also use default values
def input_numbers_default(num1=2, num2=3):
    return int(input("Enter a number: ")) * num1 - num2