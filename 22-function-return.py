def print_sum(num1, num2):
    sum = num1 + num2
    print("The sum is:", str(sum))

#a return statement in the function causes everything else to notbe run
def print_sum(num1, num2):
    sum = num1 + num2
    return
    print("The sum is:", str(sum))

#return only causes a function to exit, not the whole program
def print_sum(num1, num2):
    sum = num1 + num2
    if (sum == 0):
        return
    print("The sum is:", str(sum))

print_sum(4, 2)

def is_even(num):
    if (num % 2 == 0):
        return True
    else:
        return False
print(is_even(4))  # True