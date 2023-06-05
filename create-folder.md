# README: Criação de Estrutura de Pastas para Seções, Dias e Lições

Este script Bash automatiza a criação de uma estrutura hierárquica de diretórios para organizar seções, dias e lições, útil para gerenciamento de conteúdo em projetos educacionais ou de treinamento.

## Utilização

O script solicitará ao usuário para inserir um número inteiro para as seções, dias e lições. Em seguida, ele pedirá que você forneça nomes para cada um deles. Finalmente, o script criará a estrutura de diretórios com base nas entradas do usuário.

## Funções

### create_subfolders

Esta função recebe dois argumentos, o nome da pasta principal e um array de nomes de subpastas. Ele cria subpastas dentro da pasta principal.

### read_positive_integer

Esta função recebe uma string como prompt e solicita ao usuário que insira um número inteiro positivo. Se a entrada do usuário não for um número inteiro positivo, a função solicitará que o usuário insira o número novamente.

## Processo

1. O script solicita ao usuário o número de seções.
2. Em seguida, pede o nome de cada seção.
3. Para cada seção, ele solicita ao usuário o número de dias.
4. Em seguida, pede o nome de cada dia.
5. Para cada dia, ele solicita ao usuário o número de lições.
6. Em seguida, pede o nome de cada lição.
7. Finalmente, ele cria a estrutura de diretórios baseada nas entradas do usuário.

No final de cada ciclo, duas subpastas adicionais são criadas: "quiz" e "video-script". Essas subpastas são adicionadas a cada "dia" dentro da estrutura.

Ao concluir a execução, o script imprimirá uma mensagem de confirmação: "Estrutura de pastas e subpastas criada com sucesso."

## Executando o Script

Para executar este script, você precisa ter o Bash instalado no seu sistema. No terminal, navegue até o diretório onde o script está localizado e execute o seguinte comando:

```bash
./create-folder.sh
```

Substitua "nome_do_script.sh" pelo nome do seu script.

Assegure-se de que o script tenha permissões de execução. Caso contrário, você pode dar permissões de execução usando o seguinte comando:

```bash
chmod +x create-folder.sh
```
