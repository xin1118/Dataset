import os
from PIL import Image
import numpy as np

# 颜色类型字典
COLORS_ROOMTYPE = {
    '#1f77b4': 'living room',
    '#e6550d': 'master room',
    '#fd8d3c': 'kitchen',
    '#fdae6b': 'bathroom',
    '#fdd0a2': 'dining room',
    '#72246c': 'child room',
    '#5254a3': 'study room',
    '#6b6ecf': 'second room',
    '#2ca02c': 'guest room',
    '#37c837': 'balcony',
    '#98df8a': 'storage',
    '#d62728': 'walk-in',
    '#e6e6e6': 'external area',
    '#ffffff': 'interior door'
}

COLORS_HEX_TO_RGB = {
    '#1f77b4': (31, 119, 180, 255),
    '#e6550d': (230, 85, 13, 255),
    '#fd8d3c': (253, 141, 60, 255),
    '#fdae6b': (253, 174, 107, 255),
    '#fdd0a2': (253, 208, 162, 255),
    '#72246c': (114, 36, 108, 255),
    '#5254a3': (82, 84, 163, 255),
    '#6b6ecf': (107, 110, 207, 255),
    '#2ca02c': (44, 160, 44, 255),
    '#37c837': (55, 200, 55, 255),
    '#98df8a': (152, 223, 138, 255),
    '#d62728': (214, 39, 40, 255),
    '#e6e6e6': (230, 230, 230, 255)
}

# 指定图像文件夹路径
image_folder_path = r'G:\WORK\demo\bubble'
output_file = 'image_descriptions.txt'

# 处理文件夹中的所有图片
with open(output_file, 'w') as file:
    for image_name in os.listdir(image_folder_path):
        if image_name.endswith('.png'):
            image_path = os.path.join(image_folder_path, image_name)
            image = Image.open(image_path)

            # 将图像转换为numpy数组
            image_array = np.array(image)

            # 获取唯一颜色
            unique_colors = np.unique(image_array.reshape(-1, image_array.shape[2]), axis=0)

            # 过滤掉黑色和白色
            filtered_colors = [color for color in unique_colors if
                               not (color == [0, 0, 0, 255]).all() and not (color == [255, 255, 255, 255]).all()]

            # 颜色类型统计
            color_types = {}

            for color in filtered_colors:
                color_tuple = tuple(color)
                for hex_color, rgb_color in COLORS_HEX_TO_RGB.items():
                    if np.array_equal(color_tuple, rgb_color):
                        color_type = COLORS_ROOMTYPE[hex_color]
                        if color_type in color_types:
                            color_types[color_type] += 1
                        else:
                            color_types[color_type] = 1

            # 形成一句话
            description = f"{image_name}: This image contains " + ", ".join(
                [f"{count} {room_type}" for room_type, count in color_types.items()]) + "."

            # 输出结果
            print(description)
            file.write(description + '\n')

print("处理完成。结果已保存到文件中。")
