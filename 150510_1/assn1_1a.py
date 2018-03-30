import re
    # """the re module."""

def main():
    # print("Lets start NLP with learning Regular Expressions")
    # p = re.compile('ab*')
    # print(p.search("aabb"))


    # print(p.match(" "))

    # dial=re.compile("\'[a-zA-Z\s,]+[.,!?]'")

    test = open('test.txt', 'r')
    # print(f.read())
    # print(re.start(re.match(r"^P(.)*N", "PrannN")))
    text = test.read()
    test.close()
    scom = re.compile('\'')
    alldcom = scom.sub('\"', text)
    myreg1 = re.compile('(([\w]+)(\")([\w]+))')
    myreg2 = re.compile("###")
    myreg3 = re.compile("((?<![.,?!;]))\"(.*(?<![!.,?;(\-\-)]))\"((?=[\s.?,!;]))")
    final = myreg1.sub(r'\2###\4', alldcom)
    final = myreg3.sub(r"\1'\2'\3", final)
    final = myreg2.sub(r"'", final)
    res = open("assn1_1a.txt", "w");
    res.write(final)
    res.close()
    # print alldcom
    # print(final)


main()
