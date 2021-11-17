from PyQt5.QtWidgets import *
import FontStyle


class MyItem(QTreeWidgetItem):
    def __init__(self, *args, **kwargs):
        super(QTreeWidgetItem, self).__init__(*args, **kwargs)
        self.name = ''
        self.isItemComplete = False
        self.currentTime = 0
        self.textContent = ''

    def nextSameLevelItem(self):
        # 获取同级下一个节点，非默认的深度遍历
        # 获取并子节点数
        count = self.childCount()
        iterator = QTreeWidgetItemIterator(self)
        return iterator.__iadd__(count + 1).value()

    def getLevel(self):
        level = 0
        parent = self.parent()
        while parent:
            parent = parent.parent()
            level += 1
        return level

    def setFontTitle(self):
        # 判断层级
        level = self.getLevel()
        # 设置相应样式
        if level < 3:
            self.setFont(0, FontStyle.fontTitle[level])
        else:
            self.setFont(0, FontStyle.fontTitle[-1])
        # self.setSizeHint(0, )
        pass
