def segundo_a_minutos(segundo):
    return segundo / 60

if __name__ =="__main__":
    segundo = 150
    minutos = segundo_a_minutos(segundo)
    print(f"{segundo} segundos equivalen a {minutos} minutos.")