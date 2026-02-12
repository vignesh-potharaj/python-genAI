##### Core Features #####

# Contact Storage: Store names, phone numbers, email addresses, physical addresses, company details, job titles. 
# Organization: Group contacts with tags, labels, or lists (e.g., "Family," "Work," "Clients Q2").
# Search & Filter: Quickly find contacts by name, company, tag, or any detail.+
# Export to files: Save all the contacts to a file.


contacts = [
    {
        "name": "Rohit Sharma",
        "phone": "+91-9876543210",
        "email": "rohit.sharma@techvista.in",
        "address": "Flat 402, Green Residency, Madhapur, Hyderabad, Telangana 500081",
        "company": "TechVista Solutions",
        "job_title": "Software Engineer"
    },
    {
        "name": "Ananya Reddy",
        "phone": "+91-9123456780",
        "email": "ananya.reddy@medilife.in",
        "address": "H.No 8-3-214, Srinagar Colony, Hyderabad, Telangana 500073",
        "company": "MediLife Hospitals",
        "job_title": "HR Manager"
    },
    {
        "name": "Karthik Iyer",
        "phone": "+91-9988776655",
        "email": "karthik.iyer@finedge.com",
        "address": "Plot 17, Jubilee Hills, Hyderabad, Telangana 500033",
        "company": "FinEdge Analytics",
        "job_title": "Data Analyst"
    },
    {
        "name": "Meera Nair",
        "phone": "+91-9345678901",
        "email": "meera.nair@creativeminds.in",
        "address": "Flat 12B, Lakeview Apartments, Gachibowli, Hyderabad, Telangana 500032",
        "company": "Creative Minds Studio",
        "job_title": "Marketing Head"
    },
    {
        "name": "Arjun Verma",
        "phone": "+91-9012345678",
        "email": "arjun.verma@buildcore.in",
        "address": "Villa 23, Palm Meadows, Kompally, Hyderabad, Telangana 500014",
        "company": "BuildCore Constructions",
        "job_title": "Project Manager"
    },
    {
        "name": "Sneha Patel",
        "phone": "+91-9765432109",
        "email": "sneha.patel@healthplus.in",
        "address": "Flat 8A, Sunrise Towers, Kondapur, Hyderabad, Telangana 500084",
        "company": "HealthPlus Diagnostics",
        "job_title": "Operations Executive"
    },
    {
        "name": "Vikram Desai",
        "phone": "+91-9090909090",
        "email": "vikram.desai@cloudnet.in",
        "address": "H.No 5-9-30, Himayatnagar, Hyderabad, Telangana 500029",
        "company": "CloudNet Technologies",
        "job_title": "DevOps Engineer"
    },
    {
        "name": "Priya Menon",
        "phone": "+91-9888888888",
        "email": "priya.menon@eduprime.in",
        "address": "Flat 501, Skyline Heights, Begumpet, Hyderabad, Telangana 500016",
        "company": "EduPrime Academy",
        "job_title": "Academic Coordinator"
    },
    {
        "name": "Rahul Gupta",
        "phone": "+91-9555666777",
        "email": "rahul.gupta@retailhub.in",
        "address": "Plot 44, Banjara Hills, Hyderabad, Telangana 500034",
        "company": "RetailHub Pvt Ltd",
        "job_title": "Sales Director"
    },
    {
        "name": "Divya Kapoor",
        "phone": "+91-9700011122",
        "email": "divya.kapoor@nextgenai.in",
        "address": "Flat 903, Cyber Heights, HITEC City, Hyderabad, Telangana 500081",
        "company": "NextGen AI Labs",
        "job_title": "AI Research Associate"
    }
]

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
        print(f"{contact['name']}-----{contact['phone']}")

def add_contact():
    name_of_c = input("enter the name of the contact ")
    phone_of_c = int(input("enter the phone number "))
    email_of_c = input("enter the email of the contact ")
    company_of_c = input("enter the company of the contac ")
    job_of_c = input("enter the job of the contact ")
    new_dict = {'name' : name_of_c,
                 'phone' : phone_of_c,
                 'email' : email_of_c,
                 'company' : company_of_c,
                 'job' : job_of_c }
    print(f"Successfully added a new contact {new_dict}")
    contacts.append(new_dict)

def search_contact():
    pass
def show_all_tags():
    pass
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

