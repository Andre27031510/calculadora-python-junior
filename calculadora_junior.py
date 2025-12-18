import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


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

calculadora()

                    
                   
                    
                    
                
               



