#------------------------------------------------------------------------------
# Algo LZW

def LZW(texte):
	dictionary = {chr(i) : i for i in range(8500)}
	code = 8500
	result = []
	current_string = texte[0]
	
	for char in texte[1:]:
		if current_string + char in dictionary:
			current_string += char
		else:
			result.append(dictionary[current_string])
			dictionary[current_string + char] = code
			code += 1
			current_string = char
	if current_string:
		result.append(dictionary[current_string])
	return result, dictionary

def decode_lzw(encoded_text):
	dictionary = {i: chr(i) for i in range(8500)}
	code = 8500
	decoded_string = ""
	current_string = chr(encoded_text[0])
	decoded_string += current_string

	for code_point in encoded_text[1:]:
		if code_point in dictionary:
			entry = dictionary[code_point]
		elif code_point == code:
			entry = current_string + current_string[0]
		decoded_string += entry

		dictionary[code] = current_string + entry[0]
		code += 1
		current_string = entry

	return decoded_string

#------------------------------------------------------------------------------
# Algo de Huffman

from heapq import *

def arbre_huffman(occurrences):
	tas = []
	compteur = 0
	for lettre, occ in occurrences.items():
		heappush(tas, (occ, compteur, lettre))
		compteur += 1
	while len(tas) >= 2:
		occ1, c1, noeud1 = heappop(tas)
		occ2, c2, noeud2 = heappop(tas)
		heappush(tas, (occ1 + occ2, compteur, {0: noeud1, 1: noeud2}))
		compteur += 1
	return heappop(tas)[2]

def table_frequences(texte):
	table = {}
	for caractere in texte:
		table[caractere] = table.get(caractere, 0) + 1
	return table

def code_huffman_parcours(arbre, prefixe, code):
	if isinstance(arbre, str):
		code[arbre] = prefixe
	else:
		code_huffman_parcours(arbre[0], prefixe + '0', code)
		code_huffman_parcours(arbre[1], prefixe + '1', code)

def code_huffman(arbre):
	code = {}
	code_huffman_parcours(arbre, '', code)
	return code

def encodage(texte, code):
	texte_binaire = ''.join(code[c] for c in texte)
	return texte_binaire

def decodage(code, texte_binaire):
	code_inv = {v: k for k, v in code.items()}
	texte = ''
	tampon = ''
	for b in texte_binaire:
		tampon += b
		if tampon in code_inv:
			texte += code_inv[tampon]
			tampon = ''
	return texte

#------------------------------------------------------------------------------

print("Taux de compression avec Huffman\n")

with open('romeo_and_juliet.txt') as file_object:
	romeo_and_juliet = file_object.read()

a = code_huffman(arbre_huffman(table_frequences(romeo_and_juliet)))
b = encodage(romeo_and_juliet, a)

print(f"Taille du code : {len(b)}\n\
Taille du texte : {len(romeo_and_juliet)}\n\
Compression de 'Romeo and Juliet' : {(len(b) / (len(romeo_and_juliet) * 8)) * 100}\n")

with open('Le_Tour_du_monde_en_quatre-vingts_jours.txt') as file_object:
	tour_du_monde = file_object.read()

a = code_huffman(arbre_huffman(table_frequences(tour_du_monde)))
b = encodage(tour_du_monde, a)

print(f"Taille du code : {len(b)}\n\
Taille du texte : {len(tour_du_monde)}\n\
Compression de 'Le Tour du monde en quatre-vingts jours' : {(len(b) / (len(tour_du_monde) * 8)) * 100}\n")

#------------------------------------------------------------------------------

print("Taux de compression avec LZW\n")

with open('romeo_and_juliet.txt') as file_object:
	romeo_and_juliet = file_object.read()

print(f"Taille du code : {len(LZW(romeo_and_juliet)[0])}\n\
Taille du texte : {len(romeo_and_juliet)}\n\
Compression de 'Romeo and Juliet' : {(len(LZW(romeo_and_juliet)[0]) / len(romeo_and_juliet)) * 100}\n")

with open('Le_Tour_du_monde_en_quatre-vingts_jours.txt') as file_object:
	tour_du_monde = file_object.read()

print(f"Taille du code : {len(LZW(tour_du_monde)[0])}\n\
Taille du texte : {len(tour_du_monde)}\n\
Compression de 'Le Tour du monde en quatre-vingts jours' : {(len(LZW(tour_du_monde)[0]) / len(tour_du_monde)) * 100}")