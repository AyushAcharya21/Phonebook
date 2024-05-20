'''
Ayush Acharya
Description: 
The program will let the user use features like the ones available 
on the contacts app on our smartphones such as displaying the contacts, 
adding contacts, deleting contacts, searching for a contact etc. 
With the help of user-interaction, the program shall be able to search 
and delete contacts by inputting the first name, last name, or 
phone num (not just one info input in particular). The program will 
be using a text file (that stores all the contacts), reading the contacts 
and adding contacts. 
'''



import time #Importing time module to make the output look smoother by using the sleep() function




'''
This function takes care of the display feature of the phonebook. It acceses the text file designated for phonebook and prints out all the contacts (the whole phonebook)
'''
def display(text_file):
    print("***************** Contacts *****************")
    
    #Using the with statement to open the text file 'phonebook.txt', read it, and save it in file variable
    with open(text_file, 'r') as file:
        file_content = file.read() #Using file.read() method inside the with statement to print out the whole file i.e all contacts
    if not file_content or file_content.isspace():  # Checking if the file is empty or contains only whitespace
        print("No contacts found!")
    else:
        print(file_content)  # Using file.read() method inside the with statement to print out the whole file, i.e., all contacts
    input("\nPress enter to continue...") #Getting any key input to continue the program
    




'''
This function takes care of the search feature of the phonebook. It acceses the text file designated for phonebook and searches for a contact the user wishes to search
'''
def search(text_file):
    info = input("Enter the FirstName, LastName, or PhoneNum to search in the phonebook: ") #Searching for a contact by first name, last name or phone num
    
    #Using the with statement to open the text file 'phonebook.txt', read it, and save it in file variable
    with open(text_file, 'r') as file:
        contacts = file.read().split('\n\n') #Inside the with statement, using file.read() method and splitting the content at 2 next lines i.e '\n\n' using the split() method to create a list of individual contacts as in indidual elements of a list. Note: Each contact is splitted by 2 newlines in the first place to make the display feature as well as the phonebook text itself look good without further complications

    found_contacts = [] #Defining an empty list to store all the found contacts based on the user's search input
    
    #Using a for loop to iterate through all the contacts
    for contact in contacts:
        
        #If the given info by the user exists in contacts, adds that specific contact to found_contacts using the append method
        if info.lower() in contact.lower():
            found_contacts.append(contact)
    
    #If there exists a contact based on what the user searched for, prints out those contacts
    if found_contacts:
        print("\n\n***************** Contact(s) Found *****************\n")
        
        #Using a for loop to iterate through found contacts and printing out each found contact
        for c in found_contacts:
            print(c + "\n")
        input("Press enter to continue...") #Getting any key input to continue the program
        
    #If no contact is found based on what the user searched for, allows the user to add the contact to the phonebook
    else:
        print("\033[H\033[2J", end="")
        print("***************** Contact Not Found *****************")
        choice = input("\nEnter 1 to add this contact or enter to return to the default screen: ") #Taking in input from the user deciding whether the user wants to add the contact they couldn't find or not
        
        #If they chose to add the contact, runs the add function to add the contact
        if choice == "1":
            add()




'''
This function takes care of the add feature of the phonebook. It acceses the text file designated for phonebook and writes/adds the contact the user wants to add
'''
def add(text_file):
    print("\n***************** Add New Contact *****************\n")
    
    #Taking in the first name, last name and phone num as inputs from the user 
    first_name = input("Enter the FirstName: ")
    last_name = input("Enter the LastName: ")
    phone_num = input("Enter the PhoneNum: ")
    
    new_contact = f"\n\nFirst Name: {first_name}\nLast Name: {last_name}\nPhone Number: {phone_num}\n" #Creating a formatted string, representing the contact 
    
    #Using the with statement to open the text file 'phonebook.txt' and 'a' to write on the file (instead of 'w' which overwrites)
    with open(text_file, 'a') as file:
        file.write(new_contact) #Using file.write method to write/add the new contact

    print("\nContact added successfully! Returning to the default screen in 3 seconds...") #Completition of this feature
    time.sleep(3)  #Using time.sleep() method to wait for 2 seconds (allowing the user to read the text above) before proceeding further 




