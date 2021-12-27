print('COMANDOS: 1 - calculadorazinha (soma, subtrai, multiplica ou divide números) \n mais comandos serão adicionados quando eu tiver um tempinho ')

comando = input('\n opa! bem vindo! selecione um comando :D \n')


if comando == '1':
  conta = input('selecione um tipo de soma colocando o simbolo, por exemplo, + para somas e - para subtração. \n')
  if conta ==  '+':
    num1 = int(input('selecione um número (um inteiro, não queremos quebrar a calculadora!) (esse número irá receber a soma! \n'))
    
    num2 = int(input('agora seleciona outro número (esse será a soma!) \n '))

    print('certo! hmm... ')
    
    soma = num1 + num2 
    print(soma)
  elif conta == '-':
   num1 = int(input('selecione um número (um inteiro, não queremos quebrar a calculadora!) (esse número irá receber a subtraxao!) \n'))

   num2 = int(input('selecione outro número (esse irá ser a subrtração!)\n'))
   sub = num1 - num2

   print('Certo! hmm')
   print(sub)
  elif conta == '/':
    num1 = int(input('selecione um número (um inteiro, não queremos quebrar a calculadora!) (esse irá receber a divisão! \n'))

    num2 = int(input('selecione outro número (esse irá ser a divisão) \n'))

    div = num1 / num2 

    print('certo! hmm... ')
    print(int(div))
  elif conta == '*':
    num1 = int(input('selecione um número (um inteiro kk), (esse irá ser multiplicado!) \n')) 
    num2 = int(input('selecione outro número (será a multiplicação!\n'))

    multi = num1 * num2
    print('certo! hmm...')
    print(multi)
