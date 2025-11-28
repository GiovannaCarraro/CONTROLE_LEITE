from conexao import criar_conexo

class  Turma_model():

    def inserir_turma(self, nome, padrinho) -> bool:
        conexao, cursor = criar_conexo()

        cursor.execute("""INSERT INTO""")
