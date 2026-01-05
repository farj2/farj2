def calcular_imc(peso, altura):
    """ Calcular el índice de masa corporal (IMC) dado el peso en kg y la altura en metros."""
    return peso/(altura**2)

def clasificar_imc(imc):
    """Clasifica el IMC en categorías estándar."""
    if imc<18.5:
        return "Bajo peso"
    elif 18.5<=imc<24.9:
        return "Normal"
    elif 25<=imc<29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"
    
peso=float(input("Ingrese su peso en kgs: (Ej.: 75)"))
altura=float(input("Ingrese su altura en metros: (Ej.: 1.75)"))

imc= calcular_imc(peso, altura)
categoria=clasificar_imc(imc)

print(f"Su IMC es: {imc:.2f}, lo que indica que usted tiene: {categoria}.")

