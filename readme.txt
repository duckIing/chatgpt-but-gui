# �������ؾ���Դ
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes

# ����conda���⻷��
conda create -n pyside6 python=3.9 -y

# �������⻷��
conda activate pyside6

# ���ذ�
# pyside6 -- GUI
# pyinstaller -- ���Ϊ exe
pip install pyside6  pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple