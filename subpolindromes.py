'''https://ru.m.wikibooks.org/wiki/%D0%9A%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE_%D0%BF%D0%BE%D0%B4%D0%BF%D0%B0%D0%BB%D0%B8%D0%BD%D0%B4%D1%80%D0%BE%D0%BC%D0%BE%D0%B2'''
s = input()

def max_polindromes(s):
  i = 0
  R = 0
  L = -1
  len_polindromes = [1] + [0]*(len(s)-1)
  for i in range (1, len(s)):
    if i > R:
      k = 0
    else:
      k = min(len_polidromes[L+R-i], R-i)
    while i + k < len(s) and i - k > 0 and s[i-k] == s[i+k]:
      k += 1
    len_polindromes[i] = 2*k + 1
    if i + k > R:
      
