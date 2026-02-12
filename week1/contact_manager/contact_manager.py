##### Core Features #####

# Contact Storage: Store names, phone numbers, email addresses, physical addresses, company details, job titles. 
# Organization: Group contacts with tags, labels, or lists (e.g., "Family," "Work," "Clients Q2").
# Search & Filter: Quickly find contacts by name, company, tag, or any detail.+
# Export to files: Save all the contacts to a file.
import week1.contact_manager.contact_manager as contacts

def main():
    while True:
        print("""
                WeLCOME TO CONTACT MANAGER APP"
              
                1. View All Contacts
                2. Add Contact
                3. Search Contact
                4. Show All Tags
                5. Add Tag
                6. Remove Tag
                7. Filter by Tag
                8. Export
                9. Exit
        """)

        action_map = {
            1: view_all_contact,
            2: add_contact,
            3: search_contact,
            4:show_all_tags,
            5: add_tag,
            6: remove_tag,
            7: filter_by_tag,
            8: export_data
        }
        try:
            action = int(input("enter a number from 1 to 9 as to select an action "))
            if 1 <= action <= 9:
                if action == 9:
                    print("exiting...........")
                    break
                action_map[action]()
            else:
                print("please enter a value between 1 to 9 ")
        
        except ValueError:
            print("please enter a valid number")

def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()

        if choice in ("y", "n"):
            return choice
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def display_contact(contact):
    print("\n" + "-" * 50)
    print("CONTACT DETAILS")
    print("-" * 50)

    print(f"{'Name':12} : {contact.get('name', 'N/A')}")
    print(f"{'Phone':12} : {contact.get('phone', 'N/A')}")
    print(f"{'Email':12} : {contact.get('email', 'N/A')}")
    print(f"{'Company':12} : {contact.get('company', 'N/A')}")
    print(f"{'Job Title':12} : {contact.get('job_title', 'N/A')}")
    print(f"{'Address':12} : {contact.get('address', 'N/A')} \n")

    # # Handle tags properly
    # tags = contact.get("tags", [])
    # if tags:
    #     print(f"{'Tags':12} : {', '.join(tags)}")
    # else:
    #     print(f"{'Tags':12} : No tags")

    # print("-" * 50 + "\n")

def view_all_contact():
    for contact in contacts:
        print(f"{contacts.index(contact) + 1}. {contact['name']}------{contact['phone']}")
    print(f"{len(contacts) + 1}. Exit")
    while True:
        try:
            next_action = int(input(f"enter a number to view more details of a contact (or) enter {len(contacts) + 1} to exit"))
            if next_action == len(contacts) + 1:
                print("exiting action 1.................")
                break
            elif 1 <= next_action <= len(contacts):
                display_contact(contacts[next_action - 1])
            else: 
                print(f"please enter a value between 1 and {len(contacts) + 1}")
        except ValueError:
            print("please enter a valid number")

def add_contact():
    new_dict = {'name' : input("enter the name of the contact "),
                 'phone' : int(input("enter the phone number ")),
                 'email' : input("enter the email of the contact "),
                 'address': input("enter the address of the contact "),
                 'company' : input("enter the company of the contac "),
                 'job_title' :  input("enter the job of the contact ") }
    print(f" \n \n Successfully added a new contact ")
    contacts.append(new_dict)
    display_contact(contacts[-1])
    
    if get_yes_no("do you want to add more?(y or n) ") == 'y':
        add_contact()
    else:
        return

def search_contact():
    contact_pointer = input("enter the name of the contact you want to search")
    for contact in contacts:
        if contact_pointer in contact['name']:
            display_contact(contact)
    if get_yes_no("do you want to search more?(y or n) ") == 'y':
        search_contact()
    else:
        return

def show_all_tags():
    set_of_tags = set()
    for contact in contacts:
        for tag in contact['tags']:
            set_of_tags.add(tag)
    list_of_tags = sorted(set_of_tags)
    print("---- AVAILABLE TAGS ----")
    for  tag in list_of_tags:
        print(f"{list_of_tags.index((tag)) + 1}. {tag}")
    print("------------------------")
    if get_yes_no("do you wish to filter contacts by any tag? ('y' or 'n')") == 'y':
        filter_by_tag()
def add_tag():
    pass
def remove_tag():
    pass
def filter_by_tag():
    pass
def export_data():
    pass

if __name__ == "__main__":
    main()