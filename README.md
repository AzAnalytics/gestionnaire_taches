# ✅ Gestionnaire de tâches en console (Python)

Ce projet est une application console simple en Python pour gérer tes tâches quotidiennes.  
Elle permet d’ajouter, modifier, supprimer, marquer comme terminées ou non terminées, et filtrer les tâches.  
Les données sont stockées dans un fichier JSON pour persistance.

---

## 🚀 Fonctionnalités

- 📝 Ajouter une nouvelle tâche
- 📋 Lister toutes les tâches
- ✅ Marquer une tâche comme terminée
- 🔁 Marquer une tâche comme non terminée
- ✏️ Modifier une tâche
- ❌ Supprimer une tâche
- 🔍 Filtrer les tâches :
  - Afficher uniquement les tâches terminées
  - Afficher uniquement les tâches non terminées
- 💾 Persistance des données dans `taches.json`
- 🔐 Initialisation automatique du fichier JSON

---

## 🗂️ Structure du projet

gestionnaire_taches/
│
├── main.py              # Menu principal en console (interface utilisateur)
├── gestionnaire.py      # Toutes les fonctions de gestion des tâches
├── taches.json          # Fichier de stockage des tâches (créé automatiquement)
└── README.md            # Documentation du projet

---

## ▶️ Lancer le projet

1. Clone ce dépôt :

git clone https://github.com/AzAnalytics/gestionnaire-taches.git
cd gestionnaire-taches

2.Exécute le programme :

python main.py


3.✅ Exemples d'utilisation

=== GESTIONNAIRE DE TÂCHES ===
1. Ajouter une tâche
2. Voir toutes les tâches
3. Marquer une tâche comme terminée
