def decorator_imprimir (funcao):
    def estender_funcao_juros_simples(capital, taxa, tempo):
        print(f"CAPITAL: {capital} TAXA: {taxa} TEMPO: {tempo}")
        resultado = funcao(capital, taxa, tempo)
        print(f"RESULTADO: {resultado}")
    return estender_funcao_juros_simples

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

def juros_simples_sem_decorator(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

juros_simples(1000, 5, 6)