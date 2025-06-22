try:
    name = 'Lydia'
    print('My name is' + naem)
except:
    print("An error occurred")
print('All done!')

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
    print("All done!") 
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter  an integer!")
except:
    print("Something went wrong!")
print("All done!")
