# import cv2

# # Abrir a câmera ou o arquivo de vídeo
# # capture = cv2.VideoCapture(0)  # Use 0 para a câmera do dispositivo ou forneça o caminho do arquivo de vídeo
# # Carregar o arquivo de vídeo
# cap = 'aula3/video_original.mp4'
# capture = cv2.VideoCapture(cap)
# # Obter as dimensões do frame
# frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
# frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
# print("Largura: '{}'".format(frame_width))
# print("Altura : '{}'".format(frame_height))

# # Verificar se a câmera ou o arquivo de vídeo foi aberto corretamente
# if not capture.isOpened():
#     print("Erro ao acessar a câmera ou abrir o vídeo")
# else:
#     while capture.isOpened():
#         # Capturar o frame
#         ret, frame = capture.read()
        
#         # Verificar se o frame foi capturado corretamente
#         if ret is True:
#             # Exibir o frame original
#             cv2.imshow('Input', frame)
            
#             # Converter o frame para escala de cinza
#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
#             # Exibir o frame em escala de cinza
#             cv2.imshow('Cinza', gray)
            
#             # Esperar por uma tecla pressionada por 20 milissegundos
#             if cv2.waitKey(20) & 0xFF == ord('q'):
#                 break  # Se a tecla 'q' for pressionada, sair do loop
                
#             # Salvar o frame ao pressionar a tecla 'w'
#             if cv2.waitKey(20) & 0xFF == ord('w'):
#                 print("Salvando frame...")
#                 cv2.imwrite('print.jpg', frame)  # Salvar o frame original
#                 cv2.imwrite('gray.jpg', gray)    # Salvar o frame em escala de cinza
#         else:
#             break  # Se não foi possível capturar um novo frame, sair do loop

# # Liberar a captura de vídeo
# capture.release()

# # Fechar todas as janelas abertas pelo OpenCV
# cv2.destroyAllWindows()
import cv2
# Carregar o arquivo de vídeo
cap = 'aula3/video_original.mp4'
capture = cv2.VideoCapture(cap)

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("WIDTH: '{}'".format(frame_width))
print("HEIGHT : '{}'".format(frame_height))

if not capture.isOpened():
    print("Erro ao acessar camera ou abrir o vídeo")
else:
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:
            cv2.imshow('Input', frame)
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            cv2.imshow('Cinza', gray)
            
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

            if cv2.waitKey(20) & 0xFF == ord('w'):
                print("Salvando frame...")
                cv2.imwrite('print.jpg',frame)
                cv2.imwrite('gray.jpg',gray)
        else: break

capture.release()
cv2.destroyAllWindows()