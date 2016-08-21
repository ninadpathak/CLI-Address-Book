import pickle, os

class Contacts:
	fileName = 'AddressBook'

######################################################
##	1. Add contacts to a list, nothing special again ####
######################################################

	def add(self, name, phone):
		if len(phone) >= 10:
			contacts = {}
			f = open(Contacts.fileName,'rb')
			contacts = pickle.load(f)
			f.close()
			f = open(Contacts.fileName,'wb')
			contacts [name] = phone
			pickle.dump(contacts, f)
			print ("Contact with name {0} and number {1} has been added to the contact list".format(name,phone))
		else:
			print("The phone number you entered is too short. Please enter a valid number")
######################################################
##	2.	Just a regular function to display   #########
##		data from a variable				 #########
######################################################
	def show_contacts(self):
		try:
			f = open(Contacts.fileName,'rb')
			contacts = pickle.load(f)
			if len(contacts) == 0:
				print ("No contacts in the contact list as of now")
			else:
				print("\n")
				for name,number in contacts.items():
					print ("Name:  {0} \t Number:  {1}".format(name,number))
				print("\n")
			f.close()
		except EOFError:
			print ("There are no contacts in your contact list")
	
######################################################
##	3. 		Delete contacts by name			 #########
######################################################	
	def delete(self, name):
		try:
			f = open(Contacts.fileName, 'rb')
			contacts = pickle.load(f)
			f.close()
			del contacts[name]
			f = open(Contacts.fileName, 'wb')
			pickle.dump(contacts, f)
			f.close()
			print ("{0} was deleted successfully".format(name))
		except KeyError:
			print("The name you entered is not in the contact list")
		except EOFError:
			print("There are no contacts in your contact list")

######################################################
########		Update Contacts		##################
######################################################
	def update(self, name, number):
		try:
			f = open(Contacts.fileName, 'rb')
			contacts = pickle.load(f)
			f.close()
			if contacts[name]:
				contacts[name] = number
				f = open(Contacts.fileName, 'wb')
				pickle.dump(contacts, f)
				f.close()
				print("{0} was modified successfully ".format(name))
			else: 
				print ("{0} does not exist in the contacts".format(name))
			
		except KeyError:
			print("The name you entered is not in the contact list")
		except EOFError:
			print("There are no contacts in your contact list")
		
