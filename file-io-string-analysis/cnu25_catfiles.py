from sys import argv

if len(argv) < 3:
    exit("error -- must supply at least one input file and an output file")

txt = []

for param in argv[1:-1]:
    f = open(param)
    for line in f:
        txt += str("".join(line)).split()

txtstr = " ".join(txt)

with open(argv[-1], "w") as out_file:
    out_file.write(txtstr)