# Sistema Especialista de Doação de Sangue

Este projeto é um Sistema Especialista para determinar a elegibilidade de doadores de sangue com base em critérios como tipo sanguíneo, fator Rh, idade e peso. A interface gráfica foi desenvolvida em Python utilizando a biblioteca Tkinter e integra-se com uma base de conhecimento em Prolog.

## Funcionalidades

1. **Doar para Específico**: Determine quem está apto a doar para um receptor específico.
2. **Consultas de Pessoa**: Verifique para quem uma pessoa pode doar ou de quem pode receber sangue.
3. **Doadores por Fator Rh**: Identifique pessoas com um determinado tipo sanguíneo ou fator Rh.

## Instalação

1. **Clone o Repositório**:

   ```bash
   git clone https://github.com/limaon/sistema_doacao_sangue.git
   cd sistema_doacao_sangue
   ```

2. **Instale o SWI-Prolog**:

   Baixe e instale o [SWI-Prolog](https://www.swi-prolog.org/Download.html).

   Ou

   No Ubuntu:
   ```
   sudo apt install sudo apt-get install swi-prolog
   ```

3. **Configure o Ambiente Virtual e Instale Dependências**:

   ```bash
   python -m venv venv
   # Ative o ambiente virtual
   # No Windows:
   venv\Scripts\activate
   # No Unix ou MacOS:
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Execute o Sistema**:

   ```bash
   python main.py
   ```

## Uso

1. **Doar para Específico**: Insira o nome do receptor e clique em "Consultar" para ver os doadores aptos.
2. **Consultas de Pessoa**: Insira o nome da pessoa e escolha entre "Para Quem Pode Doar" ou "De Quem Pode Receber".
3. **Doadores por Fator Rh**: Selecione o tipo sanguíneo ou fator Rh e clique em "Buscar" para listar os doadores correspondentes.

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a licença MIT.

## **9. Testando o Sistema**

Com todos os arquivos configurados e o ambiente preparado, iniciar o sistema executando o script `main.py`. A interface gráfica será aberta, iniciando a interação com a base de conhecimento Prolog através das diferentes funcionalidades.

### **9.1. Exemplos das Consultas**

#### **9.1.1. Doar para Específico**

- **Nome do Receptor**: `ana`

  **Resultado Esperado**:

  ```
  Doadores aptos para Ana:
  - Joao
  - Davi
  ```

#### **9.1.2. Consultas de Pessoa**

- **Nome da Pessoa**: `joao`

  - **Para Quem Pode Doar**:

    ```
    Joao pode doar para:
    - Joao
    - Davi
    - Alice
    - Jose
    ```

  - **De Quem Pode Receber**:

    ```
    Joao pode receber de:
    - Joao
    - Manuel
    - Telma
    ```

#### **9.1.3. Doadores por Fator Rh**

- **Tipo Sanguíneo**: `a`

  **Resultado**:

  ```
  Pessoas com tipo sanguíneo A:
  - Joao
  - Davi
  - Maria
  - Ana
  - Alice
  - Pedro
  ```

- **Fator Rh**: `+`

  **Resultado**:

  ```
  Pessoas com fator Rh +:
  - Joao
  - Davi
  - Julia
  - Alice
  - Laura
  - Vitoria
  - Manuel
  - Jose
  ```
