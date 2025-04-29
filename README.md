# Algorithmes de Traitement de Texte

Ce dépôt contient plusieurs algorithmes de traitement de texte, notamment pour la recherche de motifs et la compression de données.

## 📌 Contenu

### 1️⃣ **Recherche de Motifs**

- **Algorithme naïf** :
  - Recherche toutes les occurrences d'un motif dans un texte en comparant caractère par caractère.
  - Complexité en temps : O(n * m), où n est la taille du texte et m la taille du motif.
  - Implémentation :
  ```python
  def occurence(m, t, i):
      for j in range(len(m)):
          if m[j] != t[i+j]:
              return False
      return True
  
  def recherche(m, t):
      pos = []
      for i in range(len(t) - len(m)):
          if occurence(m, t, i):
              print(f"Occurrence à la position {i}")
              pos.append(i)
      return pos
  ```

- **Algorithme de Boyer-Moore** :
  - Utilise une technique de décalage basée sur le motif pour ignorer des comparaisons inutiles.
  - Améliore la recherche avec une table de mauvais caractères.
  - Complexité en temps : O(n/m) en moyenne, O(n * m) dans le pire cas.
  - Implémentation :
  ```python
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
              print(f"Occurrence à la position {i}")
              i += len_m
          else:
              i += decalage(d, j, t[i + j])
  ```

- **Algorithme de Rabin-Karp** :
  - Utilise une fonction de hachage pour comparer efficacement des sous-chaînes du texte avec le motif.
  - Complexité en temps : O(n) en moyenne, O(n * m) dans le pire cas (à cause des collisions).
  - Implémentation :
  ```python
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
                  print(f"Occurrence à la position {i}")
                  pos.append(i)
          if i < len_t - len_m:
              hash_t = (hash_t * base - ord(t[i]) * (base ** len_m) + ord(t[i + len_m])) % mod
              hash_t = (hash_t + mod) % mod
      return pos
  ```

📌 **Fichier concerné** : `algo_de_recherche.py`

### 2️⃣ **Compression de Données**

- **Codage de Huffman** :
  - Compression sans perte qui attribue des codes binaires plus courts aux caractères les plus fréquents.
  - Utilise un arbre binaire pour structurer les codes.
  - Complexité en temps : O(n log n) pour la construction de l'arbre, O(n) pour l'encodage.
  - Implémentation :
  ```python
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
  ```

- **Compression LZW** :
  - Basée sur la substitution de séquences de caractères récurrentes par des codes numériques.
  - Utilise un dictionnaire dynamique pour stocker les nouvelles séquences rencontrées.
  - Complexité en temps : O(n) dans le meilleur cas, O(n²) dans le pire cas.
  - Implémentation :
  ```python
  def LZW(texte):
      dictionary = {chr(i): i for i in range(8500)}
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
  ```

📌 **Fichier concerné** : `algo_de_compression.py`
