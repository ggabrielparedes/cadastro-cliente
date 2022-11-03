import sqlconnection as sql

def menu():
    print('************* MENU DE CADASTRO *************')
    print('* [1] Cadastrar Usuário                    *')
    print('* [2] Consultar Usuário                    *')
    print('* [3] Remover Usuário                      *')
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
            remover()
        case _g:
            print('Valor invalido')
            menu()


def cadastro(): #Cadastrar usuário dentro de um banco de dados
    while True:

        login = input('Login >> ')

        while validar(login, "nm_login") >= 1: #Verificação de duplicata
            login = input('Este login já esta sendo utilizado, insira outro >> ')

        nome = input('Nome >> ')
        senha = input('Senha >> ')

        email = input('E-mail >> ')
        while validar(email, "nm_email") >= 1: #Verificação de duplicata
            email = input('Este e-mail já esta sendo utilizado, insira outro >> ')

        telefone = input('Telefone >> ')
        while validar(telefone, "cd_telefone") >= 1: #Verificação de duplicata
            telefone = input('Este telefone já esta sendo utilizado, insira outro >> ')

        cmd = c.executa_DQL(f'INSERT INTO usuario (nm_usuario, nm_senha, nm_email, nm_login, cd_telefone) VALUES ("{nome}", "{senha}", "{email}", "{login}", {telefone})')
        pergunta = input('Deseja fazer cadastrar mais um usuário? (S/N): ')
        if pergunta.lower() == 'n':
            menu()
            break


def consultar(): #Consultar usuário dentro do Banco de Dados
    while True:
        log = input('Insira um login para continuar: ')
        while validar(log, "nm_login") <= 0:
            log = input(f'Login "{log}" não encontrado tente novamente: ')

        read = c.executa_DQL(f'SELECT nm_usuario, nm_senha, nm_email, nm_login, cd_telefone FROM usuario WHERE nm_login = "{log}"')
        print(f'Dados do Usuário\nNome: {read[0][0]}\nLogin: {read[0][3]}\nSenha: {read[0][1]}\nEmail: {read[0][2]}\nTelefone: {read[0][4]}')

        resp = input('Deseja continuar? (S/N)')
        if resp.lower() == 'n':
            menu()
            break


def remover(): #Remover usuário do Banco de Dados
    while True:

        login = input('Insira o login do usuário: ')
        while validar(l, "nm_login") <= 0:
            login = input(f'Login "{l}" não encontrado tente novamente: ')

        resp = input(f'Deseja deletar o usuário com login de {login}? (S/N)>> ')
        if resp.lower() == 's':
            c.executa_DQL(f'DELETE FROM usuario WHERE nm_login = "{login}"')
            resp = input('Deseja continuar ou ir para tela de menu? (S/N)')
            if resp.lower() == 'n':
                menu()
                break


def validar(valor, coluna): #Validar existencia de um valor em uma determinada coluna,
    # retornando quantidade deste valor

    a = c.executa_DQL(f'SELECT COUNT({coluna}) AS'
                      f' x FROM usuario WHERE {coluna} = "{valor}"')
    return a[0][0]


if __name__ == '__main__':
    c = sql.ConexaoBD
    menu()
