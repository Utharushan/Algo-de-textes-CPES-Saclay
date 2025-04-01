def occurence(m, t, i):
	for j in range(len(m)):
		if m[j] != t[i+j]:
			return False
	return True

def recherche(m, t):
	pos = []
	for i in range(len(t) - len(m)):
		if occurence(m, t, i):
			print(f"occurence à la position {i}")
			pos.append(i)
	return pos

recherche("chercher", "chercher, rechercher et chercher encore")

def tab_bm(m):
	tab_list = [{} for i in range(len(m))]
	for i in range(len(m)):
		for j in range(i):
			tab_list[i][m[j]] = j
	return tab_list

def decalage(d, j, c):
	if c in d[j]:
		return j - d[j][c]
	else:
		return j + 1

def recherche_bm(m, t):
	d = tab_bm(m)
	n = len(t)
	len_m = len(m)
	i = 0
	while i <= n - len_m:
		j = len_m - 1
		while j >= 0 and m[j] == t[i + j]:
			j -= 1
		if j < 0:
			print(f"occurence à la position {i}")
			i += len_m
		else:
			i += decalage(d, j, t[i + j])

recherche_bm("chercher", "chercher, rechercher et chercher encore")

print(tab_bm("chercher"))
print(decalage(tab_bm("banane"), 3, "n"))
