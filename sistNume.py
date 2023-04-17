
def decimal2binario(num):
    
    div=num
    binario=""
    binario_reverse=""

    if (div % 2)==0:
        binario += "0"
    else:
        binario += "1"

    while num != 1:
        div = div//2
        if (div % 2) == 0:
            binario += "0"
        else:
            binario += "1"

        if div==1:
            #binario.reverse()
            binario_reverse=binario[::-1]
            break
        
    return binario_reverse


def binario2decimal(num):
    
    cadena_bin = str(num)
    posicion = len(cadena_bin) - 1
    total=0

    for i in cadena_bin:
        total += int(i) * 2**posicion
        posicion -= 1
    return total