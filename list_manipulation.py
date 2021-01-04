'''
In this file we have examples of list/array manipulation
'''
#here is an example of normal list/array manipulation using two sample lists/array
my_list = []
new_list=['p', 'o', 'p']
print(my_list)

#here is an example of adding a value to an list/array
my_list.append(2)
print(my_list)

#here is an example of adding a list/array to another list/array
my_list.append([4, 5, 6])
print(my_list)

#OR

my_list += new_list
print(my_list)

#here is an example of adding each value in a list/array to another lis/array
my_list.extend(new_list)
print(my_list)

#LIST COMPREHENSION 
#here is an example of list comprehension adding values from a list to another list
my_list = [value for value in new_list]

#here is an example of list comprehension adding a value based on a conditon to a list
my_list = [value for value in new_list if value == 'p']

#here is an example of changing the value of an item in a list during list comprehension
my_list = [value = 'Pee' if value == 'p' else value = 'Ooo' for value in new_list]
