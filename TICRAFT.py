AN='You reached the world border'
AM=' blocks too mutch, deleting highest ones.'
AL=' is corrupted and has '
AK='Console: Warning: chunk corruption, chunk '
A2=' blocks, filling in with air.'
A1=' is corrupted and misses '
A0='Console: Warning chunk corruption, chunk '
k='MCWD'
j='MCWD0'
b=None
X=int
U=str
I=len
G=print
F=range
E=True
D=False
import ti_draw as A,time as e,random as Y,ti_system as O,math as f,ti_graphics as P
l=4
m=D
n=D
AO=D
N=[]
Z=D
A3=[102,92,93,94,82,83,84,72,73,74]
M=1
g=E
o=E
AP=0,0,0
AQ=111,110,113
p=5,23,52
q=130,172,255
Q=q
r=255,255,255
s=9999999881
h=9999999988
t=9999999998
A4=9999988812
AR=[9888812222,9998881222,9999881222,9999988122,9999998812,s,s,h,h,h,t,t,t,h,s,9999998881,A4,A4,9999888122,9988812222]
def c(world):
	try:return O.recall_list(world)
	except Exception:return
def u(world,saving):
	try:O.store_list(saving,world);return E
	except:return D
def AS(world):
	K=world;G('Changing to save format.');L=D;M=[];B=-500
	for C in F(0,1000,100):
		G('Formatting world ',round((C+1)/100)+1,'/ 10.');H=[]
		for list in F(100):
			if C+list==0:H.append(K[0])
			else:
				B+=1;A=K[C+list];J=''
				if I(A)!=8:
					L=E
					if I(A)<8:
						G(A0,B,A1,8-I(A),A2)
						for N in F(8-I(A)):A.append(0)
					else:
						G(AK,B,AL,I(A)-8,AM)
						for N in F(I(A)-8):A.pop(0)
				J='1'
				for O in F(8):J+=U(A[7-O])
				H.append(X(J))
		M.append(H)
	if L:G('Console: Info: world saved succesfully!');e.sleep(3)
	return M
def v(player_x=b):
	C=player_x;H=c(j);L=D;I=D;F=D;B=[]
	if C==b:C=H[0]
	B.append(C);A=f.floor((C+499)/20)
	if C-(A*20-499)<10 or A==49:F=E
	M=f.floor(A/5);J=k;J+=U(M);B.append(A);H=c(J);N=W(A)
	if not F:I=E
	if I:B.append(A+1);K=W(A+1)
	elif F:B.append(A-1);K=W(A-1)
	if L:G('Console: Info: world loaded succesfully!');e.sleep(3)
	B.append(N);B.append(K);return B
def AT(start,world,end):
	C=world;D=[]
	for B in F(start,end):
		H=[];A=U(C[B])
		if I(A)<9:
			G(A);G(C[B]);e.sleep(3);K=E;G(A0,B-50,A1,9-I(A),A2)
			for L in F(9-I(A)):A+='0'
		for J in F(1,9):H.append(X(A[9-J]))
		D.append(H)
	return D
def W(chunk):
	A=chunk;C=f.floor(A/5);D=k;D+=U(C);B=20*(A-C*5);F=c(D)
	if A==0:B=1;E=20
	else:E=B+20
	A=AT(B,F,E);return A
def a(chunk,chunk_x):
	B=chunk_x;L=f.floor(B/5);D=k;D+=U(L);Q=B-L*5;M=[]
	for R in chunk:
		A=R;N='1'
		if I(A)!=8:
			T=E
			if I(A)<8:
				G(A0,B,A1,8-I(A),A2)
				for S in F(8-I(A)):A.append(0)
			else:
				G(AK,B,AL,I(A)-8,AM)
				for S in F(I(A)-8):A.pop(0)
		for H in F(8):N+=U(A[7-H])
		M.append(X(N))
	try:C=O.recall_list(D)
	except:C=b;G('Failed to save chunk')
	if C is not b:
		J=Q*20;K=0
		if B!=0:P=J+20
		else:J=1;K=0;P=20
		for H in F(J,P):C[H]=M[K];K+=1
	u(C,D)
