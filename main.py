import gestionnaire

def main():

    gestionnaire.initialiser_fichier()
    
    while True:
        print("\n=== GESTIONNAIRE DE TÂCHES ===")
        print("1. Ajouter une tâche")
        print("2. Voir toutes les tâches")
        print("3. Marquer une tâche comme terminée")
        print("4. Marquer une tâche comme non terminée")
        print("5. Supprimer une tâche")
        print("6. Modifier une tâche")
        print("7. Voir uniquement les tâches terminées")
        print("8. Voir uniquement les tâches non terminées")
        print("9. Quitter")

        choix = input("Ton choix : ")

        match choix:
            case "1":
                titre = input("Titre de la tâche : ")
                gestionnaire.ajouter_tache(titre)

            case "2":
                gestionnaire.afficher_taches()

            case "3":
                try:
                    index = int(input("Numéro de la tâche à marquer comme terminée : "))
                    gestionnaire.marquer_terminee(index)
                except ValueError:
                    print("❌ Veuillez entrer un nombre valide.")

            case "4":
                try:
                    index = int(input("Numéro de la tâche à marquer comme non terminée : "))
                    gestionnaire.marquer_non_terminee(index)
                except ValueError:
                    print("❌ Veuillez entrer un nombre valide.")

            case "5":
                try:
                    index = int(input("Numéro de la tâche à supprimer : "))
                    gestionnaire.supprimer_tache(index)
                except ValueError:
                    print("❌ Veuillez entrer un nombre valide.")

            case "6":
                try:
                    index = int(input("Numéro de la tâche à modifier : "))
                    gestionnaire.update_tache(index)
                except ValueError:
                    print("❌ Veuillez entrer un nombre valide.")

            case "7":
                gestionnaire.afficher_taches_terminees()

            case "8":
                gestionnaire.afficher_taches_non_terminees()

            case "9":
                print("👋 À bientôt !")
                break

            case _:
                print("❌ Choix invalide. Réessaie.")

if __name__ == "__main__":
    main()
