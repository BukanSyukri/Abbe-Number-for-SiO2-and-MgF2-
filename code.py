import matplotlib.pyplot as plt
import numpy as np

ASiO2 = np.array([0.6961663,0.4079426,0.8974794])
BSiO2 = np.array([0.0684043,0.1162414,9.896161])
AMgF2 = np.array([0.48755108,0.39875031,2.3120353])
BMgF2 = np.array([0.04338408,0.09461442,23.793604])
L = np.linspace(0.4,1,100)

R1 = 20
R2 = -20
k = ((1/R1)-(1/R2))
s = 40
t=1/s

#Refractive index of SiO2
n1SiO2 = (ASiO2[0]*L**2)/(L**2-BSiO2[0]**2)
n2SiO2 = (ASiO2[1]*L**2)/(L**2-BSiO2[1]**2)
n3SiO2 = (ASiO2[2]*L**2)/(L**2-BSiO2[2]**2)
nSiO2 = n1SiO2+n2SiO2+n3SiO2
square_n_SiO2 = 1 + nSiO2
n_SiO2 = np.sqrt(square_n_SiO2)

#Refractive index of MgF2
n1MgF2 = (AMgF2[0]*L**2)/(L**2-BMgF2[0]**2)
n2MgF2 = (AMgF2[1]*L**2)/(L**2-BMgF2[1]**2)
n3MgF2 = (AMgF2[2]*L**2)/(L**2-BMgF2[2]**2)
nMgF2 = n1MgF2+n2MgF2+n3MgF2
square_n_MgF2 = 1 + nMgF2
n_MgF2 = np.sqrt(square_n_MgF2)

#nC
LC = np.linspace(0.4,0.6563,100)

#Refractive index of SiO2
nC1SiO2 = (ASiO2[0]*LC**2)/(LC**2-BSiO2[0]**2)
nC2SiO2 = (ASiO2[1]*LC**2)/(LC**2-BSiO2[1]**2)
nC3SiO2 = (ASiO2[2]*LC**2)/(LC**2-BSiO2[2]**2)
nCSiO2 = nC1SiO2+nC2SiO2+nC3SiO2
square_nC_SiO2 = 1 + nCSiO2
nC_SiO2 = np.sqrt(square_nC_SiO2)

#Refractive index of MgF2
nC1MgF2 = (AMgF2[0]*LC**2)/(LC**2-BMgF2[0]**2)
nC2MgF2 = (AMgF2[1]*LC**2)/(LC**2-BMgF2[1]**2)
nC3MgF2 = (AMgF2[2]*LC**2)/(LC**2-BMgF2[2]**2)
nCMgF2 = nC1MgF2+nC2MgF2+nC3MgF2
square_nC_MgF2 = 1 + nCMgF2
nC_MgF2 = np.sqrt(square_nC_MgF2)

nC = np.array([nC_SiO2[-1],nC_MgF2[-1]]) 
mCSiO2 = nC[0] - 1
mCMgF2 = nC[1] - 1

#SiO2
focusSiO2kC = mCSiO2*k
Focus_SiO2kC = 1/focusSiO2kC

#MgF2
focusMgF2kC = mCMgF2*k
Focus_MgF2kC = 1/focusMgF2kC



#nD
LD = np.linspace(0.4,0.5893,100)

#Refractive index of SiO2
nD1SiO2 = (ASiO2[0]*LD**2)/(LD**2-BSiO2[0]**2)
nD2SiO2 = (ASiO2[1]*LD**2)/(LD**2-BSiO2[1]**2)
nD3SiO2 = (ASiO2[2]*LD**2)/(LD**2-BSiO2[2]**2)
nDSiO2 = nD1SiO2+nD2SiO2+nD3SiO2
square_nD_SiO2 = 1 + nDSiO2
nD_SiO2 = np.sqrt(square_nD_SiO2)

#Refractive index of MgF2
nD1MgF2 = (AMgF2[0]*LD**2)/(LD**2-BMgF2[0]**2)
nD2MgF2 = (AMgF2[1]*LD**2)/(LD**2-BMgF2[1]**2)
nD3MgF2 = (AMgF2[2]*LD**2)/(LD**2-BMgF2[2]**2)
nDMgF2 = nD1MgF2+nD2MgF2+nD3MgF2
square_nD_MgF2 = 1 + nDMgF2
nD_MgF2 = np.sqrt(square_nD_MgF2)

nD = np.array([nD_SiO2[-1],nD_MgF2[-1]]) 
mDSiO2 = nD[0] - 1
mDMgF2 = nD[1] - 1

#SiO2
focusSiO2kD = mDSiO2*k
Focus_SiO2kD = 1/focusSiO2kD

#MgF2
focusMgF2kD = mDMgF2*k
Focus_MgF2kD = 1/focusMgF2kD

#nF
LF = np.linspace(0.4,0.4861,100)

#Refractive index of SiO2
nF1SiO2 = (ASiO2[0]*LF**2)/(LF**2-BSiO2[0]**2)
nF2SiO2 = (ASiO2[1]*LF**2)/(LF**2-BSiO2[1]**2)
nF3SiO2 = (ASiO2[2]*LF**2)/(LF**2-BSiO2[2]**2)
nFSiO2 = nF1SiO2+nF2SiO2+nF3SiO2
square_nF_SiO2 = 1 + nFSiO2
nF_SiO2 = np.sqrt(square_nF_SiO2)

#Refractive index of MgF2
nF1MgF2 = (AMgF2[0]*LF**2)/(LF**2-BMgF2[0]**2)
nF2MgF2 = (AMgF2[1]*LF**2)/(LF**2-BMgF2[1]**2)
nF3MgF2 = (AMgF2[2]*LF**2)/(LF**2-BMgF2[2]**2)
nFMgF2 = nF1MgF2+nF2MgF2+nF3MgF2
square_nF_MgF2 = 1 + nFMgF2
nF_MgF2 = np.sqrt(square_nF_MgF2)

nF = np.array([nF_SiO2[-1],nF_MgF2[-1]]) 
mFSiO2 = nF[0] - 1
mFMgF2 = nF[1] - 1

#SiO2
focusSiO2kF = mFSiO2*k
Focus_SiO2kF = 1/focusSiO2kF

#MgF2
focusMgF2kF = mFMgF2*k
Focus_MgF2kF = 1/focusMgF2kF

print('nC SiO2 = ', nC_SiO2[-1])
print('nD SiO2 = ', nD_SiO2[-1])
print('nF SiO2 = ', nF_SiO2[-1])
print( )
print('nC MgF2 = ', nC_MgF2[-1])
print('nD MgF2 = ', nD_MgF2[-1])
print('nF MgF2 = ', nF_MgF2[-1])

VD_SiO2 = (nD_SiO2[-1] - 1)/(nF_SiO2[-1] - nC_SiO2)[-1]
VD_MgF2 = (nD_MgF2[-1] - 1)/(nF_MgF2[-1] - nC_MgF2[-1])
Del_F_SiO2 = Focus_SiO2kF - Focus_SiO2kC
Del_F_MgF2 = Focus_MgF2kF - Focus_MgF2kC
print('The Abbe Number for SiO2 is ', VD_SiO2)
print('The Abbe Number for MgF2 is ', VD_MgF2)
print(' The difference between focal length of F Fraunhofer line and C Fraunhofer line of SiO2 is', np.abs(Del_F_SiO2))
print(' The difference between focal length of F Fraunhofer line and C Fraunhofer line of MgF2 is', np.abs(Del_F_MgF2))
