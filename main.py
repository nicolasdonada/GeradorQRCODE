from tkinter import *
import qrcode
import os

class Qrcode:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Gerador de QRCODE")
        self.janela.geometry("400x400")
        self.janela.resizable(False, False)
        self.janela.config(bg="#333333")

        self.qrcode_image = None
        # --------------------------------------

        self.label1 = Label(self.janela, width=10, height=2, text="Digite aqui:", bg="#333333", fg="white", font="Arial 14")
        self.label1.place(x=10, y=21)
        # --------------------------------------

        self.entry1 = Entry(self.janela, width=25)
        self.entry1.place(x=140, y=38)
        # --------------------------------------

        self.botao1 = Button(self.janela, width=12, height=1, text="Gerar QRCODE", relief="flat", command=self.gerar)
        self.botao1.place(x=300, y=34)

        self.botao2 = Button(self.janela, width=12, height=1, text="Deletar QRCODE", relief="flat", command=self.deletar)
        self.botao2.place(x=300, y=340)
        # --------------------------------------

        self.label2 = Label(self.janela, bg="white")
        self.label2.pack(anchor="center", pady=70)

        self.janela.mainloop()

    def gerar(self):

        data = str(self.entry1.get())

        # Criação do objeto QRCode
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )

        # Adiciona os dados ao QR Code
        qr.add_data(data)
        qr.make(fit=True)

        # Cria uma imagem do QR Code
        img = qr.make_image(fill_color="black", back_color="white")

        filename = "qrcode.png"

        # Salva a imagem em um arquivo
        img.save("qrcode.png")

        qrcode1 = PhotoImage(file="qrcode.png")
        self.label2.configure(image=qrcode1)
        self.label2.image = qrcode1
        self.qrcode_image = PhotoImage(file=filename)

    
    def deletar(self):
        self.entry1.delete(0, END)
        

        filename = "qrcode.png"
        if os.path.exists(filename):
            os.remove(filename)
            self.label2.configure(image=None)  # Limpa a imagem do Label
            self.qrcode_image = None  # Limpa a referência da imagem

        

code = Qrcode()