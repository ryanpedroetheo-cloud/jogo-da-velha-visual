import tkinter as tk
from tkinter import messagebox

# Função para verificar se há vencedor
def verificar_vitoria():
    for i in range(3):
        # Linhas
        if botoes[i][0]["text"] == botoes[i][1]["text"] == botoes[i][2]["text"] != "":
            messagebox.showinfo("Vitória!", f"Jogador {botoes[i][0]['text']} venceu!")
            reiniciar_tabuleiro()
            return
        # Colunas
        if botoes[0][i]["text"] == botoes[1][i]["text"] == botoes[2][i]["text"] != "":
            messagebox.showinfo("Vitória!", f"Jogador {botoes[0][i]['text']} venceu!")
            reiniciar_tabuleiro()
            return
    # Diagonais
    if botoes[0][0]["text"] == botoes[1][1]["text"] == botoes[2][2]["text"] != "":
        messagebox.showinfo("Vitória!", f"Jogador {botoes[0][0]['text']} venceu!")
        reiniciar_tabuleiro()
        return
    if botoes[0][2]["text"] == botoes[1][1]["text"] == botoes[2][0]["text"] != "":
        messagebox.showinfo("Vitória!", f"Jogador {botoes[0][2]['text']} venceu!")
        reiniciar_tabuleiro()
        return

# Função para marcar a jogada
def clicar(linha, coluna):
    if botoes[linha][coluna]["text"] == "":
        botoes[linha][coluna]["text"] = jogador_atual.get()
        verificar_vitoria()
        jogador_atual.set("O" if jogador_atual.get() == "X" else "X")

# Reinicia o tabuleiro (sem zerar o placar)
def reiniciar_tabuleiro():
    for linha in botoes:
        for botao in linha:
            botao.config(text="")

# Alterna entre tema claro e escuro
def mudar_tema():
    global tema_escuro
    tema_escuro = not tema_escuro
    if tema_escuro:
        janela.config(bg="#333333")
        for linha in botoes:
            for botao in linha:
                botao.config(bg="#555555", fg="white")
        frame_botoes.config(bg="#333333")
        btn_reiniciar.config(bg="#555555", fg="white")
        btn_tema.config(bg="#555555", fg="white", text="Tema Claro")
    else:
        janela.config(bg="#f0f0f0")
        for linha in botoes:
            for botao in linha:
                botao.config(bg="#ffffff", fg="black")
        frame_botoes.config(bg="#f0f0f0")
        btn_reiniciar.config(bg="#ffffff", fg="black")
        btn_tema.config(bg="#ffffff", fg="black", text="Tema Escuro")


janela = tk.Tk()
janela.title("Jogo da Velha")
janela.geometry("300x370")

# Tema inicial
tema_escuro = False
janela.config(bg="#f0f0f0")

# Armazena quem joga
jogador_atual = tk.StringVar(value="X")

# Grade de botões (tabuleiro)
botoes = []
for i in range(3):
    linha = []
    for j in range(3):
        botao = tk.Button(janela, text="", width=10, height=3, font=("Arial", 16),
                          command=lambda i=i, j=j: clicar(i, j), bg="#ffffff")
        botao.grid(row=i, column=j, padx=5, pady=5)
        linha.append(botao)
    botoes.append(linha)

# Frame com botões de controle
frame_botoes = tk.Frame(janela, bg="#f0f0f0")
frame_botoes.grid(row=3, column=0, columnspan=3, pady=10)

btn_reiniciar = tk.Button(frame_botoes, text="Reiniciar Partida", font=("Arial", 10),
                          command=reiniciar_tabuleiro, bg="#ffffff")
btn_reiniciar.pack(side="left", padx=10)

btn_tema = tk.Button(frame_botoes, text="Tema Escuro", font=("Arial", 10),
                     command=mudar_tema, bg="#ffffff")
btn_tema.pack(side="left", padx=10)

janela.mainloop()
