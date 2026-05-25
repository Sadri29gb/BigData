# Ejercicio 1: Clasificación de edad

# Enunciado:
# Determinar si una persona es niño, adolescente, adulto o adulto mayor según su edad.

# Código:

def clasificar_edad(edad):
    if edad < 13:
        return "Niño"
    elif edad <= 17:
        return "Adolescente"
    elif edad <= 59:
        return "Adulto"
    else:
        return "Adulto mayor"

edad = 21
categoria = clasificar_edad(edad)

print(f"Edad: {edad} años")
print(f"Categoría: {categoria}")

# Resultado:
# Edad: 21 años
# Categoría: Adulto

# Explicación breve:
# Se utiliza una función con condiciones if, elif y else
# para clasificar la edad según el rango correspondiente.




# Ejercicio 2: Conversor de temperatura

# Enunciado:
# Convertir una temperatura de grados Celsius a Fahrenheit.

# Código:

def convertir_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = 30
fahrenheit = convertir_temperatura(celsius)

print(f"Temperatura en Celsius: {celsius}°C")
print(f"Temperatura en Fahrenheit: {fahrenheit}°F")

# Resultado:
# Temperatura en Celsius: 30°C
# Temperatura en Fahrenheit: 86.0°F

# Explicación breve:
# Se aplica la fórmula de conversión de Celsius a Fahrenheit
# utilizando una función para retornar el resultado.


# Ejercicio 3: Calculadora básica

# Enunciado:
# Realizar operaciones matemáticas básicas y validar división entre cero.

# Código:

def calculadora(num1, num2, operacion):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: No se puede dividir entre cero"
    else:
        return "Operación no válida"

num1 = 10
num2 = 5
operacion = "division"

resultado = calculadora(num1, num2, operacion)

print(f"Resultado: {resultado}")

# Resultado:
# Resultado: 2.0

# Explicación breve:
# El programa utiliza condiciones para identificar la operación
# matemática seleccionada y validar que no exista división entre cero.


# Ejercicio 4
# Enunciado: Determinar que un número es par o impar.
# Lógica: se usa el operador (%) para recibir el residuo de la división entre 2, si el resultado es 0 es par, si no es impar.
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "El número es par."
    else:
        return "El número es impar."
    
#cargar datos para el usuario
numero = 21
print(f"el numero ingresado es: {numero}")
print(es_par_o_impar(numero))

#Ejercicio 5
#Enunciado: tabla de multiplicar del 12.
#Lógica: se define una funcion que recibe un número, este numero llega a un for que va desde el 1 hasta el 12 para multiplicar el numero dado por cada iteración del for, luego se imprime el resultado de cada multiplicación.
def tabla_de_multiplicar(numero):
    resultado = 0
    for i in range(1,13):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

#cargar datos para el usuario

numero = 12
print(f"Tabla de multiplicar del {numero}:")
tabla_de_multiplicar(numero)

#Ejercicio 6 (Hecho por Brayan Martínez)
#enunciado: Contador de vocales en una frase.
#Lógica: se define una función que recibe una frase, luego se inicializa un contador en 0, se recorre cada letra de la frase y se verifica si es una vocal (a, e, i, o, u) y si lo es se incrementa el contador. Al final se devuelve el total de vocales encontradas.

def contador_de_vocales(frase):
    contador = 0
    vocales = ['a', 'e', 'i', 'o', 'u']
    for letra in frase:
        if letra.lower() in vocales:
            contador += 1
            
    return contador
        
#cargar datos para el usuario

frase = "Hola mundo"
print(f"La frase ingresada es: '{frase}'")
total_vocales = contador_de_vocales(frase)
print(f"El total de vocales en la frase es: {total_vocales}")

#Ejercicio 7: Promedio de calificaciones 
#• Defina o solicite 5 calificaciones. 
#• Calcule la suma total. 
#• Calcule el promedio. 
#• Indique si el estudiante aprobó o reprobó. 
#• Considere aprobado si el promedio es mayor o igual a 70. 

Notas = [88,89.5,78,65.8,70]
SumaTotal = sum(Notas)

