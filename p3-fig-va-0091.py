import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Ian gutierrez NC 0091
print("Ian gutierrez NC 0091")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro")
img_tiranosaurio = cv2.imread('Tiranosaurio.jpg')
plt.imshow(img_tiranosaurio)
plt.title('Tiranosaurio y Ian gutierrez  NC 0091')
plt.show()
print("+-+-+-+-+ puntos en la imagen +-+-+-+-+")
plt.imshow(img_tiranosaurio)
x = [100,100,500,500]
y = [100,400,500,300]
plt.scatter(x, y, s= 20,c='red')
plt.show()
print("+-+-+-+-+ cuadro azul en la imagen +-+-+-+-+")
img_tiranosaurio = cv2.imread('Tiranosaurio.jpg')
plt.imshow(img_tiranosaurio)
# nuevas cordenadas
x = [160, 160, 460, 460, 160]
y = [450, 150, 150, 450, 450]
plt.plot(x, y, c='blue')
plt.show()
print("+-+-+-+-+ circulo verde en la imagen +-+-+-+-+")

img_tiranosaurio = cv2.imread('Tiranosaurio.jpg')
plt.imshow(cv2.cvtColor(img_tiranosaurio, cv2.COLOR_BGR2RGB))

N = 30  # lados del polígono

x = np.zeros((N+1,))
y = np.zeros((N+1,))

(xc, yc) = (340, 320)
r = 150  # radio

for i in range(N+1):
    t = 2*np.pi/N*i
    x[i] = xc + r*np.cos(t)
    y[i] = yc + r*np.sin(t)

plt.plot(x, y, c='green')
plt.show()