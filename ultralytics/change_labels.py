import os

# 指定包含文件的文件夹路径
folder_path = 'F:/Yolov8/ultralytics/ultralytics/datasets/VisDrone_change/test/labels'

# 获取文件夹中的所有文件
file_list = os.listdir(folder_path)

# 定义一个函数来修改文件中的内容
def modify_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    with open(file_path, 'w') as f:
        for line in lines:
            parts = line.split()
            if len(parts) > 0:
                first_number = int(parts[0])
                if first_number == 4:
                    parts[0] = '0'
                elif first_number == 5:
                    parts[0] = '1'
                elif first_number == 6:
                    parts[0] = '2'
                elif first_number == 9:
                    parts[0] = '3'

            new_line = ' '.join(parts)
            f.write(new_line + '\n')

# 遍历文件夹中的每个文件并修改它们
for file_name in file_list:
    if file_name.endswith('.txt'):  # 确保只处理.txt文件
        file_path = os.path.join(folder_path, file_name)
        modify_file(file_path)

print("所有文件已修改完成。")
