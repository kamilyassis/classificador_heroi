import tkinter as tk
from tkinter import Tk, Toplevel, Label, Button
from tkinter import messagebox
from PIL import ImageTk, Image

#janela principal
root = Tk()
root.resizable(width=True, height=True)
root.title("Classificador de Nível de Herói")

def resultados(nome, nivel):
    resultado = Toplevel(root)
    resultado.title("Resultado")

    if nivel == "Desconhecido":
        result_label = Label(resultado, text=f"Desculpe, {nome}, mas seu nível é inclassificável!")
        result_label.pack(pady=10)
    elif nivel == "Ferro" or nivel == "Bronze":
        result_label = Label(resultado, text=f"Uau, {nome}... Você é um herói de nível {nivel}...")
        result_label.pack(pady=10)
    elif nivel == "Prata" or nivel == "Ouro":        
        result_label = Label(resultado, text=f"Uau, {nome}! Você é um herói de nível {nivel}! Impressionante!")
        result_label.pack(pady=10)
    elif nivel == "Imortal" or nivel == "Radiante":
        result_label = Label(resultado, text=f"{nome}.... Você é um herói de nível {nivel}?! \nPrecisamos conversar sobre suas horas de jogo...")
        result_label.pack(pady=10)
    else:
        result_label = Label(resultado, text=f"Uau, {nome}! Você é um herói de nível {nivel}. Você é incrível!")
        result_label.pack(pady=10)

    #imagem de acordo com o nível
    if nivel == "Ferro":
        img = Image.open('images/ferro.png')
    elif nivel == "Bronze":
        img = Image.open('images/bronze.jpg')        
    elif nivel == "Prata":
        img = Image.open('images/prata.jpg')        
    elif nivel == "Ouro":
        img = Image.open('images/ouro.jpg')        
    elif nivel == "Platina":
        img = Image.open('images/platina.jpg')        
    elif nivel == "Ascendente":
        img = Image.open('images/ascendente.png')        
    elif nivel == "Imortal":
        img = Image.open('images/imortal.jpg')        
    elif nivel == "Radiante":
        img = Image.open('images/radiante.png')        
    else:
        img = Image.open('images/desconhecido.jpg')

    #ajustes img
    img = img.resize((250, 250), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    img_label = Label(resultado, image=img)
    img_label.image = img
    img_label.pack(pady=10)

    #fechar so a janela do resultado
    ok_button = Button(resultado, text="OK", command=resultado.destroy)
    ok_button.pack(pady=10)

def classificar_heroi():
    nome_usuario = nome.get()

    try:
        xp = int(xp_usuario.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido para XP.")
        return

    if xp < 1000:
        nivel = "Ferro"
    elif 1001 <= xp <= 2000:
        nivel = "Bronze"
    elif 2001 <= xp <= 5000:
        nivel = "Prata"
    elif 5001 <= xp <= 7000:
        nivel = "Ouro"
    elif 7001 <= xp <= 8000:
        nivel = "Platina"
    elif 8001 <= xp <= 9000:
        nivel = "Ascendente"
    elif 9001 <= xp <= 10000:
        nivel = "Imortal"
    elif xp >= 10001:
        nivel = "Radiante"
    else:
        nivel = "Desconhecido"

    resultados(nome_usuario, nivel)

#interface
tk.Label(root, text="Seu nome, Herói:").grid(row=0, column=0, padx=10, pady=10)
nome = tk.Entry(root)
nome.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Quanto de XP você tem? ").grid(row=1, column=0, padx=10, pady=10)
xp_usuario = tk.Entry(root)
xp_usuario.grid(row=1, column=1, padx=10, pady=10)

classificador = tk.Button(root, text="verificar", command=classificar_heroi)
classificador.grid(row=2, columnspan=2, pady=20)

#loop da interface
root.mainloop()
