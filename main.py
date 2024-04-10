import tkinter
from tkinter import *
from tkinter import ttk

co0 = "#FFFFFF"
co1 = "#333333"
co2 = "#fcc058"
co3 = "#38576b"
co4 = "#3297a8"
co5 = "#fff873"
co6 = "#fcc058"
co7 = "#e85151"
co8 = co4
co10 = "#fcfbf7"
fundo = "#3b3b3b"

janela = Tk()
janela.title('')
janela.geometry('260x370')
janela.configure(bg=fundo)


pontuacao_1 = 0
pontuacao_2 = 0

frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

# X
app_x = Label(frame_cima, text="X", height=1, relief="flat", anchor="center", font=('Ivy 40 bold'), bg=co1, fg=co7)
app_x.place(x=25, y=10)
app_x = Label(frame_cima, text="Jogador 1", height=1, relief="flat", anchor="center", font=('Ivy 7 bold'), bg=co1, fg=co0)
app_x.place(x=17, y=70)
app_x_pontos = Label(frame_cima, text=pontuacao_1, height=1, relief="flat", anchor="center", font=('Ivy 30 bold'), bg=co1, fg=co0)
app_x_pontos.place(x=80, y=20)

# separador 

app_separador = Label(frame_cima, text=":", height=1, relief="flat", anchor="center", font=('Ivy 30 bold'), bg=co1, fg=co0)
app_separador.place(x=110, y=20)


# O
app_o = Label(frame_cima, text="O", height=1, relief="flat", anchor="center", font=('Ivy 40 bold'), bg=co1, fg=co4)
app_o.place(x=170, y=10)
app_o = Label(frame_cima, text="Jogador 2", height=1, relief="flat", anchor="center", font=('Ivy 7 bold'), bg=co1, fg=co0)
app_o.place(x=165, y=70)
app_o_pontos = Label(frame_cima, text=pontuacao_2, height=1, relief="flat", anchor="center", font=('Ivy 30 bold'), bg=co1, fg=co0)
app_o_pontos.place(x=130, y=20)



# Logica

jogador_1 = "X"
jogador_2 = "O"

tabela = [['1', '2', '3'] , ['4', '5', '6'] , ['7', '8', '9']]

jogando = 'X'
contador  = 0
joga = ''

