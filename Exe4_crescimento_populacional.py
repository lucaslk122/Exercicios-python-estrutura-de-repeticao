paisA = 80e3
paisB = 200e3
anos = 0
#Ta(total população de A) = (80e3 + (80e3*0.03)) * anos
#Tb(total população de B) = (200e3 + (200e3*0.015)) * anos
while (paisA <= paisB):
    paisA = paisA + (paisA*0.03)
    paisB = paisB + (paisB*0.015)
    anos += 1
print(f"O pais A ultrapassara o páis B em {anos} anos ")