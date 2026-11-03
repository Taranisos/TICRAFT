B8='You reached the world border'
B7=' blocks too mutch, deleting highest ones.'
B6=' is corrupted and has '
B5='Console: Warning: chunk corruption, chunk '
AP=' blocks, filling in with air.'
AO=' is corrupted and misses '
AN='Console: Warning chunk corruption, chunk '
AM=isinstance
A4='MCWD'
y='MCWD0'
x=int
k=abs
Y=str
L=None
I=print
H=len
F=range
E=True
D=False
import ti_draw as A,time as l,random as a,ti_system as W,math as m
A5=4
S=0
A6=D
A7=D
B9=D
T=[]
b=D
AQ=[102,92,93,94,82,83,84,72,73,74]
R=1
n=E
AR=44,129,21
A8=93,174,58
AS=119,203,83
AT=103,237,108
o=116,76,52
c=144,96,66
h=166,112,76
p=183,135,94
d=161,155,148
AU=104,104,104
G=116,116,116
BA=127,127,127
AV=143,143,143
AW=56,43,24
AX=76,61,38
A9=95,74,43
AA=116,90,54
AY=145,113,66
AB=152,120,73
AZ=126,98,55
Aa=159,132,77
BB=175,143,85
M=184,148,95
P=194,157,98
Ab=139,193,205
é=168,208,217
è=208,234,233
Ac=209,186,138
AC=213,196,150
AD=218,207,163
BC=227,219,176
Ad=231,228,187
Ae=237,235,203
Af=177,176,176
Ag=185,185,185
Ah=193,193,193
Ai=209,207,207
BD=214,214,214
BE=220,220,220
Aj=224,224,224
BF=230,230,230
BG=236,236,236
Ak=242,242,242
Al=43,65,41
Am=49,76,47
An=62,99,60
AE=76,121,73
BH=30,56,107
q=32,59,112
Ao=35,65,125
Ap=38,71,135
Aq=45,83,163
BI=0,0,0
BJ=111,110,113
AF=5,23,52
AG=130,172,255
Q=AG
AH=255,255,255
Ar=[AR,[6,0],[15,0],AS,[9,0],[21,0],[0,3],[18,3],[15,6],AT,[0,0],[12,3],[21,3],o,[3,3,2],[0,6],[9,6,-2],[12,9],[18,9],[15,12],[6,15,2],[21,15],[9,18,2],[0,21],[18,21],c,[18,6],[3,9,2],h,[6,6],[0,9],[6,12,2],[21,12],[0,15],[12,15],[3,18],[18,18],[15,21],p,[21,9],[3,12],[12,12],[0,18],[15,18],[21,21],d,[3,6],[15,15],[6,21]]
As=[o,[9,0,-4],[12,0],[0,3],[21,9],[3,12],[18,12,2],[6,18,2],[0,21,2],[15,21],c,[6,0],[21,0],[12,3],[3,6,2],[18,6],[15,9,2],[6,12],[12,12],[0,15],[9,15],[15,15],[12,18],[18,18],[18,21,2],p,[3,0],[15,0],[0,6],[12,6],[0,9,2],[6,15],[21,15],[15,18],[9,21],d,[3,3],[18,3],[12,15],[3,18]]
At=[AU,[6,6,2],[21,6],[18,18,-2],[3,21,2],[15,21],G,[15,0,2],[6,3],[12,3],[3,6],[12,6,3],[0,12],[9,12,3],[21,12],[0,18,-2],[9,21,2],[21,21],AV,[0,0,2],[9,0],[6,9,2],[15,9],[3,15],[9,18,3],[21,18]]
Au=[AW,[18,0],[15,3,-2],[3,6,-2],[15,12],[18,18,-2],[6,21],AX,[6,0],[3,3],[21,3,-5],[15,9],[3,12],[6,15,-2],[15,15],A9,[6,3,-2],[9,3,-4],[0,18,-2],[15,18],AY,[0,9,-3],[12,15,-3],[21,21],AB,[18,3,-2]]
Av=[AA,[9,9],[18,9,2],[0,21,2],[18,21,2],AB,[0,9],[12,9],[21,15,-2],[12,21],AZ,[9,3,-2],[3,9,2],[15,9],[6,21,2],[15,21],Aa,[9,0],[15,3],[21,6],[6,12],[21,12],[12,15],[18,15],[0,18,2],M,[0,0],[6,0],[0,3,2],[21,3],[3,6,2],[15,6],[0,12],[3,15,2],[9,18],P,[12,0,4],[3,12],[9,12,4]]
Aw=[Ab,[21,6,-6],[3,21,5],é,[21,0,-2],[6,9],[0,18,-2],[21,18],[18,21,2],è,[0,0,-6],[3,0,6],[9,6],[15,15]]
Ax=[Ac,[15,0],[6,6],AC,[0,3],[9,3,-3],[15,3,2],[12,6],[15,9],[21,9],[0,12],[12,12],[3,15],[0,18],[9,18,2],[18,18],[3,21],[12,21],[21,21],AD,[3,9,2],BC,[9,0],[18,0],[21,3],[0,6],[18,9],[15,12],[21,12],[12,15,3],Ad,[0,0],[15,6],[3,18],Ae,[6,12],[15,18]]
BK=[Af,[21,3],[0,9],[21,12],[0,18],Ag,[21,6,-2],[21,15,-2],[6,21,6],Ai,[0,0],[9,0,5],BD,[15,9,2],[15,18,2],BE,[3,9,2],[3,18,4],Aj,[9,9,2],BF,[3,6,6],[12,12,3],[3,15,6],BG,[18,3],[9,12],Ak,[3,3,5],[3,12,2]]
Ay=[Al,[0,0,-2],[6,0,-2],[12,3],[21,6],[9,9],[6,12],[21,21],Am,[21,0,-2],[3,3],[0,6,2],[18,6],[6,15],[0,18,2],An,[18,3],[15,6],[0,9],[18,9,2],[3,12,-2],[9,12,-2],[6,18],[18,18],[0,21],AE,[12,0,2],[0,15],[15,15,2],[12,18,2],[21,18],[3,21],[15,21,2]]
r=[BH,[0,0],[9,0,5],[3,3,4],[0,6,2],[12,6,4],[15,9],[3,12,3],[0,15,4],[15,15,3],[3,18,2],Ao,[6,9,2],[21,9],[18,12],[6,21,2],[15,21,2],Ap,[6,0],Aq,[21,12],[12,21]]
BL=[AR,[6,0],A8,[12,0,-2],AS,[0,0],AT,[18,0],o,[0,12],[18,18],h,[18,6],[12,12],[0,18],p,[6,6,-2]]
BM=[o,[6,0],[0,12],h,[12,0,-2],[6,12],[0,18],p,[6,6],[18,6],[12,18,2]]
BN=[AU,[6,12,3],G,[0,6,3],[6,18],AV,[12,0,2],[0,12,-2]]
BO=[AW,[18,0,-2],[6,6,-3],AX,[18,12],A9,[12,0,-3],[0,12,-2],AB,[12,18]]
BP=[A9,[0,0],AA,[6,0,2],[18,12],AY,[18,0],[0,12],AZ,[6,12,2],Aa,[6,6,2],M,[18,6],[12,18]]
BQ=[Al,[0,12,2],Am,[0,6],An,[12,0],[0,18],AE,[18,0,-3],[12,6],[6,18]]
BR=[Ab,[18,0,-2],é,[0,18,2]]
BS=[Ac,[0,6,3],[6,12],AD,[0,0],[18,0],Ad,[0,12,-2],Ae,[6,0,2],[12,18,2]]
Bg=[Ag,[12,0],[18,0,-3],[0,18,2],Ai,[6,6,2],Aj,[6,12],Ak,[12,12]]
BT=[q,[0,12,3],Ao,[12,0,2],Aq,[0,6,3],[0,18,2]]
def i(world):
	try:return W.recall_list(world)
	except Exception:return
def AI(world,saving):
	try:W.store_list(saving,world);return E
	except:return D
def BU(world):
	K=world;I('Changing to save format.');L=D;M=[];B=-500
	for C in F(0,1000,100):
		I('Formatting world ',round((C+1)/100)+1,'/ 10.');G=[]
		for list in F(100):
			if C+list==0:G.append(K[0])
			else:
				B+=1;A=K[C+list];J=''
				if H(A)!=8:
					L=E
					if H(A)<8:
						I(AN,B,AO,8-H(A),AP)
						for N in F(8-H(A)):A.append(0)
					else:
						I(B5,B,B6,H(A)-8,B7)
						for N in F(H(A)-8):A.pop(0)
				J='1'
				for O in F(8):J+=Y(A[7-O])
				G.append(x(J))
		M.append(G)
	if L:I('Console: Info: world saved succesfully!');l.sleep(3)
	return M
def AJ(player_x=L):
	C=player_x;G=i(y);M=D;H=D;F=D;B=[]
	if C==L:C=G[0]
	B.append(C);A=m.floor((C+499)/20)
	if k(C+401)>5:
		if C-(A*20-499)<6 or A==49:F=E
		N=m.floor(A/5);J=A4;J+=Y(N);B.append(A);G=i(J);O=Z(A)
		if not F:H=E
		if H:B.append(A+1);K=Z(A+1)
		elif F:B.append(A-1);K=Z(A-1)
	if M:I('Console: Info: world loaded succesfully!');l.sleep(3)
	B.append(O);B.append(K);return B
def BV(start,world,end):
	C=world;D=[]
	for B in F(start,end):
		G=[];A=Y(C[B])
		if H(A)<9:
			I(A);I(C[B]);l.sleep(3);K=E;I(AN,B-50,AO,9-H(A),AP)
			for L in F(9-H(A)):A+='0'
		for J in F(1,9):G.append(x(A[9-J]))
		D.append(G)
	return D
def Z(chunk):
	A=chunk;C=m.floor(A/5);D=A4;D+=Y(C);B=20*(A-C*5);F=i(D)
	if A==0:B=1;E=20
	else:E=B+20
	A=BV(B,F,E);return A
def e(chunk,chunk_x):
	B=chunk_x;M=m.floor(B/5);D=A4;D+=Y(M);Q=B-M*5;N=[]
	for R in chunk:
		A=R;O='1'
		if H(A)!=8:
			T=E
			if H(A)<8:
				I(AN,B,AO,8-H(A),AP)
				for S in F(8-H(A)):A.append(0)
			else:
				I(B5,B,B6,H(A)-8,B7)
				for S in F(H(A)-8):A.pop(0)
		for G in F(8):O+=Y(A[7-G])
		N.append(x(O))
	try:C=W.recall_list(D)
	except:C=L;I('Failed to save chunk')
	if C is not L:
		J=Q*20;K=0
		if B!=0:P=J+20
		else:J=1;K=0;P=20
		for G in F(J,P):C[G]=N[K];K+=1
	AI(C,D)
def BW(player_x):A=i(y);A[0]=player_x;AI(A,y)
def s(player_x,dir,chunk):
	B=chunk;A=player_x;A-=B*20-500;A=Y(A)
	if B==0:
		if A=='14':return E
	elif dir:
		if A=='15':return E
	elif A=='6':return E
	return D
def AK(x,chunk1,chunk2):
	C=chunk2;B=chunk1;D=19
	if B==0:D=18
	A=x+499-B*20
	if A>=0 and A<=D:list=[3,A]
	else:
		A=x+499-C*20;list=[4,A]
		if A==19 and C==0:list=[3,0]
	return list
def U(x,y,block):
	for B in block:
		if AM(B,list):
			if H(B)==2:A.fill_rect(B[0]+x,B[1]+y,4,4)
			elif B[2]>=0:A.fill_rect(B[0]+x,B[1]+y,B[2]*3+1,4)
			else:A.fill_rect(B[0]+x,B[1]+y,4,k(B[2])*3+1)
		else:A.set_color(*B)
def V(x,y,block):
	for B in block:
		if AM(B,list):
			if H(B)==2:A.fill_rect(B[0]+x,B[1]+y,7,7)
			elif B[2]>=0:A.fill_rect(B[0]+x,B[1]+y,B[2]*6+1,7)
			else:A.fill_rect(B[0]+x,B[1]+y,7,k(B[2])*6+1)
		else:A.set_color(*B)
def t(x,y,grass,grass4,graphics):
	B=graphics
	if B==0:A.set_color(*A8);A.fill_rect(x,y,25,7);A.set_color(*c);A.fill_rect(x,y+6,25,19)
	if B==1:A.set_color(*c);A.fill_rect(x,y,25,25);V(x,y,grass4)
	elif B==2:A.set_color(*A8);A.fill_rect(x,y,25,13);A.set_color(*c);A.fill_rect(x,y+12,25,13);U(x,y,grass)
def u(x,y,dirt,dirt4,graphics):
	B=graphics
	if B==0:A.set_color(*h);A.fill_rect(x,y,25,25)
	elif B==1:A.set_color(*c);A.fill_rect(x,y,25,25);V(x,y,dirt4)
	elif B==2:A.set_color(*h);A.fill_rect(x,y,25,25);U(x,y,dirt)
def v(x,y,stone,stone4,graphics):
	B=graphics;A.set_color(*BA);A.fill_rect(x,y,25,25)
	if B==1:V(x,y,stone4)
	elif B==2:U(x,y,stone)
def w(x,y,oak_log,oak_log4,graphics):
	B=graphics;A.set_color(*AA);A.fill_rect(x,y,25,25)
	if B==1:V(x,y,oak_log4)
	elif B==2:U(x,y,oak_log)
def z(x,y,oak_planks,oak_planks4,graphics):
	B=graphics;A.set_color(*BB);A.fill_rect(x,y,25,25)
	if B==1:V(x,y,oak_planks4)
	elif B==2:U(x,y,oak_planks)
def A0(x,y,oak_leaves,oak_leaves4,graphics):
	B=graphics
	if B==0:A.set_color(*AE);A.fill_rect(x,y,25,25)
	else:
		A.set_color(*Q);A.fill_rect(x,y,25,25)
		if B==1:V(x,y,oak_leaves4)
		else:U(x,y,oak_leaves)
def A1(x,y,glass,glass4,graphics):
	B=graphics
	if B==0:A.set_color(*è);A.fill_rect(x,y,25,25);A.set_color(*Q);A.fill_rect(x+6,y+6,13,13)
	if B==1:A.set_color(*è);A.fill_rect(x,y,25,25);A.set_color(*Q);A.fill_rect(x+6,y+6,13,13);V(x,y,glass4)
	elif B==2:A.set_color(*Q);A.fill_rect(x,y,25,25);U(x,y,glass)
def A2(x,y,sand,sand4,graphics):
	B=graphics
	if B==0:A.set_color(*AC);A.fill_rect(x,y,25,25)
	if B==1:A.set_color(*AC);A.fill_rect(x,y,25,25);V(x,y,sand4)
	elif B==2:A.set_color(*AD);A.fill_rect(x,y,25,25);U(x,y,sand)
def BX(x,y,iron,iron4,graphics):
	B=graphics
	if B==0:A.set_color(*Ah);A.fill_rect(x,y,25,25)
	if B==1:A.set_color(*Af);A.fill_rect(x,y,25,25);V(x,y,iron4)
	elif B==2:A.set_color(*Ah);A.fill_rect(x,y,25,25);U(x,y,iron)
def A3(x,y,water,water4,graphics):
	B=graphics
	if B==0:A.set_color(*q);A.fill_rect(x,y,25,25)
	if B==1:A.set_color(*Ap);A.fill_rect(x,y,25,25);V(x,y,water4)
	elif B==2:A.set_color(*q);A.fill_rect(x,y,25,25);U(x,y,water)
def Az(x,y,water):
	A.set_color(*q);A.fill_rect(x,y,161,161)
	for B in water:
		if AM(B,list):
			if H(B)==2:A.fill_rect(B[0]/3*20+x,B[1]/3*20+y,21,21)
			elif B[2]>=0:A.fill_rect(B[0]/3*20+x,B[1]/3*20+y,B[2]*20+1,21)
			else:A.fill_rect(B[0]/3*20+x,B[1]/3*20+y,21,k(B[2])*20+1)
		else:A.set_color(*B)
def BY(height):
	A=height
	if A<=1:A+=a.randint(0,1)
	elif A>=6:A-=a.randint(0,1)
	else:A+=a.randint(-1,1)
	return A
def A_(world,tree):
	if world[tree+500].count(0)>4:return E
	return D
def BZ(world):
	C=world;B=D
	while not B:
		A=[a.randint(-498,499)]
		if A_(C,A[0]):B=E
	for G in F(1,80):
		B=D
		while not B:
			A.append(a.randint(-498,499));I=E
			for J in F(H(A)-1):
				if k(A[G]-A[J])<=5:I=D
			if A_(C,A[G])and I:B=E
			if not B:A.pop()
	return A
def Ba(world,trees):
	A=world
	for C in trees:
		D=A[C+500].count(0)
		for B in F(1,3):A[C+500][D-B]=4
		for B in F(3,5):A[C+500][D-B]=6
		for B in F(-1,2,2):A[C-B+500][D-3]=6
	return A
def f(almighty_list):
	B=almighty_list;L=D;M=19;A.set_color(*Q);A.fill_rect(-1,-1,321,211);N=B[0][0]
	if B[0][1]==0:M=18
	elif B[0][2]==0:L=E
	for J in F(-6,7):
		C=17;G=287+(J*24-144);I=N+499+J-B[0][1]*20
		if I>=0 and I<=M:K=3
		else:
			I=N+499+J-B[0][2]*20;K=4
			if L and I==19:K=3;I=0
		for H in B[0][K][I]:
			if H==1:t(G,C,B[1],B[2],B[19])
			elif H==2:u(G,C,B[3],B[4],B[19])
			elif H==3:v(G,C,B[5],B[6],B[19])
			elif H==4:w(G,C,B[7],B[8],B[19])
			elif H==5:z(G,C,B[9],B[10],B[19])
			elif H==6:A0(G,C,B[11],B[12],B[19])
			elif H==7:A1(G,C,B[13],B[14],B[19])
			elif H==8:A2(G,C,B[15],B[16],B[19])
			elif H==9:A3(G,C,B[17],B[18],B[19])
			C+=24
def B0(almighty_list,dir):
	B=almighty_list;P=19;R=19;T=B[0][0]
	if B[0][1]==0:R=18
	elif B[0][2]==0:P=18
	for S in F(-6,7):
		O=D;K=0;I=17;J=287+(S*24-144);G=T+499+S-B[0][1]*20
		if G>0 and G<R:L=3
		elif G==0 or G==R:L=3;O=E;M=4
		else:
			G=T+499+S-B[0][2]*20;L=4
			if P<G:L=3;O=E;M=4;G=0
			elif G==0 or G==P:O=E;M=3
		for C in B[0][L][G]:
			N=E
			if not O:
				if C==B[0][L][G+dir][K]:N=D
			elif G==0:
				if dir==1:
					if C==B[0][M][1][K]:N=D
				elif C==B[0][M][H(B[0][M])-1][K]:N=D
			elif dir==1:
				if C==B[0][M][0][K]:N=D
			elif C==B[0][L][G-1][K]:N=D
			if N:
				if C==0:A.set_color(*Q);A.fill_rect(J,I,25,25)
				elif C==1:t(J,I,B[1],B[2],B[19])
				elif C==2:u(J,I,B[3],B[4],B[19])
				elif C==3:v(J,I,B[5],B[6],B[19])
				elif C==4:w(J,I,B[7],B[8],B[19])
				elif C==5:z(J,I,B[9],B[10],B[19])
				elif C==6:A0(J,I,B[11],B[12],B[19])
				elif C==7:A1(J,I,B[13],B[14],B[19])
				elif C==8:A2(J,I,B[15],B[16],B[19])
				elif C==9:A3(J,I,B[17],B[18],B[19])
			I+=24;K+=1
def g(x,y,block,almighty_list):
	C=block;B=almighty_list
	if C==0:A.set_color(*Q);A.fill_rect(x,y,25,25)
	elif C==1:t(x,y,B[1],B[2],B[19])
	elif C==2:u(x,y,B[3],B[4],B[19])
	elif C==3:v(x,y,B[5],B[6],B[19])
	elif C==4:w(x,y,B[7],B[8],B[19])
	elif C==5:z(x,y,B[9],B[10],B[19])
	elif C==6:A0(x,y,B[11],B[12],B[19])
	elif C==7:A1(x,y,B[13],B[14],B[19])
	elif C==8:A2(x,y,B[15],B[16],B[19])
	elif C==9:A3(x,y,B[17],B[18],B[19])
def j(x,y):A.set_color(*BI);A.fill_rect(x,y,10,4);A.fill_rect(x,y+3,4,7);A.fill_rect(x+15,y,10,4);A.fill_rect(x+21,y+3,4,7);A.fill_rect(x,y+21,10,4);A.fill_rect(x,y+15,4,7);A.fill_rect(x+15,y+21,10,4);A.fill_rect(x+21,y+15,4,7)
def B1(menu_select,prev):
	B=menu_select;A.set_color(*AH)
	if B==1:A.fill_rect(131,171,58,5);A.fill_rect(184,175,5,20);A.fill_rect(131,194,58,5);A.fill_rect(131,175,5,20)
	elif B==0:A.fill_rect(16,171,98,5);A.fill_rect(109,175,5,20);A.fill_rect(16,194,98,5);A.fill_rect(16,175,5,20)
	else:A.fill_rect(206,171,98,5);A.fill_rect(299,175,5,20);A.fill_rect(206,194,98,5);A.fill_rect(206,175,5,20)
	A.set_color(*AF)
	if prev==1:A.fill_rect(131,171,58,5);A.fill_rect(184,175,5,20);A.fill_rect(131,194,58,5);A.fill_rect(131,175,5,20)
	elif prev==0:A.fill_rect(16,171,98,5);A.fill_rect(109,175,5,20);A.fill_rect(16,194,98,5);A.fill_rect(16,175,5,20)
	else:A.fill_rect(206,171,98,5);A.fill_rect(299,175,5,20);A.fill_rect(206,194,98,5);A.fill_rect(206,175,5,20)
def Bb():
	B=D
	while not B:
		try:
			A=x(input('Where do you want to go(-490 to 490): '))
			if A>-491 and A<491:B=E
			else:I('Wrong number')
		except:I('Wrong input')
	return A
B=i(y)
if B is not L:I('Loading world...');B=AJ()
else:
	I('Creating your world...');K=0;B=[0];B9=E
	for d in F(-499,500):
		T=[];A5=BY(A5)
		for Bh in F(8-A5):T.append(0)
		T.append(1)
		if 8-H(T)>2:
			for Bc in F(2):T.append(2)
			for Bi in F(8-H(T)):T.append(3)
		else:
			for Bc in F(8-H(T)):T.append(2)
		B.append(T)
	I('Generating trees');Bd=BZ(B);B=Ba(B,Bd);I('Saving');B=BU(B);I('Doing something')
	for d in F(10):
		B2=A4;B2+=Y(d);AL=D
		while not AL:
			AL=AI(B[d],B2)
			if not AL:l.sleep(3)
	I('Saved!!');B=AJ()
K=B[0]
J=[B,Ar,BL,As,BM,At,BN,Au,BO,Av,BP,Ay,BQ,Aw,BR,Ax,BS,r,BT,S]
while E:
	if n:Az(-1,-1,r);Az(159,-1,r);A.set_color(*AF);A.fill_rect(-1,159,321,51);A.set_color(*AH);A.fill_rect(131,171,58,28);A.set_color(*BJ);A.fill_rect(20,175,90,20);A.fill_rect(135,175,50,20);A.fill_rect(210,175,90,20);A.set_color(*AH);A.draw_text(25,196,'Tutorial');A.draw_text(140,196,'Play');A.draw_text(218,196,'Nothing');n=D
	G=W.get_key(1)
	if G==45:break
	elif G==105:
		if R==1:A6=E;f(J);break
		elif R==0:
			B3=E
			while B3:
				n=E;A.clear();A.draw_text(10,20,'Welcome to Minecraft in TI');A.draw_text(10,40,'Press clear to go back');A.draw_text(10,60,'Use the arrows to move');A.draw_text(10,80,'Toolbox:');A.draw_text(10,100,'0-2, set graphics:');A.draw_text(10,120,'0: one color');A.draw_text(10,140,'1:4x4');A.draw_text(10,160,'2:8x8(takes a long time)');A.draw_text(10,180,'Enter for next page');Be=W.get_key(1)
				if G==45:break
				elif G==105:A.clear();A.draw_text(10,20,'3: change time(night/day)');A.draw_text(10,40,'4: tp(enter coodrinate and press enter');A.draw_text(10,60,'5: Build:');A.draw_text(10,80,'Arrows to move');A.draw_text(10,100,'0-9 to change block');A.draw_text(10,120,'Enter to build');A.draw_text(10,140,'Clear to stop');A.draw_text(10,160,'Press any key to get back');Be=W.get_key(1);B3=D
		else:
			A.clear();X=a.randint(0,9)
			for M in F(-1,320,24):
				for P in F(-1,210,24):
					if X==0:BX(M,P,BK,L,2)
					elif X==1:t(M,P,Ar,L,2)
					elif X==2:u(M,P,As,L,2)
					elif X==3:v(M,P,At,L,2)
					elif X==4:w(M,P,Au,L,2)
					elif X==5:z(M,P,Av,L,2)
					elif X==6:A0(M,P,Ay,L,2)
					elif X==7:A1(M,P,Aw,L,2)
					elif X==8:A2(M,P,Ax,L,2)
					else:A3(M,P,r,L,2)
			Bf=W.get_key(1);n=E;R=1;Bf=L
	elif G==26:
		if R<2:B1(R+1,R);R+=1
	elif G==24:
		if R>0:B1(R-1,R);R-=1
