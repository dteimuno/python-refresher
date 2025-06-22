age = 22
def multiply(num):
    num *= 2
    print("In multiply", str(num))
multiply(age)
print(age)  # 22, not changed because integers are immutable

nums = [1, 2, 3]
def change_first_item(list):
    list[0] = 9
change_first_item(nums)