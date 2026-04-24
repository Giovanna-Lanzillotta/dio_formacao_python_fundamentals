# Função de decoração com argumentos
# Usando *args e **kwargs na função interna

def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    
    return envelope


@duplicar
def aprender(tecnologia):
    print(f"💻 Estou aprendendo {tecnologia}")



aprender("Pyhon")