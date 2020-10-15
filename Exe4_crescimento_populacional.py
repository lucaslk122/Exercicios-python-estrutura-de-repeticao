import matplotlib.pyplot as plt
paisA = 80e3
paisB = 200e3
anos = 0
x = []
yA = []
yb = []
#Ta(total população de A) = (80e3 + (80e3*0.03)) * anos
#Tb(total população de B) = (200e3 + (200e3*0.015)) * anos
while (paisA <= paisB):
    paisA = paisA + (paisA*0.03)
    paisB = paisB + (paisB*0.015)
    anos += 1
    x.append(anos)
    yA.append(paisA)
    yb.append(paisB)
plt.plot(x,yA, color="K", label = "Pais A")
plt.plot(x,yb,color="r", label = "Pais B")
plt.xlabel("Anos")
plt.ylabel("Qunatidade de habtantes de cada pais")
plt.title("Crescimento populacional entre dois paises")
plt.grid()
plt.legend()
plt.show()
print(f"O pais A ultrapassara o páis B em {anos} anos ")