# Ejercicio 872: Obtener las palabras que se hallan separadas por mĂșltiples delimitadores.

import re

texto = 'JavaScript;Python\nC++|Java,PHP;C*Perl'

patron = ';|\n|\||,|\*'

lenguajes = re.split(patron, texto)

print(lenguajes)
