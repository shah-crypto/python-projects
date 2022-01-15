import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="contacts_book"
)

mycursor = db.cursor()


def get_all_contacts():
    mycursor.execute("SELECT * FROM `all_contacts`")

    print("Full name\tMobile number\t\tLocation")
    print("------------------------------------------------")
    for student in mycursor:
        print(student[1] + " " + student[2] +
              "\t" + student[3] + "\t\t" + student[4])
        print()


def insert_contact(first_name, last_name, mob_number, location="-"):
    if mob_number[5] != " ":
        mob_number = mob_number[:5] + " " + mob_number[5:]
    if first_name and last_name and mob_number:
        mycursor.execute(
            "INSERT INTO `all_contacts` (`id`, `first_name`, `last_name`, `phone_no`, `city`) VALUES (NULL, %s, %s, %s, %s)", (first_name, last_name, "+91 " + mob_number, location))
        db.commit()


def get_specific_contact(query):
    mycursor.execute("SELECT * FROM `all_contacts` WHERE %s IN (`first_name`,`last_name`,`phone_no`)",
                     (query,))
    res = mycursor.fetchall()
    print("Full name\tMobile number\t\tLocation")
    print("------------------------------------------------")
    for row in res:
        print(row[1] + " " + row[2] +
              "\t" + row[3] + "\t\t" + row[4])
        print()


def delete_contact(query):
    mycursor.execute(
        "DELETE FROM `all_contacts` WHERE `first_name` LIKE %s OR 'last_name' LIKE %s OR `phone_no` LIKE %s", (query, query, "+91 " + query))
    x = input("Are you sure you want to delete? Y/n: ").lower()
    if x == 'y':
        db.commit()


while True:
    print("\nWelcome to your contacts book!\nSelect one of the following options and enter your choice-\n1. Insert a new contact\n2. See all contacts\n3. See details of a specific contact\n4. Delete contact\n5. Update contact\n6. Exit")
    choice = int(input("Enter your choice: ").strip())
    if choice == 1:
        first_name = input("Enter the first name: ").strip().title()
        last_name = input("Enter the last name: ").strip().title()
        mob_number = input("Enter the 10-digit mobile number: ").strip()
        location = input("Enter the location: ").strip().title()
        insert_contact(first_name, last_name, mob_number, location)
    elif choice == 2:
        get_all_contacts()
    elif choice == 3:
        search_query = input(
            "Enter first name, last name or mobile number to search: ").strip()
        get_specific_contact(search_query)
    elif choice == 4:
        del_query = input(
            "Enter first name, last name or mobile number to search: ").strip()
        delete_contact(del_query)
    elif choice == 5:
        pass
        break
    elif choice == 6:
        print("Thank you for using the application!")
        break
    else:
        break
