import cv2
from cv2 import aruco

# Define qual câmera usar (0 é normalmente a câmera padrão)
cap = cv2.VideoCapture(0)

# Seleciona o dicionário ArUco
dictionary = aruco.Dictionary_get(aruco.DICT_6X6_50)

while True:
    # Captura o quadro da webcam
    ret, frame = cap.read()

    # Converte o quadro em escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta os marcadores no quadro
    # Corners: Lista com (x, y) coordinates ArUcos markers
    # ids: Each Marker detected
    # rejected:
    corners, ids, rejected = aruco.detectMarkers(gray, dictionary)

    # Desenha os marcadores detectados no quadro
    frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)

    # Exibe o quadro
    cv2.imshow('frame', frame_markers)

    # Se a tecla 'q' for pressionada, saia do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a captura e fecha as janelas do OpenCV
cap.release()
cv2.destroyAllWindows()
