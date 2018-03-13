import re
    # """the re module."""

def main():
    print("Lets start NLP with learning Regular Expressions")
    test = open('test.txt', 'r')
    text = test.read()
    dial = re.compile("(\s)(')(?!\s)([\w. ,\s;?]*)(')(?=[\s. ,;])") #(\s)(')(?!\s)([\w. ,\s;?]*)(')(?<=)(?=[\s.,;?])  
    final = dial.sub(r'\1"\3"', text)
    print(final)

main()
