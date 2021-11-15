from PyQt5.QtWidgets import *


class MyItem(QTreeWidgetItem):
    def __init__(self, *args, **kwargs):
        super(QTreeWidgetItem, self).__init__(*args, **kwargs)
        self.name = ''
        self.isItemComplete = False
        self.currentTime = 0
        self.textContent = ''
