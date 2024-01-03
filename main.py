import tkinter
import customtkinter
from pytube import YouTube

def iniciarDownload():
    try:
        linkYT = link.get()
        # Com isso podemos pegar varias informações referentes ao link
        objetoYT = YouTube(linkYT, on_progress_callback=progresso)
        video = objetoYT.streams.get_highest_resolution() # Pega a maior resolução do vídeo

        title.configure(text=objetoYT.title, text_color="green")
        termino.configure(text="")
        video.download() # Baixar o vídeo
        termino.configure(text="Download completo!", text_color="green")
    except:
        termino.configure(text="Erro no download, tente novamente com outro link.", text_color="red")

def progresso(stream, chunk, bytes_restante):
    # tamanho total do arquivo
    tamanho_total = stream.filesize
    bytes_baixados = tamanho_total - bytes_restante
    porcentagem_de_conclusao = bytes_baixados / tamanho_total * 100
    porcentagem = str(int(porcentagem_de_conclusao))
    nPorcentagem.configure(text=porcentagem + "%")
    nPorcentagem.update()

    # Atualizar barra de progresso
    barraProgresso. set(float(porcentagem_de_conclusao) / 100)

# Configurações de sistema
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Resolução
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Elementos UI
title = customtkinter.CTkLabel(app, text="Insira um link do Youtube")
title.pack(padx=10, pady=10)

# Link Input
url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url)
link.pack()

# Fim de download
termino = customtkinter.CTkLabel(app, text="")
termino.pack()

# Barra de progresso
nPorcentagem = customtkinter.CTkLabel(app, text="0%")
nPorcentagem.pack()

barraProgresso = customtkinter.CTkProgressBar(app, width=400)
barraProgresso.set(0)
barraProgresso.pack(padx=10, pady=10)

# Botão de download
# Sempre que o botão for clicado ele inicia a função iniciarDownload()
download = customtkinter.CTkButton(app, text="Download", command=iniciarDownload)
download.pack(padx=10 , pady=10)

# Roda o aplicativo
app.mainloop()
