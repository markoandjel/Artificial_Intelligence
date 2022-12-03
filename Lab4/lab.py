import numpy as np

def Figura3x3(i,j,figura):
    if len(figura)!=3:
        return
    else:
        if i==0 and j==0:
            return [[*figura[0],0,0],[*figura[1],0,0],[*figura[2],0,0],[*np.zeros(5,int)],[*np.zeros(5,int)]]
        elif i==0 and j==1:
            return [[0,*figura[0],0],[0,*figura[1],0],[0,*figura[2],0],[*np.zeros(5,int)],[*np.zeros(5,int)]]
        elif i==0 and j==2:
            return [[0,0,*figura[0]],[0,0,*figura[1]],[0,0,*figura[2]],[*np.zeros(5,int)],[*np.zeros(5,int)]]
        elif i==1 and j==0:
            return [[*np.zeros(5,int)],[*figura[0],0,0],[*figura[1],0,0],[*figura[2],0,0],[*np.zeros(5,int)]]
        elif i==1 and j==1:
            return [[*np.zeros(5,int)],[0,*figura[0],0],[0,*figura[1],0],[0,*figura[2],0],[*np.zeros(5,int)]]
        elif i==1 and j==2:
            return [[*np.zeros(5,int)],[0,0,*figura[0]],[0,0,*figura[1]],[0,0,*figura[2]],[*np.zeros(5,int)]]
        elif i==2 and j==0:
            return [[*np.zeros(5,int)],[*np.zeros(5,int)],[*figura[0],0,0],[*figura[1],0,0],[*figura[2],0,0]]
        elif i==2 and j==1:
            return [[*np.zeros(5,int)],[*np.zeros(5,int)],[0,*figura[0],0],[0,*figura[1],0],[0,*figura[2],0]]
        elif i==2 and j==2:
            return [[*np.zeros(5,int)],[*np.zeros(5,int)],[0,0,*figura[0]],[0,0,*figura[1]],[0,0,*figura[2]]]

def Figura4x4(i,j,figura):
    if len(figura)!=4:
        return
    else:
        if i==0 and j==0:
            return [[*figura[0],0],[*figura[1],0],[*figura[2],0],[*figura[3],0],[*np.zeros(5,int)]]
        elif i==0 and j==1:
            return [[0,*figura[0]],[0,*figura[1]],[0,*figura[2]],[0,*figura[3]],[*np.zeros(5,int)]]
        elif i==1 and j==0:
            return [[*np.zeros(5,int)],[*figura[0],0],[*figura[1],0],[*figura[2],0],[*figura[3],0]]
        elif i==1 and j==1:
            return [[*np.zeros(5,int)],[0,*figura[0]],[0,*figura[1]],[0,*figura[2]],[0,*figura[3]]]



zelena=[[1,0,0],[1,0,0],[1,1,1]]
plava=[[1,0,0],[1,1,0],[1,1,0]]
narandzasta=[[1,1,0],[1,0,0],[1,1,0]]
crvena=[[0,1,0],[1,1,1],[0,0,1]]
zuta=[[0,0,0,0],[0,0,0,0],[0,1,1,1],[1,1,0,0]] #mirorrovana je ova figura jer za to sam nasao resenje

figure=(zelena,plava,narandzasta,crvena,zuta)


matrica=[[zelena[0],0,0],[zelena[1],0,0],[zelena[2],0,0],[0,0,0,0,0],[0,0,0,0,0]]


matrica2=[[*np.zeros(5,int)],np.zeros(5),[0,0,zelena[0]],[0,0,zelena[1]],[0,0,zelena[2]]]




matrica3=[[*(zelena[0]),0,0],[*zelena[1],0,0],[*zelena[2],0,0],[0,0,0,0,0],[0,0,0,0,0]]

print(len(zuta))