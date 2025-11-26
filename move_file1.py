import os
import shutil

# 源文件夹路径（存放需要移动的文件）
folder_a = r'E:/Research/Work/202405_solar_storm/HMI_field/Doppler/hist'  # 替换为实际的文件夹a路径
# 目标文件夹路径（文件移动到这里）
folder_b = r'E:/Research/Work/202405_solar_storm/HMI_field/Doppler/distrib'  # 替换为实际的文件夹b路径

# 确保目标文件夹存在，不存在则创建
if not os.path.exists(folder_b):
    os.makedirs(folder_b)

# 遍历源文件夹中的所有文件
for filename in os.listdir(folder_a):
    # 检查文件名是否以"_Doppler.png"结尾
    if filename.endswith('_Doppler.png'):
        # 构建源文件和目标文件的完整路径
        src_path = os.path.join(folder_a, filename)
        dest_path = os.path.join(folder_b, filename)
        
        # 移动文件
        shutil.move(src_path, dest_path)
        print(f"已移动: {filename} -> {folder_b}")

print("所有符合条件的文件已处理完毕")