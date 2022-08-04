import tkinter as tk

frame = tk.Tk()
frame.title("Fucking tradutor Viking!")
frame.geometry('400x200')


def printInput():
    texto = inputtxt.get(1.0, "end-1c").upper()
    texto = texto.replace('F', '\u16A0')
    texto = texto.replace('U', '\u16A2')
    texto = texto.replace('TH', '\u16A6')
    texto = texto.replace('R', '\u16B1')
    texto = texto.replace('A', '\u16AB')
    texto = texto.replace('C', '\u16B2')
    texto = texto.replace('Q', '\u16B2')
    texto = texto.replace('K', '\u16B2')
    texto = texto.replace('G', '\u16B7')
    texto = texto.replace('W', '\u16B9')
    texto = texto.replace('V', '\u16B9')
    texto = texto.replace('H', '\u16BA')
    texto = texto.replace('N', '\u16BE')
    texto = texto.replace('I', '\u16C1')
    texto = texto.replace('J', '\u16C3')
    texto = texto.replace('EO', '\u16C7')
    texto = texto.replace('P', '\u16C8')
    texto = texto.replace('Z', '\u16C9')
    texto = texto.replace('Y', '\u16C3')
    texto = texto.replace('S', '\u16CB')
    texto = texto.replace('T', '\u16CF')
    texto = texto.replace('B', '\u16D2')
    texto = texto.replace('E', '\u16D6')
    texto = texto.replace('M', '\u16D7')
    texto = texto.replace('L', '\u16DA')
    texto = texto.replace('ING', '\u16DC')
    texto = texto.replace('O', '\u16DF')
    texto = texto.replace('D', '\u16DE')
    texto = texto.replace('X', '\u16B2' + '\u16CA')
    texto = texto.replace(' ', ':')
    texto = texto.replace('Á', '\u16AB')
    texto = texto.replace('É', '\u16D6')
    texto = texto.replace('Ó', '\u16DF')
    texto = texto.replace('Ý', '\u16C3')
    texto = texto.replace('Æ', '\u16AB' + '\u16D6')
    texto = texto.replace('Ú', '\u16A2')
    texto = texto.replace('Ð', '\u16DE')
    texto = texto.replace('Í', '\u16C1')
    texto = texto.replace(',', '')
    texto = texto.replace('Þ', '\u16A6')
    texto = texto.replace('.', '')
    lbl.config(text="Tradução: " + texto)
    with open("traducao.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)

texto1 = tk.Label(frame, text='Digite o texto que você quer traduzir: ')
texto1.pack()
inputtxt = tk.Text(frame,
                   height=5,
                   width=20)

inputtxt.pack()
printButton = tk.Button(frame,
                        text="Traduzir",
                        command=printInput)
printButton.pack()
lbl = tk.Label(frame, text="")
lbl.pack()

texto2 = tk.Label(frame, text='Criado por: Dart "Floki" Valarini ')
texto2.pack()

texto3 = tk.Label(frame, text='Será gerado um arquivo .txt com o texto para ser copiado. ')
texto3.pack()
frame.mainloop()
