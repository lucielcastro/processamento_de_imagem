import cv2

# Carregar o vídeo
video_path = 'aula3/video_original.mp4'
cap = cv2.VideoCapture(video_path)

# Carregar a logo
logo = cv2.imread('aula2/opencv_low.png')

# Definir as coordenadas onde a logo será sobreposta
y_offset = 10
x_offset = 10

# Loop para processar cada frame do vídeo
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Redimensionar a logo para que ela caiba no frame
    logo_resized = cv2.resize(logo, (100, 100))  # Ajuste o tamanho conforme necessário

    # Obter as dimensões da logo
    logo_height, logo_width, _ = logo_resized.shape

    # Definir as regiões de interesse (ROI) onde a logo será sobreposta
    roi = frame[y_offset:y_offset+logo_height, x_offset:x_offset+logo_width]

    # Aplicar thresholding na logo para criar uma máscara
    _, mask = cv2.threshold(logo_resized[:, :, 0], 220, 255, cv2.THRESH_BINARY)

    # Inverter a máscara
    mask_inv = cv2.bitwise_not(mask)

    # Aplicar a logo sobre o frame usando operações lógicas
    frame_roi_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    frame_roi_fg = cv2.bitwise_and(logo_resized, logo_resized, mask=mask)
    dst = cv2.add(frame_roi_bg, frame_roi_fg)
    frame[y_offset:y_offset+logo_height, x_offset:x_offset+logo_width] = dst

    # Exibir o frame com a logo sobreposta
    cv2.imshow('Video com Logo', frame)

    # Aguardar pela tecla 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar o objeto de captura e fechar as janelas
cap.release()
cv2.destroyAllWindows()
