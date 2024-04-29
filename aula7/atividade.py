import cv2

# Carregar a imagem principal e a máscara
imagem_principal = cv2.imread('aula7/ifcx.jpg')
mascara = cv2.imread('aula7/ifcx2.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar thresholding na máscara
_, mascara_binaria = cv2.threshold(mascara, 127, 255, cv2.THRESH_BINARY)

# Inverter a máscara
mascara_invertida = cv2.bitwise_not(mascara_binaria)

# Aplicar a máscara na imagem principal
imagem_overlay = cv2.bitwise_and(imagem_principal, imagem_principal, mask=mascara_invertida)

# Exibir a imagem resultante
cv2.imshow('Imagem com Overlay', imagem_overlay)
cv2.waitKey(0)
cv2.destroyAllWindows()
