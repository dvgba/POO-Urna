## Urna Eletrônica

Exercicio de introdução a Programação Orientada a Objetos

Com base no diagrama abaixo:

```
classDiagram
    UrnaEletronica <|-- Candidato
    UrnaEletronica <|-- Partido

    UrnaEletronica : candidatos Candidato[]
    UrnaEletronica : votos Votos []
    UrnaEletronica: secao Integer
    UrnaEletronica: zona Integer
    UrnaEletronica: inicializar()
    UrnaEletronica: adicionarVoto
    UrnaEletronica: listarTodosOsVotos
    UrnaEletronica: listarVoto

    Candidato <| -- Voto
    Voto <| -- Eleitor
    
    class Candidato{
      String nome
    
    }
    class Partido{
      int numero
      String nome
    }

    class Eleitor{
      String nome
      String tituloEleitor
    }

    class Voto{
      datetime data
    
    }
```

O exercicio foi resolvido pelo https://ifpb.github.io/intin-poo/