""" 
"""
from pathlib import Path

__all__: list[str] = [
    
]

class __ClusterNode:
    
    def __init__(self, path: str, name: str, ):
        assert isinstance(path, str), "The path it must be a String"
        assert isinstance(name, str), "The name it must be a String"
        self.path = Path(path)
        assert self.exists(), "The path doesn't exists."
        self.name = name
        
    def exists(self):
        return self.path.exists()
    

class __Cluster:
    
    def __init__(self, path: str, name: str, ):
        assert isinstance(path, str), "The path it must be a String"
        assert isinstance(name, str), "The name it must be a String"
        self.path = Path(path)
        assert self.exists(), "The path doesn't exists."
        assert self.path.is_dir(), "The path needs to be a Directory."
        self.name = name
        
    def exists(self):
        return self.path.exists()
    

class DocManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._paths = {}
        return cls._instance
    
    
    def __init__(self):
        ...