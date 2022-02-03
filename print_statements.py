def welcome_msg():
    print('\n   |-------------------------------------------------------------------|\n\
   |   Hey Coder, Welcome to the code clinic booking system.           |\n\
   |   Please sign in with your email on the window that will pop up:  |\n\
   |-------------------------------------------------------------------|\n\
    ')

    
def successful_login_msg():
    print("\n\
    |----------------------------------------------------------|\n\
    |                     SUCCESSFUL LOG-IN !!                 |\n\
    |                    WELCOME TO CODE CLINIC                |\n\
    |----------------------------------------------------------|\n\
        ")

def off_command():

    print("\n\
    |----------------------------------------------------------|\n\
    |           THANK YOU FOR USING THE CODE CLINIC            |\n\
    |   PLEASE MAKE SURE TO BE AVAILABLE FOR YOUR ALLOTED TIME |\n\
    |----------------------------------------------------------|\n\
        ")
    
    #Delete json credentials and token
    exit()

def error_msg():
    print('Sorry, I do not understand this command. \n\
        Please try again...')