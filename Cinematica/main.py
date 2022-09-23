import math
import matplotlib.pyplot as plt
import numpy as np
import cineDefs as cn

if __name__ == "__main__":
  pIy = 0.0 
  pIx = 0.0
  g = 9.81
  x = 0.00
  y = 0.00
  Y = []
  X = []
  rX = []
  rY = []

  angulo = float(input("Escolha um ângulo inicial:"))
  v0 = float(input("Digite a velocidade inicial:"))
  massa = float(input("Digite a massa do objeto:"))
  angulo = math.radians(angulo)
  anguloI = angulo

  
  vx = cn.v_x(v0, angulo)
  vy = cn.v_y(v0, angulo)
  r = cn.forRes(v = v0)
  ax = cn.aX(r, massa, angulo)
  ay = cn.aY(R = r, M = massa, ang = angulo)

  print("\nTempo    Pos_X   Pos_Y    Vel_Y     Vel_X    VTotal    A_X    A_Y    Angulo\n")
  print("---------------------------------------------------------------------------\n")

#tabela
  for i in np.linspace(0, 0.10,dtype=float,num=10):
    t = i

    ag = angulo 

    vy = cn.V(vy, t, ay)
    vx = cn.V(vx, t, ax)

    p_X = cn.pos_X(pIx, vx, t)
    p_Y = cn.pos_Y(pIy, cn.v_y(v0, ag), t, g)

    VT = cn.v_T(vx, vy)

    r = cn.forRes(v = VT)

    ax = cn.aX(r, massa, ag)
    ay = cn.aY(R = r, M = massa, ang = ag)
    
    if p_Y < 0:
      break
    
    ag = np.degrees(ag)    
    angulo = cn.anguloInst(vy, vx)

    print(f"{t: .2f}   {p_X: .2f}   {p_Y: .2f}   {vy: .2f}    {vx: .2f}   {VT: .2f}   {ax: .2f}   {ay: .2f}   {ag: .2f}\n")


  angulo = anguloI
  vx = cn.v_x(v0, angulo)
  vy = cn.v_y(v0, angulo)
  r = cn.forRes(v = v0)
  ax = cn.aX(r, massa, angulo)
  ay = cn.aY(R = r, M = massa, ang = angulo)

#Grafico sem arrasto
  for j in np.linspace(0, 4,dtype=float,num=50):
    t = j

    vy = cn.speedY(v0, g, t, angulo) 
    vx = cn.v_x(v0, angulo)

    p_X = cn.pos_X(pIx, vx, t)
    p_Y = cn.pos_Y(pIy, cn.v_y(v0, angulo), t, g)
    
    X.append(p_X)
    Y.append(p_Y)

    VT = cn.v_T(vx, vy)

    angulo = cn.anguloInst(vy, vx)
    if p_Y < 0:
      break


    angulo = anguloI
    x = 0
    y = 0 
    vRx = cn.v_x(v0, angulo)
    vRy = cn.v_y(v0, angulo)
#Grafico com arrasto
  for k in np.linspace(0, 0.10,dtype=float,num=50):
    t = k

    vRx = cn.V(vRx, t, ax)
    vRy = cn.V(vRy, t, ay)

    x = x + t * vRx
    y = y + t * vRy
    
    VT = cn.v_T(vRx, vRy)
    r = cn.forRes(v = VT)

    ax = cn.aX(r, massa, angulo)
    ay = cn.aY(R = r, M = massa, ang = angulo)

    rX.append(x)
    rY.append(y)

    if y < 0:
      break
  



  X = np.array(X)
  Y = np.array(Y)
  rX = np.array(rX)
  rY = np.array(rY)


  fig, ax = plt.subplots()
  fig.set_size_inches(10, 7)
  ax.plot(X, Y,  label = "SEM ARRASTO")
  ax.plot(rX, rY, label = "COM ARRASTO")

  ax.set_title("Lançamento de projéteis\n", fontdict={'fontsize': 20, 'fontweight' : 5, 'color' : 'Green'})
  ax.set_xlabel("X(m)", fontdict={'fontsize': 12, 'fontweight' : 5, 'color' : 'Brown'})
  ax.set_ylabel("Y(m)", fontdict={'fontsize': 12, 'fontweight' : 5, 'color' : 'Brown'})
  ax.legend()

  plt.xticks(range(0, 15))
  plt.yticks(range(0, 20, 1))
  plt.savefig('Cinematica/projetil.png')





