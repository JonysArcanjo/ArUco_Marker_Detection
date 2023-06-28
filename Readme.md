# ArUco Marker Detection
![Design sem nome (6)](https://github.com/JonysArcanjo/ArUco_Marker_Detection/assets/48812740/27303272-dba7-4edd-b9ae-4025c3f149c6)

## Sobre o Projeto

Este repositório contém uma implementação simples e eficaz de detecção de marcadores ArUco, usando OpenCV e a biblioteca imutils para manipulação de imagem.


[Artigo com detalhamento do projeto.](https://medium.com/jonys-arcanjo/detec%C3%A7%C3%A3o-de-marcadores-aruco-em-streams-de-v%C3%ADdeo-em-tempo-real-com-opencv-9a3d99c667d7)


## Estrutura do projeto
```
.
├── Readme.md
├── ar.py
├── camera_calibration.py
├── detect_video.py
├── requirements.txt
└── undistort_image.py
```

- ar.py - Detectar marcadores ArUco em tempo real usando a câmera do computador.
- camera_calibration.py - O objetivo deste código é realizar a calibração de uma câmera utilizando imagens de um tabuleiro de xadrez.
- detect_video.py - Realizar a detecção de marcadores ArUco em tempo real utilizando a câmera do computador (Desenha caixas delimitadoras em torno dos marcadores detectados e calcula e desenha as coordenadas do centro de cada marcado).
- undistort_image.py - O objetivo deste código é desdistorcer uma imagem utilizando parâmetros de calibração de câmera previamente calculados.


## Bibliotecas Utilizadas
Este projeto requer as seguintes bibliotecas:

- OpenCV
- imutils

## Aplicação em PRD
- Realidade Aumentada (AR)
- Navegação e rastreamento de robôs
- Automação industrial
- Detecção de gestos e interação humano-computador
- Monitoramento de segurança


## Conclusão
A detecção de marcadores ArUco em streams de vídeo em tempo real com OpenCV tem diversas aplicações, como realidade aumentada, navegação e rastreamento de robôs, automação industrial, detecção de gestos e interação humano-computador, e monitoramento de segurança. Os marcadores ArUco oferecem uma detecção precisa e robusta, e o OpenCV fornece funções integradas para detecção e desenho dos marcadores. Ao selecionar um dicionário de marcadores ArUco, é importante considerar a quantidade de marcadores necessários, a resolução da imagem/vídeo e a distância entre os marcadores. A detecção dos marcadores é feita utilizando a função cv2.aruco.detectMarkers, e os resultados podem ser processados e visualizados para aplicações específicas. A implementação do OpenCV para detecção de marcadores ArUco em tempo real é uma base útil para diversas aplicações de visão computacional.

## Licença

Este projeto está licenciado sob a Licença MIT.
