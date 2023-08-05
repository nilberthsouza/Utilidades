import os
contador = 1
# Obtenha o endereço de memória do usuário
endereco = input("Digite o endereço de memória: ")

# Etiqueta sera o nome do arquivo, tipo "Video1.mp4", "Video2.mp4"
nome_usuario = input("Digite a nova etiqueta: ")

# Obtem  lista de todos os arquivos no diretório especificado  
arquivos = os.listdir(endereco)

for arquivo in arquivos:
    nome_arquivo, extensao = os.path.splitext(arquivo)
    
    novo_nome = nome_usuario + str(contador) + extensao
    os.rename(os.path.join(endereco, arquivo), os.path.join(endereco, novo_nome))
    
    contador += 1