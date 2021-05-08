# -*- coding: utf-8 -*-

def S(line):
    if(line.startswith("http://")):
        stack.append("H") 
        print("Applied rule: S → H")
    elif(line.startswith("ftp://")):
        stack.append("F")
        print("Applied rule: S → F")
    elif(line.startswith("telnet://")):
        stack.append("T")
        print("Applied rule: S → T")
    elif(line.startswith("mailto::")):
        stack.append("M")
        print("Applied rule: S → M")
    else:
        "Error input"
    

def H(line):
    result = "http://"
    stack.extend("A","H1")
    line = line[len(result):]
    print("Applied rule: H → http://AH1")
    return line,result

def F(line):
    result = "ftp://"
    stack.extend("L","/","Y1")
    line = line[len(result):]
    print("Applied rule:  F → ftp://L/Y1")
    return line,result

def T(line):
    result = "telnet://"
    stack.append("L")
    line = line[len(result):]
    print("Applied rule: T → telnet://L")
    return line,result

def M(line):
    result = "mailto::"
    stack.extend("A","@","A","N")
    line = line[len(result):]
    print("Applied rule: M → mailto::A@AN")
    return line,result

def H1(line):
    result = ""
    if(line.startswith(".") or line.startswith(":")):
        stack.extend("X", "H2")
        print("Applied rule: H1 → XH2")
    elif(line.startswith("/")):
        stack.extend("Y","H3")
        print("Applied rule: H1 → YH3")
    elif(line.startswith("?")):
        result = line[0]
        stack.append("Z")
        print("Applied rule: H1 → ?Z")
    else:
        print("Applied rule: H1 → €")
    line = line[len(result):]
    return line,result
    
def X(line):
    result = ""
    if(line.startswith(".")):
        result = line[0]
        stack.extend("A", "X1")
        print("Applied rule: X → .AX1")
    if(line.startswith(":")):
        result = line[0]
        stack.append("C")
        print("Applied rule: X → :C")
    line = line[len(result):]
    return line,result
    
def H2(line):
    result = ""
    if(line.startswith("/")):
        stack.extend("Y", "H3")
        print("Applied rule: H2 → YH3")
    if(line.startswith("?")):
        result = line[0]
        stack.append("Z")
        print("Applied rule: H2 → ?Z")
    else:
        print("Applied rule: H2 → €")
    line = line[len(result):]
    return line,result
        
        
def Y(line):
    result = ""
    if(line.startswith("/")):
        result = line[0]
        stack.extend("A", "Y2")
        print("Applied rule: Y → /AY2")
    line = line[len(result):]
    return line,result
        
def H3(line):
    result = ""
    if(line.startswith("?")):
        result = line[0]
        stack.append("Z")
        print("Applied rule: H3 → ?Z")
    else:
        print("dolar")
        print("Applied rule: H3 → €")
    line = line[len(result):]
    return line,result
        
def Z(line):
    if(line[0]>=97 and line[0]<=122 or line[0]>=48 and line[0]<=57):
        stack.extend("A", "Z1")
        print("Applied rule: Z → AZ1")
    
        
def A(line):
    result = ""
    if(line[0]>=97 and line[0]<=122 or line[0]>=48 and line[0]<=57):
        result = line[0]
        stack.append("A1")
        print("Applied rule: A → xaplhaA1")
    line = line[len(result):]
    return line,result
        
def C(line):
    result = ""
    if(line[0]>=48 and line[0]<=57):
        result = line[0]
        stack.append("C1")
        print("Applied rule: C → numericC1")
    line = line[len(result):]
    return line,result
        
def X1(line):
    if(line.startswith(".") or line.startswith(":")):
        stack.append("X")
        print("Applied rule: X1 →  X")
    else:
        print("Applied rule: X1 →  €")
        
def Y2(line):    
    if(line.startswith("/")):
        stack.append("Y")
        print("Applied rule: Y2 →  Y")
    else:
        print("dolar")
        print("Applied rule: Y2 →  €")
        
def Z1(line):
    result = ""
    if(line.startswith("+")):
        result = line[0]
        stack.append("Z")
        print("Applied rule: Z1 → +Z")
    else:
        print("Applied rule: Z1 → €")
    line = line[len(result):]
    return line,result
        
def Y1(line):
    if(line[0]>=97 and line[0]<=122 or line[0]>=48 and line[0]<=57):
        stack.extend("A", "Y3")
        print("Applied rule: Y1 → AY3")
        
def Y3(line):
    if(line.startswith("/")):
        stack.append("Y")
        print("Applied rule: Y3 → Y")
    else:
        print("dolar")
        print("Applied rule: Y3 → €")
        
def L(line):
    if(line[0]>=97 and line[0]<=122 or line[0]>=48 and line[0]<=57):
        stack.extend("A", "L1")
        print("Applied rule: L→ AL1")
        
def L1(line):
    result = ""
    if(line.startswith(".") or line.startswith(":")):
        stack.append("X")
        print("Applied rule: L1 → X")
    if(line.startswith("*")):
        result = line[0]
        stack.extend("A", "@", "A", "L2")
        print("Applied rule: L1 → *A@AL2")
    if(line.startswith("@")):
        result = line[0]
        stack.extend("A", "L2")
        print("Applied rule: L1 → @AL2")
    else:
        print("Applied rule: L1 → €")
    line = line[len(result):]
    return line,result
        
def L2(line):
    if(line.startswith(".") or line.startswith(":")):
        stack.append("X")
        print("Applied rule: L2 → X")
    else:
        print("Applied rule: L2 → €")
              
def N(line):
    result = ""
    if(line.startswith(".")):
        result = line[0]
        stack.extend("A", "N1")
        print("Applied rule: N → .AN1")
    line = line[len(result):]
    return line,result
        
def N1(line):
    if(line.startswith(".")):
        stack.append("N")
        print("Applied rule: N1 → N")
    else:
        print("Applied rule: N1 → €")

def A1(line):
    if(line[0]>=97 and line[0]<=122 or line[0]>=48 and line[0]<=57):
        stack.append("A")
        print("Applied rule: A1 → A")
    else:
        print("Applied rule: A1 → €")
        
def C1(line):
    if(line[0]>=48 and line[0]<=57):
        stack.append("C")
        print("Applied rule: C1 → C")
    elif(line.startswith("/") or line.startswith("?")):
        print("Applied rule: C1 → €")
        
#-----------------------------------------------------------------------------------------------------        


file1 = open('input.txt', 'r')
Lines = file1.readlines()   
stack = []
"""
for line in Lines:
    stack = []
    result = ""
    stack.append("S")
    while(1):
        if(len(stack)==0):
            break
        value=stack.pop(0)
        line, res = rules.get(value)
        result = result + res
        print(result)
        print(line)
        for r in stack:
            print(r)

"""
    