def init_database():
    names = ["Picard", "Riker", "Data", "Geordi", "Worf"]
    ranks = ["Captain", "Commander", "Lt Commander", "Lt Commander", "Lieutenant"]
    divs = ["Command", "Command", "Operations", "Engineering", "Security"]
    ids = ["001", "002", "003", "004", "005"]

def display_menu():
    user = input("Enter your full name")
    print("Welcome", user)  
    print("\n---MENU---")
    print("1. Add member")
    print("2. Remove member")
    print("3. Update rank")
    print("4. Search crew")
    print("5. Filter by division ")
    print("6. Display roster")
    print("7. Calculate payroll")
    print("8. Count officer")
    print("9. Exit")


def add_member(names, ranks, divs, ids):
    print("\n--- ADD MEMBER ---")
    new_name = input("What is your name? ")
    new_rank = input("what is your rank")
    new_div = input("what is your division")
    new_id = input("what is your id")

    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    print("Member added")

def remove_member(names, ranks, divs, ids):
    print("\n---REMOVE CREW MEMBER---")
    remove_id = input("enter id to remove")
    if remove_id not in ids:
        print("ID not found")
    
    idx = ids.index(remove_id)
    names.pop(idx)
    ranks.pop(idx)
    divs.pop(idx)
    ids.pop(idx)
    print("Mmeber removed")