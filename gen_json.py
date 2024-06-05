import json
import re

# 读取txt文件内容
input_file_path = r'G:\WORK\demo\ssig-main\image_descriptions.txt'
output_file_path_original = r'G:\WORK\demo\ssig-main\image_descriptions.json'
output_file_path_cleaned = r'G:\WORK\demo\ssig-main\image_descriptions_cleaned.json'

# 初始化存储JSON对象的列表
json_list_original = []
json_list_cleaned = []

# 读取并处理文件
with open(input_file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line.strip():  # 忽略空行
            file_name, description = line.split(": ", 1)
            source_name = file_name.strip()
            target_name = source_name.replace('_bubble', '_ori')
            # 去掉描述中的数字
            cleaned_description = re.sub(r'\d+ ', '', description).strip()
            json_data_original = {
                "source": f"source/{source_name}",
                "target": f"target/{target_name}",
                "prompt": description.strip()
            }
            json_data_cleaned = {
                "source": f"source/{source_name}",
                "target": f"target/{target_name}",
                "prompt": cleaned_description
            }
            json_list_original.append(json_data_original)
            json_list_cleaned.append(json_data_cleaned)

# 将原始结果写入JSON文件
with open(output_file_path_original, 'w') as json_file_original:
    for item in json_list_original:
        json.dump(item, json_file_original)
        json_file_original.write('\n')

# 将去除数字后的结果写入JSON文件
with open(output_file_path_cleaned, 'w') as json_file_cleaned:
    for item in json_list_cleaned:
        json.dump(item, json_file_cleaned)
        json_file_cleaned.write('\n')

print(f"转换完成，原始JSON文件已保存至: {output_file_path_original}")
print(f"去除数字后的JSON文件已保存至: {output_file_path_cleaned}")

import json
import re

# 读取txt文件内容
input_file_path = r'G:\WORK\demo\ssig-main\image_descriptions.txt'
output_file_path_original = r'G:\WORK\demo\ssig-main\image_descriptions.json'
output_file_path_cleaned =  r'G:\WORK\demo\ssig-main\image_descriptions_cleaned.json'
output_file_path_original_mask = r'G:\WORK\demo\ssig-main\image_descriptions_original_mask.json'
output_file_path_cleaned_mask = r'G:\WORK\demo\ssig-main\image_descriptions_cleaned_mask.json'

# 初始化存储JSON对象的列表
json_list_original = []
json_list_cleaned = []
json_list_original_mask = []
json_list_cleaned_mask = []

# 读取并处理文件
with open(input_file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line.strip():  # 忽略空行
            file_name, description = line.split(": ", 1)
            source_name_bubble = file_name.strip()
            source_name_mask = source_name_bubble.replace('_bubble', '_mask')
            target_name = source_name_bubble.replace('_bubble', '_ori')
            # 去掉描述中的数字
            cleaned_description = re.sub(r'\d+ ', '', description).strip()
            json_data_original = {
                "source": f"source/{source_name_bubble}",
                "target": f"target/{target_name}",
                "prompt": description.strip()
            }
            json_data_cleaned = {
                "source": f"source/{source_name_bubble}",
                "target": f"target/{target_name}",
                "prompt": cleaned_description
            }
            json_data_original_mask = {
                "source": f"source/{source_name_mask}",
                "target": f"target/{target_name}",
                "prompt": description.strip()
            }
            json_data_cleaned_mask = {
                "source": f"source/{source_name_mask}",
                "target": f"target/{target_name}",
                "prompt": cleaned_description
            }
            json_list_original.append(json_data_original)
            json_list_cleaned.append(json_data_cleaned)
            json_list_original_mask.append(json_data_original_mask)
            json_list_cleaned_mask.append(json_data_cleaned_mask)

# 将原始结果写入JSON文件
with open(output_file_path_original, 'w') as json_file_original:
    for item in json_list_original:
        json.dump(item, json_file_original)
        json_file_original.write('\n')

# 将去除数字后的结果写入JSON文件
with open(output_file_path_cleaned, 'w') as json_file_cleaned:
    for item in json_list_cleaned:
        json.dump(item, json_file_cleaned)
        json_file_cleaned.write('\n')

# 将原始结果（mask格式）写入JSON文件
with open(output_file_path_original_mask, 'w') as json_file_original_mask:
    for item in json_list_original_mask:
        json.dump(item, json_file_original_mask)
        json_file_original_mask.write('\n')

# 将去除数字后的结果（mask格式）写入JSON文件
with open(output_file_path_cleaned_mask, 'w') as json_file_cleaned_mask:
    for item in json_list_cleaned_mask:
        json.dump(item, json_file_cleaned_mask)
        json_file_cleaned_mask.write('\n')

print(f"转换完成，原始JSON文件已保存至: {output_file_path_original}")
print(f"去除数字后的JSON文件已保存至: {output_file_path_cleaned}")
print(f"原始JSON文件（mask格式）已保存至: {output_file_path_original_mask}")
print(f"去除数字后的JSON文件（mask格式）已保存至: {output_file_path_cleaned_mask}")
