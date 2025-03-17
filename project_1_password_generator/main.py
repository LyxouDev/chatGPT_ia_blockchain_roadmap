from Password import Password

if __name__ == '__main__':
    password_ok = False

    while True:
        upper_letters = bool(input("Voulez-vous des lettres majuscules ? (Oui/Non) : ").lower() != 'non')
        lower_letters = bool(input("Voulez-vous des lettres minuscules? (Oui/Non) : ").lower()!= 'non')
        digits = bool(input("Voulez-vous des chiffres? (Oui/Non) : ").lower()!= 'non')
        ponctuation = bool(input("Voulez-vous des caractères spéciaux? (Oui/Non) : ").lower()!= 'non')

        if upper_letters or lower_letters or digits or ponctuation:
            break
        else:
            print("########### Au moins un type de caractère doit être sélectionné. ###########")

    while not password_ok:
        length = int(input("Longueur souhaitée du mot de passe (8 caractères minimum) : "))
        if length >= 8:
            password = Password(length, upper_letters, lower_letters, digits, ponctuation)
            print(password.password) if password.is_valid else print("########### Mot de passe généré invalide. ###########")
            password_ok = password.is_valid
        else:
            print("########### Le mot de passe doit avoir une longueur minimum de 8 caractères. ###########")
    