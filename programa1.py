import cv2
import numpy as ap
import matplotlib.pyplot as plt

imagen = cv2.imread('C:/Users/sergi/Documents/VSC/python/arcane.jpg')
verde = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
bordes = cv2.Canny(verde, 100, 200)

cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Color', verde)
cv2.imshow('Imagen gris bordes', bordes)
cv2.waitKey(0)
cv2.destroyAllWindows()
