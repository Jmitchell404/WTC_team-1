import quickstart,print_statements,token_removal,login
import time, os

lets_go = True
'''
Skeleton Code for the mock code/demo
 - Bavu and Thando set up basic structure
 - Use code from josh and Ryland for config and calendar showing
 - Update config and calendar functions
'''


def start():    

    print_statements.welcome_msg()
    
    time.sleep(1)
    quickstart.main() #Runs the client login from google

    print_statements.successful_login_msg()

    user_type = input('ARE YOU A STUDENT OR VOLUNTEER? ').lower()
    
    if user_type == 'student':
        login.student_sign_up_student()

    elif user_type == 'volunteer':
        login.student_sign_up_volunteer()

    lets_go == False

    token_removal.token_delete() #removes token when done with programme
    print_statements.off_command()


'''
Add error msg function(maybe)
'''       

'''
The code that automates the login process then goes in here
a in function that takes user_type and username as parameters
'''


if __name__ == "__main__":
    start()