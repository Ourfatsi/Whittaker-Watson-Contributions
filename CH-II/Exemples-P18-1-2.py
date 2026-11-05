import math
#Python Code here
#$\sum f_n \sin(n\theta)$

#f_n here is f_n = 1/n

def Serie_sin(__f,n,theta):
  s = 0
  L=[]
  for k in range(1,n):
    s = s + __f(k)*math.sin(k*theta)
    L.append(s)
  return(L)

def Serie_cos(__f,n,theta):
  s = 0
  L=[]
  if not(divmod(theta,(2*math.pi))[1] == 0):
    for k in range(1,n):
      s = s + __f(k)*math.cos(k*theta)
      L.append(s)
    return(L)
  else:
    print("Erreur : valeur paire de l'angle")
    return(-1)


def test(__Serie, __f, N, _theta):
  return(__Serie(__f,N,_theta))


def f(n):
  return(1/n)

N = 50
Theta = math.pi/17

print(test(Serie_sin,f,N,Theta))
print(test(Serie_cos,f,N,Theta))
