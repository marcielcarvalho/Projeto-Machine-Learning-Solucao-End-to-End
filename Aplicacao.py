# Construir a API --> Na estrutura do flask
from flask import Flask, request
# Lib para datas
from datetime import datetime
# Lib para carregar o modelo
import joblib
# Lib para banco SQL
import sqlite3

# Instânciando o aplicativo (app)
app = Flask(__name__)

#------------------- CARREGANDO O MODELO --------------------------------
# Carregar o modelo
modelo =joblib.load('modelo_floresta_aleatorio_v100.pkl')

#------------------- FUNÇÃO DA API --------------------------------
# Função para receber nossa API
@app.route('/api_preditivo/<area>;<rooms>;<bathroom>;<parking_spaces>;<floor>;<animal>;<furniture>;<hoa>;<property_tax>', methods=['GET'])

def funcao_01(area, rooms, bathroom, parking_spaces, floor, animal, furniture, hoa, property_tax):

    # Data e hora de inicio
    data_inicio = datetime.now()

    # Recebendo os inputs da API
    lista = [
            float(area), float(rooms), float(bathroom), float(parking_spaces), 
            float(floor), float(animal), float(furniture), float(hoa), float(property_tax)
        ]

    # Tentar previsão
    try:
        # Predict
        previsao = modelo.predict( [lista] )

        # Inserir o valor da previsão
        lista.append(str(previsao))
        
        # Concatenando a lista
        input = ''
        for valor in lista:
            input = input + ';' + str(valor)

        # Termino do processo
        data_fim = datetime.now()

        processamento = data_fim - data_inicio

        #------------------- CONEXÃO BANCO DE DADOS --------------------------------
        # Criar a conexão com o banco de dados
        conexao_banco = sqlite3.connect('Banco_Dados_API.db')
        cursor = conexao_banco.cursor()

        # Query
        query_inserir_dados = f'''
            INSERT INTO Log_API (inputs, inicio, fim, processamento)
            VALUES ( '{input}', '{data_inicio}', '{data_fim}', '{processamento}' )
        '''

        # Execultar a query
        cursor.execute(query_inserir_dados)
        conexao_banco.commit()

        # Fechando a conexão com o banco de dados
        cursor.close()

        # Retorno do modelo
        return {'Valor do aluguel': str(previsao) }
    except:
        return {'Aviso': 'Deu algum erro!'}

if __name__ == '__main__':
    app.run(debug=True)
