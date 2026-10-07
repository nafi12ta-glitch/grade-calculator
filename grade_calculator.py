print("=" * 45)
print("        STUDENT GRADE CALCULATOR")
print("=" * 45)

number_of_subjects = int(input("How many subjects do you have? "))

total = 0

for i in range(number_of_subjects):
    grade = float(input("Enter Your Grade: "))
    total = total + grade

average = total / number_of_subjects

if average >= 90:
    letter = "A"
elif average >= 88:
    letter = "B"
elif average >= 77:
    letter = "C"
elif average >= 66:
    letter = "D"
else:
    letter = "F"

print()
print("-" * 45)
print("RESULTS")
print("-" * 45)
print("Overall Average:", round(average, 2), "%")
print("Letter Grade:", letter)
print("-" * 45)
print("Thank you for using the Grade Calculator!")






