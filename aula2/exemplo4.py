import cv2

# Carregar a imagem em cores (BGR)
img = cv2.imread('aula2/logo-if.jpg', cv2.IMREAD_COLOR)

# Carregar a imagem em escala de cinza
gray = cv2.imread('logo-if.jpg', cv2.IMREAD_GRAYSCALE)

# Imprimir a forma (shape) e o tamanho (size) da imagem em cores
print(img.shape)
print(img.size)
print('='*20)

# Imprimir a forma (shape) e o tamanho (size) da imagem em escala de cinza
print(gray.shape)
print(gray.size)

# Exibir a imagem em cores usando OpenCV
cv2.imshow('Logo IF', img)

# Exibir a imagem em escala de cinza usando OpenCV
cv2.imshow('Gray', gray)

# Aguardar até que uma tecla seja pressionada
cv2.waitKey(0)

# Fechar todas as janelas abertas pelo OpenCV
cv2.destroyAllWindows()
