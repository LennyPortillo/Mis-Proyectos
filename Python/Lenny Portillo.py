
#ejercicio 1
"""

print("Hello world")

""" 
#ejercicio 2
"""
x= "Hello World!"
print(x)

"""
#ejercicio 3

x=input("Ingrese Su Nombre:")
y=input("Ingrese Su Edad:")

print("Nombre:" + x)
print("Edad:" + y)


#ejercicio 4
"""
x=input("Ingrese Su Nombre De Usuario:")
y=int(input("Ingrese Un Numero Entero:"))
 
while y>0 :
    print(x)
    y-=4
print("Hasta aca llego") 
"""
#ejercicio 5
"""
x=input("Ingrese Su Nombre de Usuario:")
fun
for item in x:
    print(item,":",len(item)," Caracteres de longitud")
"""
#Forma mas corta
""" 
x=input("Ingrese Su Nombre de Usuario:")
print("Nombre:",":","Tiene", len(x),"Letras" )

"""
#Ejercicio 6
"""
x=((3+2)/2*5)**2
print(x)
"""
#Ejercicio 7 
"""
n=int(input("Ingrese el dividendo:"))
m=int(input("Ingrese el divisor:"))


print("El Dividendo es:", n)
print("El Divisor es:", m)

print("El Cociente es:", str((n) // (m))) 
print("El Resto es:", str((n) % (m)))
"""
#Ejercicio 8
"""
x=int(input("Cantidad a Invertir:"))
t=int(input("Interes Anual:"))
y=int(input("Numero De años:"))

def inversion(x,t,y):
    r=(x*((t/100 +1)**y))
    print("El monto final sera de:", r)

inversion(x,t,y)
"""
#comienzo de funciones
#Ejercicio 9
"""
payasos=int(input("Ingrese la Cantidad vendida de Payasos:"))
munecas=int(input("Ingrese la Cantidad vendida de Muñecas:"))
valorkilo=int(input("Ingrese el valor por Kilo(sin el signo $) del transportista:"))

pesop=112/1000
pesom=75/1000
def kilopayaso():
    pesouno=(payasos*pesop)*valorkilo
    return pesouno
def kilomuneca():
    pesodos=(munecas*pesom)*valorkilo
    return pesodos
def primero():
    despachouno=int(payasos*kilopayaso())
    return despachouno
def segundo():
    despachodos=int(munecas*kilomuneca())
    return despachodos
despachototal=int(primero()+segundo())
print("El peso de cada payaso es de",pesop,"El valor por kilo del transportista es",valorkilo,"El valor final del despacho va a ser de:",kilopayaso(),"por cada payaso")
print("El peso de cada muñeca es de",pesom,"El valor por kilo del transportista es",valorkilo,"El valor final del despacho va a ser de:",kilomuneca(),"por cada muñeca")
print("Valor total del envio juntando ambos sera de:",despachototal)
"""
#Ejercicio 10
"""
edad=int(input("Ingrese su edad:"))

def calculo ():
    if edad < 18:
        print("Usted es menor de edad")
    else:
      print("Usted es mayor de edad")

calculo() 
"""
#Ejercicio 11
"""
varuno=("contraseña")

vardos=input("Ingrese La contraseña:")

varlow=vardos.lower()

def contra():
    
    if varlow == varuno:
        print("La contraseña es correcta")
    else:
        print("La contraseña es incorrecta")

contra()
"""
#Ejercicio 12
"""
div=int(input("Ingrese un Numero Entero:"))
dsor=int(input("Ingrese Un Segundo Numero:"))
def cuenta():
    if dsor == 0:
        print("El divisor No puede ser cero")
    else:
        print(div/dsor)
cuenta()
"""
#Ejercicio 13
"""
num=int(input("Ingrese numero entero:"))

def numero():
    if num > 0:
        if num % 2==0:
            print("Es un numero par")
        else:
            print("El Numero es impar")
    else:
        print("Ingrese un numero entero")

numero()
"""
#Ejercicio 14
"""
def notastrabajo(trabajador,nota, base ):
    if nota== 'inaceptable':
        nota= 0.0
        res=0.0*base
        print("Trabajador:",trabajador,"nota:",nota,"Sin plus","Base:",base)
    elif nota == 'aceptable':
        nota=0.4
        res=0.4*base
        final=res+base
        print("Trabajador:",trabajador,"Nota:", nota,"Con Plus", "Base Con Plus:", int(final))   
    elif nota == 'meritorio':
        nota=0.6 
        res=nota*base
        final=res+base
        print("Trabajador:",trabajador,"Nota:", nota,"Con Plus", "Base Con Plus:", int(final))
    elif float(nota) == 0.0:
        res=0.0*base
        print("Trabajador:",trabajador,"nota:",nota,"Sin plus","Base:",base)
    elif float(nota) == 0.4:
        res=0.4*base
        final=res+base
        print("Trabajador:",trabajador,"Nota:", nota,"Con Plus", "Base Con Plus:", int(final)) 
    elif float(nota) >= 0.6:
        res=float(nota)*base
        final=res+base
        print("Trabajador:",trabajador,"Nota:", nota,"Con Plus", "Base Con Plus:", int(final))
    else:
        print("Ingrese Una nota valida")
notastrabajo(input("Ingrese el nombre del trabajador"),input("Ingrese la nota"), 100000)
"""
#Ejercicio 15
"""
edad=int(input("Ingrese Su edad:"))
if edad <4:
    print("Edad:",edad,"Entra Gratis")
elif edad <18: 
    print("Edad:",edad,"Paga 500")
else:
    print("Edad:",str(edad),"Paga 1000")
"""
#Ejercicio 16
"""
edad=int(input("Ingrese Su edad:"))
var=1
while edad>=var:
    print("Cumpliste:",var,"años")
    var += 1
"""
#Ejercicio 17 
"""
for i in range(1, 11):
    for h in range(1, 11):
        print(i*h)
    print("")
"""
#Ejercicio 18
"""
pal=input("Ingrese Una Palabra")
for x in range(len(pal)-1, -1, -1):
    print(pal[x])
"""
#Ejercicio 19
"""
frase=input("Ingrese Una frase:")
letra=input("Ingrese Una letra:")

print("La letra Introducida se repite:",frase.count(letra),"veces")
"""
#Ejercicio 20
"""
while True:
    es=input(":")
    if es == 'salir':
        break
print(es)
"""
#Ejercicio 21
"""
x=["matematica", "historia", "quimica", "lengua"]

for x in x:
    print("Yo estudio:", x)
"""
#Ejercicio 22
"""
listauno=[1,2,3]
listados=[-1,0,2]

print(sorted(listauno + listados))
"""
#Ejercicio 23
"""
tabla={'banana':80, 'manzana':100,'pera':50,'naranja': 70}
fruta=input("Ingrese Una fruta:")
kilos=int(input("Ingrese los kilos"))

if fruta == 'banana':
    x=tabla.setdefault('banana')
    y=kilos*x
    print("El valor de", kilos, "de banana es",y)
elif fruta == 'manzana':
    x=tabla.setdefault('manzana')
    y=kilos*x
    print("El valor de", kilos, "de manzana es",y)
elif fruta == 'pera':
    x=tabla.setdefault('pera')
    y=kilos*x
    print("El valor de", kilos, "de pera es",y)
elif fruta == 'naranja':
    x=tabla.setdefault('manzana')
    y=kilos*x
    print("El valor de", kilos, "de manzana es",y)
else:
    print("Lamentamos informar que la fruta no se encuentra en nuestro stock")
"""
#Ejercicio 24
"""
cursos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
creditos_totales = 0
for materia, creditos in cursos.items():
    print(materia, "tiene", creditos, "creditos")
    creditos_totales += creditos
print("Numero total de los creditos del curso: ", creditos_totales)
"""
#Ejercicio 25(usar get o remove)
"""
abecedario = {'a', 'b', 'c','d', 'e', 'f','g', 'h', 'i','j', 'k', 'l','m', 'n', 'o','p', 'q', 'r','s', 't', 'u','v', 'w', 'x','y','z'}

abecedario.remove('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')

print(abecedario)
"""
 
