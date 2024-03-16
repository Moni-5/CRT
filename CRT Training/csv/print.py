import csv
class printing:
    def login(self):
        with open('student.csv','r',newline='') as file:
            read=csv.DictReader(file)
            for row in read:
                print(row['studentID'],end=" ")
                print(row['rollno'],end=" ")
                print("",end="\n")
                
obj=printing()
obj.login()