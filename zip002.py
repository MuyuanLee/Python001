import os
import zipfile

def zip_folders(source_folder, output_folder):
    # 获取源文件夹中所有子文件夹的列表
    folders = [f for f in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, f))]

    # 创建存储压缩包的目标文件夹（改为名字为 "003"）
    new_folder_path = os.path.join(source_folder, '003')
    os.makedirs(new_folder_path, exist_ok=True)

    # 遍历每个子文件夹并创建相应的压缩包
    for folder in folders:
        folder_path = os.path.join(source_folder, folder)
        zip_file_name = os.path.join(new_folder_path, f"{folder}.zip")

        with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # 将子文件夹中的所有文件添加到压缩包中
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, arcname)

if __name__ == "__main__":
    source_folder = r'D:\下载1\001\002'

    # 调用函数进行压缩
    zip_folders(source_folder, source_folder)

    print("压缩完成！压缩包存储在 '003' 文件夹中。")
