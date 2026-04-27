# função para calcular a média
def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media

# função para verificar aprovação
def verificar_aprovacao(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

# função para gerar relatório
def gerar_relatorio(nome, media, situacao):
    print("Aluno:", nome)
    print("Média:", media)
    print("Situação:", situacao)

# exemplo de uso
nome = "João"
nota1 = 7
nota2 = 5

media = calcular_media(nota1, nota2)
situacao = verificar_aprovacao(media)

gerar_relatorio(nome, media, situacao)