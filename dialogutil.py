from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel


def open_dialog(message, x, y, width, height):
    dialog = QDialog()
    dialog.setWindowTitle("Dialog")
    # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
    dialog.setWindowModality(Qt.ApplicationModal)

    label = QLabel(message, dialog)
    label.move(x, y)
    # layout = QVBoxLayout(dialog)
    # layout.addWidget(label)
    dialog.resize(width, height)
    dialog.exec_()