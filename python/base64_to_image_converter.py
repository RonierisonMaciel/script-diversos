import mysql.connector
import base64
import os

# Configurações
DATABASE_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '', #password se houver
    'database': 'data_base_name'
}
OUTPUT_DIRECTORY = 'caminho_diretorio_de_saida'

# Criação de diretório de saída
os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

with mysql.connector.connect(**DATABASE_CONFIG) as conn, conn.cursor() as cursor:
    
    cursor.execute('SELECT id, foto FROM fotos_noticias')
    rows = cursor.fetchall()

    for image_id, image_base64_data in rows:
        image_path = os.path.join(OUTPUT_DIRECTORY, f'image_{image_id}.png')
        
        if image_base64_data:
            image_data = base64.b64decode(image_base64_data)
            with open(image_path, 'wb') as image_file:
                image_file.write(image_data)
