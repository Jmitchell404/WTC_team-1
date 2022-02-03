import  os

def token_delete():
    filePath = '/home/wtc/Projects-Thando/Group Project/team-1/token.json'

    if os.path.exists(filePath):
        os.remove(filePath)
