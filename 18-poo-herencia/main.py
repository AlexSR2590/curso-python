import clases

persona = clases.Persona()

#nombre = input("Escribe tu nombre: ")
#apellidos = input("Escribe tus apellidos: ")
#altura = input("Escribe tu altura: ")
#edad = int(input("Escribe tu edad: "))

persona.setNombre("Luis")
persona.setApellidos("Ortega")
persona.setAltura("1.75 metros")
persona.setEdad("28 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(f"La persona {persona.getNombre()}: {persona.hablar()} ")
print("-----------------------")
informatico = clases.Informatico()

informatico.setNombre("Carlos")
informatico.setApellidos("Albisar")

print(f"El informático es: {informatico.getNombre()} {informatico.getApellidos()} ")
print("-----------------------")

informatica = clases.Informatico()
informatica.setNombre("Anaid")
informatica.setApellidos("Delgado")
print(f"La informática es: {informatica.getNombre()} {informatica.getApellidos()}")
print(f"Los lenguajes que se: {informatica.getLenguajes()}")
print(f"Experiencia: {informatica.experiencia}")
print("-----------------------")

tecnico = clases.TecnicoRedes()
print(tecnico.auditarRedes)
tecnico.setNombre("Alejandro")
tecnico.setEdad("27 años")
print(tecnico.getNombre(), tecnico.lenguajes)
print(f"Edad: {tecnico.getEdad()}")