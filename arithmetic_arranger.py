def arithmetic_arranger(lista,*args):
    longitud = list()
    numerador = list()
    denominador = list()
    separador = list ()
    string = str()
    resultado_suma= list()

    imp_resul = args

    if len (lista) > 5:
            return "Error: Too many problems."
    for i in range(len(lista)):
        elemento = lista[i].split()
        if (elemento[1] != '+') and (elemento[1] != '-'):
            return "Error: Operator must be '+' or '-'."
        if (len (elemento [0]) > 4) or (len(elemento [2]) > 4):
            return "Error: Numbers cannot be more than four digits."
        try:
            elemento[0] = int(elemento [0])
            elemento[2] = int(elemento [2])
        except:
            return "Error: Numbers must only contain digits."

    for i in range(len(lista)):
        elemento = lista[i].split()
        primer_digito = int(elemento [0])
        segundo_digito = int(elemento [2])
        if primer_digito > segundo_digito:
            longitud.append(len(str(primer_digito))+2)
        else:
            longitud.append(len(str(segundo_digito))+2)

    for i in range(len(lista)):
        elemento = lista[i].split()
        primer_digito = int(elemento [0])
        segundo_digito = int(elemento [2])
        operador = elemento [1]
        if operador == "+":
            suma = primer_digito + segundo_digito
        else:
            suma = primer_digito - segundo_digito
        resultado_suma.append(str(suma))


    for i in range (len(lista)):
        elemento = lista[i].split()
        primer_digito = elemento[0]
        numerador.append(primer_digito.rjust(longitud[i]))
        segundo_digito = elemento[2]
        simbolo = elemento[1]
        denominador.append (simbolo +" " + segundo_digito.rjust(longitud[i]-2))
        separador.append( "-" * (longitud[i]))
        resultado_suma[i] = resultado_suma[i].rjust(longitud[i])
    for i in range (len(lista)):
        string = string + numerador[i]
        if i < (len(lista)-1):
            string = string + "    "
    string = string + '\n'
    for i in range (len(lista)):
        string = string + denominador[i]
        if i < (len(lista)-1):
            string = string + "    "
    string = string + '\n'
    for i in range (len(lista)):
        string = string + separador[i]
        if i < (len(lista)-1):
            string = string + "    "


    if imp_resul:
        string = string + '\n'
        for i in range (len(lista)):
            string = string + resultado_suma[i]
            if i < (len(lista)-1):
                string = string + "    "

    return string
