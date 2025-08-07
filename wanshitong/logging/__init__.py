""" 
"""

__all__: list[str] = [
    
]


class Logger:
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._paths = {}
        else:
            raise Exception("There is a instance of Logger")
        return cls._instance
