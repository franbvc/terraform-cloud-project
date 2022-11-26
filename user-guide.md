# Proposta
Essa aplicação foi criada com o intuito de proporcionar uma experiência simples e amigável para usuários que buscam criar uma infraestrutura de cloud na AWS de forma rápida e fácil.

# Overview
Primeiramente, deve-se ressaltar que a aplicação foi desenvolvida para ser utilizada em conjunto com o [Terraform](https://www.terraform.io/). O Terraform é uma ferramenta de automação de infraestrutura que permite que o usuário crie, altere e destrua recursos de cloud de forma declarativa. O app foi desenvolvido para facilitar a criação de arquivos de configuração do Terraform, escritos em JSON.

### IMPORTANTE
Para que a aplicação funcione corretamente, é necessário que o usuário tenha o Terraform instalado em sua máquina. Para mais informações, acesse o site oficial do Terraform. Além disso, também é necessário ter o python3 com os requerimentos do arquivo `requirements.txt` instalados em um ambiente virtual.

## Como utilizar


O objetivo desse manual é explicar o funcionamento da aplicação e como utiliza-la.

Fluxo:
Create -> copia arquivo da pasta terraform/config -> adiciona recursos ao arquivo -> salva na pasta commit

Update -> acessa arquivo da pasta commit -> altera recursos do arquivo -> salva na pasta commit

Delete -> acessa arquivo da pasta commit -> deleta recursos do arquivo -> salva na pasta commit

Commit Changes -> verifica quais arquivos na pasta commit sao diferentes do da pasta terraform/config ->
pergunta ao usuario quais arquivos ele deseja commitar -> copia os arquivos da pasta commit para a pasta terraform/config

Stash -> copia os arquivos da pasta terraform/config para a pasta commit 

* O usuário não deve criar um recurso (Create) de mesmo tipo, antes de realizar um Commit Changes. Caso contrário, o arquivo de configuração do Terraform será sobrescrito e os recursos criados serão perdidos.

Exemplo: O usuário cria um recurso do tipo `EC2 Instance` utilizando o Create. Em seguida, ele decide outro recurso do tipo `EC2 Instance` utilizando o Create. Nesse caso, o arquivo de configuração do Terraform, presente na pasta commit, será sobrescrito e o primeiro recurso criado será perdido.

* Antes de utilizar o Update e o Delete é sugerido que o usuário utilize o Stash ou Commit Changes, para garantir que os arquivos da pasta commit estejam sincronizados com os da pasta terraform/config.

OK
Create -> Commit -> Apply
Update -> Commit -> Apply
Delete -> Commit -> Apply
Create -> Delete -> Commit -> Apply

NOT OK
Create -> Create -> Commit -> Apply ()
