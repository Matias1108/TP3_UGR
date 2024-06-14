from abc import ABC, abstractmethod

# Clase abstracta Persona que define la estructura básica para todas las personas
class Persona(ABC):
    def __init__(self, nombre, apellido, edad, dni, ocupacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.ocupacion = ocupacion
        
        
    @abstractmethod
    def mostrar_informacion(self):
        pass
    
    #generador de ID basado en los atrib
    
    def generador_ids(self):
         return f"{self.apellido[:2]}{self.nombre[-2:]}{self.ocupacion}"
    
    #en este  metodo mientras que cuando llame a la funcion no defina nuevamente un atributo los mismos se mantendran sin modificaciones.
    def actualizar_info(self, nombre= None, apellido=None, edad=None, dni=None, ocupacion=None):
        if nombre is not None:
            self.nombre = nombre
        if apellido is not None:
            self.apellido = apellido
        if edad is not None:
            self.edad = edad
        if dni is not None:
            self.dni = dni
        if ocupacion is not None:
            self.ocupacion = ocupacion
    
    #creo la class Estudiante que hereda de Persona y que como propio atributo usa self.__matricula
# y esta como privado el cual puedo manejar externamente mediante getters y setters  
class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, dni, ocupacion, matricula):
        super().__init__(nombre, apellido, edad, dni, ocupacion)
        self.__matricula = matricula
    
    
    def mostrar_informacion(self):
        return f"Me llamo {self.nombre}{self.apellido}, de {self.edad} años, mi dni es {self.dni} soy {self.ocupacion},  y mi matricula es {self.__matricula}"
    
    def estudiando_parciales(self):
        return f"{self.nombre} se esta preparando para los parciales"
    
    # Getter para el atributo matricula  
    @property  
    def matricula(self):
        return self.__matricula
     # Setter para el atributo matricula  
    @matricula.setter
    def matricula(self, valor):
        self.__matricula = valor
        
#creo la class Docente que hereda de Persona y que como propio atributo usa self.__asignatura
# y esta como privado el cual puedo manejar externamente mediante getters y setters       
    
class Docente(Persona):
    def __init__(self, nombre, apellido, edad, dni,  ocupacion,  asignatura):
        super().__init__(nombre, apellido, edad, dni,  ocupacion)
        self.__asignatura = asignatura        
    
    def mostrar_informacion(self):
        return f"Me llamo {self.nombre}{self.apellido}, de {self.edad} años, trabajo de {self.ocupacion} ,  mi dni es {self.dni} y la asignatura que enseño es {self.__asignatura}"
    
    def preparando_parciales(self):
        return f"{self.nombre} {self.apellido} esta preparando los parciales para los alumnos de su cursada en {self.asignatura}" 
       
    # Getter para el atributo asignatura
    @property  
    def asignatura(self):
        return self.__asignatura
    # Setter para el atributo asignatura 
    @asignatura.setter
    def asignatura(self, valor):
        self.__asignatura = valor

#creo la class Administrativo que hereda de Persona y que como propio atributo usa self.__legajo
# y esta como privado, el cual puedo manejar externamente mediante getters y setters            
class Administrativo(Persona):
    def __init__(self, nombre, apellido, edad, dni,  ocupacion, legajo):
        super().__init__(nombre,apellido, edad, dni,  ocupacion)    
        self.__legajo = legajo    
    
    
    def mostrar_informacion(self):
        return f"Me llamo {self.nombre}{self.apellido}, de {self.edad} años, trabajo como {self.ocupacion}, mi dni es {self.dni} y mi legajo es {self.__legajo}" 
    
    def enviando_cuotas(self):
        return f"{self.nombre} {self.apellido} esta preparando los comprobantes para el pago mensua lde la matricula" 
    
    # Getter para el atributo legajo
    @property  
    def legajo(self):
        return self.__legajo
    # Setter para el atributo legajo
    @legajo.setter
    def legajo(self, valor):
        self.__legajo = valor
        
