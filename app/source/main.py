import sys
import os
import boto3
from dotenv import load_dotenv
import urllib3

# Suprimir avisos de requisições HTTPS não verificadas
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Adiciona o diretório 'functions' ao caminho do Python
sys.path.append(os.path.join(os.path.dirname(__file__), 'functions'))

from s3_functions import (
    list_files_in_bucket, upload_file_to_bucket, download_file_from_bucket, 
    delete_file_from_bucket, create_folder_in_bucket, delete_folder_from_bucket, 
    move_file_in_bucket
)

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()


def main():

    # Configuração do cliente S3 para LocalStack
    s3 = boto3.client(
        's3',
        endpoint_url=os.getenv('ENDPOINT_URL'),
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('REGION_NAME'),
        verify=False
    )

    # Nome do bucket
    bucket_name = 'alanceloth'

    # List files in bucket
    files = list_files_in_bucket(s3, bucket_name)
    print(f"Files in bucket '{bucket_name}': {files}")

    # # Create a folder in bucket
    # create_folder_status = create_folder_in_bucket(s3, bucket_name, 'pandas')
    # print(f"Create folder status: {create_folder_status}")

    # # Upload a file to bucket
    # upload_status = upload_file_to_bucket(s3, 'app/data/pandas/clientes.csv', bucket_name, 'pandas/clientes.csv')
    # print(f"Upload status: {upload_status}")
    # upload_status = upload_file_to_bucket(s3, 'app/data/pandas/transacoes.csv', bucket_name, 'pandas/transacoes.csv')
    # print(f"Upload status: {upload_status}")
    # upload_status = upload_file_to_bucket(s3, 'app/data/pandas/transacoes_itens.csv', bucket_name, 'pandas/transacoes_itens.csv')
    # print(f"Upload status: {upload_status}")

    # # Download a file from bucket
    # download_status = download_file_from_bucket(s3, bucket_name, 'object-name-in-s3', 'path/to/save/file.txt')
    # print(f"Download status: {download_status}")

    # # # Delete a file from bucket
    # delete_status = delete_file_from_bucket(s3, bucket_name, 'app/data/pandas/clientes.csv')
    # print(f"Delete status: {delete_status}")

    # delete_status = delete_file_from_bucket(s3, bucket_name, 'app/data/pandas/transacoes.csv')
    # print(f"Delete status: {delete_status}")

    # delete_status = delete_file_from_bucket(s3, bucket_name, 'app/data/pandas/transacoes_itens.csv')
    # print(f"Delete status: {delete_status}")

    # # # Delete a folder from bucket
    # delete_folder_status = delete_folder_from_bucket(s3, bucket_name, 'app')
    # print(f"Delete folder status: {delete_folder_status}")

    # # Move a file within the bucket
    # move_file_status = move_file_in_bucket(s3, bucket_name, 'source-file.txt', 'destination-folder/destination-file.txt')
    # print(f"Move file status: {move_file_status}")

if __name__ == "__main__":
    main()