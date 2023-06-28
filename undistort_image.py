import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

def undistort_image(image_path, calibration_file):
    # Carrega os parâmetros de calibração
    with np.load(calibration_file) as X:
        mtx, dist, _, _ = [X[i] for i in ('mtx', 'dist', 'rvecs', 'tvecs')]

    # Carrega a imagem
    img = cv2.imread(image_path)

    # Desdistorce a imagem
    h, w = img.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

    # Desdistorce
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

    return img, dst


def plot_images(img, dst):
    # Plota a imagem original e a imagem desdistorcida lado a lado
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
    plt.title('Undistorted Image')

    plt.show()


def main():
    # Analisa os argumentos de entrada
    parser = argparse.ArgumentParser(description='Undistort an image using camera calibration parameters.')
    parser.add_argument('-i', '--image_path', type=str, required=True, help='Path to the input image.')
    args = parser.parse_args()

    # Desdistorce a imagem
    img, dst = undistort_image(args.image_path, 'calib.npz')

    # Plota as imagens
    plot_images(img, dst)


if __name__ == '__main__':
    main()
