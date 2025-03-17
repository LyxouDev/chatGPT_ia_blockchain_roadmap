# **Mini-Projet 1 : Générateur de mots de passe sécurisé**

## **Objectif**
Développer un programme en Python capable de générer des mots de passe sécurisés en fonction des critères choisis par l'utilisateur.

---

## **Compétences visées**
- Utilisation des bibliothèques Python standard (`random`, `secrets`, `string`)
- Manipulation des chaînes de caractères
- Gestion des entrées utilisateur
- Application des bonnes pratiques de sécurité pour la génération de mots de passe

---

## **Consignes**

### **1. Fonctionnalités obligatoires**
Le programme doit permettre :
- De générer un mot de passe aléatoire.
- De choisir la longueur du mot de passe (minimum 8 caractères, recommandé 12 ou plus).
- D’inclure ou non :
  - Des lettres majuscules
  - Des lettres minuscules
  - Des chiffres
  - Des caractères spéciaux (ex: `@`, `#`, `!`, `%`, etc.)
- D’afficher le mot de passe généré.

### **2. Fonctionnalités optionnelles (pour aller plus loin)**
- Assurer qu’au moins un caractère de chaque type sélectionné est inclus.
- Ajouter une option permettant de générer plusieurs mots de passe en une seule exécution.
- Ajouter une option pour copier automatiquement le mot de passe généré dans le presse-papier (`pyperclip`).
- Vérifier la robustesse du mot de passe généré avec un indicateur de force.
- Enregistrer les mots de passe générés dans un fichier (option sécurisée).

---

## **Contraintes techniques**
- Le programme doit être écrit en Python 3.
- Il doit utiliser la bibliothèque `secrets` pour garantir la sécurité (éviter `random` pour la génération des caractères).
- L’interface peut être en ligne de commande ou avec une interface graphique simple (`Tkinter` ou `PyQt` pour les plus avancés).

---

## **Structure recommandée du programme**
1. **Demander les préférences utilisateur** (longueur, types de caractères).
2. **Valider les entrées utilisateur** (s’assurer qu’au moins un type de caractère est sélectionné).
3. **Générer le mot de passe** selon les critères.
4. **Afficher le mot de passe généré**.
5. **(Optionnel) Copier dans le presse-papier ou enregistrer dans un fichier**.

---

## **Exemple de sortie attendue**
```plaintext
Bienvenue dans le générateur de mots de passe sécurisé !
Entrez la longueur du mot de passe : 12
Inclure des majuscules ? (o/n) : o
Inclure des minuscules ? (o/n) : o
Inclure des chiffres ? (o/n) : o
Inclure des caractères spéciaux ? (o/n) : o

Mot de passe généré : G@7xYp!s3dLw
