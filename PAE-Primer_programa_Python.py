#PROPÓSITO DEL PROGRAMA
"""
Las presentes líneas de código permiten la creación de un programa interactivo dividido en 3 secciones.
1ra Sección: Permiten el cálculo de operaciones básicas, tales como la suma,resta, multiplicación y
división de de distintos números, ya sean enteros (int) o decimales (float).
2da Sección: Permite medir la longitud de un texto ingresado y guardar ese dato como una variable dentro del programa
para un futuro uso.
3ra Sección: Permite la conversión de datos ingresados de int a float, y viceversa, dejando de esta manera la libertad
de realizar operaciones con los resultados.

Lo más destacable del programa es que permite la interacción del usuario con el programa, permitiendo que él decida los
datos a ingresar, siendo estos los fundamentos básicos de un programa profesional
"""

#1. OPERACIONES BÁSICAS Y TIPOS DE DATOS
#Esta sección del programa permitirá al usuario realizar operaciones matemáticas básicas con diferentes tipo de de números

print("OPERACIONES BÁSICAS")

#Las siguientes lineas indican que operación se procederá a hacer, además, permite el ingreso de datos por parte del usuario
print("Función Suma")
a = int(input("El primer número (entero) es: ",))
b = int(input("El primer número (entero) es: ",))
sum = a+b #En la presente linea se encuentra el comando de la suma
print("La suma de los números es:",sum)

#El proceso se repite, tan solo que el input cambia a float, permitiendo el ingreso de números decimales
print("Función Resta")
a = float(input("El primer número (decimal) es: ",))
b = float(input("El primer número (decimal) es: ",))
rest = a-b #De igual manera, la linea indica que se realizará una resta
print("La resta de los números es:",rest)

#Las líneas de código se repiten solo cambia la operación que se realiza
print("Función Multiplicación")
a = int(input("El primer número (entero) es: ",))
b = int(input("El primer número (entero) es: ",))
mult = a*b #Operación multiplicación
print("La multiplicación de los números es:",mult)

print("Función Multiplicación")
a = float(input("El primer número (decimal) es: ",))
b = float(input("El primer número (decimal) es: ",))
div = a/b #Operación división
print("La división de los números es:",div)

print() #Este print vacio se encuentrará cada que se termine una sección del programa para permitir una visualización más estética

#######################################################################################################################

#2. MANIPULACIÓN DE CADENAS DE TEXTO
#Esta sección se especializa en brindar la posibiliadad de ingresar un texto y que el programa mida la longitud del mismo

print("MEDIR LONGITUD DE TEXTO")

#Se permite al usuario ingresar el texto que el requiera medir, en este caso el nombre
name = str(input("Su nombre es: ",))
n_ch = len(name) #En esta línea se procede a contar la longitud del texto
print("El número de caracteres (contando espacios) de su nombre,",name,",es:",n_ch)

print()

#######################################################################################################################

#3. CONVERSIÓN DE TIPOS DATOS
#En esta última sección,se permite el ingreso de números y la conversión de los mismos.

print("CONVERSIÓN DE TIPOS DATOS")

#Se permite que el usuario ingrese dos números, el primero entero y el segundo decimal
d = int(input("Escriba un número entero: ",))
e = float(input("Escriba un número decimal: "))

#Estos números son cambiados de entero a decimal y viceversa
f = float(d)
i = int(e)

print("Su número entero,",d,", transformado a decimal es:",f)
print("Su número decimal,",e,", transformado a decimal es:",i)