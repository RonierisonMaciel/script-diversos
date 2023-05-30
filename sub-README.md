# DisplayNameExtractor

## Descrição

`DisplayNameExtractor` é um script Python que extrai todas as anotações `@DisplayName` de um ou mais arquivos `.java`. O texto de cada `@DisplayName` é escrito em um arquivo `.json` com a seguinte estrutura:

```json
{
    "description": "<texto de @DisplayName>",
    "bonus": false
}
```

Cada objeto no arquivo JSON corresponde a um `@DisplayName` nos arquivos `.java` de entrada.

## Requisitos

- Python 3.6 ou superior

## Como usar

1. Coloque o script `display_name_extractor.py` na mesma pasta dos seus arquivos `.java`.

2. Abra o script e altere a seguinte linha para incluir os nomes dos seus arquivos `.java`:

```python
files = ['file1.java', 'file2.java', 'file3.java']
```

Substitua `'file1.java', 'file2.java', 'file3.java'` pelos nomes dos seus arquivos de origem.

3. Execute o script na linha de comando:

```bash
python display_name_extractor.py
```

4. O script criará um arquivo `output.json` na mesma pasta, contendo os textos de todos os `@DisplayName` encontrados nos arquivos `.java`.

## Detalhes do script

- O script usa a biblioteca `re` para encontrar todas as ocorrências de `@DisplayName` nos arquivos `.java`.
- A expressão regular `r"@DisplayName\(\"(.*?)\"\)"` é usada para extrair o texto de cada `@DisplayName`.
- O texto de cada `@DisplayName` é escrito em um arquivo `.json` com a chave "description".
- Cada objeto no arquivo `.json` também tem uma chave "bonus", que é sempre definida como `false`.
- O arquivo `.json` é escrito em UTF-8 para suportar caracteres não ASCII.
