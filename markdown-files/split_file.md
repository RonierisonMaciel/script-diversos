# Script para Dividir Arquivos

Este script Python foi projetado para dividir um arquivo de texto grande em arquivos menores, com base em um limite de tamanho. Ele garante que a divisão ocorra no final de uma linha e não no meio. Além disso, uma string especificada é inserida como a primeira linha de cada novo arquivo.

## Como Funciona

O script contém a função `split_file(file_path, size_limit=2*1024**3, first_line="this is the first line")`, onde `file_path` é o caminho para o arquivo grande a ser dividido, `size_limit` é o tamanho máximo de cada arquivo dividido (o padrão é 2GB), e `first_line` é a string a ser inserida como a primeira linha em cada arquivo dividido.

A função cria arquivos menores nomeados como `textfile_{counter}.txt`, onde `{counter}` é um número que começa em 1, incrementado para cada novo arquivo.

A função lê o arquivo de entrada linha por linha. Para cada linha, se o tamanho do arquivo de saída atual somado ao tamanho da nova linha exceder o `size_limit`, ou se não houver arquivo de saída atual (`output_file` for None), um novo arquivo de saída é criado.

## Uso

Para dividir um arquivo, chame a função `split_file` com o caminho para o arquivo como primeiro argumento.

Por exemplo, para dividir um arquivo chamado `yourfile.txt`, você pode chamar a função da seguinte maneira:

```python
split_file("yourfile.txt")
```

## Requisitos

Este script requer Python 3 para funcionar. Nenhuma biblioteca adicional é necessária.

## Atenção

Este script irá sobrescrever arquivos com o mesmo nome no diretório sem aviso prévio. É aconselhável usar este script em um diretório dedicado para evitar qualquer perda de dados potencial.
