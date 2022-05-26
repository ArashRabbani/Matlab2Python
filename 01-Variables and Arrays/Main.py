import numpy as np
#1
A=1
#2
B=np.uint8(1)
#3
C=np.float64(1)
#4
D=round(1.5)
#5
E=np.zeros((5,5))
#6 
F=np.ones((5,5))
#7 
G=np.random.rand(5,5)
#8 
H=np.random.randint(1,5,(3,3))
#9 
I=np.arange(1,6)
#10 
J=np.flip(np.arange(1,6),0)
#11 
K=np.transpose(np.ones((3,4)))
#12 
L=np.reshape(np.ones((5,5)),[25,1])
#13 
M=np.ones((5,5)); M=np.reshape(M,(1,-1))
#14
N=np.linspace(1,10,5)
#15
O=np.concatenate(([1,2],[3,4,5]),axis=0)
#16
P=np.random.rand(5,5)
np.save('Var.npy',P)
#17
P=np.load('Var.npy')
#18 struct
class struct:
        pass
R=struct()
R.var1=12
R.var2=13
    