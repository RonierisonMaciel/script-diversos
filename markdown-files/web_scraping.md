# Script de Web Scraping para Concursos de Professor no Nordeste

Este script foi desenvolvido para coletar informações sobre concursos na área de docência (professor) para cargos de nível superior na região Nordeste do Brasil. Ele faz o scraping da página de concursos do site PCI Concursos, especificamente da seção dedicada ao Nordeste ou Nacional.

## Características

O script coleta as seguintes informações sobre cada concurso:

- Título do concurso
- Localização (estado)
- Vaga e salário oferecido
- Descrição da vaga (por exemplo, "Professor Substituto")
- Nível de educação exigido (por exemplo, "Superior")
- Data limite para inscrição
- Link direto para a página do concurso

Os resultados são salvos em um arquivo `.json` chamado `docente_professor.json`.

## Como usar

1. **Pré-requisitos**:
   - Python 3.x
   - Bibliotecas: `requests`, `BeautifulSoup4`, `re`, `json`. Você pode instalá-las usando pip:

     ```bash
     pip install requests beautifulsoup4
     ```

   - Caso deseje usar o `../python/requirements_concursos.txt`, existe as lib utilizadas. Basta rodar o comando abaixo:

     ```bash
     pip install -r requirements_concursos.txt
     ```

2. **Execução**:
   - Baixe o script e navegue até o diretório onde ele está localizado.
   - Execute o script usando o comando:

     ```bash
     python nome_do_script.py
     ```

   - Após a execução, verifique o arquivo `docente_professor.json` no mesmo diretório para ver os resultados.

## Observações

- O script foi desenvolvido com base na estrutura do site PCI Concursos em setembro de 2023. Mudanças na estrutura do site podem afetar a funcionalidade do script.
- Certifique-se de ter uma conexão estável com a internet ao executar o script.
- O uso excessivo de web scraping pode levar a restrições de IP. Use com moderação e sempre respeite os `robots.txt` e termos de serviço dos sites.
