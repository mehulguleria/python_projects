import pandas as pd
from datetime import date
from pathlib import Path
import time
import os 

homedir = os.environ['USERPROFILE']
x = homedir.split("\\")
username = x[-1]

print("***Student Attendence***")

noOfStudents = int(input("Enter no. of students: "))
print("Enter 1 to mark present and 0 to mark absent.")
def createdata():
    global attendence
    attendence = [] 
    global Index
    Index = []
    for i in range(1, noOfStudents + 1):
        try:
            a = int(input(f"Roll number {i} "))
            if a == 0 or a == 1:
                attendence.append(a)
                Index.append(i)
            else:
                print("Enter only 0 and 1")
                createdata()
                break
        except Exception as er:
            print("///error///\n", er)
            createdata()

createdata()
def savedata():
    try:
        if Path(f'C:/Users/{username}/Desktop/attendence.csv').is_file():
            df = pd.read_csv(f'C:/Users/{username}/Desktop/attendence.csv')
            df[str(date.today())] = attendence
            df.to_csv(f'C:/Users/{username}/Desktop/attendence.csv', index=False)
        else:
            data = {"Roll number": Index, str(date.today()):attendence}
            df1 = pd.DataFrame(data)
            df1.to_csv(f'C:/Users/{username}/Desktop/attendence.csv', index=False)
    except PermissionError:
        print("///error///\nNote: Do not open the attendence file in other editor. Close the file and then try again")
        print("\nRetrying in 3 sec...\n")
        time.sleep(3)
        savedata()


savedata()
print("Data saved successfully...")