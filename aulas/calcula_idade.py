from datetime import datetime

data_nasc = input('Digite sua data de nascimento (dd//mm//aaaa):')
nascimento = datetime.strptime(data_nasc, "%d/%m/%Y")
hoje = datetime.today()
idade = hoje.year - nascimento.year

print(f'você tem {idade} anos atualmente')

if idade >= 18:
    print("Você já é de maior")
else:
    print("Você é de menor")