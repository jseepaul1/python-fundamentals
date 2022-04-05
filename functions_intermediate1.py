# Update Values in Dictionaries and ListsUpdate Values in Dictionaries and Lists

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)  # output:[[5, 2, 3], [15, 8, 9]]

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students[0])  # output:{'first_name': 'Michael', 'last_name': 'Bryant'}

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])  # output:['Andres', 'Ronaldo', 'Rooney']

# Change the value 20 in z to 30
z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30
print(z)  # output:[{'x': 10, 'y': 30}]

# Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries,
# the function loops through each dictionary in the list and prints each key
# and the associated value. For example, given the following list:
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterate_dictionary():
    for obj in students:
        print(
            f"first_name - {obj['first_name']}, last_name - {obj['last_name']}")


iterate_dictionary()
# output:first_name - Michael, last_name - Jordan,first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen, # first_name - KB, last_name - Tonel

# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list)
# that, given a list of dictionaries and a key name, the function prints the value stored in
# that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:


def iterate_dictionary2(key_name, some_list):
    for obj in some_list:
        print(obj[key_name])


iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)

# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
# prints the name of each key along with the size of its list,
# and then prints the associated values within each key's list. For example:
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    print(len(some_dict['locations']), "LOCATIONS")
    for location in some_dict['locations']:
        print(location)
    print(len(some_dict['instructors']), "INSTRUCTORS")
    for instructor in some_dict['instructors']:
        print(instructor)


printInfo(dojo)
