import os
import tkinter as tk 
from tkinter import messagebox

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculadora_grafica():
    janela = tk.Tk()
    janela.title('Calculadora Python Junior')
    janela.geometry('320x450')
    janela.configure(bg='#f0f0f0')
    janela.resizable(False, False)
    
    # Configurar colunas para ficarem mais próximas
    for i in range(4):
        janela.grid_columnconfigure(i, weight=1, uniform='col')

    display_var = tk.StringVar()
    display_var.set('0')
    num1 = 0
    operacao = ''
    novo_numero = True
    historico = []  # Lista para armazenar histórico de cálculos

    def clicar_numero(numero):
        nonlocal novo_numero
        if novo_numero:
            display_var.set(str(numero))
            novo_numero = False
        else:
            atual = display_var.get()
            display_var.set(atual + str(numero))

    def clicar_operacao(op):
        nonlocal num1, operacao, novo_numero
        num1 = float(display_var.get())
        operacao = op
        novo_numero = True

    def calcular_resultado():
        nonlocal num1, operacao, novo_numero, historico
        try:
            num2 = float(display_var.get())
            if operacao == '+':
                resultado = num1 + num2
                calculo = f'{num1} + {num2} = {resultado}'
            elif operacao == '-':
                resultado = num1 - num2
                calculo = f'{num1} - {num2} = {resultado}'
            elif operacao == 'x':
                resultado = num1 * num2
                calculo = f'{num1} x {num2} = {resultado}'
            elif operacao == '÷':
                if num2 != 0:
                    resultado = num1 / num2
                    calculo = f'{num1} ÷ {num2} = {resultado}'
                else:
                    display_var.set('Erro')
                    return
            elif operacao == '**':
                resultado = num1 ** num2
                calculo = f'{num1} ** {num2} = {resultado}'
            elif operacao == '%':
                resultado = (num2 / 100) * num1
                calculo = f'{num2}% de {num1} = {resultado}'
            
            historico.append(calculo)  # Adiciona ao histórico
            display_var.set(str(resultado))
            novo_numero = True
        except:
            display_var.set('Erro')

    def limpar():
        nonlocal num1, operacao, novo_numero
        display_var.set('0')
        num1 = 0
        operacao = ''
        novo_numero = True

    def raiz_quadrada():
        nonlocal historico
        try:
            num = float(display_var.get())
            if num >= 0:
                resultado = num ** 0.5
                calculo = f'√{num} = {resultado}'
                historico.append(calculo)  # Adiciona ao histórico
                display_var.set(str(resultado))
            else:
                display_var.set('Erro')
        except:
            display_var.set('Erro')
    
    def mostrar_historico():
        if historico:
            hist_texto = '\n'.join(historico[-10:])  # Últimos 10 cálculos
            messagebox.showinfo('Histórico', f'Últimos cálculos:\n\n{hist_texto}')
        else:
            messagebox.showinfo('Histórico', 'Nenhum cálculo realizado ainda.')

    # Display
    display = tk.Entry(janela, textvariable=display_var, font=('Arial', 24), 
                      justify='right', state='readonly', bg='white', bd=3, relief='sunken')
    display.grid(row=0, column=0, columnspan=4, padx=5, pady=15, sticky='ew', ipady=10)

    # Botões - Linha 1
    tk.Button(janela, text='C', font=('Arial', 14), bg='#ff9999', 
              command=limpar, width=6, height=2).grid(row=1, column=0, padx=1, pady=1, sticky='ew')
    tk.Button(janela, text='√', font=('Arial', 14), bg='#ffcc99', 
              command=raiz_quadrada, width=6, height=2).grid(row=1, column=1, padx=1, pady=1, sticky='ew')
    tk.Button(janela, text='**', font=('Arial', 14), bg='#ffcc99', 
              command=lambda: clicar_operacao('**'), width=6, height=2).grid(row=1, column=2, padx=1, pady=1, sticky='ew')
    tk.Button(janela, text='÷', font=('Arial', 14), bg='#cce5ff', 
              command=lambda: clicar_operacao('÷'), width=6, height=2).grid(row=1, column=3, padx=1, pady=1, sticky='ew')

    # Botões - Linha 2
    tk.Button(janela, text='7', font=('Arial', 14), bg='white', 
              command=lambda: clicar_numero(7), width=6, height=2).grid(row=2, column=0, padx=1, pady=1, sticky='ew')
    tk.Button(janela, text='8', font=('Arial', 14), bg='white', 
              command=lambda: clicar_numero(8), width=6, height=2).grid(row=2, column=1, padx=1, pady=1, sticky='ew')
    tk.Button(janela, text='9', font=('Arial', 14), bg='white', 
              command=lambda: clicar_numero(9), width=6, height=2).grid(row=2, column=2, padx=1, pady=1, sticky='ew')
    tk.Button(janela, text='x', font=('Arial', 14), bg='#cce5ff', 
              command=lambda: clicar_operacao('x'), width=6, height=2).grid(row=2, column=3, padx=1, pady=1, sticky='ew')

    # Botões - Linha 3
    tk.Button(janela, text='4', font=('Arial', 14), bg='white', 
              command=lambda: clicar_numero(4), width=6, height=2).grid(row=3, column=0, padx=1, pady=1, sticky='ew')
    tk.Button(janela, text='5', font=('Arial', 14), bg='white', 
              command=lambda: clicar_numero(5), width=6, height=2).grid(row=3, column=1, padx=1, pady=1, sticky='ew')
    tk.Button(janela, text='6', font=('Arial', 14), bg='white', 
              command=lambda: clicar_numero(6), width=6, height=2).grid(row=3, column=2, padx=1, pady=1, sticky='ew')
    tk.Button(janela, text='-', font=('Arial', 14), bg='#cce5ff', 
              command=lambda: clicar_operacao('-'), width=6, height=2).grid(row=3, column=3, padx=1, pady=1, sticky='ew')

    # Botões - Linha 4
    tk.Button(janela, text='1', font=('Arial', 14), bg='white', 
              command=lambda: clicar_numero(1), width=6, height=2).grid(row=4, column=0, padx=1, pady=1, sticky='ew')
    tk.Button(janela, text='2', font=('Arial', 14), bg='white', 
              command=lambda: clicar_numero(2), width=6, height=2).grid(row=4, column=1, padx=1, pady=1, sticky='ew')
    tk.Button(janela, text='3', font=('Arial', 14), bg='white', 
              command=lambda: clicar_numero(3), width=6, height=2).grid(row=4, column=2, padx=1, pady=1, sticky='ew')
    tk.Button(janela, text='+', font=('Arial', 14), bg='#cce5ff', 
              command=lambda: clicar_operacao('+'), width=6, height=2).grid(row=4, column=3, padx=1, pady=1, sticky='ew')

    # Botões - Linha 5
    tk.Button(janela, text='H', font=('Arial', 14), bg='#cccccc', 
              command=mostrar_historico, width=6, height=2).grid(row=5, column=0, padx=1, pady=1, sticky='ew')
    tk.Button(janela, text='0', font=('Arial', 14), bg='white', 
              command=lambda: clicar_numero(0), width=6, height=2).grid(row=5, column=1, padx=1, pady=1, sticky='ew')
    tk.Button(janela, text='.', font=('Arial', 14), bg='white', 
              command=lambda: clicar_numero('.'), width=6, height=2).grid(row=5, column=2, padx=1, pady=1, sticky='ew')
    tk.Button(janela, text='=', font=('Arial', 14), bg='#0066cc', fg='white', 
              command=calcular_resultado, width=6, height=2).grid(row=5, column=3, padx=1, pady=1, sticky='ew')

    janela.mainloop()


