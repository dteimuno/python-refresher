try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except (ZeroDivisionError, ValueError) :
    print("An error occurred:")
except ArithmeticError:
    print("Math error occurred")
except:
    print("Something went wrong!")
print("All done!")

def calculate_user_input:
    try:
        x = int(input("Enter a number: "))
        y = 1 / x
        print(y)
    except (ZeroDivisionError) :
        print("You can't divide by zero!")
    except :
        print("Something went wrong!")
    return None

#you can manually raise exceptions using raise to simulate an error
def calculate_user_input:
    raise ZeroDivisionError

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except (ZeroDivisionError) :
    print("You can't divide by zero!")
except :
    print("Something went wrong!")
return None


#AssertionError: assert raises an assertion error if the expression evaluates to a falsy  value

import math
x = int(input("Enter a number: "))
assert x >= 0

x  = math.sqrt(x)
print("Result:", x)