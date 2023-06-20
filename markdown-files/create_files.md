# Script de Criação de Arquivos

Este script Python é projetado para criar um número especificado de arquivos de texto com um determinado número de linhas em cada arquivo. Cada linha contém uma mensagem de saudação única.

## Como Funciona

O script contém uma função `create_files(num_files)`, onde `num_files` é o número de arquivos que você deseja criar. Esta função irá criar o número especificado de arquivos nomeados como `file_{i}.txt`, onde `{i}` é um número de 1 a `num_files`.

Cada arquivo criado conterá 20 linhas e cada linha conterá uma string formatada como `"Hello {j}! in file number {i}\n"`, onde `{j}` é o número da linha e `{i}` é o número do arquivo.

## Uso

Para criar arquivos, chame a função `create_files` com o número de arquivos que deseja criar como argumento.

Por exemplo, para criar 10 arquivos nomeados de `file_1.txt` a `file_10.txt` cada um com 20 linhas, você pode chamar a função da seguinte maneira:

```python
create_files(10)
```

No script fornecido, `create_files(1)` é chamado, o que irá criar um único arquivo `file_1.txt` com 20 linhas.

## Requisitos

Este script requer Python 3 para funcionar. Nenhuma biblioteca adicional é necessária.

## Aviso

Este script substituirá arquivos com o mesmo nome no diretório sem aviso prévio. É aconselhável usar este script em um diretório dedicado para evitar qualquer perda de dados potencial.
