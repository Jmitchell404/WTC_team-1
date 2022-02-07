import print_statements

    
def student_sign_up_student():
    student_input = input('Would you like to book a slot? \n\
if not, enter "exit" to leave program \n\
please enter Y/N: ')

    while True:
        if student_input.lower() == "y" or student_input.lower() == 'yes' :
            date = input('Enter date: ')
            time = input('Enter time: ')
            print(f'Your slot has been booked for {date} at {time}')
            break
        elif student_input == "n":
            print_statements.off_command()

        else:
            print_statements.error_msg()
            break
    
            
def student_sign_up_volunteer():
    student_input = input('Would you like to book a slot? \n\
if not, enter "exit" to leave program \n\
please enter Y/N: ')

    while True:
        if student_input.lower() == "y" or student_input.lower() == 'yes' :
            date = input('Enter date: ')
            time = input('Enter time: ')
            print(f'Your slot has been booked for {date} at {time}')
            break
        elif student_input == "n":
            print_statements.off_command()

        else:
            print_statements.error_msg()
            break