def AU(player_x):A=c(j);A[0]=player_x;u(A,j)
def i(player_x,dir,chunk):
	B=chunk;A=player_x;A-=B*20-499;A=U(A)
	if B==0:return D
	elif dir:
		if A=='10':return E
	elif A=='8':return E
	return D
def w(x,chunk1,chunk2):
	C=chunk2;B=chunk1;D=19
	if B==0:D=18
	A=x+499-B*20
	if A>=0 and A<=D:list=[3,A]
	else:
		A=x+499-C*20;list=[4,A]
		if A==19 and C==0:list=[3,0]
	return list
def A5(x,y):P.drawImage('MCGRS',x,y)
def A6(x,y):P.drawImage('MCDRT',x,y)
def A7(x,y):P.drawImage('MCSTN',x,y)
def A8(x,y):P.drawImage('MCOKL',x,y)
def A9(x,y):P.drawImage('MCOKP',x,y)
def AA(x,y):A.set_color(*Q);A.fill_rect(x-1,y-31,17,17);P.drawImage('MCOKV',x,y)
def AB(x,y):A.set_color(*Q);A.fill_rect(x-1,y-31,17,17);P.drawImage('MCGLS',x,y)
def AC(x,y):P.drawImage('MCSND',x,y)
def AD(x,y):P.drawImage('MCWTR',x,y)
def AV(height):
	A=height
	if A<=1:A+=Y.randint(0,1)
	elif A>=6:A-=Y.randint(0,1)
	else:A+=Y.randint(-1,1)
	return A
def AE(world,tree):
	if world[tree+500].count(0)>4:return E
	return D
def AW(world):
	C=world;B=D
	while not B:
		A=[Y.randint(-498,499)]
		if AE(C,A[0]):B=E
	for G in F(1,80):
		B=D
		while not B:
			A.append(Y.randint(-498,499));H=E
			for J in F(I(A)-1):
				if abs(A[G]-A[J])<=5:H=D
			if AE(C,A[G])and H:B=E
			if not B:A.pop()
	return A
def AX(world,trees):
	A=world
	for C in trees:
		D=A[C+500].count(0)
		for B in F(1,3):A[C+500][D-B]=4
		for B in F(3,5):A[C+500][D-B]=6
		for B in F(-1,2,2):A[C-B+500][D-3]=6
	return A
def x(world):
	B=world;I=D;J=19;A.set_color(*Q);A.fill_rect(-1,-1,321,211);K=B[0]
	if B[1]==0:J=18
	elif B[2]==0:I=E
	for G in F(-9,11):
		L=112;M=144+G*16;C=K+499+G-B[1]*20
		if C>=0 and C<=J:H=3
		else:
			C=K+499+G-B[2]*20;H=4
			if I and C==19:H=3;C=0
		for N in B[H][C]:R(M,L,N);L+=16
def AF(world,dir):
	B=world;M=19;N=19;P=B[0]
	if B[1]==0:N=18
	elif B[2]==0:M=18
	for O in F(-9,11):
		L=D;G=0;Q=112;S=144+O*16;A=P+499+O-B[1]*20
		if A>0 and A<N:C=3
		elif A==0 or A==N:C=3;L=E;K=4
		else:
			A=P+499+O-B[2]*20;C=4
			if A==0 or A==M:L=E;K=3
			elif M<A:C=3;L=E;K=4;A=0
		for H in B[C][A]:
			J=E
			if not L:
				if H==B[C][A+dir][G]:J=D
			elif A==0:
				if dir==1:
					if H==B[C][1][G]:J=D
				elif H==B[K][I(B[K])-1][G]:J=D
			elif dir==1:
				if H==B[K][0][G]:J=D
			elif H==B[C][A-1][G]:J=D
			if J:R(S,Q,H)
			Q+=16;G+=1
