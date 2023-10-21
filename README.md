# README - Projeto de Criptografia de Arquivos com AES (Modo CBC)

Este projeto em Python permite criptografar e descriptografar arquivos utilizando o algoritmo de criptografia AES no modo CBC (Cipher Block Chaining). Para utilizar o projeto, siga as instruções abaixo.

## Requisitos

Antes de usar o projeto, certifique-se de que possui os requisitos instalados. Você pode fazer isso executando o seguinte comando:

```bash
pip install -r requirements.txt
```

Certifique-se de que o Python e o gerenciador de pacotes `pip` estejam instalados no seu sistema.

## Utilização

### Criptografia de Arquivos

Para criptografar um arquivo, execute o codigo e escolha a opção 1, digite 1 + enter:

![image](https://github.com/aureliodeboa/Aes/assets/53971991/6163e0b0-7a75-4c93-9762-98aa2afbb698)


- `caminho_do_arquivo`: O caminho para o arquivo que você deseja cifrar. Se o arquivo estiver na mesma pasta do código, basta digitar o nome do arquivo (por exemplo, "texto_claro.txt").
- `chave`: A chave de criptografia que você deseja utilizar. Certifique-se de usar uma chave segura e mantê-la em segredo.

O arquivo cifrado será gerado na mesma pasta do código.

### Descriptografar de Arquivos

Para descriptografar um arquivo, execute o codigo e escolha a opção 2, digite 2 depois tecle enter:

![image](https://github.com/aureliodeboa/Aes/assets/53971991/6163e0b0-7a75-4c93-9762-98aa2afbb698)

- `caminho_do_arquivo_cifrado`: O caminho para o arquivo que você deseja decifrar. Certifique-se de fornecer o caminho correto para o arquivo cifrado.
- `chave`: A mesma chave de criptografia que foi usada para cifrar o arquivo.


O arquivo decifrado será gerado na mesma pasta do código.

## Exemplo de Uso

Cifrar um arquivo:

![image](https://github.com/aureliodeboa/Aes/assets/53971991/d2353926-8f9c-4e58-9fa3-2f6812bab721)

Resultado:
![image](https://github.com/aureliodeboa/Aes/assets/53971991/512806c7-8ab7-4a79-a651-2389d000e2ef)


Decifrar um arquivo:

![image](https://github.com/aureliodeboa/Aes/assets/53971991/b80e9bd2-2086-4531-a63f-d433d7f73d3c)

Resultado:

![image](https://github.com/aureliodeboa/Aes/assets/53971991/84a63417-3704-4e29-8601-490f6066c9d7)




## Limitações
-Por utilizar um vetor de inicialização fixo nessa implementação, acredito que esse codigo só seja capaz de descriptografar arquivos que tenha o mesmo IV.
-O IV utilizado é IV= 'fala, seu lindo!'.encode('utf8'), como pode ser visto no codigo.


## Observações

- Certifique-se de manter suas chaves seguras, pois a segurança do sistema depende fortemente da confidencialidade da chave.
- O arquivo criptografado não  terá a extensão , e o arquivo decifrado tabém não.
- Se o arquivo a ser criptografado ou descriptografado estiver na mesma pasta do código, você pode simplesmente fornecer o nome do arquivo como o caminho.

Ps: 'fala, seu lindo' é uma piada interna.
