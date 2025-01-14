from PIL import Image
import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine


def image_to_music(image_path, output_path):
    # 打开图像并转换为RGB
    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = np.array(image)

    # 定义一些参数
    duration_per_color = 100  # 每种颜色的持续时间（毫秒）
    base_frequency = 220  # 基础频率（A3音）

    # 初始化音频片段
    audio = AudioSegment.silent(duration=0)

    # 遍历每个像素的颜色
    for row in pixels:
        for (r, g, b) in row:
            # 将RGB值转换为频率
            frequency = base_frequency + (r + g + b) / 3
            # 生成对应频率的音符
            sine_wave = Sine(frequency).to_audio_segment(duration=duration_per_color)
            # 将音符添加到音频片段中
            audio += sine_wave