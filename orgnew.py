import os
import shutil
import zipfile

def move_zip_files(source_folder):
    # 创建002文件夹
    new_folder = os.path.join(source_folder, '002')
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path) and filename.endswith('.zip'):
            # 将压缩包移动到002文件夹中
            shutil.move(file_path, new_folder)

    # 将002文件夹中的压缩包分别存储到新文件夹中
    for zip_file in os.listdir(new_folder):
        zip_folder_name = os.path.splitext(zip_file)[0] + '2'
        zip_folder_path = os.path.join(new_folder, zip_folder_name)
        os.mkdir(zip_folder_path)

        # 解压缩压缩包到新文件夹中
        with zipfile.ZipFile(os.path.join(new_folder, zip_file), 'r') as zip_ref:
            zip_ref.extractall(zip_folder_path)

# 指定路径的文件夹
source_folder = r'D:\Telegram Foleder\泽泽女主\001'
move_zip_files(source_folder)
