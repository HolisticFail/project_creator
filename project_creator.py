#This script allow you to create new project (folder / files)
from pathlib import Path

menu = [
    "Créer un dossier & un fichier",
    "Créer le projet",
    "Quitter",
]
separator = "-"*50
menu_nbr = len(menu)
project_creator = dict()

chemin = Path.home() / "Desktop" 
while True: 
    print()
    print(separator)
    print()
    #Menu iteration (also put a number before each menu)
    for i, menu_iteration in enumerate(menu, 1):
        print(f"{i}. {menu_iteration}")
    choice_user = input(f"Indiquez votre choix entre 1 et {menu_nbr} : ")
    #loop in case invalid input from user
    if not (choice_user.isdigit() and 1 <= int(choice_user) <= menu_nbr):
        print(f"Veuillez choisir parmi les {menu_nbr} choix suivants : ")
    #name your folder & name your file
    elif choice_user == "1":
        folder_creation = input("Indiquez un nom de dossier : ")
        file_creation = input("Indiquez un nom de fichier (ne pas oublier l'extension) : ")  
    #create folder and file on the desktop
    elif choice_user == "2":
        #import key and value in dict
        project_creator[folder_creation] = [file_creation]
        #scan the dict
        for main_folder, main_file in project_creator.items():
            #creation of folder and file on desktop
            for file in main_file:
                folder_path = chemin / main_folder 
                file_path = chemin / main_folder / file
                folder_path.mkdir(exist_ok=True, parents=True)
                file_path.touch()
                print("Nouveau projet créé !")

    else:
        break

print("Au revoir !")

