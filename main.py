import json
import os

filename = "student.json"
file = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(file, filename)
SCHOOL_NAME = "ABC COLLAGE"

def load():
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save(data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    
def add_student(data):
    print(f"{'-'*20} {SCHOOL_NAME} {'-'*20}\n")
    while True:
       
        name = input("Enter Student Name ==> ").strip().title()
        
        if len(name) > 0 and name.replace(" ", "").isalpha():
            break
        print("Enter a Valid Name!")
            
    while True:
        try:
            age = int(input("Age: => ").strip())
            break
        except ValueError:
            print("Enter Valid Age.")

    while True:
        COURSES = [
            "Python Programming",
            "Web Development",
            "Data Science",
            "Java Development",
            "Cyber Security",
            "Artificial Intelligence",
            "Digital Marketing",
            "Graphic Designing",
            "Full Stack Development",
            "Cloud Computing"
        ]
        try:
            for i, c in enumerate(COURSES, 1):
                print(f"{i}. {c}")
                
            c = int(input("Choose Course: (1 or 2... or 10) => ").strip())
            
            if 1 <= c <= len(COURSES):
                user_course = COURSES[c-1]
                break
            else:
                print("Invalid option! Choose a valid option.")
        except ValueError:
            print("Please Choose A Valid Option.")
            
    student_data = {
        "name": name,
        "roll_no": max(s['roll_no'] for s in data) 
        + 1 if data else 1,
        "age": age,          
        "course": user_course   
    }
    data.append(student_data)
    save(data)
    print(f"Hello {name}! Welcome to {SCHOOL_NAME}. Your Roll no. is {student_data['roll_no']}")

def show_student(data):
    if not data:
        print("There is no student enrollment yet.")
        return
    print(f"\n==================== [ {SCHOOL_NAME} Students List ] ====================\n")
    print(f"{'Name':<20} | {'Roll No':<10} | {'Age':<5} | {'Course':<25}")
    print("-" * 75)
    
    for s in data:
        print(f"{s['name']:<20} | {s['roll_no']:<10} | {s['age']:<5} | {s['course']:<25}")
    print("=" * 75)
    
def search_student(data):
    if not data:
        print("There is no student enrollment yet.")
        return
    try:
        roll = int(input("Enter Roll No For Student Details. => ").strip())
    except ValueError:
        print("Enter valid Roll No.")
        return
    
    for r in data:
        if r['roll_no'] == roll:
            print(f"{'Name':<20} | {'Roll No':<10} | {'Age':<5} | {'Course':<25}")
            print("-" * 75)
            
            print(f"{r['name']:<20} | {r['roll_no']:<10} | {r['age']:<5} | {r['course']:<25}")
            print("=" * 75)
            break
    else:
        print("No student of this roll number was found. Check you roll no.")
        
def delete_student(data):
    if not data:
        print("There is no student enrollment yet for delete.")
        return
    try:
        roll_for_del = int(input("Enter Roll No. => ").strip())
    except ValueError:
        print("Enter valid Roll No.")
        return
    
    for i, r in enumerate(data):
        if r['roll_no'] == roll_for_del:
            removed = data.pop(i)
            save(data)
            print(f"Success! {removed['name']} (Roll No: {removed['roll_no']}) ka record delete kar diya gaya hai.")
            break
    else:
        print("Ye Roll No. exist nahi karta!")
        
def menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student by Roll No")
    print("4. Delete Student")
    print("5. Exit")

def main():
    data = load()
    while True:
        menu()
        try:
            choice = int(input("Enter your choice (1-5) ==> ").strip())
            
            if choice == 1:
                add_student(data)
            elif choice == 2:
                show_student(data)
            elif choice == 3:
                search_student(data)
            elif choice == 4:
                delete_student(data)
            elif choice == 5:
                print("Thank you for using Student Management System. Goodbye!")
                break
            else:
                print("Invalid option! Please Enter Number Between (1-5)")
                
        except ValueError:
            print("Please Enter A Valid Number!")

if __name__ == "__main__":
    main()       