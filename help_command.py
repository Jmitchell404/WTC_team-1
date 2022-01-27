def need_help():
    """
    when "help" is typed in by the user it will print out the help variable
    """
    help = """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - in the direction that one is facing or travelling
BACK - in the direction that one is not facing or travelling
SPRINT - accelerates in the direction that one is not facing or travelling
LEFT - turns left
RIGHT - turns right"""

    print(help)
    return help