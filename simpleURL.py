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
    return line,''

def H(line):
    stack.extend(["H1","A","http://"])
    print("Applied rule: H → http://AH1")

def F(line):
    stack.extend(["Y1","/","L","ftp://"])
    print("Applied rule:  F → ftp://L/Y1")

def T(line):
    stack.extend(["L", "telnet://"])
    print("Applied rule: T → telnet://L")

def M(line):
    stack.extend(["N","A","@","A","mailto::"])
    print("Applied rule: M → mailto::A@AN")

def H1(line):
    if(line.startswith(".") or line.startswith(":")):
        stack.extend(["H2","X"])
        print("Applied rule: H1 → XH2")
    elif(line.startswith("/")):
        stack.extend(["H3","Y"])
        print("Applied rule: H1 → YH3")
    elif(line.startswith("?")):
        stack.extend(["Z", "?"])
        print("Applied rule: H1 → ?Z")
    else:
        print("Applied rule: H1 → €")
    
def X(line):
    if(line.startswith(".")):
        stack.extend(["X1", "A", "."])
        print("Applied rule: X → .AX1")
    if(line.startswith(":")):
        stack.extend(["C", ":"])
        print("Applied rule: X → :C")
    
def H2(line):
    if(line.startswith("/")):
        stack.extend(["H3","Y"])
        print("Applied rule: H2 → YH3")
    if(line.startswith("?")):
        stack.extend(["Z", "?"])
        print("Applied rule: H2 → ?Z")
    else:
        print("Applied rule: H2 → €")

        
def Y(line):
    if(line.startswith("/")):
        stack.extend(["Y2", "A", "/"])
        print("Applied rule: Y → /AY2")
        
def H3(line):
    if(line.startswith("?")):
        stack.extend(["Z","?"])
        print("Applied rule: H3 → ?Z")
    else:
        print("dolar")
        print("Applied rule: H3 → €")
        
def Z(line):
    if(line[0]>='a' and line[0]<='z' or line[0]>='0' and line[0]<='9'):
        stack.extend(["Z1", "A"])
        print("Applied rule: Z → AZ1")
        
def A(line):
    if(line[0]>='a' and line[0]<='z' or line[0]>='0' and line[0]<='9'):
        stack.extend(["A1", line[0]])
        print("Applied rule: A → xaplhaA1")
        
def C(line):
    if(line[0]>='0' and line[0]<='9'):
        stack.extend(["C1", line[0]])
        print("Applied rule: C → numericC1")
        
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
    if(line.startswith("+")):
        stack.extend(["Z", "+"])
        print("Applied rule: Z1 → +Z")
    else:
        print("Applied rule: Z1 → €")
        
def Y1(line):
    if(line[0]>='a' and line[0]<='z' or line[0]>='0' and line[0]<='9'):
        stack.extend(["Y3","A"])
        print("Applied rule: Y1 → AY3")
        
def Y3(line):
    if(line.startswith("/")):
        stack.append("Y")
        print("Applied rule: Y3 → Y")
    else:
        print("dolar")
        print("Applied rule: Y3 → €")
        
def L(line):
    if(line[0]>='a' and line[0]<='z' or line[0]>='0' and line[0]<='9'):
        stack.extend(["L1", "A"])
        print("Applied rule: L→ AL1")
        
def L1(line):
    if(line.startswith(".") or line.startswith(":")):
        stack.append("X")
        print("Applied rule: L1 → X")
    if(line.startswith("*")):
        stack.extend(["L2", "A", "@", "A", "*"])
        print("Applied rule: L1 → *A@AL2")
    if(line.startswith("@")):
        stack.extend(["L2", "A", "@"])
        print("Applied rule: L1 → @AL2")
    else:
        print("Applied rule: L1 → €")
        
def L2(line):
    if(line.startswith(".") or line.startswith(":")):
        stack.append("X")
        print("Applied rule: L2 → X")
    else:
        print("Applied rule: L2 → €")
              
def N(line):
    if(line.startswith(".")):
        stack.extend(["N1", "A", "."])
        print("Applied rule: N → .AN1")
        
def N1(line):
    if(line.startswith(".")):
        stack.append("N")
        print("Applied rule: N1 → N")
    else:
        print("Applied rule: N1 → €")

def A1(line):
    if(line[0]>='a' and line[0]<='z' or line[0]>='0' and line[0]<='9'):
        stack.append("A")
        print("Applied rule: A1 → A")
    else:
        print("Applied rule: A1 → €")
        
def C1(line):
    if(line[0]>='0' and line[0]<='9'):
        stack.append("C")
        print("Applied rule: C1 → C")
    elif(line.startswith("/") or line.startswith("?")):
        print("Applied rule: C1 → €")
        
#------------------------------------------------------------------------------       

nonterminals = ["S","H","F","T","M","H1","X","H2","Y","H3","Z","A","C","X1",
                "Y2","Z1","Y1","Y3","L","L1","L2","N","N1","A1","C1"]

file1 = open('input.txt', 'r')
Lines = file1.readlines() 
stack = []
choice = ""
noSteps = 0
for line in Lines:
    stack = []
    stack.append("S")
    if(choice == "e"):
        break
    while(1):
        if(choice!="r" and noSteps==0):
            choice = input("Please enter your choice (r RUN ALL, n NEXT STEP, numeric NUMBER OF STEPS, e END EXCECUTION):\n")
        if(len(stack)==0):
            if(line == '\n'):
                    print("\n\nCorrect input\n\n")
            else:
                print("\n\nIncorrect input\n\n")
            break
        if(choice == "n"):
            noSteps = 1
        if(choice.isnumeric()):
            noSteps = int(choice)
        if(choice == "e"):
            break
        while(choice == "r" or noSteps > 0):
            if(choice!="r"):
                noSteps = noSteps - 1
            if(len(stack)==0):                
                break
            value=stack.pop()
            print("\npoped from stack: " + value)
            if(value in nonterminals):
                eval(value+'(line)')
            else:
                line = line[len(value):]
            print("input: " + line + "stack: ")
            print(stack)

file1.close()    