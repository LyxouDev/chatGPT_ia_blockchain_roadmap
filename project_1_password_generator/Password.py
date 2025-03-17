import random
import string

class Password:
    def __init__(self, length: int, upper_letters: bool= True, lower_letters: bool= True, digits: bool= True, ponctuation: bool= True) -> None:
        """
            Initialise une instance de la classe Password.

            Args:
                length (int): La longueur du mot de passe à générer.
                upper_letters (bool, optional): True pour inclure des lettres majuscules, False sinon. Par défaut à True.
                lower_letters (bool, optional): True pour inclure des lettres minuscules, False sinon. Par défaut à True.
                digits (bool, optional): True pour inclure des chiffres, False sinon. Par défaut à True.
                ponctuation (bool, optional): True pour inclure des caractères spéciaux, False sinon. Par défaut à True.

            Attributes:
                password (str): Le mot de passe généré.
                is_valid (bool): True si le mot de passe est valide, False sinon.

            Returns:
                None
        """
        self.password = self.generate_password(length, upper_letters, lower_letters, digits, ponctuation)
        self.is_valid = self.validate_password()

    def validate_password(self) -> bool:
        """
            Vérifie si le mot de passe généré est valide.
            
            Returns:
                bool: True si le mot de passe est valide, False sinon.
        """
        if len(self.password) < 8:
            return False
        if not any(char.isdigit() for char in self.password) and self.digits:
            return False
        if not any(char.isupper() for char in self.password) and self.upper_letters:
            return False
        if not any(char.islower() for char in self.password) and self.lower_letters:
            return False
        if not any(char in string.punctuation for char in self.password) and self.ponctuation:
            return False
        return True

    def generate_password(self, length: int, upper_letters: bool, lower_letters: bool, digits: bool, punctuation: bool) -> str:
        """
            Génère un mot de passe aléatoire de la longueur spécifiée.

            Args:
                length (int): La longueur du mot de passe à générer.

            Returns:
                str: Le mot de passe généré.
        """
        list_letters = string.ascii_letters if upper_letters and lower_letters else string.ascii_lowercase if lower_letters else string.ascii_uppercase if upper_letters else ''
        list_digits = string.digits if digits else ''
        list_punctuation = string.punctuation if punctuation else ''
        return ''.join(random.choices(list_letters + list_digits + list_punctuation, k=length))
    