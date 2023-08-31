# ArUco Marker Detection

![249529818-27303272-dba7-4edd-b9ae-4025c3f149c6](https://github.com/JonysArcanjo/ArUco_Marker_Detection/assets/48812740/efdb84ad-e7a6-45ba-b0a6-a084bcfd17ba)

## Project Objective

This project contains a simple and efficient implementation of ArUco marker detection, using OpenCV and the imutils library for image manipulation.

## Project structure
```
.
├── Readme.md
├── ar.py
├── camera_calibration.py
├── detect_video.py
├── requirements.txt
└── undistort_image.py
```

* ar.py - Detectar marcadores ArUco em tempo real usando a câmera do computador.
* camera_calibration.py - O objetivo deste código é realizar a calibração de uma câmera utilizando imagens de um tabuleiro de xadrez.
* detect_video.py - Realizar a detecção de marcadores ArUco em tempo real utilizando a câmera do computador (Desenha caixas delimitadoras em torno dos marcadores detectados e calcula e desenha as coordenadas do centro de cada marcado).
* undistort_image.py - O objetivo deste código é desdistorcer uma imagem utilizando parâmetros de calibração de câmera previamente calculados.

## Libraries Used
Este projeto requer as seguintes bibliotecas:

- OpenCV
- imutils


## Application in PRD
- Augmented Reality (AR)
- Navigation and tracking of theft
- Industrial automation
- Gesture detection and human-computer interaction
- Security monitoring

## Conclusion

The detection of ArUco markers in real-time video streams with OpenCV has various applications, such as augmented reality, navigation and theft tracking, industrial automation, gesture detection and human-computer interaction, and security monitoring. 

ArUco markers offer accurate and robust detection, and OpenCV provides built-in functions for detecting and unleashing two markers. When selecting an ArUco marker dictionary, it is important to consider the number of markers needed, the resolution of the image/video and the distance between the markers. Detection of two markers is done using the cv2.aruco.detectMarkers function, and the results can be processed and displayed for specific applications. 

The OpenCV implementation for ArUco marker detection in real time is a useful base for various computer vision applications.

# License
This project is licensed under the MIT License.
