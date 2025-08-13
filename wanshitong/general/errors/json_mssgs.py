""" 
"""

from typing import Literal


__all__: list[str] = [
    "error_text_and_description",
    "module_group_errors",
    "error_json",
    "_ERRORS"
]

type error_text_and_description = dict[str, str]
type module_group_errors = dict[str,error_text_and_description]
type error_json = dict[str, module_group_errors]


class Errors(): 
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._paths = {}
        return cls._instance
    
    def __init__(self):
        self.ERRORS = __ERRORS
        
    def add_error_file(self, errors_dict: error_json):
        # TODO: Validar que errors_dict sea diccionario
        # TODO: Validar que errors_dict sus codigos no sean codigos existentes o repetidos
        self.ERRORS.update(errors_dict)
        

__ERRORS: error_json = {
    "logging": {
        "assert_path_format": {
            "code": "",
            "text": "",
            "description": "",
            },
        "assert_path_format": {
            "code": "",
            "text": "",
            "description": "",
            },
        },
    "main": {
        "example": {
            "code": "",
            "text": "",
            "description": "",
            }
        },
    
    "errors": {
        "example": {
            "code": "",
            "text": "",
            "description": "",
            }
        }
    
}