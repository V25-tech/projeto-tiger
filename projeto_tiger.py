# ==========================
# Sistema de Gerenciamento Acadêmico
# ==========================

def calcular_media(notas):
    """
    Calcula a média aritmética de uma lista de notas.

    Args:
        notas (list of float): Lista contendo as notas do estudante.
                               Cada nota deve ser representada como um número de ponto flutuante.

    Returns:
        float: Valor da média aritmética das notas fornecidas.
               Caso a lista esteja vazia, retorna 0.0 para evitar divisão por zero.
    """
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


def verificar_aprovacao(media, media_minima=7.0):
    """
    Verifica se o estudante foi aprovado ou reprovado com base na média obtida.

    Args:
        media (float): Média calculada das notas do estudante.
        media_minima (float, opcional): Média mínima exigida para aprovação.
                                        O valor padrão é 7.0, mas pode ser ajustado conforme regras institucionais.

    Returns:
        str: Retorna 'Aprovado' se a média for maior ou igual à média mínima.
             Retorna 'Reprovado' caso contrário.
    """
    if media >= media_minima:
        return "Aprovado"
    else:
        return "Reprovado"


def gerar_relatorio(alunos):
    """
    Gera um relatório com nome, matrícula, curso, média e situação de aprovação
    para cada estudante da lista fornecida.

    Args:
        alunos (list of dict): Lista de dicionários contendo dados dos estudantes.
                               Cada dicionário deve conter pelo menos os atributos:
                               'matricula' (str), 'nome' (str), 'curso' (str),
                               'notas' (list of float) e 'status' (str).

    Returns:
        None: Apenas imprime o relatório no terminal.
    """
    print("=== RELATÓRIO DE DESEMPENHO ACADÊMICO ===")
    for aluno in alunos:
        matricula = aluno.get("matricula", "N/A")
        nome = aluno.get("nome", "Sem nome")
        curso = aluno.get("curso", "Não informado")
        notas = aluno.get("notas", [])
        status_aluno = aluno.get("status", "Indefinido")

        media = calcular_media(notas)
        situacao = verificar_aprovacao(media)

        print(f"Matrícula: {matricula}")
        print(f"Aluno: {nome}")
        print(f"Curso: {curso}")
        print(f"Status: {status_aluno}")
        print(f"  Média: {media:.2f}")
        print(f"  Situação: {situacao}")
        print("----------------------------------------")


# ==========================
# Exemplo de uso
# ==========================

estudantes = [
    {
        "matricula": "2026001",
        "nome": "Ana Silva",
        "curso": "Engenharia de Software",
        "notas": [8.5, 7.0, 9.0],
        "status": "Ativo"
    },
    {
        "matricula": "2026002",
        "nome": "Bruno Santos",
        "curso": "Ciência da Computação",
        "notas": [6.0, 5.5, 7.0],
        "status": "Ativo"
    },
    {
        "matricula": "2026003",
        "nome": "Carla Oliveira",
        "curso": "Sistemas de Informação",
        "notas": [9.5, 8.0, 9.0],
        "status": "Ativo"
    }
]

# Gerar relatório completo
gerar_relatorio(estudantes)




# Teste da função calcular_media
assert calcular_media([8.0, 7.0, 9.0]) == 8.0
assert calcular_media([]) == 0.0

# Teste da função verificar_aprovacao
assert verificar_aprovacao(8.0) == "Aprovado"
assert verificar_aprovacao(6.5) == "Reprovado"
assert verificar_aprovacao(7.0) == "Aprovado"

print("✅ Todos os testes com assert passaram!")



# Testes simples com assert

# Teste da função calcular_media
assert calcular_media([8.0, 7.0, 9.0]) == 8.0
assert calcular_media([]) == 0.0

# Teste da função verificar_aprovacao
assert verificar_aprovacao(8.0) == "Aprovado"
assert verificar_aprovacao(6.5) == "Reprovado"
assert verificar_aprovacao(7.0) == "Aprovado"

print("✅ Todos os testes com assert passaram!")
import unittest

class TestSistemaAcademico(unittest.TestCase):
    def test_calcular_media(self):
        self.assertEqual(calcular_media([8.0, 7.0, 9.0]), 8.0)
        self.assertEqual(calcular_media([]), 0.0)
        self.assertAlmostEqual(calcular_media([6.5, 7.5]), 7.0)

    def test_verificar_aprovacao(self):
        self.assertEqual(verificar_aprovacao(8.0), "Aprovado")
        self.assertEqual(verificar_aprovacao(6.5), "Reprovado")
        self.assertEqual(verificar_aprovacao(7.0), "Aprovado")
        self.assertEqual(verificar_aprovacao(7.5, media_minima=8.0), "Reprovado")

if __name__ == "__main__":
    unittest.main()
