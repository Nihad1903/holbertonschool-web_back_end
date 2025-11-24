#!/usr/bin/env python3
""" Module of basic authentification """
from typing import TypeVar
import base64
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """ Basic authentification class """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Extracts and returns the Base64 part of the Authorization
            header for Basic Authentication.
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None

        # Check if the header starts with 'Basic ' (with space at the end)
        if not authorization_header.startswith('Basic '):
            return None

        # Extract the Base64 part after 'Basic ' (which is 6 characters long)
        base64_credentials = authorization_header[6:].strip()

        return base64_credentials

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decodes a Base64-encoded string and returns it as UTF-8 string """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extracts user email and password from a decoded Base64
            authorization header.
        """
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on email and password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Search for the user in the database
        user_list = []
        try:
            user_list = User.search({"email": user_email})
            if user_list == []:
                return None
        except Exception:
            return None

        # Assuming `search` returns a list of users,
            # we should take the first user.
        user = user_list[0]

        # Check if the provided password matches the user's stored password
        if user.is_valid_password(user_pwd):
            return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the User instance for a request.
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth_header = self.extract_base64_authorization_header(
            auth_header)
        if base64_auth_header is None:
            return None

        decoded_auth_header = self.decode_base64_authorization_header(
            base64_auth_header)
        if decoded_auth_header is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(
            decoded_auth_header)
        if user_email is None or user_pwd is None:
            return None

        user = self.user_object_from_credentials(user_email, user_pwd)
        return user