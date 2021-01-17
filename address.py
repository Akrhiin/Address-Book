#initial user selection
def choiceSelect():
    import time
    while True:
        #select what you want to do
        print('\n1. View contacts \n2. Add contacts \n3. Delete contacts\n')
        choice = str(input('What would you like to do? '))
        #format selection
        choice = choice.strip().lower()
        if choice == 'view contacts':
            choice = '1'
        elif choice == 'add contacts':
            choice = '2'
        elif choice == 'delete contacts':
            choice = '3'
        #input selection
        if choice == '1':
            return('1')
        elif choice == '2':
            return('2')
        elif choice == '3':
            return('3')
        else:
            print('Please provide a valid input.')
            time.sleep(1)
            continue
print(choiceSelect())

"""
import re

if choiceSelect() == '1':
    #view contacts
    
    letter = input('What letter do you want to look through?')
    book = open('addressdata.txt', 'r')
    book = book.read()
    
    print('1b')
if choiceSelect() == '2':
    #add contacts
    print('2b')
if choiceSelect() == '3':
    #delete contacts
    print('3b')
"""