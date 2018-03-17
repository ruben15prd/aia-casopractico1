# -*- coding: utf-8 -*-
titularesDeportes = []
titularesPolitica = []
titularesSociedad = []

# Saco los datos de los archivos txt y los almaceno en variables
[ [ [ titularesDeportes.append(line[:-1]) ] if line[-1]=='\n' else titularesDeportes.append(line) ] for line in open("deportes.txt", 'r') ]
[ [ [ titularesPolitica.append(line[:-1]) ] if line[-1]=='\n' else titularesPolitica.append(line) ] for line in open("politica.txt", 'r') ]
[ [ [ titularesSociedad.append(line[:-1]) ] if line[-1]=='\n' else titularesSociedad.append(line) ] for line in open("sociedad.txt", 'r') ]

titularesDeportes = titularesDeportes[0].split(". ")
titularesPolitica = titularesPolitica[0].split(". ")
titularesSociedad = titularesSociedad[0].split(". ")
print("\n\n", len(titularesSociedad))
print("\n\n", titularesSociedad[3])
