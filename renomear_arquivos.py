import os
contador = 1
endereco = input("Digite o endereço de memória: ")

nome_usuario = input("Digite a nova etiqueta: ")

arquivos = os.listdir(endereco)

for arquivo in arquivos:
    nome_arquivo, extensao = os.path.splitext(arquivo)
    
    novo_nome = nome_usuario + str(contador) + extensao
    os.rename(os.path.join(endereco, arquivo), os.path.join(endereco, novo_nome))
    
    contador += 1
