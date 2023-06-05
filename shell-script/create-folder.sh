#!/bin/bash

create_subfolders() {
    local parent_folder="$1"
    local subfolders=("${!2}")

    for subfolder in "${subfolders[@]}"; do
        mkdir -p "$parent_folder/$subfolder"
    done
}

read_positive_integer() {
    local prompt="$1"
    local input
    while true; do
        read -p "$prompt" input
        case $input in
            ''|*[!0-9]*)
                echo "Por favor, insira um número inteiro positivo." >&2
                ;;
            *)
                echo $input
                break
                ;;
        esac
    done
}

num_secoes=$(read_positive_integer "Informe o número de seções: ")

secao_names=()
for ((secao=1; secao<=num_secoes; secao++)); do
    read -p "Informe o nome da seção $secao: " secao_name
    secao_names+=("$secao_name")
done

for secao in "${secao_names[@]}"; do
    secao_folder="$secao"

    num_dias_secao=$(read_positive_integer "Informe o número de dias para a seção $secao: ")

    dia_names=()
    for ((dia=1; dia<=num_dias_secao; dia++)); do
        read -p "Informe o nome do dia $dia para a seção $secao: " dia_name
        dia_names+=("$dia_name")
    done

    for dia in "${dia_names[@]}"; do
        dia_folder="$dia"
        conteudo="conteudo"

        num_licoes_dia=$(read_positive_integer "Informe o número de lições para o dia $dia na seção $secao: ")

        licao_names=()
        for ((licao=1; licao<=num_licoes_dia; licao++)); do
            read -p "Informe o nome da lição $licao para o dia $dia na seção $secao: " licao_name
            licao_names+=("$licao_name")
        done

        licao_names+=("quiz" "video-script")

        create_subfolders "$secao_folder"
        create_subfolders "$secao_folder/$dia_folder"
        create_subfolders "$secao_folder/$dia_folder/$conteudo" licao_names[@]
    done
done

echo "Estrutura de pastas e subpastas criada com sucesso."
