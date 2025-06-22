#list append
#append or insert
#append inserts value at end of list
countries = ['USA', 'Canada', 'Mexico', 'Germany', 'France']
countries.append('Italy')  # adds 'Italy' to the end of the list
countries.insert(0, 'Spain')  # adds 'Spain' to the beginning of the list
#swap value in a list
temp = countries[0]  # stores the first item in a temporary variable
countries[0] = countries[1]  # replaces the first item with the second item
countries[1] = temp  # replaces the second item with the temporary variable
#easier way to swap values
countries[0], countries[1] = countries[1], countries[0]  # swaps the first two items
#sort and reverse
ages = [25, 30, 22, 35, 28]
ages.sort()  # sorts the list in ascending order
print(ages)  # prints the sorted list
ages.reverse()  # reverses the order of the list.