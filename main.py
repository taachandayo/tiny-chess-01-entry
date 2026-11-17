import json,os,sys,urllib.request
U=os.getenv("MAKEFUN_ENV_URL")
L=30000
G=0
V={'p':100,'n':320,'b':330,'r':500,'q':900,'k':0}
H=(-21,-19,-12,-8,8,12,19,21)
K=(-11,-10,-9,-1,1,9,10,11)
D={'b':(-11,-9,9,11),'r':(-10,-1,1,10)}
T={'n':(H,0),'k':(K,0),'b':(D['b'],1),'r':(D['r'],1),'q':(D['b']+D['r'],1)}
Y={21:'Q',25:'KQ',28:'K',91:'q',95:'kq',98:'k'}
X=Exception
def p(f):
 p=f.split();b=list('#'*20+'#........#'*8+'#'*20);y=7
 for r in p[0].split('/'):
  x=0
  for c in r:
   if c.isdigit():x+=int(c)
   else:b[21+10*y+x]=c;x+=1
  y-=1
 return b,p[1],-1 if p[3]=='-'else 21+10*(int(p[3][1])-1)+"abcdefgh".index(p[3][0]),set(p[2])-{'-'}
def q(i):return "abcdefgh"[i%10-1]+str(i//10-1)
def A(b,s,w):
 pa,kn,kg,bi,ro,qu='PNKBRQ'if w else'pnkbrq'
 if b[s+9-18*w]==pa or b[s+11-22*w]==pa:return 1
 for d,p in((H,kn),(K,kg)):
  for x in d:
   if b[s+x]==p:return 1
 for ds,x,y in((D['b'],bi,qu),(D['r'],ro,qu)):
  for d in ds:
   i=s+d
   while b[i]=='.':i+=d
   if b[i]in(x,y):return 1
 return 0
def M(o,m):
 b=list(o[0]);s,e=o[1:3];f,t,r=m;p=b[f];b[f]='.'
 if p.lower()=='p'and t==e and t%10!=f%10:b[t-10 if p=='P'else t+10]='.'
 if p in'Kk'and abs(t-f)==2:
  if t>f:b[t-1],b[t+1]=b[t+1],'.'
  else:b[t+1],b[t-2]=b[t-2],'.'
 b[t]=r.upper()if p.isupper()and r else r.lower()if r else p
 e=-1
 if p=='P'and t-f==20:e=f+10
 if p=='p'and f-t==20:e=f-10
 return b,'b'if s=='w'else'w',e,o[3]-set(Y.get(f,'')+Y.get(t,''))
def g(o):
 b,s,e,c=o;w=s=='w';m=[]
 for i,x in enumerate(b):
  if not x.isalpha()or x.isupper()!=w:continue
  t=x.lower();d=10 if w else-10
  if t=='p':
   j=i+d
   if b[j]=='.':
    if j>90 or j<29:m.append((i,j,'q'))
    else:
     m.append((i,j,''))
     if i//10 in(3,8)and b[j+d]=='.':m.append((i,j+d,''))
   for z in(-1,1):
    j=i+d+z;q=b[j]
    if q.isalpha()and q.isupper()!=w:m.append((i,j,'q'if j>90 or j<29 else''))
    elif j==e:m.append((i,j,''))
  else:
   ds,sl=T[t]
   for d in ds:
    j=i+d
    while 1:
     q=b[j]
     if q=='.'or(q.isalpha()and q.isupper()!=w):m.append((i,j,''))
     if q!='.'or not sl:break
     j+=d
 for r,k,v in(('K',25,1),('Q',25,-1))if w else(('k',95,1),('q',95,-1)):
  if r in c and not any(A(b,x,not w)for x in(k,k+v))and set(b[k+v:k+4*v:v][:2+(v<0)])=={'.'}:m.append((k,k+2*v,''))
 return[x for x in m if not A((B:=M(o,x)[0]),B.index('K'if s=='w'else'k'),s=='b')]
def e(o):
 b,s=o[:2];c=0
 for i,x in enumerate(b):
  z=x.lower()
  if z not in V:continue
  y,a=divmod(i-21,10);d=min(a,7-a)+min(y,7-y);u=y if x.isupper()else 7-y
  if z=='p':q=4*u
  elif z=='n':q=4*d-6
  elif z=='r':q=d
  elif z=='k':q=-4*d
  else:q=0
  c+=(V[z]+q)if x.isupper()else-(V[z]+q)
 return c if s=='w'else-c
def O(o,m):
 b=o[0]
 return sorted(m,key=lambda x:-V.get(b[x[1]].lower(),0)*10+V[b[x[0]].lower()]-(8*V[x[2]]if x[2]else 0))
def n(o,d,a,b,l):
 global G
 G+=1
 if G>L:raise X
 if d<1:return qs(o,a,b,l)
 m=g(o)
 if not m:return-30000+l if A(o[0],o[0].index('K'if o[1]=='w'else'k'),o[1]=='b')else 0
 for x in O(o,m):
  v=-n(M(o,x),d-1,-b,-a,l+1)
  if v>a:a=v
  if a>=b:break
 return a
def qs(o,a,b,l):
 global G
 G+=1
 if G>L:raise X
 s=e(o)
 if s>=b:return s
 if s>a:a=s
 d=o[0];m=[x for x in g(o)if d[x[1]]!='.'or x[2]or(d[x[0]].lower()=='p'and x[1]==o[2])]
 for x in O(o,m):
  v=-qs(M(o,x),-b,-a,l+1)
  if v>a:a=v
  if a>=b:break
 return a
def S(o):
 global G
 G=0;m=O(o,g(o))
 if not m:return None
 b=m[0]
 for d in range(1,8):
  try:
   a=-99999;c=m[0]
   for x in m:
    v=-n(M(o,x),d-1,-99999,-a,1)
    if v>a:a=v;c=x
   b=c
  except X:break
 return b
def post(path,body):
 r=urllib.request.Request(U+path,json.dumps(body).encode(),{'content-type':'application/json'})
 try:return json.load(urllib.request.urlopen(r))
 except Exception as x:sys.exit(x)
def pick(gm):
 try:
  m=S(p(gm['fen']));u=q(m[0])+q(m[1])+m[2]
  if u in gm['legal_moves']:return u
 except:pass
 return gm['legal_moves'][0]
def main():
 if not U:sys.exit("MAKEFUN_ENV_URL is not set")
 while 1:
  o=post('/game',{})
  if o['status']=='done':break
  while o['status']=='your_move':
   o=post('/move',{'game':o['game'],'move':pick(o)})
if __name__=='__main__':main()
