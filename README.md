# desafio_python_MELI

## Objetivo: 

Simular a extração de dados de um API e a geração de um arquivo .csv com os campos mais relevantes para uma análise futura.

## Diagrama de Alto Nível

<img width="737" height="181" alt="image" src="https://github.com/user-attachments/assets/f0b116ab-aa82-4d36-b2e5-188b4776b806" />



## Documentação do Projeto

### Resumo:

O script simula uma chamada a uma API para obter uma lista de 100 IDs e após obter a lista, simula uma chamada para cada id para obter os detalhes do mesmo. Por fim, os dados de cada id são salvos em um arquivo.csv para possibilitar/facilitar uma análise futura.

### Como Replicar o processo ?

Para replicar o processo, recomendamos os seguintes passos:

1. Certifique-se que você tem o Python instalado na sua máquina. Caso não tenha, você pode acessar esse link e seguir com a instalção: https://www.python.org/downloads/
   
2. Com o Python instalado, você pode criar uma pasta em seu computador, em documentos por exemplos, e nomeá-la como extract_compliance_data

   C:\Users\seu usuário\Documents\extract_compliance_data
   
3. Em seguida, você pode adicionar nessa pasta o arquivo extract_compliance_data.py, disponibilizado nesse repositório.

4. Para rodar o código, certifique-se que você tenha as bibliotecas abaixo instaladas:
   
   -requests
   
   -pandas
   
   Para fazer essa verificação, você pode abrir o prompt de comando e digitar o seguinte comando:
   
      pip show biblioteca
   
      exemplo: pip show requests

   Caso você não tenha as bibliotecas instaladas, você pode digitar o seguinte comando no prompt de comando:
   
      pip install biblioteca
   
      exemplo: pip install requests
   
5. Com o Python e as bibliotecas instaladas você pode, também no prompt de comando, acessar o diretório onde o seu arquivo .py está salvo através do comando abaixo:

   cd C:\Users\seu usuário\Documents\extract_compliance_data
   
   E rodar o código através do comando abaixo:
   
      python extract_compliance_data.py
   
   **IMPORTANTE: Como a API não existe, criamos um modo simulação que gera os ids e os dados. No código, existe uma variável que habilita o modo simulação:
   
      MODO_SIMULACAO = True
   
   Caso a API fosse criada e fosse possível realizar chamadas, o código já está pronto para isso ! Basta desabilitar o modo simulação atribuindo:
  
      MODO_SIMULACAO = False
   
6. Ao finalizar a execução, você poderá visualizar um arquivo .csv, no mesmo diretório, com os dados dos ids que foram consultados.

### Desafios/Bloqueios

1. Tokens de autenticação - Seria necessário consultar a documentação da API para entender o método de autenticação
2. Limites de taxa - A API pode limitar o número de chamadas/requisições por unidade de tempo. Para resolver esse problema, poderíamos utilizar time.sleep(tempo entre chamadas/requisições). No código extract_compliance_data.py foi adicionado essa função.  
3. Estrutura JSON variável - Quando utilizamos APIs reais nem sempre a estrutura dos dados é fixa. Pode acontecer, por exemplo, de alguns registros terem campos faltantes. No nosso exemplo os registros tem o campo responsavel, mas pode acontecer que algum registro não tenha. Nesse caso, poderíamos usar o .get() para atribuir um valor caso o campo não exista no registro.

   responsavel = item.get("responsavel", "Desconhecido")
