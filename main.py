import logging
import sys
import UI_MyItem
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import hotKey

###
# 继承自 WorkTool，删除完成度和时间管理
###

if __name__ == '__main__':
    logging.basicConfig(level=logging.NOTSET)
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    # ui = test2.Ui_MainWindow(MainWindow)
    ui = UI_MyItem.Ui_MainWindow(MainWindow)

    hot_key = hotKey.HotKey()
    hot_key.ShowWindow.connect(ui.hot_key_event)
    hot_key.start()  # 开启热键监听的线程

    MainWindow.setWindowIcon(QIcon('./design/workTool.jpg'))
    MainWindow.show()


    sys.exit(app.exec_())

    pass
