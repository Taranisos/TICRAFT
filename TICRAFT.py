AI='You reached the world border'
AH=' blocks too mutch, deleting highest ones.'
AG=' is corrupted and has '
AF='Console: Warning: chunk corruption, chunk '
y=' blocks, filling in with air.'
x=' is corrupted and misses '
w='Console: Warning chunk corruption, chunk '
i='MCWD'
h='MCWD0'
g=int
a=None
V=str
I=len
G=print
F=range
E=True
D=False
import ti_draw as A,time as d,random as X,ti_system as O,math as e,ti_graphics as P
j=4
k=D
l=D
AJ=D
N=[]
Y=D
z=[102,92,93,94,82,83,84,72,73,74]
M=1
m=E
AK=0,0,0
AL=111,110,113
n=5,23,52
o=130,172,255
Q=o
p=255,255,255
def b(world):
	try:return O.recall_list(world)
	except Exception:return
def q(world,saving):
	try:O.store_list(saving,world);return E
	except:return D
def AM(world):
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
						G(w,B,x,8-I(A),y)
						for N in F(8-I(A)):A.append(0)
					else:
						G(AF,B,AG,I(A)-8,AH)
						for N in F(I(A)-8):A.pop(0)
				J='1'
				for O in F(8):J+=V(A[7-O])
				H.append(g(J))
		M.append(H)
	if L:G('Console: Info: world saved succesfully!');d.sleep(3)
	return M
def r(player_x=a):
	C=player_x;H=b(h);L=D;I=D;F=D;B=[]
	if C==a:C=H[0]
	B.append(C);A=e.floor((C+499)/20)
	if abs(C+401)>5:
		if C-(A*20-499)<10 or A==49:F=E
		M=e.floor(A/5);J=i;J+=V(M);B.append(A);H=b(J);N=W(A)
		if not F:I=E
		if I:B.append(A+1);K=W(A+1)
		elif F:B.append(A-1);K=W(A-1)
	if L:G('Console: Info: world loaded succesfully!');d.sleep(3)
	B.append(N);B.append(K);return B
def AN(start,world,end):
	C=world;D=[]
	for B in F(start,end):
		H=[];A=V(C[B])
		if I(A)<9:
			G(A);G(C[B]);d.sleep(3);K=E;G(w,B-50,x,9-I(A),y)
			for L in F(9-I(A)):A+='0'
		for J in F(1,9):H.append(g(A[9-J]))
		D.append(H)
	return D
def W(chunk):
	A=chunk;C=e.floor(A/5);D=i;D+=V(C);B=20*(A-C*5);F=b(D)
	if A==0:B=1;E=20
	else:E=B+20
	A=AN(B,F,E);return A
def Z(chunk,chunk_x):
	B=chunk_x;L=e.floor(B/5);D=i;D+=V(L);Q=B-L*5;M=[]
	for R in chunk:
		A=R;N='1'
		if I(A)!=8:
			T=E
			if I(A)<8:
				G(w,B,x,8-I(A),y)
				for S in F(8-I(A)):A.append(0)
			else:
				G(AF,B,AG,I(A)-8,AH)
				for S in F(I(A)-8):A.pop(0)
		for H in F(8):N+=V(A[7-H])
		M.append(g(N))
	try:C=O.recall_list(D)
	except:C=a;G('Failed to save chunk')
	if C is not a:
		J=Q*20;K=0
		if B!=0:P=J+20
		else:J=1;K=0;P=20
		for H in F(J,P):C[H]=M[K];K+=1
	q(C,D)
def AO(player_x):A=b(h);A[0]=player_x;q(A,h)
def f(player_x,dir,chunk):
	B=chunk;A=player_x;A-=B*20-499;A=V(A)
	if B==0:return D
	elif dir:
		if A=='10':return E
	elif A=='8':return E
	return D
def s(x,chunk1,chunk2):
	C=chunk2;B=chunk1;D=19
	if B==0:D=18
	A=x+499-B*20
	if A>=0 and A<=D:list=[3,A]
	else:
		A=x+499-C*20;list=[4,A]
		if A==19 and C==0:list=[3,0]
	return list
def A0(x,y):P.drawImage('MCGRS',x,y)
def A1(x,y):P.drawImage('MCDRT',x,y)
def A2(x,y):P.drawImage('MCSTN',x,y)
def A3(x,y):P.drawImage('MCOKL',x,y)
def A4(x,y):P.drawImage('MCOKP',x,y)
def A5(x,y):A.set_color(*Q);A.fill_rect(x-1,y-31,17,17);P.drawImage('MCOKV',x,y)
def A6(x,y):A.set_color(*Q);A.fill_rect(x-1,y-31,17,17);P.drawImage('MCGLS',x,y)
def A7(x,y):P.drawImage('MCSND',x,y)
def A8(x,y):P.drawImage('MCWTR',x,y)
def AP(height):
	A=height
	if A<=1:A+=X.randint(0,1)
	elif A>=6:A-=X.randint(0,1)
	else:A+=X.randint(-1,1)
	return A
