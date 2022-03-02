import logging

f = open('american-english')
dictionary = []
for line in f:
    dictionary += str("".join(line.lower())).split()

logging.basicConfig(filename='missing_words.log', level=logging.DEBUG)
f = open('misspell.txt')
txt = []

for line in f:
    txt += str("".join(line)).split()

for i in range(len(txt)):
    word = txt[i].strip("""'.?!,-";:'""").lower()

    if word not in dictionary:
        logging.debug('  Unidentified Word:  ' + word)
