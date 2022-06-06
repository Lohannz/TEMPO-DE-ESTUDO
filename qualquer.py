#EU SEI QUE UM DIA VOCÊ CONSEGUIRÁ! 

from curses import A_STANDOUT


dia = 24
qualquer_coisa = 1.30
comer = 1.30
dormir = int(input('tempo de sono:'))
escola_ou_trabalha = int(input('quantas horas você trabalha, estuda ou faz atividades obrigatórias: '))
diarest = (dia - qualquer_coisa  - comer - dormir - escola_ou_trabalha)


if dormir >= 8 and diarest < 5:
    print("tente ficar acordado mais um pouco, isso deve te dar mais tempo!")
if dormir <= 6 :
    print('dormir tão pouco assim não faz bem.')

print(f'SEU TEMPO PARA ESTUDAR É DE:{round(diarest, 2)}')
print('você tem {} horas para dormir, {} para comer e {} hora para descansar, tomar banho e refrescar a cabeça.'.format(dormir, comer, qualquer_coisa))
print('tente dar intervalos de 15 minutos a cada 1 hora de estudo. BOM SORTE GUERREIRO!.')

#LUTE E AVANCE!

