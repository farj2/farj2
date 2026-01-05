#FUNCIONES
def calcular_imc(peso, altura):
    """ Calcula el Indice de Masa Corporal (IMC) dividiendo el peso por el cuadrado de la altura
    Args:
    peso: dado en kg
    altura: dado en mts"""
    return peso/(altura**2)

def clasificar_imc(imc):
    if imc<18.5:
        print("Bajo peso (estas flaco bro)")
    elif 18.5<=imc<24.9:
        print("Normal (buen cuerpo bro)")
    elif 25<=imc<29.9:
        print("Sobrepeso (ejercitate gordo)")
    else:
        print("Obesidad (hola tanque xdd)")


#LÓGICA PRINCIPAL
peso=float(input("Ingresa tu peso en kilogramos: "))
altura=float(input("Ingresa tu altura en metros: "))

imc=round(calcular_imc(peso,altura), 2)
clasificar_imc(imc)

print(f"Tu IMC es {imc}, por lo tanto estás {clasificar_imc}")

