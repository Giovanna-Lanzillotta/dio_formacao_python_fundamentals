# Inner functions
# Definir funções dentro de outras funções

def pai():
    print("Escrevendo da pai() função")

    def filho1():
        print("Escrevendo da filho1() função")

        def neto():
            print("Escrevendo neto() da função")


        neto()


    def filho2():
        print("Escrevendo da filho2() função")

    
    filho2()
    filho1()


pai()