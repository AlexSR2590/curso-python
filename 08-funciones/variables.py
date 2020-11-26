"""
Variables locales y globales
"""
frase = "Esto es una variable global"

print(frase)

def holaMundo():
	frase = "Esto es una variable local"
	return frase

print(holaMundo())