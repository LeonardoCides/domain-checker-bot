# Verificador de Disponibilidade de Domínio

Este script utiliza o Selenium WebDriver para verificar a disponibilidade de um domínio no site de registro de domínios [registro.br](https://www.registro.br). Ele verifica se um domínio específico está disponível para compra, retornando uma mensagem sobre a disponibilidade do domínio.

## Funcionalidades
- Verifica se um domínio está disponível no [registro.br](https://www.registro.br).
- Utiliza Selenium WebDriver para automatizar o processo de pesquisa no site.
- Retorna uma mensagem indicando se o domínio está disponível ou não.

## Como usar

1. **Pré-requisitos**
   - Python 3.x
   - Selenium
   - WebDriver do Chrome (ou outro navegador de sua escolha)

2. **Instalação**
   - Clone este repositório:
     ```bash
     git clone https://github.com/LeonardoCides/domain-checker-bot
     ```
   - Instale as dependências:
     ```bash
     pip install selenium
     ```

3. **Configuração**
   - Baixe o [ChromeDriver](https://sites.google.com/chromium.org/driver/) e coloque o arquivo executável no diretório correto (como especificado no código).
   - Verifique se o caminho para o ChromeDriver está correto no código:
     ```python
     service = Service("/home/axl/bots/chromedriver")  # Altere o caminho conforme necessário
     ```

4. **Execução**
   - Execute o script:
     ```bash
     python bot.py
     ```
   - O script irá verificar a disponibilidade do domínio `cides.store` e imprimir se o domínio está disponível ou não.

## Exemplo de saída
