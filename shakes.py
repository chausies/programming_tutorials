from urllib2 import urlopen
url = "http://composingprograms.com/shakespeare.txt"
data = urlopen(url).read()
text = data.split()
words = set(text)
