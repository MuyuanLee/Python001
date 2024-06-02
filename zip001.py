import os
from zipfile import ZipFile

def zip_files_in_folder(folder_path):
    # 获取文件夹中的所有文件
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # 创建一个保存压缩包的文件夹（改为名字为 "001"）
    output_folder = os.path.join(folder_path, '001')
    os.makedirs(output_folder, exist_ok=True)

    for file in files:
        file_path = os.path.join(folder_path, file)
        
        # 创建一个与文件同名的压缩包
        zip_file_path = os.path.join(output_folder, f"{os.path.splitext(file)[0]}.zip")

        # 打开压缩包并将文件添加到其中
        with ZipFile(zip_file_path, 'w') as zipf:
            zipf.write(file_path, os.path.basename(file_path))

    print("压缩完成！")

if __name__ == "__main__":
    folder_to_compress = r'D:\下载2'
    zip_files_in_folder(folder_to_compress)
