noOfStudents = int(input("Enter the number of students whose contact will be in phonebook: "))

phoneBook = {}

nameList = []
contactList = []

for i in range(0, noOfStudents):
    print("\nEnter the name of the student no", i + 1, ":")
    name = input()
    nameList.append(name)

    print("Enter the contact number of", name, ":")
    contactNo = int(input())
    contactList.append(contactNo)

    phoneBook[name] = contactNo

print("\nThe contact list is: ", phoneBook)

while (1):
    print("\n\nPHONEBOOK PROGRAM")
    print("\nType 0 if you want to exit this program and print the whole phonebook, or,\nType,\n1. Update Phonebook\n2. Search contact number by name\n3. Print whole phonebook")
    action = input()
    if action == "1" or action == "2":
        if action == "1":
            print("\nEnter the name of the student:")
            updateName = input()
            nameList.append(updateName)

            print("Enter the contact number of", updateName, ":")
            updateNo = int(input())
            contactList.append(updateNo)

            phoneBook[updateName] = updateNo
            print("\nUpdation done!")

        elif action == "2":
            print("\nEnter the name whose contact number you want:")
            updateName = input()
            if updateName in nameList:
                print("Contact number of", updateName,
                      "is:", phoneBook[updateName])
            else:
                print("Entered name is not in the phonebook")
        else:
            print("Invaid key")
            
    elif action == "3":
            print("\nPrinting whole Phonebook")
            print(phoneBook)

    else:
        print("\nExiting phonebook program...")
        break


print("\n\nPHONEBOOK:", phoneBook, "\n")