'''
This function takes care of the delete feature of the phonebook. It acceses the text file designated for phonebook and allows the user to delete a certain contact or all contacts
'''
def delete(text_file):
    print("\n***************** Delete Contact *****************\n")
    
    #Taking in an info to track down the contact the user wants to delete or if they want to erase all contact
    info = input("Enter the FirstName/LastName/PhoneNum to delete a contact from the phonebook:\nOR\nEnter X to erase all contacts: \n")
    
    #If they entered "X", erases all contacts
    if info == "X":
        open(text_file, 'w').close() #Opening the text file and using the .close() method to erase all contacts
        print("\n\nErased all contacts! Returning to the default screen in 3 seconds...")
        time.sleep(3) #Using time.sleep() method to wait for 2 seconds (allowing the user to read the text above) before proceeding further 
    
    #If they didn't enter "X", that means they want to erase a certain contact
    else:
        
        #Using the with statement to open the text file 'phonebook.txt' and 'r' to read the file
        with open(text_file, 'r') as file:
            contacts = file.read().split('\n\n') #Creating a list of individual contacts using the split method to split at 2 newlines
        updated_contacts = [c for c in contacts if info.lower() not in c.lower()] #Creating a list of updated_contacts without the contact the user wanted to erase
        
        #Using the with statement to open the text file 'phonebook.txt' and 'w' to overwrite the file with updated contacts (after erasing the contact the user wanted to erase)
        with open(text_file, 'w') as file:
            file.write('\n\n'.join(updated_contacts)) #Using file.write() method to write on the text file. Joining 2 newlines with the list of updated contacts to create a proper display of updated contacts
        print("\n\nErased the given contact from the system! Returning to the default screen in 3 seconds...")
        time.sleep(3) #Using time.sleep() method to wait for 2 seconds (allowing the user to read the text above) before proceeding further 
      
      
      
        
'''
This function puts together all the features of phonebook into a function. Note: Creating a function for the whole phonebook program allows to create multiple phonebook objects that could work with multiple text files if needed
'''
def phonebook(text_file):
    
    # Checking if the file exists and creating if it doesn't
    with open(text_file, 'a'):
        pass
    
    user_input = "" #Initializing the user input to run the while loop correctly. This variable determines which feature the user wants to use
    
    #The while loop allows the program to run forever till the user inputs "5" (stops the program)
    while user_input != "5":
        print("\033[H\033[2J", end="") #Clearing the screen
        user_input = input("""***************** Welcome to Phonebook *****************
1. Display Your Existing Contacts
2. Add a New Contact
3. Search A Contact
4. Delete A Contact/All Contacts
5. Exit
Enter your entry here (1/2/3/4/5): """) #Taking in an input that represents a feature of phonebook the user wishes to use
        print("\033[H\033[2J", end="") #Clearing the screen
        
        #If the user inputs 1, using the display method to display all contacts
        if user_input == "1":
            display(text_file)
            
        #If the user inputs 2, using the add method to allow the user to add a contact
        elif user_input == "2":
            add(text_file)
            
        #If the user inputs 3, using the search method to search a contact
        elif user_input == "3":
            search(text_file)
            
        #If the user inputs 4, using the delete method to delete a contact or all contacts
        elif user_input == "4":
            delete(text_file)
        elif user_input != "5":
            print("Invalid input! Returning to the default screen in 2 seconds...")
            time.sleep(2.2)
        
    #This part runs after the while loop stops i.e after the user inputs 5:
    print("\033[H\033[2J", end="") #Clearing the screen
    print("\nStopping the program in 2 seconds...")
    time.sleep(2) #Using time.sleep() method to wait for 2 seconds (allowing the user to read the text above) before proceeding further 
    print("\033[H\033[2J", end="") #Clearing the screen



phonebook("savedContacts.txt") #Outside, caling the phonebook function for the text file "cps109_a1_output.txt"                                                                                                         q