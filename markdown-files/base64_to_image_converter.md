# Base64 to Image Converter

Este script foi desenvolvido para converter dados de imagem armazenados em formato base64 em um banco de dados MySQL em arquivos de imagem reais e salvá-los em um diretório especificado.

## Requisitos

- Python 3
- `mysql-connector-python` - Uma biblioteca Python para conectar e interagir com bancos de dados MySQL.

## Configuração

1. Instale a biblioteca necessária:

   ```bash
   pip install mysql-connector-python
   ```

2. Clone o repositório e navegue até o diretório que contém o script.

3. Atualize as configurações do banco de dados no script:

   ```python
   DATABASE_CONFIG = {
       'host': 'localhost',  # Endereço do servidor MySQL
       'user': 'root',  # Nome do usuário MySQL
       'password': '',  # Senha do usuário MySQL
       'database': 'data_base_name'  # Nome do banco de dados
   }
   ```

4. Defina o diretório de saída para as imagens:

   ```python
   OUTPUT_DIRECTORY = 'caminho_diretorio_de_saida'
   ```

## Uso

Execute o script utilizando o Python:

```bash
python base64_to_image_converter.py
```

Ao executar, o script irá:

1. Conectar-se ao banco de dados MySQL especificado.
2. Buscar todos os registros da tabela `fotos_noticias` que contêm dados de imagem em base64.
3. Decodificar cada registro de imagem e salvar no diretório especificado como `.png`.

## Observações

- Certifique-se de que o usuário do banco de dados tenha permissões adequadas para ler da tabela `fotos_noticias`.
- O script atualmente assume que todas as imagens são no formato `.png`. Se necessário, você pode modificar o script para determinar o formato da imagem com base nos dados ou em outra coluna da tabela.

## Licença

Este script é fornecido "como está", sem garantias. Fique à vontade para adaptá-lo conforme suas necessidades.
