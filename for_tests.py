from dateutil.relativedelta import relativedelta
from datetime import datetime, date

def calcula(ano, mes, dia):
    nasc = date(ano, mes, dia)
    hoje = datetime.today().date()
    idade = relativedelta(nasc, hoje)
    return f'{idade.months} meses e {idade.days} dias'

ano = int(input('Ano: '))
mes = int(input('Mês: '))
dia = int(input('Dia: '))
resultado = calcula(ano, mes, dia)
print(resultado)