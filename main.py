from UrnaEletronica import UrnaEletronica
from CandidatoNaoExistente import CandidatoNaoExistente
from Candidato import Candidato
from Partido import Partido
from Eleitor import Eleitor
from Voto import Voto

from datetime import datetime

urna = UrnaEletronica()

sair = "nao"

while(sair == "nao"):
    print("Bem vindo a Urna Eletronica")
    
    nome = input("Digite o seu nome: ")
    tituloEleitor = input("Digite o numero do título de eleitor")
    numero = int(input("Digite o numero do candidato que deseja votar para presidente: "))
    
    try:
        candidato = urna.recuperarCandidato(numero)
        eleitor = Eleitor(nome, tituloEleitor)
        voto = Voto(datetime.now(), candidato, eleitor)

        urna.adicionarVoto(voto)
        sair = input("Daseja sair? (sim ou não)")
        
    except CandidatoNaoExistente:
        print("Candidato não existente, tente novamente")
        
print("Votação Encerrada")

print("----------------")
todosOsVotos = urna.listarTodosOsVotos()
print("Total de Votos: ",len(todosOsVotos))
for voto in todosOsVotos:
    print(voto)

print("----------------")
lula = urna.recuperarCandidato(13)
votosLula = urna.listarVotos(lula)
print("Total de Votos de Fernando Haddad: ", len(votosLula))
for voto in votosLula:
    print(voto)

print("----")
FHC = urna.recuperarCandidato(45)
votosFHC = urna.listarVotos(FHC)
print("Total de Votos de Jair Bolsonaro: ", len(votosFHC))
for voto in votosFHC:
    print(voto)