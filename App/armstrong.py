def ArmStrong(num:int):
    # Convertimos en cadena esto lo que permite trabajarse por parte
    if not isinstance(num,int):
        return "Solo se aceptan Numeros"
    
    if num == 0:
        return "Numero diferente de Cero"
    
    if num < 0:
        return "Numero positivo necesario"

    convert = str(num)
    #Se declara el array donde se almacenaran los datos
    digits = []

    try:
        for numero in convert:
            #usamos int para la conversion a numero
            digits.append(int(numero))
    except Exception as e:
        return "Solo se Reciben numeros",e
    # Declaracion de la variable donde se guarda el resultado del operacion
    a = 0
    # Verificamos los numeros de forma individual
    for i in digits:
        a += i**len(digits)
    #verificamos el resultado
    if a == num:
        return "Has conseguido un numero de ArmStrong, narcisita."
    else:
        return "Solo conseguiste un numero mas."

