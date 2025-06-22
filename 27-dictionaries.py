usernames = {
    "lydia": "lydia123",
    "john": "john123",
    "peter": "peter123"
}
#for dictionaries we use keys to access values
print(usernames["lydia"])  # lydia123
#print back keys
print(usernames.keys())  # dict_keys(['lydia', 'john', 'peter'])
for key in usernames.keys():
    print(key + "-" + usernames[key])

#print back values
print(usernames.values())  # dict_values(['lydia123', 'john123', 'peter123'])

#items method
print(usernames.items())  # dict_items([('lydia', 'lydia123'), ('john', 'john123'), ('peter', 'peter123')])
#modifying values
usernames["lydia"] = "newpassword" 
#or
# usernames.update({"lydia": "newpassword"})   
print(usernames)

#deleting items
del usernames["john"]

#remove all items from dictionary
usernames.clear()

#remove last  item from dictionary
usernames.popitem()