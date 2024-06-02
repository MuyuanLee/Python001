import os
import shutil

# 定义A文件夹路径
folder_A = r'D:\下载1'  # 将 'path_to_A_folder' 替换为实际的A文件夹路径

# 遍历A文件夹中的每个二级文件夹
for root, dirs, files in os.walk(folder_A):
    for dir_name in dirs:
        # 获取当前二级文件夹的路径
        current_dir = os.path.join(root, dir_name)
        # 遍历当前二级文件夹中的每个文件
        for file_name in os.listdir(current_dir):
            # 构建源文件的完整路径
            source_file = os.path.join(current_dir, file_name)
            # 构建目标文件的完整路径（将文件移动到A文件夹中）
            target_file = os.path.join(folder_A, file_name)
            # 移动文件
            shutil.move(source_file, target_file)
            print(f"Moved '{file_name}' to '{folder_A}'")