promedio = sum(Notas)/len(Notas)

estado= "Aprobado" if promedio >= 70 else "Reprobado"

print(f"\n Resultados:")
print(f"Suma total: {SumaTotal:.2f}")
print(f"Promedio: {promedio:.2f}")
print(f"Estado: {estado}")

#Ejercicio 8: Lista de números positivos y negativos 
#• Defina o solicite 10 números. 
#• Cuente cuántos son positivos, negativos y ceros. 
#• Muestre un resumen final.

Numeros = [0.23, -8, 6, 4, 45, -9, 0, 56, -1]
positivos = negativos = ceros = 0 

for i in range(len(Numeros)):
    if Numeros[i] > 0:
        positivos += 1
    elif Numeros[i] < 0:
        negativos += 1
    else:
        ceros += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Ceros:     {ceros}")


#Ejercicio 9: Mayor y menor de una lista 
#• Cree una lista con varios números enteros. 
#• Encuentre el número mayor. 
#• Encuentre el número menor. 
#• Calcule la diferencia entre ambos. 
#• Explique el uso de max() y min(). 

numeros = [15, -3, 42, 8, 0, 27, -10, 56, 12, 3]

mayor = max(numeros)
menor = min(numeros)
diferencia = mayor - menor

print(f"Lista: {numeros}")
print(f"Mayor:    {mayor}")
print(f"Menor:    {menor}")
print(f"Diferencia: {diferencia}")


#Ejercicio #10 : Diccionario de Estudiantes
#Enunciado: Crear un diccionario con los datos de un estudiante y mostrar la informacion de forma ordenada
#Logica: Acceder a los valores usando las claves del diccionario.

# Diccionario del estudiante

estudiante = {
    "nombre": "Danny Lopez",
    "edad": 20,
    "carrera": "Ingenieria en Sistemas",
    "promedio": 90,
    "estado": "Aprobado"
}



print("DATOS DEL ESTUDIANTE")
print("Nombre:", estudiante["nombre"])
print("Edad:", estudiante["edad"])
print("Carrera:", estudiante["carrera"])
print("Promedio:", estudiante["promedio"])
print("Estado:", estudiante["estado"])

#Explicacion:
print("\nLos valores se acceden usando la clave entre corchetes.")
print('Ejemplo: estudiante["nombre"]')

#Resultado:
#DATOS DEL ESTUDIANTE
#Nombre: Danny Lopez
#Edad: 20
#Carrera: Ingenieria en Sistemas
#Promedio: 90
#Estado: Aprobado

#Los valores se acceden usando la clave entre corchetes.
#Ejemplo: estudiante["nombre"]


#Ejercicio #11: Funcion para calcular descuento
#nunciado: Crear una funcion que calcule el precio
#Logica: Calcular el descuento y mostrar el precio final.

# Función para calcular descuento

def calcular_descuento(precio, descuento):
    precio_final = precio - (precio * descuento / 100)
    return precio_final


precio_original = 1000
porcentaje = 20


resultado = calcular_descuento(precio_original, porcentaje)


print("Precio original:", precio_original)
print("Descuento:", porcentaje, "%")
print("Precio final:", resultado)

# Explicación
print("\nLa función recibe el precio original y el porcentaje de descuento.")
print("La función retorna el precio final con el descuento aplicado.")

#Resultado:
#Precio original: 1000
#Descuento: 20 %
#Precio final: 800.0

#La función recibe el precio original y el porcentaje de descuento.
#La función retorna el precio final con el descuento aplicado.


#Ejercicio #12: Validación de contraseña.
#Enunciado: Crear un programa que valide si una contraseña cumple con los requisitos de seguridad.
#LOgica: El programa revisa si la contraseña cumple los requisitos de seguridad y muestra si es válida o no.


# Contraseña definida

contraseña = "Kere2025"



tiene_numero = any(caracter.isdigit() for caracter in contraseña)
tiene_mayuscula = any(caracter.isupper() for caracter in contraseña)
tiene_minuscula = any(caracter.islower() for caracter in contraseña)
longitud = len(contraseña) >= 8

