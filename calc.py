def calculadora():
    print("=== Calculadora em Python ===")
    print("Operações disponíveis:")
    print("+  soma")
    print("-  subtração")
    print("*  multiplicação")
    print("/  divisão")
    print("Digite 'sair' para encerrar.\n")

    while True:
        operacao = input("Escolha a operação (+, -, *, /): ").strip()

        if operacao.lower() == "sair":
            print("Calculadora encerrada.")
            break

        if operacao not in ["+", "-", "*", "/"]:
            print("Operação inválida.\n")
            continue

        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: digite apenas números.\n")
            continue

        if operacao == "+":
            resultado = n1 + n2
        elif operacao == "-":
            resultado = n1 - n2
        elif operacao == "*":
            resultado = n1 * n2
        elif operacao == "/":
            if n2 == 0:
                print("Erro: divisão por zero.\n")
                continue
            resultado = n1 / n2

        print(f"Resultado: {resultado}\n")


calculadora()

import tkinter as tk

# Função chamada ao clicar nos botões
def clicar(valor):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, atual + str(valor))

def limpar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.resizable(False, False)

# Campo de texto
entrada = tk.Entry(janela, font=("Arial", 24), justify="right")
entrada.pack(fill="x", padx=10, pady=10)

# Frame dos botões
botoes = tk.Frame(janela)
botoes.pack()

# Lista de botões
layout = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
]

# Criar botões
for texto, linha, coluna in layout:
    if texto == "=":
        btn = tk.Button(botoes, text=texto, width=5, height=2,
                        font=("Arial", 14), command=calcular)
    else:
        btn = tk.Button(botoes, text=texto, width=5, height=2,
                        font=("Arial", 14),
                        command=lambda t=texto: clicar(t))
    btn.grid(row=linha, column=coluna, padx=5, pady=5)

# Botão limpar
btn_limpar = tk.Button(janela, text="C", font=("Arial", 14),
                       command=limpar)
btn_limpar.pack(fill="x", padx=10, pady=10)

# Rodar app
janela.mainloop()

git init
git add .
git commit -m "calculadora"
