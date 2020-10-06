from models import Pessoas

#insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Luiza', idade=22)
    print(pessoa)
    pessoa.save()

#realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Ana').first()
    print(pessoa.idade)

#altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ana').first()
    pessoa.idade = 20
    pessoa.save()


if __name__=='__main__':
    #insere_pessoas()
    altera_pessoa()
    consulta_pessoas()