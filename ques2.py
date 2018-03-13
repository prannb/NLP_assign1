import re
# from sklearn.neural_network import MLPClassifier
# from sklearn.datasets import load_svmlight_file
# import sys
# from sklearn import load_svmlight_file

WINDOW_SIZE = 4

def main():
    test = open('send2.txt', 'r')
    text = test.read()
    test.close()
    # print(len(text))
    # return
    l = len(text)

    myreg1 = re.compile("[.!?]")
    
    arr = myreg1.finditer(text)
    
    # print(arr[0].start)
    out = []
    inp = []
    
    # print(text)
    for match in arr:
        start = match.start()
        if (text[start+1]=="<" and text[start+2]=="/" and text[start+3]=="s" and text[start+4]==">"):
            out.append(1)
            s = text[start-WINDOW_SIZE:start+1]
            for i in range(4, WINDOW_SIZE+4):
                if(start+i+1 >=l):
                    print("pramn")
                    inp.append(s)
                    break
                if(text[start+i+1]=="<" and text[start+i+2]=="s"):
                    start=start+3
                s=s+text[start+i+1]
        else:
            out.append(0)
            s = text[start-WINDOW_SIZE:start+1]
            for i in range(0, WINDOW_SIZE):
                if(text[start+i+1]=="<"  and text[start+i+2]=="s"):
                    start=start+3
                s=s+text[start+i+1]
        inp.append(s)
    
    print(inp)

main()
