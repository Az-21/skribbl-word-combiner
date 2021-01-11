import glob, os

customWords = []

os.chdir("C:\\Github\\skribbl")
for file in glob.glob("*.txt"):
    with open(file, 'r') as f:
        f_contents = f.read()
        customWordTemp = f_contents.split(',')
        customWords.extend(customWordTemp)


#print(customWords)

strCustomWords = ', '.join(map(str, customWords))
with open('output.txt', 'w') as f:
    f.write(strCustomWords)