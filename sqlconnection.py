import mysql.connector


class ConexaoBD:
    def __init__(self, host = 'localhost', user = 'root', password = '@dministrator231', db = 'dbcadastro'):
        self.host = host
        self.user = user
        self.pwd = password
        self.db = db

    def conectar(self):
        self.conexao = mysql.connector.connect(host=self.host, user=self.user, password=self.pwd, database=self.db)
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        self.conexao.close()
        self.cursor.close()

    def executa_dql(self, sql):
        self.conectar()
        self.cursor.execute(sql)
        resposta = self.cursor.fetchall()
        self.conexao.commit()
        self.desconectar()
        return resposta

    # def executa_dml(self, sql):
    #     self.conectar()
    #     self.cursor.execute(sql)
    #     resposta = self.cursor.fetchall()
    #     self.conexao.commit()
    #     self.desconectar()
    #     return resposta

