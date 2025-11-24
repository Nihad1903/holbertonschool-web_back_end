#!/usr/bin/env python3
"""
Class to manage the API authentication
"""

from flask import request
from typing import List, TypeVar
import os

User = TypeVar('User')


class Auth():
    """ Class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ function require_auth
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ function authorization_header
        """
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> User:
        """ function current_user
        """
        return None

    def session_cookie(self, request=None):
        """ Returns the value of the session cookie from the request
        """
        if request is None:
            return None

        session_name = os.getenv('SESSION_NAME', '_my_session_id')

        return request.cookies.get(session_name)
