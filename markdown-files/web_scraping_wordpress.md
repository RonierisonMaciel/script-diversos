# Web Scraper para Extração de Dados de Usuários

Este script foi criado para extrair dados de usuários de um website específico. Ele irá coletar usernames, nomes e emails de todos os usuários listados em uma determinada página e salvar essas informações em um arquivo CSV.

## Requisitos

- Python 3.6 ou superior
- Selenium WebDriver
- BeautifulSoup
- pandas

## Instalação

1. Clone este repositório ou baixe o script.
2. Instale as dependências usando pip:

```bash
pip install selenium beautifulsoup4 pandas
```

3. Baixe o [driver adequado](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/) para o seu navegador e adicione o executável ao seu PATH.

## Uso

1. Execute o script:

```bash
python crawler_wordpress_user.py
```

2. Quando solicitado, insira suas credenciais de login para o website.

O script irá então acessar o site, navegar até a página de usuários, extrair os dados dos usuários e salvar essas informações em um arquivo CSV chamado `users.csv` no diretório atual.

## Aviso

Este script é apenas para fins educacionais e não deve ser usado para scraping em websites sem permissão. Certifique-se de estar em conformidade com os Termos de Serviço do site e as leis de scraping de dados do seu país.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma Issue ou um Pull Request.