def A9(world,tree):
	if world[tree+500].count(0)>4:return E
	return D
def AQ(world):
	C=world;B=D
	while not B:
		A=[X.randint(-498,499)]
		if A9(C,A[0]):B=E
	for G in F(1,80):
		B=D
		while not B:
			A.append(X.randint(-498,499));H=E
			for J in F(I(A)-1):
				if abs(A[G]-A[J])<=5:H=D
			if A9(C,A[G])and H:B=E
			if not B:A.pop()
	return A
def AR(world,trees):
	A=world
	for C in trees:
		D=A[C+500].count(0)
		for B in F(1,3):A[C+500][D-B]=4
		for B in F(3,5):A[C+500][D-B]=6
		for B in F(-1,2,2):A[C-B+500][D-3]=6
	return A
def t(world):
	B=world;I=D;J=19;A.set_color(*Q);A.fill_rect(-1,-1,321,211);K=B[0]
	if B[1]==0:J=18
	elif B[2]==0:I=E
	for G in F(-9,11):
		L=112;M=144+G*16;C=K+499+G-B[1]*20
		if C>=0 and C<=J:H=3
		else:
			C=K+499+G-B[2]*20;H=4
			if I and C==19:H=3;C=0
		for N in B[H][C]:T(M,L,N);L+=16
def AA(world,dir):
	B=world;M=19;N=19;P=B[0]
	if B[1]==0:N=18
	elif B[2]==0:M=18
	for O in F(-9,11):
		L=D;G=0;Q=112;R=144+O*16;A=P+499+O-B[1]*20
		if A>0 and A<N:C=3
		elif A==0 or A==N:C=3;L=E;K=4
		else:
			A=P+499+O-B[2]*20;C=4
			if M<A:C=3;L=E;K=4;A=0
			elif A==0 or A==M:L=E;K=3
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
			if J:T(R,Q,H)
			Q+=16;G+=1
def T(x,y,block):
	B=block
	if B==0:A.set_color(*Q);A.fill_rect(x-1,y-31,17,17)
	elif B==1:A0(x,y)
	elif B==2:A1(x,y)
	elif B==3:A2(x,y)
	elif B==4:A3(x,y)
	elif B==5:A4(x,y)
	elif B==6:A5(x,y)
	elif B==7:A6(x,y)
	elif B==8:A7(x,y)
	elif B==9:A8(x,y)
def c(x,y):A.set_color(*AK);A.fill_rect(x,y,7,3);A.fill_rect(x,y+2,3,5);A.fill_rect(x+10,y,7,3);A.fill_rect(x+14,y+2,3,5);A.fill_rect(x,y+14,7,3);A.fill_rect(x,y+10,3,5);A.fill_rect(x+10,y+14,5,3);A.fill_rect(x+14,y+10,3,7)
def AB(menu_select,prev):
	B=menu_select;A.set_color(*p)
	if B==1:A.fill_rect(131,171,58,5);A.fill_rect(184,175,5,20);A.fill_rect(131,194,58,5);A.fill_rect(131,175,5,20)
	elif B==0:A.fill_rect(16,171,98,5);A.fill_rect(109,175,5,20);A.fill_rect(16,194,98,5);A.fill_rect(16,175,5,20)
	else:A.fill_rect(206,171,98,5);A.fill_rect(299,175,5,20);A.fill_rect(206,194,98,5);A.fill_rect(206,175,5,20)
	A.set_color(*n)
	if prev==1:A.fill_rect(131,171,58,5);A.fill_rect(184,175,5,20);A.fill_rect(131,194,58,5);A.fill_rect(131,175,5,20)
	elif prev==0:A.fill_rect(16,171,98,5);A.fill_rect(109,175,5,20);A.fill_rect(16,194,98,5);A.fill_rect(16,175,5,20)
	else:A.fill_rect(206,171,98,5);A.fill_rect(299,175,5,20);A.fill_rect(206,194,98,5);A.fill_rect(206,175,5,20)
def AS():
	B=D
	while not B:
		try:
			A=g(input('Where do you want to go(-485 to 485): '))
			if A>-486 and A<486:B=E
			else:G('Wrong number')
		except:G('Wrong input')
	return A
B=b(h)
if B is not a:G('Loading world...');B=r()
else:
	G('Creating your world...');J=0;B=[0];AJ=E
	for u in F(-499,500):
		N=[];j=AP(j)
		for AX in F(8-j):N.append(0)
		N.append(1)
		if 8-I(N)>2:
			for AT in F(2):N.append(2)
			for AY in F(8-I(N)):N.append(3)
		else:
			for AT in F(8-I(N)):N.append(2)
		B.append(N)
	G('Generating trees');AU=AQ(B);B=AR(B,AU);G('Saving');B=AM(B);G('Doing something')
	for u in F(10):
		AC=i;AC+=V(u);v=D
		while not v:
			v=q(B[u],AC)
			if not v:d.sleep(3)
	G('Saved!!');B=r()
