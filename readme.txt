# 配置下载镜像源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes

# 创建conda虚拟环境
conda create -n pyside6 python=3.9 -y

# 激活虚拟环境
conda activate pyside6

# 下载包
# pyside6 -- GUI
# pyinstaller -- 打包为 exe
pip install pyside6  pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple