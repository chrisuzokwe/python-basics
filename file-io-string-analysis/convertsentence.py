slang2kings = {'gr8': 'great', 'btw': 'by the way', 'imho': 'in my humble opinion', 'jk': 'just kidding',
               'l8r': 'later', 'np': 'no problem', 'r': 'are', 'u': 'you', 'y': 'why', 'ttyl': 'talk to you later',
               'l8': 'late', 'atm': 'at the moment', 'lmk': 'let me know', 'tia': 'thanks in advance',
               'brb': 'be right back'}

message = raw_input('Enter message to translate:')
message = message.split()
newsen = []

for i in range(len(message)):
    word = message[i]
    char = []

    if word[-1] in ".?!,;:":
        char = word[-1]
        word = word.strip(".?!,;:")
        if word in slang2kings:
            newsen += (slang2kings[word]) + str(char) + " "
        else:
            newsen += word + str(char) + " "

    else:
        if word in slang2kings:
            newsen += (slang2kings[word]) + " "
        else:
            newsen += word + " "




print "".join(newsen)