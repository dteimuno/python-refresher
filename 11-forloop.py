#will create variable from 0 to 9
for i in range(10):
    print("i is:", i)
for i in range(1,5):
    print("i is:", i)
#run for loop but stop at certain value:
for i in range(5):
    if i == 2:
        break
    print("i is:", i)
print("next problem")
#Skip current iteration(in this case skip i):
for i in range(5):
    if i == 2:
        continue
    print("i is:", i)
