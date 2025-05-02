class User:
    def __init__(self, email: str, password: str):
        """
        Initialize a User instance with an email and password.

        Args:
            email (str): The user's email address.
            password (str): The user's password.
        """

        self.email = email
        self.password = password
