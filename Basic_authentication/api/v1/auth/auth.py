#!/usr/bin/env python3
'''Auth class module
'''
from flask import request
from typing import List, TypeVar


class Auth():
    '''Auth Class'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''Require Auth function
        '''
        if not path:
            return True

        elif not excluded_paths:
            return True

        elif path in excluded_paths or (path + '/') in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        '''Authorization Header'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''Current User'''
        return None
