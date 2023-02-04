# Faça um programa que leia o noem de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# Ex.: Ana Maria de Souza
# primeiro = Ana / último = Souza

nome = str(input('Digite seu nome: ')).strip()
separado = nome.split()
print(f'Seu primeiro nome é: {separado[0]}.\n'
      f'Seu último nome é: {separado[-1]}.')
      # outra forma: 
      # f'Seu ultimo nome é: {separado[len(separado)-1]}')
