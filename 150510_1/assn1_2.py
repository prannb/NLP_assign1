import re
from sklearn.neural_network import MLPClassifier
import numpy as np
# from sklearn.datasets import load_svmlight_file
# import sys
# from sklearn import load_svmlight_file

WINDOW_SIZE = 3                             #the window size to consider

def compare1(A, X, i):                      #function to convert a matrix of chars to that containing 1s & 0s
    # for i in range(0,l-1):
    a = np.zeros((14))
    for j in range(0,WINDOW_SIZE):
        if(X[i][j]>='a' and X[i][j]<='z'):
            a[0] = 1
        elif(X[i][j]>='A' and X[i][j]<='Z'):
            a[1] = 1
        elif(X[i][j]==' '):
            a[2] = 1
        elif(X[i][j]=='\n'):
            a[3] = 1
        elif(X[i][j]=='\''):
            a[4] = 1
        elif(X[i][j]==','):
            a[5] = 1
        elif(X[i][j]==';'):
            a[6] = 1
    for j in range(WINDOW_SIZE+1,2*WINDOW_SIZE+1):
        if(X[i][j]>='a' and X[i][j]<='z'):
            a[7] = 1
        elif(X[i][j]>='A' and X[i][j]<='Z'):
            a[8] = 1
        elif(X[i][j]==' '):
            a[9] = 1
        elif(X[i][j]=='\n'):
            a[10] = 1
        elif(X[i][j]=='\''):
            a[11] = 1
        elif(X[i][j]==','):
            a[12] = 1
        elif(X[i][j]==';'):
            a[13] = 1
        # elif(X[i][j]==' '):
    A = np.vstack((A, a))
    return A



def main():
    test = open('train.txt', 'r')
    text = test.read()
    test.close()
    l = len(text)

    myreg1 = re.compile("[.!?]")
    
    arr = myreg1.finditer(text)
    
    out = []
    inp = []
    
    for match in arr:                               #creating the output and input
        start = match.start()
        if(start>=l):
            break
        if (text[start+1]=="<" or text[start+2] == "<"):
            out.append(1)
            s = text[start-WINDOW_SIZE:start+1]
            for i in range(0, WINDOW_SIZE):
                if(start+i+1 >=l):
                    # print("pramn")
                    inp.append(s)

                    a=" "*WINDOW_SIZE
                    inp.append(a)
                    break
                if(text[start+i+1]=="<" and text[start+i+2]=="s"):
                    start=start+3
                if(text[start+i+1]=="<" and text[start+i+2]=="/"):
                    start=start+4
                s=s+text[start+i+1]
        else:
            out.append(0)
            s = text[start-WINDOW_SIZE:start+1]
            for i in range(0, WINDOW_SIZE):
                if(text[start+i+1]=="<"  and text[start+i+2]=="s"):
                    start=start+3
                s=s+text[start+i+1]
        inp.append(s)
    inp = inp[0:len(out)]
    X=np.array(list(inp[0]))
    for i in range(1, len(out)-1):
        x = np.array(list(inp[i]))
        X=np.vstack((X, x))
    Y=np.array(out[0:len(out)-1])
    i=0
    A = np.zeros((14))
    for i in range(0,len(out)-1):
        A=compare1(A, X, i)
    A = np.delete(A, (0), axis=0)
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 4), random_state=1)
    clf.fit(A, Y)
    
    ##****************************Testing starts here********************************************##
    file_test = open("testq2.txt", "r")             #input file
    text_test = file_test.read()
    file_test.close()
    file_testres = open("testres.txt", "r")         #output file
    text_testres = file_testres.read()
    file_testres.close()

    arr1 = myreg1.finditer(text_test)
    arr2 = myreg1.finditer(text_testres)
    i=0;
    ind = []
    for mat in arr2:
        ind.append(mat.start())
    # print(ind)
    i=0
    yes = 0
    for match in arr1:
        start = match.start()
        a = np.zeros((14,1))
        j=0
        for j in range(start-WINDOW_SIZE,start):
            # print(j)
            if(text_test[j]>='a' and text_test[j]<='z'):
                a[0] = 1
            elif(text_test[j]>='A' and text_test[j]<='Z'):
                a[1] = 1
            elif(text_test[j]==' '):
                a[2] = 1
            elif(text_test[j]=='\n'):
                a[3] = 1
            elif(text_test[j]=='\''):
                a[4] = 1
            elif(text_test[j]==','):
                a[5] = 1
            elif(text_test[j]==';'):
                a[6] = 1
        for j in range(start+1,start+1+WINDOW_SIZE):
            if(j>=len(text_test)):
                a[10] = 1
                break;
            # print(j)
            if(text_test[j]>='a' and text_test[j]<='z'):
                a[7] = 1
            elif(text_test[j]>='A' and text_test[j]<='Z'):
                a[8] = 1
            elif(text_test[j]==' '):
                a[9] = 1
            elif(text_test[j]=='\n'):
                a[10] = 1
            elif(text_test[j]=='\''):
                a[11] = 1
            elif(text_test[j]==','):
                a[12] = 1
            elif(text_test[j]==';'):
                a[13] = 1
        a = a.reshape(1,14)
        # print(a)
        b = clf.predict(a)
        if((text_testres[ind[i]+1] == "<" or text_testres[ind[i]+2] == "<") and b==1):
            yes = yes + 1
        elif((text_testres[ind[i]+1] != "<" and text_testres[ind[i]+2] != "<") and b==0):
            yes = yes + 1
        i = i + 1
    print(((yes*1.0)/i)*100)

main()
