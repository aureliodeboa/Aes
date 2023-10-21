# $ pip install -r requirements.txt
# Author.: Aurélio-Jose
# Date...: 21/10/2023


from Crypto.Cipher import AES #O AES
import hashlib # biblioteca de hash

#Variaveis importantes
mode =  AES.MODE_CBC #conforme pedido modo encadeado
IV =  'fala, seu lindo!'.encode('utf8') # vetor de inicializaçao, por algum motivo o AES dessa lib precisa disso.


#função que adiciona padding ao arquivo para ele ser mod 16
def add_Padding(arquivo):
    while len(arquivo) % 16 != 0:
        arquivo = arquivo + b'0'
    return arquivo

#funçao para leitura de arquivos
def open_file(path,modo):
    with open(path,modo) as f:
        return f.read()

#função para salvar arquivos
def save_file(path,arquivo):
    with open(path, 'wb') as e:
        e.write(arquivo)

#função para cifrar
def cifrar(path,chave):
    key = hashlib.sha256(chave).digest()
    cipher = AES.new(key,mode,IV)
    arquivo = open_file(path,'rb') #modo de leitura binario
    arquivo_pad = add_Padding(arquivo) # adiciona padding ao arquivo caso precise
    arquivo_cifrado = cipher.encrypt(arquivo_pad) #cifra o arquivo
    save_file('arquivo_cifrado',arquivo_cifrado) #salva o arquivo decifrado no local do codigo

#função para decifrar
def decifrar(path,chave):
    key = hashlib.sha256(chave).digest()
    cipher = AES.new(key,mode,IV) 
    arquivo_cifrado = open_file(path,'rb')
    arquivo_decifrado = cipher.decrypt(arquivo_cifrado)

    with open ('arquivo_decifrado','wb') as df: 
        df.write(arquivo_decifrado.rstrip(b'0'))  # isso é para tirar o padding que foi colado



#modo de operação linha de comando
if __name__ == '__main__':
   while True:
    # Apresenta o menu ao usuário
    print("Escolha uma opção:")
    print("1 - Para Criptografar usando AES-CBC")
    print("2 - Para Decriptografar usando AES-CBC")
    print("0 - Sair")

    # Solicita a entrada do usuário
    escolha = input("Digite o número da opção desejada: ")

    
    if escolha == "1":
        path = input('digite o caminho do arquivo para ser criptografado: ')
        chave = input('Digite a chave : ')
        cifrar(path,chave.encode("utf8"))
        print('\n Arquivo criptografado!')
       
    elif escolha == "2":
        path = input('digite o caminho completo do arquivo para ser descriptografado: ')
        chave = input('Digite a chave : ')
        decifrar(path,chave.encode("utf8"))
        print('\n Arquivo descriptografado!')
       
    elif escolha == "0":
        print("Saindo do programa. Valeu!")
        break
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 0 para sair.")

   
 