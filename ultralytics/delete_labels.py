import os

# 要删除的类别列表
classes_to_delete = set([0, 1, 2, 3, 7, 8, 10, 11])

# 图像文件夹和文本文件夹的路径
image_folder = 'ultralytics/datasets/VisDrone/test/images'
label_folder = 'ultralytics/datasets/VisDrone/test/labels'

# 遍历图像文件夹
for image_filename in os.listdir(image_folder):
    # 检查图像对应的文本文件是否存在
    image_name, _ = os.path.splitext(image_filename)
    label_filename = os.path.join(label_folder, image_name + '.txt')

    if os.path.exists(label_filename):
        # 读取文本文件内容
        with open(label_filename, 'r') as label_file:
            lines = label_file.readlines()

        # 检查文本文件中的类别是否需要删除
        new_lines = []
        for line in lines:
            class_id, *rest = line.strip().split(' ')
            if int(class_id) not in classes_to_delete:
                new_lines.append(line)

        # 如果删除了所有类别，则删除图像和文本文件
        if len(new_lines) == 0:
            os.remove(os.path.join(image_folder, image_filename))
            os.remove(label_filename)
        else:
            # 否则，将更新后的文本写回文件
            with open(label_filename, 'w') as label_file:
                label_file.writelines(new_lines)

print("删除操作完成")
