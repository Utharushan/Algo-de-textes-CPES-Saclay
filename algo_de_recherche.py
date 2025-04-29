# Recherche naïve

def occurence(m, t, i):
	for j in range(len(m)):
		if m[j] != t[i+j]:
			return False
	return True

def recherche_naive(m, t):
	pos = []
	for i in range(len(t) - len(m)):
		if occurence(m, t, i):
			print(f"occurence à la position {i}")
			pos.append(i)
	return pos

recherche_naive("chercher", "chercher, rechercher et chercher encore")

# Recherche Boyer-Moore 

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
	pos = []
	while i <= n - len_m:
		j = len_m - 1
		while j >= 0 and m[j] == t[i + j]:
			j -= 1
		if j < 0:
			print(f"occurence à la position {i}")
			pos.append(i)
			i += len_m
		else:
			i += decalage(d, j, t[i + j])
	return pos

recherche_bm("chercher", "chercher, rechercher et chercher encore")

# Recherche Rabin-Karp

def hash_chaine(s, base=256, mod=101):
	h = 0
	for char in s:
		h = (h * base + ord(char)) % mod
	return h

def recherche_rk(m, t, base=256, mod=101):
	len_m = len(m)
	len_t = len(t)
	hash_m = hash_chaine(m, base, mod)
	hash_t = hash_chaine(t[:len_m], base, mod)
	pos = []

	for i in range(len_t - len_m + 1):
		if hash_m == hash_t:
			if t[i:i+len_m] == m:
				print(f"occurence à la position {i}")
				pos.append(i)
		if i < len_t - len_m:
			hash_t = (hash_t * base - ord(t[i]) * (base ** len_m) + ord(t[i + len_m])) % mod
			hash_t = (hash_t + mod) % mod
	return pos

recherche_rk("chercher", "chercher, rechercher et chercher encore")
