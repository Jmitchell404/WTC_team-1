


def student_sign_up_input():
    #calender output function
    student_input= input('Would you like to book a slot? \n\
if not, enter "exit" to leave program \n\
please enter y/n: ')
    # return student_input

    
def student_sign_up():
   
    if student_input == "y":
        date = input('Enter date: ')
        time = input('Enter time: ')
        print(f'Your slot has been booked for {date} at {time}')
        # break
    elif student_input != "y" or student_input != "n":
        student_sign_up_input()
    elif student_input == "n":
        exit()
            
def volunteer_sign_up():
    
    if student_input == "y":
        date = input('Enter date: ')
        time = input('Enter time: ')
        print(f'Your volunteer slot has been assigned for {date} at {time}')
        # break
    elif student_input != "y" or student_input != "n":
        student_sign_up_input()
    elif student_input == "n":
        exit()
    ...       




    
    
  




if __name__ == "__main__":
    student_input= student_sign_up_input() 
    student_sign_up()
   
