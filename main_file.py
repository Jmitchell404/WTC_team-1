import quickstart,print_statements,token_removal
import time, os

lets_go = True
'''
Skeleton Code for the mock code/demo
- Bavu and Thando set up basic structure
- Use code from josh and Ryland for config and calendar showing
- 
'''





def start():
    lets_go = True
    while lets_go == True:

        print_statements.welcome_msg()
        
        time.sleep(1)
        quickstart.main() #Runs the client login from google

        print_statements.successful_login_msg()

        user_type = input('ARE YOU A STUDENT OR VOLUNTEER?').lower()
        
        if user_type == 'student':
            student_sign_up()

        elif user_type == 'volunteer':
            volunteer_sign_up()

    lets_go == False

    token_removal.token_delete() #Will
    print_statements.off_command()


        





    # os.remove()



























    # off_command.off_command()


    # username= input('Please enter your student email: ')
    # if '@student.wethinkcode' in username:
    #     print('Welcome')
     

    
    # user_type = input(' Are you a user or volunteer?')
    # if user_type ==   'volunteer':
    #     print('Would you like to view the calendar? ')

    # elif user_type == 'user':
    #     print('Would you like to view the calendar? ')

    # else:
    #     print('error message') #Josh's code
    #     return False

'''
error msg function
'''       



'''
The code that automates the login process then goes in here
a in function that takes user_type and username as parameters
'''


if __name__ == "__main__":
    start()