# aca instancio las diferentes subclases
estudiante1 = Estudiante("Matias", " Espinosa", 34, 34555444, "estudiante ","MAT1108")
estudiante2 =Estudiante("John", " Fits", 28, 35654432, "estudiante ", "FITS123")
estudiante3 = Estudiante("Michael", " Jackson", 25, 43123456, "estudiante ", "MICKJSN2020")
profe1 = Docente("Mati", "Perez", 45 , 23456789, "profesor ", "Programacion 2")
profe2 = Docente("Peter", "Pan", 34,  355678908, "profesor ", "Programacion 1")
profe3 = Docente("Bruno", "Conti", 31,  32456789, "profesor ", "Programacion 2")
admin1 = Administrativo("Pepe","Pompin", 37,  25432111, "administrativo ", "FK1234")
admin2 = Administrativo("Jose Maria", " Listorti", 35, 45324785, "administrativo ","NSPN1234")
# Lista de personas para recorrer y mostrar información
personas = [estudiante1,estudiante2,estudiante3,profe1, profe2, profe3, admin1, admin2]

#coleccio nde personas, dodne se recorre a cada persona y accede al metodo mostrar_informacion
for persona in personas:
    print (persona.mostrar_informacion())
    
#2 funcion de filtrado  por edad

def filtrar_por_edad (personas, edad_minima):
    return [persona for persona in personas if persona.edad > edad_minima]

#por ocupacion
def filtrar_por_ocupacion (personas, ocupacion):
    return [persona for persona in personas if persona.ocupacion == ocupacion]

#por nombre y apellido
def filtro_por_nombre_apellido (personas, nombre_o_apellido):
    return [persona for persona in personas if nombre_o_apellido.lower() in persona.nombre.lower() or nombre_o_apellido.lower() in persona.apellido.lower()]

# Filtrar personas mayores de 30 años
mayores_de_30 = filtrar_por_edad(personas, 30)
print("Los mayores de 30 son: ")
for persona in mayores_de_30:
    print(persona.mostrar_informacion())
#filtrar solo profes.    
solo_profes = filtrar_por_ocupacion (personas, "profesor")
print("Los profesores encontrados: ")
for persona in solo_profes:
    print(persona.mostrar_informacion())    
#filtrar personas con apellido "Espinosa"    
con_apellido_espinosa = filtro_por_nombre_apellido(personas, " Espinosa")
print("Personas con apellido 'Espinosa' :")
for persona in con_apellido_espinosa:
    print(persona.mostrar_informacion())
    
#generacion de id unico para cada persona, haciendo el recorrido con un for in
for persona in personas:
    print(persona.generador_ids())

#aca llamo a la funcion actualizar_info y se modifican solo los valores que especifiqué para Matias Espinosa
print("\nActualizando información de 'Matias Espinosa'...\n")
estudiante1.actualizar_info(edad = 35, dni= 34883555 )

for persona in personas:
    print(persona.mostrar_informacion())
    
#metodos especificos para cada clase   
print (estudiante1.estudiando_parciales())

print (profe1.preparando_parciales())

print (admin1.enviando_cuotas())

#el ultimo paso de Crea una función que reciba una lista de objetos Persona y llame a los
#métodos de cada objeto sin conocer su tipo específico no lo hice porque no salió.

#de lo que si salio, va el resumen:

# 1. Encapsulacion: 
#  Atributos privados ('__matricula', '__asignatura', '__legajo') están encapsulados y accesibles solo a través de 'getters' y 'setters', sto protege los datos internos y permite un control específico sobre cómo se acceden y modifican.

# 2. Herencia:
# La clase abstracta 'Persona' sirve como base para 'Estudiante', 'Docente', y 'Administrativo', permitiendo compartir código común y ademas esas subclases heredan atributos y métodos de 'Persona' y pueden añadir o modificar su propio comportamiento.

# 3. Polimorfismo:
#  El método mostrar_informacion() es un ejemplo de polimorfismo porque c/subclase implementa este método de manera diferente según su contexto.

# 4. Abstraccion:
#   La clase Persona tiene abstraccion, definiendo solo la estructura y comportamiento común. Las subclases  implementan detalles específicos como la matrícula de un estudiante o la asignatura de un docente.

#COMPARACIÓN DE IMPLEMENTACIONES

#
# Atributos como nombre, apellido, edad, dni, y ocupacion son públicos y atributos específicos como matricula, asignatura, y legajo son privados, asegurando que se accedan y modifiquen solo a través de métodos controlados como getters y setters.


#  Los métodos  estudiando_parciales, preparando_parciales, y enviando_cuotas demuestran cómo cada clase puede tener comportamientos únicos.

