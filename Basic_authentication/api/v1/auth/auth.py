#!/usr/bin/env python3
"""
Authentication module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class for API authentication management
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path
        """

        if path is None or excluded_paths is None or not excluded_paths:
            return True

        # Normalize paths by ensuring they end with '/'
        normalized_path = path if path.endswith('/') else path + '/'
        normalized_excluded = [
            p if p.endswith('/') else p + '/' for p in excluded_paths
        ]

        return normalized_path not in normalized_excluded

    def authorization_header(self, request=None) -> str:
        """ Returns the Authorization header if present, otherwise None """
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None for now (to be implemented later) """
        return None
