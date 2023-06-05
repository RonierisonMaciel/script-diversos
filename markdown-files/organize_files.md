# Organizador de Arquivos

Este script Python organiza arquivos em um diretório específico, classificando-os em subdiretórios baseados em suas extensões de arquivo. Por exemplo, todos os arquivos `.txt` serão movidos para uma pasta chamada `.txt`, todos os arquivos `.jpg` serão movidos para uma pasta chamada `.jpg`, e assim por diante.

## Como usar

1. Garanta que você tenha Python instalado em seu sistema. Este script foi testado com Python 3.7, mas deve funcionar com outras versões também.

2. Baixe o arquivo `organize_files.py`.

3. Abra o arquivo `organize_files.py` com um editor de texto de sua escolha.

4. No final do script, você verá a seguinte linha de código:

   ```python
   if __name__ == "__main__":
       source_directory = "<diretorio_aqui>"
       organize_files_by_extension(source_directory)
   ```

5. Substitua `"<diretorio_aqui>"` pelo diretório que você deseja organizar. Por exemplo, se você deseja organizar arquivos no diretório `C:\Users\username\Documents`, a linha deve ficar assim:

   ```python
   if __name__ == "__main__":
       source_directory = "C:\\Users\\username\\Documents"
       organize_files_by_extension(source_directory)
   ```

    Linux ou macOS

   ```python
   if __name__ == "__main__":
    source_directory = "/home/username/Documents"
    organize_files_by_extension(source_directory)
    ```

6. Salve e feche o arquivo.

7. Abra um terminal ou prompt de comando.

8. Navegue até o diretório onde você salvou `organize_files.py`.

9. Execute o seguinte comando:

   ```bash
   python organize_files.py
   ```

10. O script irá organizar os arquivos no diretório especificado, criando subdiretórios conforme necessário e movendo os arquivos para os subdiretórios apropriados.
