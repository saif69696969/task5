# ==========================================
# TASK 5: Tuples & Sentence Processing
# ==========================================

# Question 1: Student Information Tuple
print("--- Question 1: Student Info Tuple ---")
name = input("Enter Name: ").strip()
age = int(input("Enter Age: "))
program = input("Enter Program: ").strip()
marks = float(input("Enter Marks: "))
student_info = (name, age, program, marks)
print("student_info =", student_info)

# Question 2: Sentence Analyzer
print("\n--- Question 2: Sentence Analysis ---")
sentence = input("Enter a sentence: ")
print(f"Characters: {len(sentence)}")
print(f"Words     : {len(sentence.split())}")
print(f"Vowels    : {sum(1 for c in sentence if c.lower() in 'aeiou')}")
print(f"Spaces    : {sum(1 for c in sentence if c.isspace())}")
print(f"Digits    : {sum(1 for c in sentence if c.isdigit())}")

# Question 3: Employee Records List
print("\n--- Question 3: Employees List of Tuples ---")
employees = []
for i in range(1, 4):
    print(f"Enter details for Employee {i}:")
    emp_name = input("  Name  : ").strip()
    emp_age = int(input("  Age   : "))
    emp_salary = float(input("  Salary: "))
    employees.append((emp_name, emp_age, emp_salary))
print("employees =", employees)

# Question 4: Tuple Even & Odd Counter
print("\n--- Question 4: Tuple Even/Odd Counter ---")
numbers = (10, 15, 20, 25, 30, 35, 40)
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Numbers tuple:", numbers)
print("Even numbers :", even_count)
print("Odd numbers  :", odd_count)