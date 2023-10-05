class Partido:
    def __init__(self, numero, nome):
        self.nome = nome
        self.numero = numero
        
    def __str__(self):
        return f"numero={self.numero}, nome={self.nome}"
    