"""
def suma(a,b):
    sumatoria= a + b
    return sumatoria
 
print(suma(a=int(input("A")), b=int(input("B"))))
"""
"""
a=input("A:")

def calculo():
    global a
    a= 8-4
    print(a)

calculo()
"""
"""
num=int(input("ingrese:"))
fact=0
def factorial(num):
    global fact
    
    if num==1:
        return 1
    else:
        fact = num * factorial(num -1)
    return fact
    print(fact)

factorial(num)
print(fact)
"""
""" 
payasos=int(input("Ingrese la Cantidad vendida de Payasos:"))
munecas=int(input("Ingrese la Cantidad vendida de Muñecas:"))
valorkilo=int(input("Ingrese el valor por Kilo(sin el signo $) del transportista:"))

pesop=112/1000
pesom=75/1000

pesouno=int((payasos*pesop)*valorkilo)
    
pesodos=int((munecas*pesom)*valorkilo)
   
    
despachouno=int(payasos*pesouno)


despachodos=int(munecas*pesodos)
    
despachototal=int(despachouno+despachodos)
print("El peso de cada payaso es de",pesop,"El valor por kilo del transportista es",valorkilo,"El valor final del despacho va a ser de:",pesouno,"por cada payaso")
print("El peso de cada muñeca es de",pesom,"El valor por kilo del transportista es",valorkilo,"El valor final del despacho va a ser de:",pesodos,"por cada muñeca")
print("Valor total del envio juntando ambos sera de:",despachototal)
"""
"""   
import random     

x=['Lenny', 'Alan','jesus', 'laura',  'juan','pedro'  ]   
for sorteo in range(6):
    ganador= x[random.randint(0,4)]
    print('Sorteo', sorteo +1, ':', ganador)

"""
import random     
x=['lenny', 'marcelo']
print("Gano:", random.sample(x,1))
"""
