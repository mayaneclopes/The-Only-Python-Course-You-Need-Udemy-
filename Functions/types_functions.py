def pure_fc(paramet):
    return paramet * 10

total = 0

#not recommended
def impure_fc(paramet):
    global total
    total += paramet
    
def recursive_fc(p):
    if p == 0:
        return "All done"
    return recursive_fc(p-1)
print(recursive_fc(3))

#anon functions/lambdas
types = ["A", "B", "C", "B"]

variable_name = list(filter(lambda name: name=="B", types))
print(variable_name)

nome_completo = lambda nome,sobrenome: f'Nome: {nome.title()}\nSobrenome: {sobrenome.title()}'
print(nome_completo('isaac','newton'))