#this file contains example on how 
#to switch two variable between themselves
#without introducing new variables

#define the main program which will make use of 
#an external function
def main():
    first = input('Please input a word or number')
    last = input('Please input a word or number')
    swap(first, last)

#define an external function(OPTIONAL) that will 
#switch the variable
def swap(first, last):
    first, last = last, first
    print('First: ', first, '/', 'Last: ', last)

#Execute the program
main()