while A6:
	G=W.get_key(1)
	if G==45:e(B[3],B[1]);e(B[4],B[2]);BW(K);A.clear();A6=D;break
	elif G==26:
		if K!=493:
			K+=1;B[0]=K
			if B[1]>B[2]:
				if s(K,E,B[1]):e(B[4],B[2]);B[2]=B[1]+1;B[4]=Z(B[2])
			elif s(K,E,B[2]):e(B[3],B[1]);B[1]=B[2]+1;B[3]=Z(B[1])
			J[0]=B;B0(J,-1)
			if b:A.set_color(*Q);A.fill_rect(23,0,280,18);b=D
		else:A.set_color(0,0,0);A.draw_text(24,20,B8);b=E
	elif G==24:
		if K!=-493:
			K-=1;B[0]=K
			if B[1]<B[2]:
				if s(K,D,B[1]):e(B[4],B[2]);B[2]=B[1]-1;B[4]=Z(B[2])
			elif s(K,D,B[2]):e(B[3],B[1]);B[1]=B[2]-1;B[3]=Z(B[1])
			J[0]=B;B0(J,1)
			if b:A.set_color(*Q);A.fill_rect(23,0,280,18);b=D
		else:A.set_color(0,0,0);A.draw_text(24,20,B8);b=E
	elif G==83:
		A7=E;C=[7,4];C.append(AK(K+C[0]-7,B[1],B[2]));N=(C[0]-1)*24-1;O=24*C[1]+17
		while A7:
			j(N,O);G=W.get_key(1)
			if G==45:A7=D;g(N,O,B[C[2][0]][C[2][1]][C[1]],J)
			elif G==26:
				if C[0]!=13:g(N,O,B[C[2][0]][C[2][1]][C[1]],J);C[0]+=1;C[2]=AK(K+C[0]-7,B[1],B[2]);N+=24;j(N,O)
			elif G==24:
				if C[0]!=1:g(N,O,B[C[2][0]][C[2][1]][C[1]],J);C[0]-=1;C[2]=AK(K+C[0]-7,B[1],B[2]);N-=24;j(N,O)
			elif G==25:
				if C[1]!=0:g(N,O,B[C[2][0]][C[2][1]][C[1]],J);C[1]-=1;O-=24;j(N,O)
			elif G==34:
				if C[1]!=7:g(N,O,B[C[2][0]][C[2][1]][C[1]],J);C[1]+=1;O+=24;j(N,O)
			else:
				for B4 in AQ:
					if G==B4:B[C[2][0]][C[2][1]][C[1]]=AQ.index(B4);g(N,O,B[C[2][0]][C[2][1]][C[1]],J)
	elif G==102:
		if S!=0:S=0;J[19]=S;f(J)
	elif G==92:
		if S!=1:S=1;J[19]=S;f(J)
	elif G==93:
		if S!=2:S=2;J[19]=S;f(J)
	elif G==94:
		if Q==AG:Q=AF
		else:Q=AG
		f(J)
	elif G==82:K=Bb();B=AJ(K);J[0]=B;f(J)
I('Console: Info: Program stopped succesfully')