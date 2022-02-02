def sign_up():
    print('Welcome to the code clinic')
    username= input('Please enter your student email: ')
    if '@student.wethinkcode' in username:
        print('Welcome')
     

    
    user_type = input(' Are you a user or volunteer?')
    if user_type ==   'volunteer':
        print('Would you like to view the calendar? ')

    elif user_type == 'user':
        print('Would you like to view the calendar? ')

    else:
        print('error message') #Josh's code
        return False

'''
error msg function
'''       



'''
The code that automates the login process then goes in here
a in function that takes user_type and username as parameters
'''


if __name__ == "__main__":
    sign_up()