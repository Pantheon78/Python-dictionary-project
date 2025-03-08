students = {}

def add_student(ame , grades):
    students[name] = grades
    print (f"student {name} is successfully added")
    
def update_grades(name, new_grades):
    if name in students:
        students[name] = new_grades
        print(f"student[name] grades has been updated")
        
def view_grades(name):
    if name in students:
        print(f"{name}'s Grades: {students[name]}")
        
    else:
        print(f"student {name} was not found")
        
    def calculate_average(name):
        if name in students:
            avg= sum(students[name]) / len(students[name])
            print(f"{name}'average grade : {avg:.2f}")
            
        else:
            print(f"student{name} was not found")
            
while True:
    print("\nSTUDENTS REPORT CARD SYSTEM")
    print("1. Add students")
    print("2. update Grades")
    print("3. View Grades")  
    print("4. calculate Average")
    print("5. Exit")             
    
    choice = input("Enter your choice:")
    
    if choice == "1":
        name = input("Enter students name:")
        grades =list(map(int, input("Enter grades seperated by space:").split()))
        add_student(name , grades)
        
    elif choice == "2":
        name = input("Enter students name:")
        grades = list(map(int, input("Enter new_grades sepearted by space:").split()))
        update_grades(name , new_grades)
        
    elif choice == "3":
        name=("Enter students name:")
        view_grades(name)
        
    elif choice == "4":
        name("Enter student name:")
        calculate_average(name)
        break
    else:
        print("invalid choice.Please try again!")
        