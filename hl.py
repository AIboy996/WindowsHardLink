"""
本脚本必须使用命令行作为主文件(__name__ == "__main__")调用！
需要传入参数(脚本文件，源目录，目标目录)
调用示例：
python hl.py example output
"""
import os
import sys

def main():
    args = sys.argv
    source, target = args[1:]
    print(*zip(["运行的脚本", "源目录", "目标目录"], args), sep='\n')

    for item in os.walk(source):
        folder = item[0]
        files = item[2]
        # 创建对应的文件夹
        os.system(f"mkdir {folder.replace(source, target)}")
        for file in files:
            filepath = os.path.join(folder, file)
            targetpath = filepath.replace(source, target)
            # 创建硬链接
            os.system(f"mklink /H {targetpath} {filepath}")


if __name__ == "__main__":
    try:
        main()
    except:
        print(__doc__)
else:
    print(__doc__)