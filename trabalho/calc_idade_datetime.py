from datetime import date, datetime
from dateutil.relativedelta import relativedelta

def calc_idade(ano, mes, dia):
    nasc = date(ano, mes, dia)
    hoje = datetime.today().date()
    idade = relativedelta(hoje, nasc)
    return f"Sua idade: {idade.years} anos, {idade.months} meses e {idade.days} dias."

ano = int(input('Ano: '))
mes = int(input('Mês: '))
dia = int(input('Dia: '))
resultado = calc_idade(ano, mes, dia)
print(resultado)