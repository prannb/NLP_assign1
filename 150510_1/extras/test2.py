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
    scom = re.compile('\'')
    alldcom = scom.sub('\"', text)
    myreg1 = re.compile('(([\w]+)(\")([\w]+))')
    myreg2 = re.compile('s\"')
    myreg3 = re.compile('#')
    final = myreg1.sub(r'\2#\4', alldcom)
    final = myreg3.sub('\'', final)
    final = myreg2.sub('s\'', final)
    
    # print alldcom
    print(final)


main()
