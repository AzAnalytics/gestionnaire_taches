import json
import os

FICHIER_TACHES = "taches.json"

# Chargement des tâches depuis le fichier JSON
def charger_taches():
    if not os.path.exists(FICHIER_TACHES):
        return []
    with open(FICHIER_TACHES, "r", encoding="utf-8") as f:
        contenu = f.read().strip()
        if not contenu:
            return []  # fichier vide, on retourne une liste vide
        return json.loads(contenu)

# Sauvegarde des tâches dans le fichier JSON
def sauvegarder_taches(taches):
    with open(FICHIER_TACHES, "w", encoding="utf-8") as f:
        json.dump(taches, f, indent=4, ensure_ascii=False)

# Ajouter une nouvelle tâche
def ajouter_tache(titre):
    taches = charger_taches()
    nouvelle = {
        "titre": titre,
        "terminee": False
    }
    taches.append(nouvelle)
    sauvegarder_taches(taches)
    print("✅ Tâche ajoutée !")

# Marquer une tâche comme terminée
def marquer_terminee(index):
    taches = charger_taches()
    if 1 <= index <= len(taches):
        taches[index - 1]["terminee"] = True
        sauvegarder_taches(taches)
        print("✅ Tâche marquée comme terminée !")
    else:
        print("❌ Numéro de tâche invalide.")

#Supprimer une tâche
def supprimer_tache(index):
    taches = charger_taches()
    if 1 <= index <= len(taches):
        del taches[index - 1]
        sauvegarder_taches(taches)
        print("✅ Tâche supprimée !")
    else:
        print("❌ Numéro de tâche invalide.")

# Modifier une tâche
def update_tache(index):
    taches = charger_taches()
    if 1 <= index <= len(taches):
        titre = input("Nouveau titre de la tâche : ")
        taches[index - 1]["titre"] = titre
        sauvegarder_taches(taches)
        print("✅ Tâche modifiée !")
    else:
        print("❌ Numéro de tâche invalide.")

# Marquer une tâche comme non terminée
def marquer_non_terminee(index):
    taches = charger_taches()
    if 1 <= index <= len(taches):
        taches[index - 1]["terminee"] = False
        sauvegarder_taches(taches)
        print("✅ Tâche marquée comme non terminée !")
    else:
        print("❌ Numéro de tâche invalide.")

# Afficher les tâches en cours
def afficher_taches():
    taches = charger_taches()
    if not taches:
        print("Aucune tâche pour le moment.")
    else:
        for i, t in enumerate(taches, 1):
            statut = "✅" if t["terminee"] else "⏳"
            print(f"{i}. {t['titre']} {statut}")

# Afficher les tâches terminées
def afficher_taches_terminees():
    taches = charger_taches()
    if not taches:
        print("Aucune tâche pour le moment.")
    else:
        for i, t in enumerate(taches, 1):
            if t["terminee"]:
                statut = "✅"
                print(f"{i}. {t['titre']} {statut}")
            else:
                print("Aucune tâche terminée pour le moment.")
                break

# Afficher les tâches non terminées
def afficher_taches_non_terminees():
    taches = charger_taches()
    if not taches:
        print("Aucune tâche pour le moment.")
    else:
        for i, t in enumerate(taches, 1):
            if not t["terminee"]:
                statut = "⏳"
                print(f"{i}. {t['titre']} {statut}")
            else:
                print("Aucune tâche non terminée pour le moment.")
                break

# Afficher les tâches
def afficher_taches():
    taches = charger_taches()
    if not taches:
        print("Aucune tâche pour le moment.")
    else:
        for i, t in enumerate(taches, 1):
            statut = "✅" if t["terminee"] else "⏳"
            print(f"{i}. {t['titre']} {statut}")

# Initialisation des tâches
def initialiser_fichier():
    if not os.path.exists(FICHIER_TACHES):
        with open(FICHIER_TACHES, "w", encoding="utf-8") as f:
            f.write("[]")
            print("Fichier de tâches initialisé.")
    else:
        print("Fichier de tâches déjà existant.")

