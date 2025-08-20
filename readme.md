# WeatherView 🌦️

Uma aplicação web simples e funcional para consultar a previsão do tempo atual em qualquer lugar do mundo, com um sistema de contas de usuário para salvar locais e visualizar o histórico de buscas.

---

## Sobre o Projeto

O **WeatherView** foi criado para oferecer uma experiência rápida e direta de consulta meteorológica. A aplicação utiliza a **API de Geocodificação do Google Maps** para converter qualquer busca de local em coordenadas geográficas (latitude e longitude) e, em seguida, busca os dados do tempo através da **API Open-Meteo**.

O principal diferencial do projeto é seu sistema de contas de usuário, que permite a qualquer pessoa registrada salvar suas localidades favoritas para acesso rápido e manter um histórico organizado de todas as pesquisas realizadas.

---

## ✨ Principais Funcionalidades

* **Consulta de Tempo:** Obtenha informações como temperatura atual, máxima, mínima e condições do tempo (chuva, névoa, neve, etc.).
* **Busca Flexível:** Graças à API do Google, a busca por locais é flexível e inteligente.
* **Sistema de Contas:** Crie uma conta e faça login para acessar funcionalidades exclusivas.
* **Locais Salvos:** Usuários logados podem salvar e remover localidades de uma lista de favoritos.
* **Histórico de Buscas:** Todas as suas pesquisas ficam salvas em um histórico ordenado pela mais recente, de onde também é possível adicionar um local aos favoritos.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

* **Back-end:** Python, Flask
* **Front-end:** HTML, CSS, JavaScript
* **Banco de Dados:** SQLite
* **Template Engine:** Jinja

---

## 🚀 Como Executar o Projeto Localmente

Para rodar o WeatherView na sua máquina, siga os passos abaixo.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/WeatherView.git](https://github.com/seu-usuario/WeatherView.git)
    cd WeatherView
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    O projeto precisa das bibliotecas listadas no arquivo `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    Você precisará de uma chave da API de Geocodificação do Google Maps. Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave:
    ```
    API_KEY="SUA_CHAVE_DO_GOOGLE_MAPS_AQUI"
    ```

5.  **Execute a aplicação:**
    Com tudo configurado, inicie o servidor Flask.
    ```bash
    flask run
    ```
    Acesse `http://127.0.0.1:5000` no seu navegador para ver o projeto funcionando!

---

## 🔗 APIs

* **[Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview)** - Utilizada para a conversão de nomes de locais em coordenadas.
* **[Open-Meteo](https://open-meteo.com/)** - Utilizada para obter os dados de previsão do tempo.
