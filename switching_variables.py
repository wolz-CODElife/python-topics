#this file contains example on how 
#to switch two variable between themselves
#without introducing new variables

def main():
    first = input('Please input a word or number')
    last = input('Please input a word or number')
    swap(first, last)

def swap(first, last):
    first, last = last, first
    print('First: ', first, '/', 'Last: ', last)

#Execute the program
main()
