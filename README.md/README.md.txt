README.md

# projeto-tiger
│Sistema de Gerenciamento Acadêmico – Experiência Prática 4).
├── projeto_tiger.py   # 
 principal com funções e testes
├── print   
├── test_projeto_tiger.py        #teste                # print da tela com teste concluído 
├── README.md          # Documentação do projeto


# 🐯 Experiência Prática 4 - Projeto Tiger

## 📌 Introdução
Este projeto implementa um Sistema de Gerenciamento Acadêmico em Python.  
O sistema permite cadastrar estudantes, calcular médias de notas, verificar aprovação e gerar relatórios de desempenho acadêmico.  
Além disso, foram incluídos testes automatizados utilizando `assert` e `unittest`, garantindo a confiabilidade das funções principais.


## ▶️ Como executar o projeto
python test_projeto_tiger.py
python -m unittest projeto_tiger.py


projeto tiger>python projeto_tiger.py

🛠 https://linkedln.com/vanusa-ferreira-6a60b637b

https://github.com/V25-tech/projeto-tiger.git

## 🧪 Reflexão sobre as estratégias de validação

Para garantir a confiabilidade do sistema, foram aplicadas duas estratégias de testes complementares:

- **Testes com `assert`**  
  Utilizados diretamente no código para validar rapidamente as funções principais. Essa abordagem simples permitiu verificar se os cálculos de média e a lógica de aprovação/reprovação estavam corretos em cenários básicos.

- **Testes estruturados com `unittest`**  
  Implementados em arquivos específicos de teste (`test_projeto_tiger.py` e `test_notas.py`), cobrindo diferentes situações:
  - Condições normais de aprovação e reprovação.  
  

Essa combinação de **testes simples e rápidos** com **testes mais robustos e organizados** assegurou que o sistema fosse validado tanto em cenários comuns quanto em casos limite. Com isso, foi possível confirmar a estabilidade e a confiabilidade do código antes da entrega final.

