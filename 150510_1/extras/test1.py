import re
    # """the re module."""

def main():
    print("Lets start NLP with learning Regular Expressions")
    # p = re.compile('ab*')
    # print(p.search("aabb"))


    # print(p.match(" "))

    # dial=re.compile("\'[a-zA-Z\s,]+[.,!?]'")

    test = open('test.txt', 'r')
    # print(f.read())
    # print(re.start(re.match(r"^P(.)*N", "PrannN")))
    text = test.read()
    # print(text)
    # dial = re.compile('(\n\'[\w ,.!?]+\')|(\.[ ]\'[\w ,.!?]+\')')
    # dial1 = re.compile('([\n]+\'[\w ,.!?\n]+\'[., \n*])|(,[ ]\'[\w ,.!?\n]+\'[., \n*])|(\.[ ]\'[\w ,.!?\n]+\'[., \n*])')
    dial1 = re.compile('(\n+\'(([\w ,.;\-!?\n])|([\w]*\'[\w]+)|([\w]+\'[\w]*))+\'([., ]|\n+))')
    dial2 = re.compile('((,|;)[ ]\'(([\w ,.;\-!?\n])|([\w]+\'[\w]+)|([\w]+\'[\w]*))+\'(\.|,| |\n+))')
    dial3 = re.compile('(\.[ ]\'(([\w ,.;\-!?\n])|([\w]+\'[\w]+)|([\w]+\'[\w]*))+\'([., ]|\n+))')
    dial4 = re.compile("\s(')(?!\s)(.*)(')(?=\s)")  
    lines1 = dial1.finditer(text)
    lines2 = dial2.finditer(text)
    lines3 = dial3.finditer(text)
    # while dial1
    i = 0
    for match in lines1:
        print(match.group())
        i = i+1
        print(i)

    print("######################################################################")
    for match in lines2:
        print(match.group())
        i = i+1
        print(i)

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    for match in lines3:
        print(match.group())
        i = i+1
        print(i)

        # print(lines1[i])
    # i=0
    # for i in range(200):
    #     print(i)
    #     print(lines3[i])
        
    # for line in f:
#     print(line)
#     rq=raw_input()


main()
