f = open('mary.txt')
count_list = {}
txt = []

for line in f:
    txt += str("".join(line)).split()

for i in range(len(txt)):
    word = txt[i].strip('.?!,;:"').lower()

    if word not in count_list:
        count_list[word] = 1

    elif word in count_list:
        count_list[word] += 1

print count_list