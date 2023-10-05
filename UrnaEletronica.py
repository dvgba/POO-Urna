from Candidato import Candidato
from Partido import Partido
from CandidatoNaoExistente import CandidatoNaoExistente


class UrnaEletronica:
    def __init__(self):
        self.candidatos = []
        self.voto = []
        self.__inicializar()

    def __inicializar(self):
        pt = Partido(13, "PT")
        candidato01 = Candidato("Luis Inacio Lula da Silva", pt)
        psdb = Partido(45, "PSDB")
        candidato02 = Candidato("Fernando Henrique Cardoso", psdb)

        self.candidatos.append(candidato01)
        self.candidatos.append(candidato02)

        self.secao = 123
        self.zona = 321

    def adicionarVoto(self, voto):
        self.votos.append(voto)

    def listarTodosOsVotos(self):
        return self.votos

    def listarVotos(self, candidato):
        votosCandidato = []

        for voto in self.votos:
            if voto.candidato.partido.numero == candidato.partido.numero:
                votosCandidato.append(voto)
        return votosCandidato

    def recuperarCandidato(self, numero):
        candidato = None
        for c in self.candidatos:
            if c.numero == numero:  # Comparar com o número do candidato, não do partido
                candidato = c

        if candidato is None:
            raise CandidatoNaoExistente

        return candidato
