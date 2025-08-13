""" 
"""

from wanshitong.general.errors.json_mssgs import *
from wanshitong.general.errors.errors import *

__all__: list[str] = [
    "json_mssgs",
    "errors",
]


def get_error(module: str, err_name: str, return_code: bool = False) -> str:
    
    #  Check if the arguments type are correct.
    assert isinstance(module, str),\
        ""
        
    assert isinstance(err_name, str),\
        ""
        
    assert isinstance(return_code, bool),\
        ""
    
    
    __err_module = _ERRORS.get(module)
    #  Check if the key exists, 
    assert __err_module is not None,\
        f'There isn\'t any module called "{module}".'
        
    __error = __err_module.get(err_name)
    #  Check if the key exists, the value to return is the error dictionary.
    assert __error is not None,\
        f'There isn\'t any Error called "{err_name}".'
        
        
    if not return_code:
        __error_text = __error.get('text')
        #  Check if the key exists, the value to return is the error text.
        assert __error_text is not None,\
            f'System ERROR,The text error is empty.'
            
        #  Check if the error text is an string.
        assert isinstance(__error_text, str), \
            "System ERROR, The text error isn't a string."
            
        return __error_text
    
    
    elif return_code:
        __error_code = __error.get('code')
        #  Check if the key exists, the value to return is the error text.
        assert __error_code is not None,\
            f'System ERROR,The code error is empty.'
            
        #  Check if the error text is an string.
        assert isinstance(__error_code, str), \
            "System ERROR, The code error isn't a string."
            
        return __error_code

