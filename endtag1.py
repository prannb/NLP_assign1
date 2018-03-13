import re


def main():
    # print("werty")
    test = open('test.txt', 'r')
    # print(f.read())
    # print(re.start(re.match(r"^P(.)*N", "PrannN")))
    text = test.read()
    # text = test.read()
    scom = re.compile('\'')
    alldcom = scom.sub('\"', text)
    myreg1 = re.compile('(([\w]+)(\")([\w]+))')
    myreg2 = re.compile('s\"')  
    myreg3 = re.compile('#')
    final = myreg1.sub(r'\2#\4', alldcom)
    # print(final)
    final = myreg3.sub('\'', final)
    final1 = myreg2.sub('s\'', final)

    myreg4 = re.compile('(\n\n+)')
    myreg5 = re.compile('([\n <s>]\"[\w !?\-;.,]+\"[\w!? \-;,]+)\.([ \n])')
    myreg6 = re.compile('(<s>[\w!? \-;,]+)\.([ \n])')
    final2 = myreg4.sub(r'</s>\1<s>', final1)
    final2 = "<s>"+final2
    final2 = myreg5.sub(r'\1</s>. <s>', final2)
    final2 = myreg6.sub(r'\1</s>.<s>', final2)
    # while(myreg6.search(final2)!=None):
    #     x=raw_input()
    #     final2 = myreg6.sub(r'\2</s>.\3<s>', final2)
    print(final2)

    # print(re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text))
    # print(re.split(r'   (?<!\w\.\w.) (?<![A-Z][a-z]\.) (?<=\.|\?)\s   ', text))



main()
