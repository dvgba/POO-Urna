class Eleitor:
    def __init__(self, nome, tituloEleitor):
        self.nome = nome
        self.tituloEleitor = tituloEleitor
        
    def __str__(self):
        return f"nome={self.nome}, Titulo de eleitor={self.tituloEleitor}"