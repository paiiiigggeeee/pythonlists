import random  # call to be used later in program


def main():
    print('Welcome to the Guest List Program!')


guest_list = []  # initializing variable to an empty list


# define print_statement function for re-use
# Enumerate returns the index of list item numbered
def print_statement():
    for index, guest in enumerate(guest_list):  # for every name in the guest_list
        print(f' Name {index + 1} is {guest}')


while True:  # using while loop to ask for names of guests
    guest = input('Please enter names your of guests. Please click enter if you have no more names to enter.')
    # while list is not stopped, input is asked for

    if guest:  # An empty string is False
        if guest in guest_list:
            print('You already added that name to your list.')
        else:
            guest_list.append(guest)  # append() adds is the method to add name to list
    else:  # if name is not entered the statement breaks
        break

print('Thank you. The guest names are:')

# while statement asks user if they would like to delete a name
while True:
    delete_yes = input('Do you want to delete a name (yes/no):').lower()  # lower() method is applied to user's input
    if delete_yes == 'yes':  # if statement defines 'yes' statement
        guest = input('Enter the guest name you want to delete') # asks user to input guest name
        if guest in guest_list:
            guest_list.remove(guest) # requested guest name is removed from list using remove() method
            print('Name: {} deleted from list'.format(guest))  # print statement reads off deleted name
        else:  # if name is not in list, else statement prints the following message
            print('Name not found')
    else:  # end while loop when 'no' is inputted
        break

print_statement()  # call print statement function

# while statement asks user how many prizes should be given out
while True:
    prizes = int(input('Enter how many prizes there should be:'))  # prize variable is defined as user input
    if prizes > len(guest_list):  # if statement checks to see if entered prize number is greater than guest list length
        print('Prize count is more than the number of guests.')
    else:  # if entry is valid the while loop is ended
        break

winners = random.sample(guest_list, prizes)  # winners variable is intialized using random.sample method with
# guest_list and prize variables

print('Total number of guests: {}'.format(len(guest_list)))  # Final number of guests is printed
print_statement() # defined print function is called
print('Winner Names') # winner names are printed out in a list
print(winners)
