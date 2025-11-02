# Exercise 1.6: Contact Book Manager

# 1. Add new contact (name, phone, email)
# 2. View all contacts
# 3. Search contact by name
# 4. Delete contact
# 5. Update contact information
contacts = { 'ali' : { 'phone' : '01115842589', 'email' : 'ali@iti.com'} }

def Contact_Book_Manager ():
    while True:
        PrintMenu('Contact Book Manager',['Add new contact (name, phone, email)', 'View all contacts', 'Search contact by name', 'Delete contact', 'Update contact information', 'Exit'])
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            name = input("Enter item name: ")
            phone = input("Enter item phone: ")
            email = input("Enter item email: ")
            add_new_contact(name, phone, email)
        elif choice == '2':
            view_all_contacts()
        elif choice == '3':
            search_contact_by_name()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            update_contact_information()
        elif choice == '6':
            print("Exiting Contact Book Manager.")
            return
    
        



def add_new_contact(name, phone, email):
        if name in contacts:
            print(f"Contact '{name}' already exists.")
        else:
            contacts[name] = {'phone': phone, 'email': email}
            print(f"Contact '{name}' saved!")


def view_all_contacts():
        if not contacts:
            print("No contacts found.")
        else:
            for name, info in contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def search_contact_by_name():
        name = input("Enter contact name to search: ")
        if name in contacts:
            info = contacts[name]
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
        else:
            print(f"Contact '{name}' not found.")

def delete_contact():
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print(f"Contact '{name}' not found.")

def update_contact_information():
        name = input("Enter contact name to update: ")
        if name in contacts:
            phone = input("Enter new phone: ")
            email = input("Enter new email:")
            if phone:
                contacts[name]['phone'] = phone
            if email:
                contacts[name]['email'] = email
            print(f"Contact '{name}' updated.")
        else:
            print(f"Contact '{name}' not found.")


def PrintMenu(name: str ,options: list[str]):
    name = name if len(name) % 2 == 0 else name + ' '
    print('╔' + '═'*50 + '╗')
    print('╟'+ ('─'* (25 - int(len(name)/2))) + name +('─'* (25 - int(len(name)/2)))+'╢')
    print('╠═══╦' + '═'*46 + '╣')
    for i in range(0, len(options)):
        print(f'║ {i+1} ║'+(' ' + options[i]+ ' '*60)[:46]+ '║')
        if(i < len(options)-1): print('╠═══╬' + '═'*46 + '╣')
    print('╚═══╩' + '═'*46 + '╝')


Contact_Book_Manager ()