def R(x,y,block):
	B=block
	if B==0:A.set_color(*Q);A.fill_rect(x-1,y-31,17,17)
	elif B==1:A5(x,y)
	elif B==2:A6(x,y)
	elif B==3:A7(x,y)
	elif B==4:A8(x,y)
	elif B==5:A9(x,y)
	elif B==6:AA(x,y)
	elif B==7:AB(x,y)
	elif B==8:AC(x,y)
	elif B==9:AD(x,y)
def d(x,y):A.set_color(*AP);A.fill_rect(x,y,7,3);A.fill_rect(x,y+2,3,5);A.fill_rect(x+10,y,7,3);A.fill_rect(x+14,y+2,3,5);A.fill_rect(x,y+14,7,3);A.fill_rect(x,y+10,3,5);A.fill_rect(x+10,y+14,5,3);A.fill_rect(x+14,y+10,3,7)
def AY(sea):
	for B in F(0,305,16):
		A=sea[X(B/16)]
		for C in F(30,175,16):A=U(A);R(B,C,X(A[X(C/16)-1]))
def AG(menu_select,prev):
	B=menu_select;A.set_color(*r)
	if B==1:A.fill_rect(131,171,58,5);A.fill_rect(184,175,5,20);A.fill_rect(131,194,58,5);A.fill_rect(131,175,5,20)
	elif B==0:A.fill_rect(16,171,98,5);A.fill_rect(109,175,5,20);A.fill_rect(16,194,98,5);A.fill_rect(16,175,5,20)
	else:A.fill_rect(206,171,98,5);A.fill_rect(299,175,5,20);A.fill_rect(206,194,98,5);A.fill_rect(206,175,5,20)
	A.set_color(*p)
	if prev==1:A.fill_rect(131,171,58,5);A.fill_rect(184,175,5,20);A.fill_rect(131,194,58,5);A.fill_rect(131,175,5,20)
	elif prev==0:A.fill_rect(16,171,98,5);A.fill_rect(109,175,5,20);A.fill_rect(16,194,98,5);A.fill_rect(16,175,5,20)
	else:A.fill_rect(206,171,98,5);A.fill_rect(299,175,5,20);A.fill_rect(206,194,98,5);A.fill_rect(206,175,5,20)
def AZ():
	B=D
	while not B:
		try:
			A=X(input('Where do you want to go(-485 to 485): '))
			if A>-486 and A<486:B=E
			else:G('Wrong number')
		except:G('Wrong input')
	return A
B=c(j)
if B is not b:G('Loading world...');B=v()
else:
	G('Creating your world...');J=0;B=[0];AO=E
	for y in F(-499,500):
		N=[];l=AV(l)
		for Ae in F(8-l):N.append(0)
		N.append(1)
		if 8-I(N)>2:
			for Aa in F(2):N.append(2)
			for Af in F(8-I(N)):N.append(3)
		else:
			for Aa in F(8-I(N)):N.append(2)
		B.append(N)
	G('Generating trees');Ab=AW(B);B=AX(B,Ab);G('Saving');B=AS(B);G('Doing something')
	for y in F(10):
		AH=k;AH+=U(y);z=D
		while not z:
			z=u(B[y],AH)
			if not z:e.sleep(3)
	G('Saved!!');B=v()
