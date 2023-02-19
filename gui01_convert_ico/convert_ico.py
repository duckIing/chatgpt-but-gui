import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog
from PySide6.QtGui import QPixmap, QIcon
from set_gui_windows_ico import *


class ImageToIcon(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("图片转ICO")
        self.setGeometry(200, 200, 350, 250)

        # new
        icon = QIcon(icon_path)
        self.setWindowIcon(icon)

        # 创建控件
        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 200, 200)
        self.label.setScaledContents(True)

        self.select_btn = QPushButton("选择图片", self)
        self.select_btn.setGeometry(220, 50, 100, 30)

        self.convert_btn = QPushButton("转换", self)
        self.convert_btn.setGeometry(220, 90, 100, 30)

        # 绑定信号槽
        self.select_btn.clicked.connect(self.select_image)
        self.convert_btn.clicked.connect(self.convert_to_icon)

        # 显示窗口
        self.show()

    def select_image(self):
        # 弹出文件选择对话框
        file_name, _ = QFileDialog.getOpenFileName(self, "选择图片", "", "Images (*.png *.xpm *.jpg *.bmp)")

        if file_name:
            # 显示选择的图片
            pixmap = QPixmap(file_name)
            self.label.setPixmap(pixmap)

            # 保存文件名和路径
            self.file_name = file_name
            self.file_path = os.path.dirname(file_name)

    def convert_to_icon(self):
        if not hasattr(self, "file_name"):
            return

        # 生成ICO文件名
        base_name = os.path.splitext(os.path.basename(self.file_name))[0]
        icon_name = f"{base_name}.ico"
        icon_path = os.path.join(self.file_path, icon_name)

        # 转换为ICO文件
        icon = QIcon(self.file_name)
        pixmap = icon.pixmap(256, 256)
        pixmap.save(icon_path, "ico")

        # 显示转换结果
        msg = f"{self.file_name} 已成功转换为 {icon_name}"
        self.label.setText(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageToIcon()
    sys.exit(app.exec())
