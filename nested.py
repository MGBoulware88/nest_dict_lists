x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

""" A
1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
2. Change the last_name of the first student from 'Jordan' to 'Bryant'
3. In the sports_directory, change 'Messi' to 'Andres'
4. Change the value 20 in z to 30
"""

#1
x[1][0] = 15
print(x)
#2
students[0]["last_name"] = "Bryant"
print(students)
#3
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
#4
z[0]["y"] = 30
print(z)

""" B
iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
"""
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
    for dict in list:
        #print(dict)
        for key in dict:
            print(f"{key} - {dict[key]}")

check = iterateDictionary(students)
print(check)

""" C
Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.
"""

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(key,list):
    for dict in list:
        print(f"{dict[key]}")

check = iterateDictionary2('last_name',students)
print(check)


""" D
Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
prints the name of each key along with the size of its list, 
and then prints the associated values within each key's list.
"""
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for key in dict:
        print(len(dict[key]),key)
        for idx in dict[key]:
            print(idx)

check = printInfo(dojo)

