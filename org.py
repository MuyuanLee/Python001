import os
import shutil

def move_files_to_folders(source_folder, output_folder):
    # 创建目标文件夹（存储新建的文件夹，改为名字为 "002"）
    new_folder_path = os.path.join(source_folder, '002')
    os.makedirs(new_folder_path, exist_ok=True)

    # 获取源文件夹中所有文件的列表
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    # 遍历每个文件并移动到新建的文件夹中
    for file in files:
        file_path = os.path.join(source_folder, file)

        # 创建新的文件夹来存储单个文件
        folder_name = os.path.splitext(file)[0]
        output_folder_path = os.path.join(new_folder_path, folder_name)
        os.makedirs(output_folder_path, exist_ok=True)

        # 移动文件到新建的文件夹中
        shutil.move(file_path, os.path.join(output_folder_path, file))

        # 重命名新建的文件夹
        new_folder_name = folder_name + "2"
        os.rename(output_folder_path, os.path.join(new_folder_path, new_folder_name))

if __name__ == "__main__":
    source_folder = r'D:\Telegram Foleder\伊轩女主\001'

    # 调用函数进行文件移动和文件夹重命名
    move_files_to_folders(source_folder, source_folder)

    print("文件移动和文件夹重命名完成！新建的文件夹存储在 '002' 文件夹中。")