J=B[0]
while E:
	if g:
		if o:AY(AR)
		A.set_color(*p);A.fill_rect(-1,158,321,52);A.set_color(*r);A.fill_rect(131,171,58,28);A.set_color(*AQ);A.fill_rect(20,175,90,20);A.fill_rect(135,175,50,20);A.fill_rect(210,175,90,20);A.set_color(*r);A.draw_text(25,196,'Tutorial');A.draw_text(140,196,'Play');A.draw_text(218,196,'Nothing');g=D;o=D
	H=O.get_key(1)
	if H==45:break
	elif H==105:
		if M==1:m=E;x(B);break
		elif M==0:
			AI=E
			while AI:
				A.clear();A.draw_text(10,20,'Welcome to Minecraft in TI');A.draw_text(10,40,'Press clear to go back');A.draw_text(10,60,'Use the arrows to move');A.draw_text(10,80,'Toolbox:');A.draw_text(10,100,'0: tp(enter coodrinate and press enter');A.draw_text(10,120,'2: change time(night/day)');A.draw_text(10,140,'Enter for next page');g=E;o=E;Ac=O.get_key(1)
				if H==45:break
				elif H==105:A.clear();A.draw_text(10,20,'1: Build:');A.draw_text(10,40,'Arrows to move');A.draw_text(10,60,'0-9 to build');A.draw_text(10,80,'Clear to stop');A.draw_text(10,100,'Press any key to get back');Ac=O.get_key(1);AI=D;M=1
		else:
			A.clear();V=Y.randint(0,8)
			for S in F(0,320,16):
				for T in F(30,240,16):
					if V==0:AC(S,T)
					elif V==1:A5(S,T)
					elif V==2:A6(S,T)
					elif V==3:A7(S,T)
					elif V==4:A8(S,T)
					elif V==5:A9(S,T)
					elif V==6:AA(S,T)
					elif V==7:AB(S,T)
					else:AD(S,T)
			g=E;Ad=O.get_key(1);M=1;Ad=b
	elif H==26:
		if M<2:AG(M+1,M);M+=1
	elif H==24:
		if M>0:AG(M-1,M);M-=1
while m:
	H=O.get_key(1)
	if H==45:a(B[3],B[1]);a(B[4],B[2]);AU(J);A.clear();m=D;break
	elif H==26:
		if J!=489:
			J+=1;B[0]=J
			if B[1]>B[2]:
				if i(J,E,B[1]):a(B[4],B[2]);B[2]=B[1]+1;B[4]=W(B[2])
			elif i(J,E,B[2]):a(B[3],B[1]);B[1]=B[2]+1;B[3]=W(B[1])
			B=B;AF(B,-1)
			if Z:A.set_color(*Q);A.fill_rect(23,0,280,18);Z=D
		else:A.set_color(0,0,0);A.draw_text(24,20,AN);Z=E
	elif H==24:
		if J!=-488:
			J-=1;B[0]=J
			if B[1]<B[2]:
				if i(J,D,B[1]):a(B[4],B[2]);B[2]=B[1]-1;B[4]=W(B[2])
			elif i(J,D,B[2]):a(B[3],B[1]);B[1]=B[2]-1;B[3]=W(B[1])
			B=B;AF(B,1)
			if Z:A.set_color(*Q);A.fill_rect(23,0,280,18);Z=D
		else:A.set_color(0,0,0);A.draw_text(24,20,AN);Z=E
	elif H==92:
		n=E;C=[9,4];C.append(w(J+C[0]-9,B[1],B[2]));K=144;L=176
		while n:
			d(K-1,L-31);H=O.get_key(1)
			if H==45:n=D;R(K,L,B[C[2][0]][C[2][1]][C[1]])
			elif H==26:
				if C[0]!=19:R(K,L,B[C[2][0]][C[2][1]][C[1]]);C[0]+=1;C[2]=w(J+C[0]-9,B[1],B[2]);K+=16;d(K-1,L-31)
			elif H==24:
				if C[0]!=0:R(K,L,B[C[2][0]][C[2][1]][C[1]]);C[0]-=1;C[2]=w(J+C[0]-9,B[1],B[2]);K-=16;d(K-1,L-31)
			elif H==25:
				if C[1]!=0:R(K,L,B[C[2][0]][C[2][1]][C[1]]);C[1]-=1;L-=16;d(K-1,L-31)
			elif H==34:
				if C[1]!=7:R(K,L,B[C[2][0]][C[2][1]][C[1]]);C[1]+=1;L+=16;d(K-1,L-31)
			else:
				for AJ in A3:
					if H==AJ:B[C[2][0]][C[2][1]][C[1]]=A3.index(AJ);R(K,L,B[C[2][0]][C[2][1]][C[1]])
	elif H==102:J=AZ();B=v(J);x(B)
	elif H==93:
		if Q==q:Q=p
		else:Q=q
		x(B)
G('Console: Info: Program stopped succesfully')