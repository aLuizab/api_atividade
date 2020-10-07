from models import Pessoas

#insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Botelho', idade=44)
    print(pessoa)
    pessoa.save()

#realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Luiza').first()
    print(pessoa.idade)

#altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ana').first()
    pessoa.nome = 'Botelho'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Luiza').first()
    pessoa.delete()

if __name__=='__main__':
    #insere_pessoas()
    #altera_pessoa
    #exclui_pessoa()
    consulta_pessoas()