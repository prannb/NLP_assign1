import re
    # """the re module."""

def main():
    # print("Lets start NLP with learning Regular Expressions")
    test = open('test.txt', 'r')
    text = test.read()
    test.close()
    # print(text)
    
    myreg3 = re.compile("G. K.")
    myreg2 = re.compile("G K#")
    myreg4 = re.compile("([.?!])([\s])([A-Z]|['])")
    myreg5 = re.compile("([.?!])(\n\n+)")
    # myreg6 = re.compile('(<s>[\w \-:;,\n]+)([.!?])([ \n])')
    myreg7 = re.compile('G\. K\. C\.')
    myreg8 = re.compile('Mr\.')
    myreg9 = re.compile('G K C')
    myreg10 = re.compile('Mr')
    # myreg11 = re.compile('\"')
    final2 = myreg7.sub(r'G K C', text)
    final2 = myreg8.sub(r'Mr', final2)
    final2 = myreg3.sub(r'G K#', final2)
    final2 = myreg4.sub(r"\1</s>\2<s>\3", final2)
    final2 = "<s>"+final2
    final2 = myreg5.sub(r"\1</s>\2<s>", final2)
    
    # final2 = myreg5.sub(r'\1</s>\2<s>\3', final2)
    # final2 = myreg6.sub(r'\1</s>\2<s>\3', final2)
    # i=0
    # while(myreg6.search(final2)!=None):
    #     final2 = myreg6.sub(r'\1</s>.\n<s>', final2)
    #     i=i+1

    final2 = myreg9.sub(r'G. K. C.', final2)
    final2 = myreg10.sub(r'Mr.', final2)
    final2 = myreg2.sub(r'G. K.', final2)
    
    # final2 = myreg11.sub(r"'", final2)
    # print(final2)
    send = open("send2.txt", "w");
    send.write(final2)
    send.close()

main()
