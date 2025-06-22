num = 100
def input_number():
    global own_num
    own_num = 50 #local variable
    result = int(input("Enter a number: ")) * 100
    return result #return means return a value from a function