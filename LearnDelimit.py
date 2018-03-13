import re
from sklearn.neural_network import MLPClassifier
# from sklearn.datasets import load_svmlight_file
import sys
# from sklearn import load_svmlight_file

WINDOW_SIZE = 4

def main():
    print("Start Learning")
    traindatafile = sys.argv[1]

	# The training file is in libSVM format
    tr_data = load_svmlight_file(traindatafile);
    print(tr_data)
    quit
    test = open('send2.txt', 'r')
    text = test.read()
    print(text)
    return

    myreg1 = re.compile("[.!?]")
    
    arr = myreg1.finditer(text)
    
    # print(arr[0].start)
    out = []
    inp = [[]]
    
    # print(text)
    for match in arr:
        start = match.start()
        print(text[start+1])
        s = text[start-WINDOW_SIZE:start]
        s = s + text[start] + text[start+5:start+5+WINDOW_SIZE]
        inp.append(s)
        if (text[start+1]=="<"): #&& text[start+2]=='/' && text[start+3]=='s' && text[start+4]=='>'):
            out.append(1)
        else:
            out.append(0)
    
    
    
    print(out)
    print(inp)

main()
