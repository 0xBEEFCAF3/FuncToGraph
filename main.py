import math
from matplotlib import pyplot as plt

class node:
    def __init__(self,left,right,op):
       self.right = right
       self.left = left
       self.op = op
       self.next = None
          
    def write(self):
        k = self
        while(True):
            print(k.right, " " , k.op , " " , k.left)
            #if type(self.right) == node and type(self.left) == node
            if type(k.right) == node:
                k = k.right
            elif type(k.left) == node:
                k = k.left
            else:
                break
class funct_to_graph:
	
    def __init__(self,eq,r):
        self.eq = eq
        self.ops = ['+','-','*','/']
        self.range = r
        
    def Make_list(self,k):
        #SAMPLE EQ = "(X + Y )" or (X + (Z + Y) )
        ops = []
        exp = []
        
        X = node(None,None,None)
        
        arr_eq = list(k)
		  #only three things to deal with so this can be done manually
        for i in arr_eq:
            if i == '(':
                continue
            elif i in self.ops:
                ops.append(i)
            elif i == ')':
                right = exp.pop()
                op = ops.pop()
                left  = exp.pop()
                
                exp.append(node(left,right,op))
            else:            
                exp.append(i)
                
        head = exp.pop()
        
        X.left = head.left
        X.right = head.right
        X.op = head.op
        
        return X
    #node K shold return a float or int
    def calc(self,k,var):
        A = k.left
        B = k.right
        print(A,B)
        if isinstance(A,node) and isinstance(B,node):
            A = self.calc(A,var)
            B = self.calc(B,var)
        elif isinstance(A,node):
            A = self.calc(A,var)
        elif isinstance(B,node):
            print("gets called")
            B = self.calc(B,var)
        

        #check if there is varialble
        if not str(A).isdigit() and type(A) != float:
            A = var
        if not str(B).isdigit() and type(B) != float:
            B = var    
        
        A = float(A)
        B = float(B)
        
        print("A: ", A , "B: " , B, "op: " , k.op  , "return: " , A*B)        
        
        
        if k.op == "+":
            return A + B
        elif k.op == "-":
            return A - B
        elif k.op == "*":
            
            return A * B
        else:
            if B != 0: return A / B
            else: return None
    def run(self):
         Xs = []
         Ys = [i for i in self.range]

         for i in self.range:
             Xs.append(self.calc(self.Make_list(self.eq),i))
         plt.figure(1)
         plt.plot(Ys,Xs,'--r')
         plt.draw()
         plt.show()

         
###Testing Code


k = input()
obj =funct_to_graph(k,range(-10,10))
obj.run()
