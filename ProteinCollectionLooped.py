## Group Exercise 05 - Loops and Lists

# This program should create again a nested dictionary with a biochemical or biological background.
# It should contain at least three different lists.
# Create an options menu similar to Group Exercise 04. (Let the user either display, manipulate or add an entry to your main dictionary)
# If the user wants to look at the contents of a list, use a loop.
# Include an option that allows the user to see which entries are already in your main dictionary (use a loop again).
# To make sure that the inputs of the user are possible use while loops so that
# the program continues only after the input of the user is correct.

import json

Proteins = {}
Proteins["PRDM1"] = {"Name":"PR domain zinc finger protein 1", "Length":825, "Function":"Transcription regulation", "Location": "Chromosome 6"}
Proteins["IRF1"] = {"Name":"Interferon regulatory factor 1", "Length":325, "Function":"Antiviral defense", "Location":"Chromosome 5"}
Proteins["STAT1"] = {"Name":"Signal transducer and activator of transcription 1" , "Length":750, "Function":"Antiviral defense", "Location":"Chromosome 2"}
Proteins["MCM5"] = {"Name":"Minichromosome maintenance complex component 5", "Length":734, "Function":"DNA replication", "Location": "Chromosome 22"}
Proteins["ORC2"] = {"Name":"Origin recognition complex subunit 2", "Length":577, "Function":"DNA replication", "Location":"Chromosome 2"}
Proteins["CDC6"] = {"Name":"Cell division control protein 6 homolog", "Length":560, "Function": "Cell division", "Location":"Chromosome 17"}
Proteins["PSKH1"] = {"Name":"Serine/threonine-protein kinase H1", "Length":424, "Function":"Kinase", "Location":"Chromosome 16"}
Proteins["MAPK2"] = {"Name":"Mitogen-activated protein kinase 2", "Length":400, "Function":"Kinase", "Location":"Chromosome 1"}

print("Here is the Protein dictionary:")
tmp = json.dumps(Proteins, indent=4)
print(tmp)
while True:
    user_op = input("\nWhat action would you like to perform for the dictionary? \nChoose either search, add, delete or change.\nType q to exit the program.\n")
# Adding to the dictionary. Either a whole new protein or add a new key-value pair to an existing protein
    if user_op == "add":
        user_input = input("Do you want to add a whole new protein (new) or add information to an existing protein (add)?\n")
        if user_input == "new":
            print("Please provide the information of the protein you want to add.")
            prot_abbr = input("Abbreviation of the protein: ")
            if prot_abbr in Proteins:
                print(f"{prot_abbr} already exists in the dictionary! It will not be added to avoid errors.")
            else:
                prot_name = input("Full name: ")
                prot_length = int(input("Length (Amino acids): "))
                prot_function = input("Function: ")
                prot_location = int(input("Location (Chromosome): "))
                Proteins[prot_abbr] = {"Name":prot_name, "Length":prot_length, "Function":prot_function, "Location":(f"Chromosome {prot_location}")}

                tmp = json.dumps(Proteins[prot_abbr], indent=4)
                print(f"This is the new entry for {prot_abbr}: \n{tmp}")
        elif user_input == "add":
            print("Please provide the information you want to add. Choose a protein from the following list:")
            print(*list(Proteins.keys()), sep=', ')
            prot_abbr = input("Abbreviation of the protein: ")
            if prot_abbr in Proteins:
                prot_key = input("Key: ")
                prot_value = input("Value: ")
                if prot_value.isdigit():
                    prot_value = int(prot_value)
                Proteins[prot_abbr][prot_key] = prot_value

                tmp = json.dumps(Proteins[prot_abbr], indent=4)
                print(f"This is the updated entry for {prot_abbr}: \n{tmp}")
            else:
                print(f"{prot_abbr} was not found in the dictionary!")
        else:
            print("Invalid Input")
# Deleting an entry. Asks the user for the abbreviation of the protein, which should be deleted.
    elif user_op == "delete":
        print("Which protein do you want to delete? Choose a protein from the following list:")
        print(*list(Proteins.keys()), sep=', ')
        prot_abbr= input("Abbreviation of the protein: ")
        if prot_abbr in Proteins:
            del Proteins[prot_abbr]

            tmp = json.dumps(Proteins, indent=4)
            print(f"This is the new dictionary: \n{tmp}")
        else:
            print(f"{prot_abbr} was not found in the dictionary!")
# Changing entries. Can only change values and not keys.
    elif user_op == "change":
        print("Which protein do you want to change? Choose from the following list:")
        print(*list(Proteins.keys()), sep=', ')
        prot_abbr = input("Abbreviation of the protein: ")
        if prot_abbr in Proteins:
            print("Choose from the following list, which part you want to change:")
            print(*list(Proteins[prot_abbr].keys()), sep=', ')
            prot_key = input()
            if prot_key in list(Proteins[prot_abbr].keys()):
                prot_value = input("New information: ")
                if prot_value.isdigit():
                    prot_value = int(prot_value)
                Proteins[prot_abbr][prot_key] = prot_value

                tmp = json.dumps(Proteins, indent=4)
                print(f"This is the new dictionary: \n{tmp}")
            else:
                print(f"{prot_key} is no available key in {prot_abbr}.")
        else:
            print(f"{prot_abbr} was not found in the dictionary!")
# Exit the program
    elif user_op == "q":
        exit()
# Search for a protein
    elif user_op == "search":
        prot_abbr = input("Which protein are you looking for? \nAbbreviation: ")
        if prot_abbr in Proteins:
            tmp = json.dumps(Proteins[prot_abbr], indent=4)
            print(f"Here is the entry for {prot_abbr}: \n{tmp}")
        else:
            print(f"{prot_abbr} was not found in the dictionary!")
# Invalid input if none of the above are true
    else:
        print("Invalid Input")
