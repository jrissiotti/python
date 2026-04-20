# 03 Data structure


# Lists -> mutable structure, I can repeat values
my_list: list = ["Jorge", "Hacker", "Python", 19]
print(my_list)

my_list.append("Rissiotti")
print(my_list)

my_list.remove("Hacker")
print(my_list)
print(my_list[1])

my_list[1] = "Skeleton"
print(my_list)

my_list.sort(key = str) # 19 is still int; key = str only uses it as text for sorting, it doesn't convert it 
print(my_list)
print(type(my_list))


# Tuples -> immutable structure, I can repeat values
my_tuple: tuple = ("Jorge", "Rissiotti", "jrissiotti", 19)
print(my_tuple[1]) # Access
print(my_tuple[3])
sorted(my_tuple, key = str)
print(my_tuple)
print(type(my_tuple))


# Set -> disordered structure, I can not repeat values
my_set: set = {"Egg", "Bread", "Apple", "Rice" }
print(my_set)
my_set.add("jrissiotti3@gmail.com")
print(my_set)
my_set.remove("Egg")
print(my_set)
sorted(my_set) # cannot be ordered
print(my_set)
print(type(my_set))


# Dictionaries
my_dict: dict = {
    "Name" : "Jorge",
    "Surname" : "Rissiotti",
    "Alias" : "jrissiotti",
    "Age" : "19"
}

my_dict["Email"] = "jrissiotti3@gmail.com"
print(my_dict)
del my_dict["Surname"]
print(my_dict)
print(my_dict["Age"])
my_dict["Age"] = "20"
print(my_dict)
my_dict = dict(sorted(my_dict.items()))
print(my_dict)
print(type(my_dict))


"""
EXTRA:

english: Create a simple contact list per terminal.
        - You must implement functionalities for searching, inserting, updating, and deleting contacts.
        - Each contact must have a name and a phone number.
        - The program first asks for the desired operation,
        and then the necessary data to carry it out.
        - The program cannot allow the entry of non-numeric phone numbers with more than
        11 digits (or any number of digits you choose).
        - You must also offer a program termination option.

spanish: Crea una agenda de contactos simple por terminal.
        - Debes implementar funcionalidades de búsqueda, inserción, actualización
        y eliminación de contactos.
        - Cada contacto debe tener un nombre y un número de teléfono.
        - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
        y a continuación los datos necesarios para llevarla a cabo.
        - El programa no puede dejar introducir números de teléfono no numéricos y con más
        de 11 dígitos (o el número de dígitos que quieras).
        - También se debe proponer una operación de finalización del programa.
"""

def my_agenda():
    agenda = {}
   
    while True:
        print("1. Search contact")
        print("2. Add contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Exit")
        
        option = input("\nWhat do you want to do?: ")
        
        match option:
            case "1":
                name = input("Enter the contact name to search: ")
                if name in agenda:
                    print(f"{name} phone number is {agenda[name]}")
                else:
                    print(f"{name} does not exist in the contact list")
                    
            case "2":
                name = input("Enter the contact name: ")
                phone = input("Enter the contact number: ")
                if phone.isdigit() and 0 < len(phone) <= 11:
                    agenda[name] = phone
                    print(f"Contact {name} added successfully.")
                else:
                    print("Enter a number with maximum 11 digits")
                    
            case "3":
                name = input("Enter the contact name to update: ")
                if name in agenda:
                    phone = input("Enter the contact number: ")
                    if phone.isdigit() and 0 < len(phone) <= 11:
                        agenda[name] = phone
                        print(f"Contact {name} updated successfully.")
                    else:
                        print("Enter a number with maximum 11 digits")
                else:
                    print(f"{name} does not exist in the contact list")
                   
            case "4":
                name = input("Enter the contact name to delete: ")
                if name in agenda:
                    del agenda[name]
                    print(f"Contact {name} deleted successfully.")
                else:
                    print(f"{name} does not exist in the contact list")
                   
            case "5":
                print("Leaving the agenda")
                break
                
            case _:
                print("Invalid option, choose an option between 1 - 5")
               

my_agenda()

