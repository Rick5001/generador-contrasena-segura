import string
import secrets

def generar_contraseña(longitud=15, usar_mayus=True, usar_minus=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ''
    
    if usar_mayus:
        caracteres += string.ascii_uppercase
    if usar_minus:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Debes seleccionar al menos un tipo de carácter.")

    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña

# --- MAIN ---
if __name__ == "__main__":
    print(" Generador de Contraseñas Seguras")

    personalizar = input("¿Quieres personalizar las características de la contraseña? (s/n): ").lower()

    if personalizar == 's':
        try:
            longitud = int(input(" Longitud de la contraseña (mínimo 8, recomendado 12-16): "))
            usar_mayus = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
            usar_minus = input("¿Incluir minúsculas? (s/n): ").lower() == 's'
            usar_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
            usar_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'

            contraseña_segura = generar_contraseña(
                longitud,
                usar_mayus,
                usar_minus,
                usar_numeros,
                usar_simbolos
            )

            print(f"\n Contraseña generada: {contraseña_segura}")

        except ValueError as ve:
            print("❌ Error:", ve)
        except Exception as e:
            print("❌ Ocurrió un error:", e)

    else:
        contraseña_segura = generar_contraseña()
        print(f"\n Contraseña generada automáticamente: {contraseña_segura}")
