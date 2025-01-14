import cv2
import numpy as np
from skimage import util


def calculate_sharpness(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray_image, cv2.CV_64F).var()
    return laplacian_var


def calculate_saturation(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    saturation = hsv_image[:, :, 1].mean()
    return saturation


def calculate_contrast(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    contrast = gray_image.std()
    return contrast


def calculate_noise(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    noise = np.var(util.random_noise(gray_image, mode='gaussian'))
    return noise


def calculate_information(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"未找到图像: {image_path}")

    resolution = image.shape[0] * image.shape[1]
    sharpness = calculate_sharpness(image)
    saturation = calculate_saturation(image)
    contrast = calculate_contrast(image)
    noise = calculate_noise(image)

    # 属性的加权和，惩罚噪声
    information_score = (0.3 * resolution +
                         0.3 * sharpness +
                         0.2 * saturation +
                         0.2 * contrast -
                         0.1 * noise)

    return information_score


def compare_images(image1_path, image2_path):
    try:
        info1 = calculate_information(image1_path)
        info2 = calculate_information(image2_path)

        print(f"图像1的信息分数: {info1}")
        print(f"图像2的信息分数: {info2}")

        if info1 > info2:
            print("图像1包含更多信息。")
        elif info1 < info2:
            print("图像2包含更多信息。")
        else:
            print("两张图像包含相同的信息量。")
    except FileNotFoundError as e:
        print(e)


# 示例用法：
image1_path = 'E:\SHJD\pic01.jpg'
image2_path = 'E:\SHJD\pic03.jpg'
compare_images(image1_path, image2_path)