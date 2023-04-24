
def decimal2binario(num):
    
    div = num
    binario = ""
    binario_reverse=""

    if (div % 2)==0:
        binario += "0"
    else:
        binario += "1"

    while div != 1:
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

def decimal2hexadecimal(num):
    
    nums_hexa = "0123456789ABCDEF"
    mod = num % 16
    hexa = ""

    if num == 0:
        return "0"
    
    while num > 0:
        mod = num % 16
        hexa = nums_hexa[mod] + hexa
        num = num // 16
    return hexa

def decimal2octal(num):
    mod= num % 8
    octal = ""

    if num == 0:
        return "0"
    
    while num > 0:
        mod = num % 8
        octal = str(mod) + octal
        num = num // 8
    return octal

###########################################################################################################

def binario2decimal(num):
    
    cadena_bin = str(num)
    posicion = len(cadena_bin) - 1
    total=0

    for i in cadena_bin:
        total += int(i) * 2**posicion
        posicion -= 1
    return total

def binario2hexadecimal(num):
    decimal = binario2decimal(num)
    hexa = decimal2hexadecimal(decimal)
    return hexa

def binario2octal(num):
    decimal = binario2decimal(num)
    octal = decimal2octal(decimal)
    return octal

#############################################################################################################

def hexadecimal2decimal(num):

    nums_hexa = {"A" : 10,
                 "B" : 11,
                 "C" : 12,
                 "D" : 13,
                 "E" : 14,
                 "F" : 15}
    
    hexa = str(num)[::-1]
    decimal = 0
    posicion = 0

    for i in hexa:
        if i in nums_hexa:
            decimal += nums_hexa[i] * 16** posicion
        else:
            decimal += int(i) * 16 ** posicion
        posicion += 1

    return decimal

def hexadecimal2binario(num):

    decimal = hexadecimal2decimal(num)
    binario = decimal2binario(decimal)

    return binario

def hexadecimal2octal(num):

    decimal = hexadecimal2decimal(num)
    octal = decimal2octal(decimal)

    return octal

###########################################################################################################

def octal2decimal(num):
    cadena_oct = str(num)
    posicion = len(cadena_oct) - 1
    total=0

    for i in cadena_oct:
        total += int(i) * 8**posicion
        posicion -= 1
    return total

def octal2binario(num):
    
    decimal = octal2decimal(num)
    binario = decimal2binario(decimal)

    return binario

def octal2hexadecimal(num):

    decimal = octal2decimal(num)
    hexa = decimal2hexadecimal(decimal)

    return hexa
