import cv2

img = cv2.imread('aula2/logo-if.jpg')

b, g, r = cv2.split(img)

cv2.imshow('BGR',img)
cv2.imshow('Red',r)
cv2.imshow('Green',g)
cv2.imshow('Blue',b)

res = cv2.merge([r,g,b])
cv2.imshow('RGB',res)

cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2

# # Carregar a imagem
# img = cv2.imread('logo-if.jpg')

# # Separar os canais de cores
# b, g, r = cv2.split(img)

# # Exibir os canais de cores separadamente
# cv2.imshow('BGR', img)
# cv2.imshow('Red', r)
# cv2.imshow('Green', g)
# cv2.imshow('Blue', b)

# # Mesclar os canais de cores na ordem correta para obter a imagem RGB
# res = cv2.merge([r, g, b])

# # Exibir a imagem RGB mesclada
# cv2.imshow('RGB', res)

# # Aguardar pressionamento de qualquer tecla
# cv2.waitKey(0)

# # Fechar todas as janelas do OpenCV
# cv2.destroyAllWindows()
