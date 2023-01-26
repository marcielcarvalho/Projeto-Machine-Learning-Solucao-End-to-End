# Projeto Machine Learning end-to-end

Nesse projeto propomos uma solução completa end-to-end, indo desde a extração dos dados, tratamento, análise exploratório até o treinamento do modelo de machine learning. Além disso, criamos uma API onde o usuário interage e consegue através da inserção dos atributos o resultado de aluguel para o imóvel desejado. Ou seja, nosso objetivo nesse projeto é treinar um modelo com dados de imóveis para alugar, que retorno o valor do aluguel para o usuário.

Nossos dados constituem de uma base com dados de casas para aluguel, com 13 classes diferentes, como por exemplo a cidade de localização do imóvel, número de quartos, número de banheiros, se aceita animais ou não, taxa de condomínio, valor do aluguel, entre outros (os dados estão disponível no arquivo localmente __houses_to_rent.csv__ ou no site https://www.kaggle.com/, podendo ser baixado diretamente no [link](https://www.kaggle.com/datasets/rubenssjr/brasilian-houses-to-rent)). Como em nossos dados, mais de 50% dos dados eram da cidade de São Paulo, filtramos os dados apenas para a cidade de São Paulo e foi realizado o treinamento apenas para essa cidade.

No arquivo __Projeto_Machine_Learning_Treinamento_Modelo.ipynb__ realizamos o tratamento dos dados, uma análise exploratória, além de fazermos o treinamento de nosso modelo. Nesse projeto, utilizamos o _Random Forest Regresson_.

Com o modelo treinado, fizemos a exportação para que possamos construir a infraestrutura da API, carregamos o modelo no arquivo __modelo_floresta_aleatorio_v100.pkl__.

Em __Criacao_Banco_Dados.ipynb__ fizemos a criação do banco de dados (__Banco_Dados_API.db__) utilizando a lib _sqlite3_. Esse banco tem como objetivo armazenar os dados quando o usuário fizer uma consulta na API.

Chegamos assim o momento da criação da API, arquivo __Aplicacao.py__. Nessa aplicação, utilizamos a lib _Flask_ para criarmos a conexão web. Com o arquivo __Conexao_com_API.ipynb__ podemos assim realizar nossas consultas.
