import hashlib

wordlist = open('DanielMiessler-Top10000.txt', 'r')

outfile = open('outFile.txt', 'w')
i = 0

for line in wordlist:
    fulltext = line.strip('\n')
    hashed = hashlib.sha256()
    hashed.update(fulltext.encode())
    hashed = hashed.hexdigest()
    outfile.write("Test" + str(i) + ":" + hashed + ":" + str(i) + "\n")
    print(i)
    i = i + 1