J=B[0]
while E:
	if m:A.set_color(*n);A.fill_rect(-1,158,321,52);A.set_color(*p);A.fill_rect(131,171,58,28);A.set_color(*AL);A.fill_rect(20,175,90,20);A.fill_rect(135,175,50,20);A.fill_rect(210,175,90,20);A.set_color(*p);A.draw_text(25,196,'Tutorial');A.draw_text(140,196,'Play');A.draw_text(218,196,'Nothing');m=D
	H=O.get_key(1)
	if H==45:break
	elif H==105:
		if M==1:k=E;t(B);break
		elif M==0:
			AD=E
			while AD:
				m=E;A.clear();A.draw_text(10,20,'Welcome to Minecraft in TI');A.draw_text(10,40,'Press clear to go back');A.draw_text(10,60,'Use the arrows to move');A.draw_text(10,80,'Toolbox:');A.draw_text(10,100,'0: tp(enter coodrinate and press enter');A.draw_text(10,120,'2: change time(night/day)');A.draw_text(10,140,'Enter for next page');AV=O.get_key(1)
				if H==45:break
				elif H==105:A.clear();A.draw_text(10,20,'5: Build:');A.draw_text(10,40,'Arrows to move');A.draw_text(10,60,'0-9 to change block');A.draw_text(10,80,'Enter to build');A.draw_text(10,100,'Clear to stop');A.draw_text(10,120,'Press any key to get back');AV=O.get_key(1);AD=D;M=1
		else:
			A.clear();U=X.randint(0,8)
			for R in F(0,320,16):
				for S in F(30,240,16):
					if U==0:A7(R,S)
					elif U==1:A0(R,S)
					elif U==2:A1(R,S)
					elif U==3:A2(R,S)
					elif U==4:A3(R,S)
					elif U==5:A4(R,S)
					elif U==6:A5(R,S)
					elif U==7:A6(R,S)
					else:A8(R,S)
			AW=O.get_key(1);M=1;AW=a
	elif H==26:
		if M<2:AB(M+1,M);M+=1
	elif H==24:
		if M>0:AB(M-1,M);M-=1
while k:
	H=O.get_key(1)
	if H==45:Z(B[3],B[1]);Z(B[4],B[2]);AO(J);A.clear();k=D;break
	elif H==26:
		if J!=489:
			J+=1;B[0]=J
			if B[1]>B[2]:
				if f(J,E,B[1]):Z(B[4],B[2]);B[2]=B[1]+1;B[4]=W(B[2])
			elif f(J,E,B[2]):Z(B[3],B[1]);B[1]=B[2]+1;B[3]=W(B[1])
			B=B;AA(B,-1)
			if Y:A.set_color(*Q);A.fill_rect(23,0,280,18);Y=D
		else:A.set_color(0,0,0);A.draw_text(24,20,AI);Y=E
	elif H==24:
		if J!=-488:
			J-=1;B[0]=J
			if B[1]<B[2]:
				if f(J,D,B[1]):Z(B[4],B[2]);B[2]=B[1]-1;B[4]=W(B[2])
			elif f(J,D,B[2]):Z(B[3],B[1]);B[1]=B[2]-1;B[3]=W(B[1])
			B=B;AA(B,1)
			if Y:A.set_color(*Q);A.fill_rect(23,0,280,18);Y=D
		else:A.set_color(0,0,0);A.draw_text(24,20,AI);Y=E
	elif H==92:
		l=E;C=[9,4];C.append(s(J+C[0]-9,B[1],B[2]));K=144;L=176
		while l:
			c(K-1,L-31);H=O.get_key(1)
			if H==45:l=D;T(K,L,B[C[2][0]][C[2][1]][C[1]])
			elif H==26:
				if C[0]!=19:T(K,L,B[C[2][0]][C[2][1]][C[1]]);C[0]+=1;C[2]=s(J+C[0]-9,B[1],B[2]);K+=16;c(K-1,L-31)
			elif H==24:
				if C[0]!=0:T(K,L,B[C[2][0]][C[2][1]][C[1]]);C[0]-=1;C[2]=s(J+C[0]-9,B[1],B[2]);K-=16;c(K-1,L-31)
			elif H==25:
				if C[1]!=0:T(K,L,B[C[2][0]][C[2][1]][C[1]]);C[1]-=1;L-=16;c(K-1,L-31)
			elif H==34:
				if C[1]!=7:T(K,L,B[C[2][0]][C[2][1]][C[1]]);C[1]+=1;L+=16;c(K-1,L-31)
			else:
				for AE in z:
					if H==AE:B[C[2][0]][C[2][1]][C[1]]=z.index(AE);T(K,L,B[C[2][0]][C[2][1]][C[1]])
	elif H==102:J=AS();B=r(J);B=B;t(B)
	elif H==93:
		if Q==o:Q=n
		else:Q=o
		t(B)
G('Console: Info: Program stopped succesfully')