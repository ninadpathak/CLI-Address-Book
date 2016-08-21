#!/usr/bin/python3
from functions import *

c = Contacts() ## Creating class object

# While loop for running the "choice" part unless user exits

while True:
	print("\n")
	
	choice = input("Enter a choice \n 1. Add Contact \n 2. Show Contacts \n 3. Delete Contact \n 4. Modify an entry \n 5. Exit \n ->> ")

	if choice == "1":
		user_name = input("Enter the name: ")
		user_num = input("Enter phone number: ")
		c.add(user_name,user_num)
		del user_name, user_num
	elif choice == "2":
		c.show_contacts()
	elif choice == "3":
		user_name = input("Enter the name you want to delete: ")
		c.delete(user_name)
	elif choice == "4":
		user_name = input("Enter the name you want to change: ")
		user_number = input("Enter the new number: ")
		c.update(user_name,user_number)
	elif choice == "5":
		exit()
	else:
		print ("Invalid choice")
