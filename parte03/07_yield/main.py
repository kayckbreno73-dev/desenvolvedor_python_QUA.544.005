from modulo import eq_2o_grau, limpar

def main():
    limpar()
    print("calculo da equação do segundo grau")

    a=float(input("informe um valor de 'a': ").replace(",","."))
    b=float(input("informe um valor de 'b': ").replace(",","."))
    c=float(input("informe um valor de 'c': ").replace(",","."))

    limpar()

    if a !=0:
        result=eq_2o_grau(a,b,c)
        print("resultado da equação de 2o grau: ")
        for x in result:
            print(f"x = {x}")
    else:
       print("valores informados não são de equação de segundo grau")

if __name__  =="__main__":
    main()