# Store student and classmate information in dictionaries
student = {
    "name": "Lewis Fonsi",
    "address": "City of Candon, Ilocos Sur",
    "fav_num": 25,
    "age": 25,
    "allowance": 500.0
}

classmate = {
    "name": "Andrea Andres",
    "address": "City of Vigan, Ilocos Sur",
    "fav_num": 18,
    "age": 21,
    "allowance": 700.0
}

# Store the lengths of the names in a list
name_lengths = [len(student["name"]), len(classmate["name"])]

def compare_students():
    # Conditional logic to check addresses and compare name lengths
    if "Ilocos Sur" in student["address"] and "Ilocos Sur" in classmate["address"]:
        print(f"{student['name']} is from {student['address']}") 
        print(f"{classmate['name']} is from {classmate['address']}")
        
        if name_lengths[0] > name_lengths[1]:
            print(f"{classmate['name']} has a longer name than {student['name']} with {name_lengths[1]} letters over {name_lengths[0]} letters")
        else:
            print(f"{student['name']} has a longer name than {classmate['name']} with {name_lengths[0]} letters over {name_lengths[1]} letters")
    elif "Ilocos Sur" in studentAddress and classmateAddress:
        sName_Split = studentName.split(" - ")
        cName_Split = classmateName.split(" - ")
        print ("One among", sName_Split, "or", cName_Split, "lives in Ilocos Sur")
    else:
        print("None of the students live in Ilocos Sur")

# Call the function to compare students
compare_students()

# Arithmetic operations
AddAge = student["age"] + classmate["age"]
print(f"The added age of {classmate['name']} and {student['name']} is {AddAge}")

SubFavNum = student["fav_num"] - classmate["fav_num"]
print(f"The subtracted value of favnum of {classmate['name']} and {student['name']} is {SubFavNum}")

combinedWeeklyAllowance = student["allowance"] + classmate["allowance"]
rounded_number = format(combinedWeeklyAllowance, ".2f")
print(f"The weekly allowance of {classmate['name']} and {student['name']} is {rounded_number} pesos")

# List operations
classList = [student["name"], classmate["name"]]
classList_Ext = [student["address"], classmate["address"]]
for value in (classList, classList_Ext):
    print(value)

classNumbers = [student["fav_num"], student["age"], int(student["allowance"]),
                classmate["age"], classmate["fav_num"], int(classmate["allowance"])]

# Reverse sort the classNumbers list
classNumbers.sort(reverse=True)
print(classNumbers)

for value1 in classNumbers:
    print(value1)

def quizTwo(studentNameCS):
    print(f"Congratulations on Quiz 2, {studentNameCS}")

# Ask for user input
user_name = input("Enter your name: ")
quizTwo(user_name)