# Resultado

if tiene_numero and tiene_mayuscula and tiene_minuscula and longitud:
    print("La contraseña es válida")
else:
    print("La contraseña no es válida")

#Resultado: "La contraseña es válida"



#Ejercicio 13: Sistema simple de inventario
#• Cree una lista de productos.
#• Cada producto debe tener código, nombre, precio y cantidad disponible.
#• Muestre todos los productos.
#• Busque un producto por código.
#• Calcule el valor total del inventario.
    
inventario = [
    {"codigo": "001", "nombre": "bolsa de pan", "precio": 30.0, "cantidad": 10},
    {"codigo": "002", "nombre": "Caja de leche", "precio": 35.0, "cantidad": 5},
    {"codigo": "003", "nombre": "Carton de huevos", "precio": 110.0, "cantidad": 3}
]

print("--- LISTA DE PRODUCTOS ---")
for prod in inventario:
    print(f"Código: {prod['codigo']} | Nombre: {prod['nombre']} | Precio: L{prod['precio']} | Stock: {prod['cantidad']}")

print("-" * 30)

codigo_a_buscar = "002"
encontrado = False

print(f"\n--- BUSCANDO EL CÓDIGO: {codigo_a_buscar} ---")
for prod in inventario:
    if prod["codigo"] == codigo_a_buscar:
        print(f"¡Encontrado! Producto: {prod['nombre']}, Precio: L{prod['precio']}, Stock: {prod['cantidad']}")
        encontrado = True
        break 

if not encontrado:
    print("Producto no encontrado.")

print("-" * 30)

valor_total = 0.0

for prod in inventario:
      valor_total += prod["precio"] * prod["cantidad"]

print(f"\n--- VALOR TOTAL DEL INVENTARIO ---")
print(f"El valor total acumulado es: L{valor_total}")


#Ejercicio 14: Registro de ventas
#• Cree una lista de ventas.
#• Cada venta debe tener cliente, producto, cantidad y precio unitario.
#• Calcule el total por venta.
#• Calcule el total general vendido.
#• Identifique el cliente con la compra más alta.


ventas = [
    {"cliente": "Ana", "producto": "Teclado", "cantidad": 2, "precio_unitario": 15.0},
    {"cliente": "Carlos", "producto": "Monitor", "cantidad": 1, "precio_unitario": 120.0},
    {"cliente": "Juan", "producto": "Mouse", "cantidad": 3, "precio_unitario": 10.0}
]

total_general = 0.0
cliente_mas_alto = ""
compra_mas_alta = 0.0

print("--- DETALLE DE VENTAS ---")

for v in ventas:

    total_venta = v["cantidad"] * v["precio_unitario"]
    print(f"Cliente: {v['cliente']} | Producto: {v['producto']} | Total Venta: L{total_venta}")
    

    total_general += total_venta
    

    if total_venta > compra_mas_alta:
        compra_mas_alta = total_venta
        cliente_mas_alto = v["cliente"]

print("-" * 40)


print(f"Total general vendido en el negocio: L{total_general}")
print(f"El cliente con la compra más alta fue {cliente_mas_alto} (Gastó: L{compra_mas_alta})")



#Ejercicio 15: Limpieza básica de texto
#• Defina o solicite una frase.
#• Elimine espacios al inicio y al final.
#• Convierta el texto a minúsculas.
#• Reemplace espacios dobles por un solo espacio.
#• Cuente cuántas palabras contiene.
#• Explique los métodos strip(), lower(), replace() y split().


frase_mal = "   Hola  Mundo   Clase  Big Data    "

print(f"Frase Original: '{frase_mal}'")

frase_bien = frase_mal.strip()

frase_bien = frase_bien.lower()

frase_bien = frase_bien.replace("  ", " ")
frase_bien = frase_bien.replace("  ", " ")

print(f"Frase Corregida:   '{frase_bien}'")

lista_palabras = frase_bien.split()

total_palabras = len(lista_palabras)

print(f"La frase contiene {total_palabras} palabras.")

