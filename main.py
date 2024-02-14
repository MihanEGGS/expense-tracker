#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 

#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# - iespēja atlasīt 10 lielākus izdevumus
# - iespēja atlasīt 10 mazākus izdevumus
# - iespēja apskatīt vidējo izdevumu summu
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#
import json
a = 0
expenses = []
TotalSum = 0
# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)
expenses_file = open('expenses.json') # opening JSON file
expenses = json.load(expenses_file) # returns JSON object as a dictionary
expenses_file.close()
while True:
    print("1. ievadīt izdevumus: nosaukumu, summu un kategoriju ")
    print("2. atspoguļot uz ekrāna visus izdevumus ")
    print("3. iespēja atlasīt 10 lielākus izdevumus ")
    print("4. iespēja atlasīt 10 mazākus izdevumus ")
    print("5. iespēja apskatīt vidējo izdevumu summu ")
    print("e. Exit ")
    command = input("\nChoose command:")
    if command == "1":
        Name = input ("Ievadiet nosaukumu ")
        Summ = int(input ("Ievadiet summu "))
        Kategorie = input("Ievadiet kategoriju ") 
        category = {
            "Name" : Name,
            "Sum" : Summ,
            "Kategorie" : Kategorie

        }
        expenses.append(category)
    elif command == "2":
        print(expenses)
    elif command == "3":
        def sortede(expenses):
            return int(expenses["Sum"])
        neu = sorted(expenses, key =sortede, reverse = True)
        for x in neu[:10]:
            print(x)
    elif command == "4":
        def sortede(expenses):
            return int(expenses["Sum"])
        neu = sorted(expenses, key =sortede)
        for x in neu[:10]:
            print(x)
    elif command == "5":
        for i in expenses:
            a += 1
            TotalSum = TotalSum + i["Sum"]
        AverageRaw = TotalSum/a
        Average = round(AverageRaw, 2)
        print("Average sum is ", Average)
    if command == "e":
        print("Exiting...")
        break

# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)
with open("expenses.json", "w") as file: 
    json.dump(expenses, file)

