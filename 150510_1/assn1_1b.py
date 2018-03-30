import re
    # """the re module."""

def main():
    # print("Lets start NLP with learning Regular Expressions")
    test = open('fullTest.txt', 'r')
    text = test.read()
    test.close()
    # print(text)
    myreg = re.compile("Dr#")
    myreg1 = re.compile("Dr.")
    myreg3 = re.compile("G. K.")
    myreg2 = re.compile("G K#")
    myreg4 = re.compile("([.?!])([\s])([A-Z]|['])")
    myreg5 = re.compile("(\n\n+)")
    myreg7 = re.compile('G\. K\. C\.')
    myreg8 = re.compile('Mr\.')
    myreg9 = re.compile('G K C#')
    myreg10 = re.compile('Mr#')
    myreg11 = re.compile('[?] \'')
    myreg12 = re.compile('###!')
    
    final2 = myreg7.sub(r'G K C#', text)
    final2 = myreg8.sub(r'Mr#', final2)
    final2 = myreg3.sub(r'G K#', final2)
    final2 = myreg1.sub(r'Dr#', final2)
    final2 = myreg11.sub(r"###!", final2)
    
    final2 = myreg4.sub(r"\1</s>\2<s>\3", final2)
    final2 = "<s>"+final2
    final2 = myreg5.sub(r"</s>\1<s>", final2)
    
    final2 = myreg9.sub(r'G. K. C.', final2)
    final2 = myreg10.sub(r'Mr.', final2)
    final2 = myreg2.sub(r'G. K.', final2)
    final2 = myreg.sub(r'Dr.', final2)
    final2 = myreg12.sub(r"? '", final2)
    
    l = len(final2)
    final2 = final2[0: l-4]
    send = open("train.txt", "w");
    send.write(final2)
    send.close()

main()
