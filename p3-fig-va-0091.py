import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Ian gutierrez NC 0091
print("Ian gutierrez NC 0091")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro")
mi_imagen = cv2.imread('Tiranosaurio.jpg')
plt.imshow(mi_imagen)
plt.title('Tiranosaurio y Ian gutierrez  NC 0091')
plt.show()
print("+-+-+-+-+ puntos en la imagen +-+-+-+-+")
plt.imshow(mi_imagen)
x = [100,100,300,500]
y = [100,400,500,400]
plt.scatter(x, y, s= 20,c='red')
plt.show()
