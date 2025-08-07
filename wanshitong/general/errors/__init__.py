""" 
"""

__all__: list[str] = [
    
]

class InstanceError(Exception):
    """Excepción lanzada cuando ocurre un error relacionado con instancias."""
    pass

    def __init__(self, message="Error de instancia."):
        self.message = message
        super().__init__(self.message)
        
    
class SingletonError(InstanceError):
    """" Error al intentar de instanciar un Singleton más de una vez """
    
    ...