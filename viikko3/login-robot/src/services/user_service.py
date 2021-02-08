from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)
        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        
        existing_user = self._user_repository.find_by_username(username)
        if existing_user:
            raise Exception(
                f"User with username {username} already exists"
        )

        if len(username)<3:
            raise Exception(
                f"Username must be at least 3 characters long"
        )
        pattern = re.compile("[a-z]+")
        if pattern.fullmatch(username)==None:
            raise Exception(
                f"Username can only consists of characters a-z"
        )
        if len(password)<8:
            raise Exception(
                f"Password must be at least 8 characters long"
        )
        pattern = re.compile("[A-Za-z]+")
        if pattern.fullmatch(password) != None:
            raise Exception(
            f"Password must contain numbers"
        )




