# from urllib2 import urlopen
# url = "http://composingprograms.com/shakespeare.txt"
# data = urlopen(url).read().lower()
import sys
write = sys.stdout.write
with open("shakespeare.txt") as f:
  data = f.read().lower()
words = data.split()
words = [ word for word in words ]
set_of_words = set(words)

T = 3
d = {}

for i in range(2, len(words)-1):
  for t in range(T):
    gram = t*(None,) + tuple(words[i-T+t+1:i+1])
    if not gram in d:
      d[gram] = {}
    if not words[i+1] in d[gram]:
      d[gram][words[i+1]] = 0
    d[gram][words[i+1]] += 1

d = { t: max(d[t].keys(), key = lambda k : d[t][k]) for t in d.keys() }
while True:
  word = raw_input("Give a starting word for the sentence: ")
  if not word in set_of_words:
    print "Word not in shakespeare.txt. Try another"
    continue
  gram = (T-2)*(None,) + (".", word)
  i = 0
  while i < 40:
    if word in ['.', ',', '?', ';', ':', '!']:
      write(word)
    else:
      write(" " + word)
    j = 0
    while not gram in d:
      gram = list(gram)
      gram[j] = None
      gram = tuple(gram)
      j += 1
    word = d[gram]
    gram = list(gram)
    for j in range(len(gram)-1):
      gram[j] = gram[j+1]
    gram[-1] = word
    gram = tuple(gram)
    if gram[-2]==".":
      break
    i += 1
  print ""
