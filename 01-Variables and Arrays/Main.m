%1
A=1
%2
B=uint8(1)                    
%3
C=double(1)                 
%4
D=round(1.5)
%5
E=zeros(5,5)
%6 
F=ones(5,5)
%7 
G=rand(5,5)
%8 
H=randi([1,5],3,3)
%9 
I=[1:5]
%10 
J=flip([1:5],2)
%11 
K=ones(3,4)'
%12 
L=reshape(ones(5,5),[25,1])
%13 
M=ones(5,5); M=M(:)
%14
N=linspace(1,10,5)
%15
O=cat(2,[1,2],[3,4,5])
%16
P=rand(5,5)
save('Var.mat','P')
%17
load('Var.mat')
%18 struct
R.var1=12
R.var2=13









