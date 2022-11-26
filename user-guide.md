# Proposta
Essa aplicação foi criada com o intuito de proporcionar uma experiência simples e amigável para usuários que buscam criar uma infraestrutura de cloud na AWS de forma rápida e fácil.

# Overview
Primeiramente, deve-se ressaltar que a aplicação foi desenvolvida para ser utilizada em conjunto com o [Terraform](https://www.terraform.io/). O Terraform é uma ferramenta de automação de infraestrutura que permite que o usuário crie, altere e destrua recursos de cloud de forma declarativa. O app foi desenvolvido para facilitar a criação de arquivos de configuração do Terraform, escritos em JSON.

### IMPORTANTE
Para que a aplicação funcione corretamente, é necessário que o usuário tenha o Terraform instalado em sua máquina. Para mais informações, acesse o site oficial do Terraform. Além disso, também é necessário ter o python3 com os requerimentos do arquivo `requirements.txt` instalados em um ambiente virtual.

# Funcionamento
O coração da aplicação é o arquivo `main.tf`. Esse arquivo é responsável por criar os recursos de cloud na AWS. Ele acessa os arquivos de configuração JSON, presentes na pasta `terraform/config` e cria os recursos de acordo com as informações contidas neles. O arquivo `main.tf` e todos os outros arquivos `.tf` não precisam/devem ser alterados pelo usuário, a não ser que ele queira adicionar ou remover tipos de recursos da estrutura padrão.

Como a organização e estrutura dos arquivos JSON de configuração é relativamente simples, caso o usuário deseje configurar os recursos manualmente, ele pode simplesmente alterar os arquivos JSON e executar o comando `terraform apply` para que os recursos sejam criados na AWS. Para obter exemplos, o usuário pode acessar os templates de configuração disponíveis na pasta `terraform/config-template`.

Por fim, caso o usuário deseje alterar a região da AWS, ele pode alterar o valor da variável `region` no arquivo `terraform/config/config.json`. 

# Passo a passo para o uso da aplicação
## 1. Criar um ambiente virtual com o python3
```bash
python3 -m venv ./venv
```

### 1.1 Caso esteja utilizando python3.10 ou superior
Alterar linha no arquivo: 
```
...\.venv\Lib\site-packages\prompt_toolkit\styles\from_dict.py
```
De:
```python
from collections import Mapping
```
Para:
```python 
from collections.abc import Mapping
```

## 2. Criar um arquivo .env na raiz do projeto
```bash
touch .env
```

## 2.1. Adicionar asvariáveis de ambiente no arquivo .env com base no arquivo .env.template

## 3. Ativar o ambiente virtual
```bash
source ./venv/Scripts/activate
```

## 4. Instalar os requerimentos
```bash
pip install -r requirements.txt
```

## 5. Executar o app
```bash
python main.py
```


# Fluxo de trabalho

O fluxo de funcionamento do app leva como inspiração o fluxo de trabalho do git. O usuário cria configurações de recursos, com a função `Create` (presente na aba `Edit Plan` do app), que são salvas em arquivos JSON na pasta `commit`. Após isso, o usuário deve utilizar a função `Commit Changes` (presente na aba `Edit Plan` do app) para que as configurações criadas sejam copiadas para a pasta `terraform/config` (que o arquivo `main.tf` utiliza como base para aplicar o plano). Por fim, o usuário deve utilizar a função `apply` (presente na aba `Execute Command` do app) para que as configurações sejam enviadas para a AWS.

Para desfazer mudanças salvas na pasta `commit`, o usuário pode utilizar a função `Stash`, que copia as configurações da pasta `terraform/config` para a pasta `commit`.

## Fluxo de funcionamento:
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
