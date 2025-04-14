# Reverse Shell em Python

## Autor

**Miguel** **Vasco** 

Este repositório contém um script de reverse shell em Python que permite a execução remota de comandos em uma máquina alvo.

## Funcionalidades

- Conexão reversa para executar comandos remotamente.
- Simples e fácil de usar.

## Como Usar

1. **Clone o repositório:**
    ```bash
   git clone https://github.com/Miguel-Vasco7/reverse_shell.py.git
   cd reverse_shell.py
   ```

2. **Modifique o script:**
   - Altere `<ip_do_listener>` para o seu endereço IP no script.

3. **Inicie o listener:**
   ```bash
   nc -lvp 222 
   ```

4. **Execute o script:**
   ```bash
   python3 reverse_shell.py
   ```

## Aviso

Use esta ferramenta apenas em ambientes controlados e com permissão explícita. O uso indevido pode ser ilegal.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
