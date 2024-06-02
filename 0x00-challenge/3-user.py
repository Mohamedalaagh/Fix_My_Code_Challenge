#!/usr/bin/python3
"""
User Model
"""
import hashlib
import uuid


class User:
    """
    User class to manage user data and password hashing.
    
    Attributes:
        id (str): Public string unique identifier (UUID).
        __password (str): Private string to store the hashed password in MD5.
    """

    __password = None

    def __init__(self):
        """
        Initialize a new user.
        
        The constructor assigns a unique UUID to the `id` attribute.
        """
        self.id = str(uuid.uuid4())

    @property
    def password(self):
        """
        Password getter.
        
        Returns:
            str: The hashed password.
        """
        return self.__password

    @password.setter
    def password(self, pwd):
        """
        Password setter.
        
        This setter hashes the password using MD5 and stores it in the 
        `__password` attribute.
        
        Args:
            pwd (str): The password to hash and store.
        
        Sets to `None` if `pwd` is `None` or not a string.
        """
        if pwd is None or not isinstance(pwd, str):
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd):
        """
        Validate the provided password.
        
        This method compares the provided password with the stored hashed password.
        
        Args:
            pwd (str): The password to validate.
        
        Returns:
            bool: `True` if the provided password matches the stored hashed password,
                  `False` otherwise.
        
        Validation fails if `pwd` is `None`, not a string, or if no password is set.
        """
        if pwd is None or not isinstance(pwd, str):
            return False
        if self.password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest().lower() == self.password


if __name__ == '__main__':
    print("Test User")

    user_1 = User()
    if user_1.id is None:
        print("New User should have an id")

    user_2 = User()
    if user_1.id == user_2.id:
        print("User.id should be unique")

    u_pwd = "myPassword"
    user_1.password = u_pwd
    if user_1.password == u_pwd:
        print("User.password should be hashed")

    if user_2.password is not None:
        print("User.password should be None by default")

    user_2.password = None
    if user_2.password is not None:
        print("User.password should be None if set to None")

    user_2.password = 89
    if user_2.password is not None:
        print("User.password should be None if set to an integer")

    if not user_1.is_valid_password(u_pwd):
        print("is_valid_password should return True if it's the correct password")

    if user_1.is_valid_password("Fakepwd"):
        print("is_valid_password should return False if it's not the correct password")

    if user_1.is_valid_password(None):
        print("is_valid_password should return False if compared with None")

    if user_1.is_valid_password(89):
        print("is_valid_password should return False if compared with an integer")

    if user_2.is_valid_password("No pwd"):
        print("is_valid_password should return False if no password set before")

