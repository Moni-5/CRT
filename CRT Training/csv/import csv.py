import csv
f=open("student.csv","a",newline="")
a=csv.writer(f)
a.writerow(["studentID","rollno","mobilenumber","name"])
studentid=int(input("enter the studentid:"))
rollno=int(input("enterthe rollno:"))
name=input("enter the name:")
mobilenumber=int(input("enter the mobilenumber:"))
a.writerow([studentid,rollno,mobilenumber,name])
print("your data is save")
class printing:
    def login(self,studentID,rollno):
        with open('student.csv','r',newline='') as file:
            read=csv.DictReader(file)
            for row in read:
                print(row[studentID])
                print(row[rollno])