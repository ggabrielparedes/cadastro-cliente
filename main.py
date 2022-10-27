pessoa = []
endereco = []


def menu():
    print('************* MENU DE CADASTRO *************')
    print('* [1] Cadastrar Usuário                    *')
    print('* [2] Consultar Usuário                    *')
    print('* [3] Consultar Banco de Dados             *')
    print('* [0] Sair                                 *')
    print('********************************************')
    v = input('Escolha [0] [1] [2] [3] >> ')
    match v:
        case '0':
            exit()
        case '1':
            cadastro()
        case '2':
            consultar()
        case '3':
            l = input('Insira o login do usuário: ')
            while not validar(l):
                l = input('Login não encontrada tente novamente: ')
            consultar_db(l)
        case _g:
            print('Valor invalido')
            menu()


def cadastro():
    while True:
        dados = {}
        dados['nome'] = (input('Nome >> '))

        # Verificação de duplicata de login.
        dados['login'] = input('Login >> ')
        lista = {i['login']: i for i in pessoa}
        while dados['login'] in lista:
            dados['login'] = input(f'[O Login {dados["login"]} esta em uso, insira outro login]: ')

        dados['senha'] = input('Senha >> ')

        dados['email'] = input('E-mail >> ')
        lista = {i['email']: i for i in pessoa}
        while dados['email'] in lista:
            dados['email'] = input(f'[O E-mail {dados["email"]} esta em uso, insira outro login]: ')

        dados['telefone'] = input('Telefone >> ')
        lista = {i['telefone']: i for i in pessoa}
        while dados['telefone'] in lista:
            dados['telefone'] = input(f'[O Telefone {dados["telefone"]} esta em uso, insira outro login]: ')
        pessoa.append(dados)

        pergunta = input('Deseja fazer mais um(S/N): ')
        if pergunta == 'n':
            menu()
            break


def validar(log):
    lista = {i['login']: i for i in pessoa}
    try:
        b = lista[log]
        return True
    except KeyError:
        return False


def consultar():
    while True:
        log = input('Insira um login para continuar: ')
        lista = {i['login']: i for i in pessoa}

        while not validar(log):
            log = input(f'Login "{log}" não encontrado tente novamente: ')

        temp = lista[log]
        print(f'Dados do Usuário\nNome: {temp["nome"]}\nLogin: {temp["login"]}  \nSenha: '
              f'{temp["senha"]} \nEmail: {temp["telefone"]}')

        resp = input('Deseja continuar? (S/N)')
        if resp.lower() == 'n':
            menu()
            break


def consultar_db(login):
    while True:
        lista = {i['login']: i for i in pessoa}
        s = lista[login]
        print(f'Nome: {s["nome"]}\nLogin: {s["login"]}')
        resp = input('Deseja continuar? (S/N)')
        if resp.lower() == 'n':
            menu()
            break


if __name__ == '__main__':
    menu()
