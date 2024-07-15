import pandas as pd
from faker import Faker
import random
import time

fake = Faker('pt_BR')

# Função para gerar documento único (CPF ou CNPJ)
def generate_unique_document(existing_documents):
    while True:
        document = fake.cpf() if random.choice([True, False]) else fake.cnpj()
        if document not in existing_documents:
            existing_documents.add(document)
            return document

# Tabela Clientes
def create_client_data(num_records):
    data = []
    existing_documents = set()
    
    for _ in range(num_records):
        nome = fake.name()
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d')
        endereco = fake.address().replace("\n", ", ")
        documento = generate_unique_document(existing_documents)
        email = fake.email()
        telefone = fake.phone_number()
        optin_email = random.choice([True, False])
        optin_telefone = random.choice([True, False])
        data_cadastro = fake.date_this_decade().strftime('%Y-%m-%d')
        id_cliente = documento
        
        data.append([nome, data_nascimento, endereco, documento, email, telefone, optin_email, optin_telefone, data_cadastro, id_cliente])
        
    columns = ["Nome", "Data Nascimento", "Endereço", "Documento", "Email", "Telefone", "Optin Email", "Optin Telefone", "Data Cadastro", "ID Cliente"]
    return pd.DataFrame(data, columns=columns)

# Tabela Transações
def create_transaction_data(num_records, client_ids):
    data = []
    for _ in range(num_records):
        id_cliente = random.choice(client_ids)
        id_transacao = fake.uuid4()
        valor_transacao = round(random.uniform(10.0, 1000.0), 2)
        quantidade_itens = random.randint(1, 10)
        valor_desconto = round(random.uniform(0.0, 50.0), 2)
        valor_frete = round(random.uniform(5.0, 20.0), 2)
        endereco_entrega = fake.address().replace("\n", ", ")
        status_transacao = random.choice(["em processamento", "cancelado", "faturado"])
        status_entrega = "cancelado" if status_transacao == "cancelado" else random.choice(["em processamento", "entregue"])
        
        data.append([id_cliente, id_transacao, valor_transacao, quantidade_itens, valor_desconto, valor_frete, endereco_entrega, status_transacao, status_entrega])
        
    columns = ["ID Cliente", "ID Transação", "Valor Transação", "Quantidade Itens", "Valor Desconto", "Valor Frete", "Endereço Entrega", "Status Transação", "Status Entrega"]
    return pd.DataFrame(data, columns=columns)

# Tabela Transações Itens
def create_transaction_items_data(num_records, transaction_ids):
    data = []
    for _ in range(num_records):
        id_transacao = random.choice(transaction_ids)
        id_sku = fake.uuid4()
        nome_sku = fake.word().capitalize()
        valor_sku = round(random.uniform(5.0, 500.0), 2)
        quantidade_sku = random.randint(1, 5)
        desconto_sku = round(random.uniform(0.0, 30.0), 2)
        marca = fake.company()
        modelo = fake.word().capitalize()
        cor = fake.color_name()
        
        data.append([id_transacao, id_sku, nome_sku, valor_sku, quantidade_sku, desconto_sku, marca, modelo, cor])
        
    columns = ["ID Transação", "ID SKU", "Nome SKU", "Valor SKU", "Quantidade SKU", "Desconto SKU", "Marca", "Modelo", "Cor"]
    return pd.DataFrame(data, columns=columns)

def generate_pandas_data(num_clients, num_transactions, num_transaction_items):
    # num_clients = 1
    # num_transactions = 2
    # num_transaction_items = 5

    start_time = time.time()
    
    clients_df = create_client_data(num_clients)
    transactions_df = create_transaction_data(num_transactions, clients_df["ID Cliente"].tolist())
    transaction_items_df = create_transaction_items_data(num_transaction_items, transactions_df["ID Transação"].tolist())
    
    clients_df.to_csv("app/data/pandas/clientes.csv", index=False)
    transactions_df.to_csv("app/data/pandas/transacoes.csv", index=False)
    transaction_items_df.to_csv("app/data/pandas/transacoes_itens.csv", index=False)

    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    time_taken = generate_pandas_data(1_000_000, 3_000_000, 5_000_000)
    print(f"Tempo total com Pandas: {time_taken:.2f} segundos")