def calculadora():
    historico = []
    # menu principal 
    while True:
        
        print(f'{"=" * 5} Calculadora {"=" * 5}')
        print('Selecione a operação desejada:') 
        print(f'[1] - Soma (+)')
        print(f'[2] - Subtração (-)')
        print(f'[3] - Multiplicação (x)')
        print(f'[4] - Divisão (/)')
        print(f'[5] - Potenciação (**)')
        print(f'[6] - Raiz Quadrada (√)')
        print(f'[7] - Porcentagem (%)')
        print(f'[8] - Histórico de Operações')
        print(f'[9] - Sair')

        operacao = input('Digite a operação desejada (1/2/3/4/5/6/7/8): ')

        if operacao in ['1', '2', '3', '4', '5', '6', '7']:
  
            print(f'{"-" * 10} Você escolheu a operação {operacao} {"-" * 10}')

            try:
                num1 = float(input('Digite o primeiro número: '))
                num2 = float(input('Digite o segundo número: '))
            except ValueError:
                print('Entrada inválida. Por favor, insira números válidos.')
                continue
        
          
            if operacao == '1':
                resultado = num1 + num2
                calculo = f'{num1} + {num2} = {resultado}'
                historico.append(calculo)
                print(f'O resultado de {num1} + {num2} é: {resultado}')
                input('Pressione Enter para continuar...')
            elif operacao == '2':
                resultado = num1 - num2
                calculo = f'{num1} - {num2} = {resultado}'
                historico.append(calculo)
                print(f'O resultado de {num1} - {num2} é: {resultado}')
                input('Pressione Enter para continuar...')
            elif operacao == '3':
                resultado = num1 * num2
                calculo = f'{num1} x {num2} = {resultado}'
                historico.append(calculo)
                print(f'O resultado de {num1} x {num2} é: {resultado}')
                input('Pressione Enter para continuar...')
            elif operacao == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    calculo = f'{num1} / {num2} = {resultado}'
                    historico.append(calculo)
                    print(f'O resultado de {num1} / {num2} é: {resultado}')
                else:
                    print('Erro: Divisão por zero não é permitida.')
                    continue
            elif operacao == '5':
                resultado = num1 ** num2
                calculo = f'{num1} ** {num2} = {resultado}'
                historico.append(calculo)
                print(f'O resultado de {num1} ** {num2} é: {resultado}')
            elif operacao == '6':
                try:
                    num1 = float(input('Digite o número para calcular a raiz quadrada: '))
                    if num1 >= 0:
                         resultado1 = num1 ** 0.5
                         calculo1 = f'√{num1} = {resultado1}'
                         historico.append(calculo1)
                         print(f'A raiz quadrada de {num1} é: {resultado1}')
                    else:
                         print('Erro: Raiz quadrada de número negativo não é permitida.')
                except ValueError:
                    print('Digite apenas números!')
                
            elif operacao == '7':
                resultado = (num2 / 100) * num1
                calculo = f'{num2}% de {num1} = {resultado}'
                historico.append(calculo)
                print(f'{num2}% de {num1} é: {resultado}')
        elif operacao == '8':
            print(f'{"-" * 10} Histórico de Operações {"-" * 10}')
            if historico:
                for item in historico:
                    print(item)
            else:
                print('Nenhuma operação realizada ainda.')

            input('Pressione Enter para continuar...')
        elif operacao == '9':
            limpar_tela()
            
            print('Saindo da calculadora. Até mais!')
            break
        else:
            print('Operação inválida. Por favor, tente novamente.')
        print('\n') 

calculadora_grafica()


                    
                   
                    
                    
                
               





                    
                   
                    
                    
                
               