def iniciar_jogo():
    def controlar(botao):
        global jogando
        global contador 
        global joga 
        global pontuacao_1
        global pontuacao_2

        # Verificando se o botão não esta preenchido
        if botao['text'] == '':
            if jogando == 'X':
                cor = co7
            if jogando == 'O':
                cor = co8
            
            botao['fg'] = cor
            botao['text'] = jogando
            
            # Atualizar a matriz tabela
            for i in range(3):
                for j in range(3):
                    if botao == btns[i*3+j]:
                        tabela[i][j] = jogando

            contador += 1

            # Imprimir o estado atual da matriz tabela
            print("Matriz tabela após jogada:")
            for row in tabela:
                print(row)

            # Lógica de verificação do vencedor de acordo com as colunas horizontais, verticais e deitadas, ou empate
            if contador >= 5 and contador < 9:
                for i in range(3):
                    # Verificar linhas
                    if tabela[i][0] == tabela[i][1] == tabela[i][2] != '':
                        vencedor(jogando)
                        print('Vencedor na linha', i+1)
                for j in range(3):
                    # Verificar colunas
                    if tabela[0][j] == tabela[1][j] == tabela[2][j] != '':
                        vencedor(jogando)
                        print('Vencedor na coluna', j+1)
                # Verificar diagonais
                if tabela[0][0] == tabela[1][1] == tabela[2][2] != '':
                    vencedor(jogando)
                    print('Vencedor na diagonal principal')
                if tabela[0][2] == tabela[1][1] == tabela[2][0] != '':
                    vencedor(jogando)
                    print('Vencedor na diagonal secundária')
            if contador == 9:
                vencedor("Empate")


            # Alternar jogador
            if jogando == 'X':
                jogando = 'O'
                joga = "Jogador 1"
            else: 
                jogando = 'X'
                joga = "Jogador 2"

    def vencedor(vencedor):
        global tabela
        global contador
        contador = 0
        tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        global pontuacao_1
        global pontuacao_2

        # Dá a pontuação para o vencedor ou notifica o empate
        if vencedor=="X":
            pontuacao_1 += 1
        elif vencedor=="O":
            pontuacao_2 += 1
        else:
            print("Empate!")

        # Atualizar o texto dos widgets de pontuação
        app_x_pontos.config(text=pontuacao_1)
        app_o_pontos.config(text=pontuacao_2)

        # Print das pontuações atualizadas (opcional)
        print("Pontuação do Jogador 1:", pontuacao_1)
        print("Pontuação do Jogador 2:", pontuacao_2)

        btn_0.config(text='')
        btn_1.config(text='')
        btn_2.config(text='')
        btn_3.config(text='')
        btn_4.config(text='')
        btn_5.config(text='')
        btn_6.config(text='')
        btn_7.config(text='')
        btn_8.config(text='')
        
        #temrinar jogo
    
    # linhas 
    app_linha1 = Label(frame_baixo, text="", height=23, relief="flat", pady=5 ,anchor="center", font=('Ivy 5 bold'), bg=co0, fg=co0)
    app_linha1.place(x=90, y=15)

    app_linha2 = Label(frame_baixo, text="", height=23, relief="flat", pady=5 ,anchor="center", font=('Ivy 5 bold'), bg=co0, fg=co0)
    app_linha2.place(x=157, y=15)

    app_linha3 = Label(frame_baixo, text="  ", width=46, relief="flat", padx=2 ,anchor="center", font=('Ivy 5 bold'), bg=co0, fg=co0)
    app_linha3.place(x=30, y=63)

    app_linha4 = Label(frame_baixo, text="  ", width=46, relief="flat", padx=2 ,anchor="center", font=('Ivy 5 bold'), bg=co0, fg=co0)
    app_linha4.place(x=30, y=123)

    # Linha 1 botão
    btn_0 = Button(frame_baixo, command=lambda: controlar(btns[0]), text="", width=3, font=('Ivy 20 bold'), relief="flat", overrelief=RIDGE, bg=fundo, fg=co7)
    btn_0.place(x=30, y=15)

    btn_1 = Button(frame_baixo, command=lambda: controlar(btns[1]), text="", width=3, font=('Ivy 20 bold'), relief="flat", overrelief=RIDGE, bg=fundo, fg=co7)
    btn_1.place(x=96, y=15)

    btn_2 = Button(frame_baixo, command=lambda: controlar(btns[2]), text="", width=3, font=('Ivy 20 bold'), relief="flat", overrelief=RIDGE, bg=fundo, fg=co7)
    btn_2.place(x=162, y=15)

    # Linha 2 botão
    btn_3 = Button(frame_baixo, command=lambda: controlar(btns[3]), text="", width=3, font=('Ivy 20 bold'), relief="flat", overrelief=RIDGE, bg=fundo, fg=co7)
    btn_3.place(x=30, y=75)

    btn_4 = Button(frame_baixo, command=lambda: controlar(btns[4]), text="", width=3, font=('Ivy 20 bold'), relief="flat", overrelief=RIDGE, bg=fundo, fg=co7)
    btn_4.place(x=96, y=75)

    btn_5 = Button(frame_baixo, command=lambda: controlar(btns[5]), text="", width=3, font=('Ivy 20 bold'), relief="flat", overrelief=RIDGE, bg=fundo, fg=co7)
    btn_5.place(x=162, y=75)

    # Linha 3 botão
    btn_6 = Button(frame_baixo, command=lambda: controlar(btns[6]), text="", width=3, font=('Ivy 20 bold'), relief="flat", overrelief=RIDGE, bg=fundo, fg=co7)
    btn_6.place(x=30, y=135)

    btn_7 = Button(frame_baixo, command=lambda: controlar(btns[7]), text="", width=3, font=('Ivy 20 bold'), relief="flat", overrelief=RIDGE, bg=fundo, fg=co7)
    btn_7.place(x=96, y=135)

    btn_8 = Button(frame_baixo, command=lambda: controlar(btns[8]), text="", width=3, font=('Ivy 20 bold'), relief="flat", overrelief=RIDGE, bg=fundo, fg=co7)
    btn_8.place(x=162, y=135)

    btns = [btn_0, btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8]

# Botão iniciar jogo 

btn_iniciar = Button(frame_baixo, command=iniciar_jogo, text="Jogar", width=10, font=('Ivy 10 bold'), relief="raised", overrelief=RIDGE, bg=fundo, fg=co0)
btn_iniciar.place(x=82, y=195)


janela.mainloop()
