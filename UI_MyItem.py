# -*- coding: utf-8 -*-
from time import time
import logging
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from InheritItemTest import MyItem
from MyQTextEdit import MyQTextEdit
from IoProcess import IoProcess
from config import columnDict


# 备份！

# def log(func):
#     def wrapper(*arg, **kw):
#         logging.debug("this is info message")
#         return func(*arg, **kw)
#     return wrapper
# todo 增加关于


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        # super(Ui_MainWindow, self).__init__()
        self.MainWindow = MainWindow
        self.itemCount = 0

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        # MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) # 窗口置顶
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # 水平布局1
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.Button_Add = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Add.setObjectName("Button_Add")
        self.horizontalLayout.addWidget(self.Button_Add)

        self.Button_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Delete.setObjectName("Button_Delete")
        self.horizontalLayout.addWidget(self.Button_Delete)

        self.Button_MoveLeft = QtWidgets.QPushButton(self.centralwidget)
        self.Button_MoveLeft.setObjectName("Button_MoveUp")
        self.horizontalLayout.addWidget(self.Button_MoveLeft)

        self.Button_MoveRight = QtWidgets.QPushButton(self.centralwidget)
        self.Button_MoveRight.setObjectName("Button_MoveRight")
        self.horizontalLayout.addWidget(self.Button_MoveRight)

        self.Button_MoveUp = QtWidgets.QPushButton(self.centralwidget)
        self.Button_MoveUp.setObjectName("Button_MoveUp")
        self.horizontalLayout.addWidget(self.Button_MoveUp)

        self.Button_MoveDown = QtWidgets.QPushButton(self.centralwidget)
        self.Button_MoveDown.setObjectName("Button_MoveDown")
        self.horizontalLayout.addWidget(self.Button_MoveDown)

        self.Button_ExpandAll = QtWidgets.QPushButton(self.centralwidget)
        self.Button_ExpandAll.setObjectName("Button_ExpandAll")
        self.horizontalLayout.addWidget(self.Button_ExpandAll)

        self.Button_CollapseAll = QtWidgets.QPushButton(self.centralwidget)
        self.Button_CollapseAll.setObjectName("Button_CollapseAll")
        self.horizontalLayout.addWidget(self.Button_CollapseAll)


        # 水平布局2
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        # tree widget
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 31, 500, 200))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.currentItemChanged.connect(self.current_item_changed)
        # self.treeWidget.setAcceptDrops(True)
        # self.treeWidget.setDragEnabled(True)
        # self.treeWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.horizontalLayout_2.addWidget(self.treeWidget)
        # 列宽
        self.treeWidget.setColumnWidth(0, 200)
        # self.root = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.root = MyItem(self.treeWidget)
        self.selectedItem = self.root
        # self.selectedItem = self.treeWidget.currentItem()

        self.io = IoProcess(self.root)

        # text edit
        # self.textEdit = MyQTextEdit(self.horizontalLayoutWidget_2)
        # self.textEdit.setEnabled(True)
        # self.textEdit.setObjectName("textEdit")
        # self.horizontalLayout_2.addWidget(self.textEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        # 菜单栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1049, 23))
        self.menubar.setObjectName("menubar")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        self.about = QtWidgets.QMenu(self.menubar)
        self.about.setObjectName("about")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.save = QtWidgets.QAction(MainWindow)
        self.save.setObjectName("save")
        self.load = QtWidgets.QAction(MainWindow)
        self.load.setObjectName("load")
        self.file.addAction(self.load)
        self.file.addAction(self.save)
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.about.menuAction())

        self.retranslateUi(MainWindow)

        # 自定义
        self.addSignal(MainWindow)
        self.addSlot()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文档分块管理"))
        self.treeWidget.headerItem().setText(columnDict['block'], _translate("MainWindow", "分块"))
        self.treeWidget.headerItem().setText(columnDict['des'], _translate("MainWindow", "描述"))
        self.treeWidget.headerItem().setText(columnDict['remark'], _translate("MainWindow", "备注"))
        self.treeWidget.headerItem().setText(columnDict['link'], _translate("MainWindow", "链接"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(columnDict['block'], _translate("MainWindow", "根"))
        # 因加载逻辑，根命名暂不可编辑
        # self.root.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable)

        self.treeWidget.setSortingEnabled(__sortingEnabled)
        # 按钮名称及快捷键
        self.Button_Add.setText(_translate("MainWindow", "+"))
        self.Button_Add.setShortcut('alt+n')
        self.Button_Delete.setText(_translate("MainWindow", "-"))
        self.Button_Delete.setShortcut('delete')
        self.Button_MoveLeft.setText(_translate("MainWindow", "←"))
        self.Button_MoveLeft.setShortcut('shift+left')
        self.Button_MoveRight.setText(_translate("MainWindow", "→"))
        self.Button_MoveRight.setShortcut('shift+right ')
        self.Button_MoveUp.setText(_translate("MainWindow", "↑"))
        self.Button_MoveUp.setShortcut('shift+up')
        self.Button_MoveDown.setText(_translate("MainWindow", "↓"))
        self.Button_MoveDown.setShortcut('shift+down')
        self.Button_ExpandAll.setText(_translate("MainWindow", "Expand All"))
        self.Button_CollapseAll.setText(_translate("MainWindow", "Fold All"))
        # 按层级折叠: todo


        self.file.setTitle(_translate("MainWindow", "文件"))
        self.about.setTitle(_translate("MainWindow", "关于"))
        self.save.setText(_translate("MainWindow", "保存"))
        self.load.setText(_translate("MainWindow", "导入"))

    def addSignal(self, MainWindow):
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addSlot(self):
        self.Button_Add.clicked.connect(self.addButtonClicked)
        self.Button_Delete.clicked.connect(self.deleteButtonClicked)
        self.Button_MoveLeft.clicked.connect(self.moveLeftButtonClicked)
        self.Button_MoveRight.clicked.connect(self.moveRightButtonClicked)
        self.Button_MoveUp.clicked.connect(self.moveUpButtonClicked)
        self.Button_MoveDown.clicked.connect(self.moveDownButtonClicked)
        self.Button_ExpandAll.clicked.connect(self.expandAllButtonClicked)
        self.Button_CollapseAll.clicked.connect(self.collapseAllButtonClicked)

        self.treeWidget.itemClicked['QTreeWidgetItem*', 'int'].connect(self.clickedItem)
        self.menubar.triggered[QAction].connect(self.processtrigger)
        # self.textEdit.textChanged.connect(lambda: self.saveTextEditContent(self.selectedItem))
        # todo：失去焦点的响应
        # self.textEdit.focusOutEvent = self.saveTextEditContent

    def clickedItem(self, item):
        # 获取到点击的item，记录到全局变量
        self.selectedItem = item
        logging.debug("SelectedItem: {}".format(self.selectedItem.text(0)))
        # if self.selectedItem is self.root:
        #     logging.debug("SelectedItem: root".format(
        #         # self.selectedItem.__class__(),
        #         # self.selectedItem.takeChildren()
        #     ))
        # else:
        #     logging.debug("SelectedItem: {}, Class: {}, Parent: {}".format(
        #         self.getItemName(self.selectedItem),
        #         self.selectedItem.__class__(),
        #         self.selectedItem.parent().text(0),
        #         # self.selectedItem.takeChildren()
        #     ))

    def addButtonClicked(self):
        self.itemCount += 1
        # child = QTreeWidgetItem(self.selectedItem)
        child = MyItem(self.selectedItem)
        # todo:设置选中状态，更新selectdItem，使得应用快捷键操作
        # child.setSelected(True)
        logging.info('addButtonClicked')
        # 默认展开
        self.selectedItem.setExpanded(1)
        # 可拖拽
        # 设置图标占位

        # 子
        # 子可拖拽
        # child.setFlags(child.flags() & ~QtCore.Qt.ItemIsDropEnabled)
        # 子可输入
        child.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable)

        # todo： 默认可输入状态
        child.setText(columnDict['block'], '分块{}'.format(self.itemCount))
        logging.debug('set new child text')

        # 为当前节点和父节点增加计数
        # 从第二列取
        # 当前节点更新计数

    def deleteButtonClicked(self):
        # 本节点执行删除，暂只支持叶子节点
        # 递归更新计数
        # 若删除未完成节点，则父(0,-1)，递归减数，并判断完成
        # 若删除完成节点，则父(-1,-1)，递归减数，并判断完成
        try:
            self.selectedItem.parent().removeChild(self.selectedItem)
        except AttributeError:
            return

    def moveLeftButtonClicked(self):
        # 将节点及子节点提高一个层级，置于父节点下一位
        logging.info('moveLeftButtonClicked')
        currentParent = self.selectedItem.parent()
        # 若对根下层节点操作，则不进行
        if currentParent == self.root:
            pass
        else:
            # take
            currentIndex = currentParent.indexOfChild(self.selectedItem)
            item = currentParent.takeChild(currentIndex)
            # inset 到 parent 所在 list
            objectParent = currentParent.parent()
            objectIndex = objectParent.indexOfChild(currentParent)
            objectParent.insertChild(objectIndex, item)
        return

    def moveRightButtonClicked(self):
        # 将节点及子节点降低一个层级，置于同级的下一个节点下
        # 要求：1 有同级下一个节点
        logging.info('moveRightButtonClicked')
        currentParent = self.selectedItem.parent()
        currentIndex = currentParent.indexOfChild(self.selectedItem)
        # 若对根下层节点操作，则不进行
        if currentIndex == -1:
            pass
        else:
            # take
            # 暂时无法通过迭代器拿到下一个节点 todo
            # itemNext = QTreeWidgetItemIterator(self.selectedItem)
            item = currentParent.takeChild(currentIndex)
            # inset 到 同级下一个节点 所在 list 首位
            itemNext = currentParent.takeChild((currentIndex))
            itemNext.insertChild(0, item)
            # 挂回，保持展开
            currentParent.insertChild(currentIndex, itemNext)
            itemNext.setExpanded(True)
        return

    def moveUpButtonClicked(self):
        # 将节点及子节点向上移动
        # take children
        parent = self.selectedItem.parent()
        index = parent.indexOfChild(self.selectedItem)
        isExpanded = self.selectedItem.isExpanded()
        if index == 0:
            pass
        else:
            childList = parent.takeChildren()
            item = childList.pop(index)
            childList.insert(index - 1, item)
            parent.addChildren(childList)
        # 保持选中状态
        self.selectedItem.setSelected(1)
        # 保持折叠/非折叠状态
        self.selectedItem.setExpanded(isExpanded)
        return

    def moveDownButtonClicked(self):
        # 将节点及子节点向下移动
        # take children
        parent = self.selectedItem.parent()
        index = parent.indexOfChild(self.selectedItem)
        isExpanded = self.selectedItem.isExpanded()
        if index == -1:
            pass
        else:
            childList = parent.takeChildren()
            item = childList.pop(index)
            childList.insert(index + 1, item)
            parent.addChildren(childList)
        # 保持选中状态
        self.selectedItem.setSelected(1)
        # 保持折叠/非折叠状态
        self.selectedItem.setExpanded(isExpanded)
        return

    def expandAllButtonClicked(self):
        self.treeWidget.expandAll()

    def collapseAllButtonClicked(self):
        self.treeWidget.collapseAll()

    def processtrigger(self, q):
        # 输出那个Qmenu对象被点击
        if q is self.save:
            logging.debug("Save Clicked")
            self.io.save()

        elif q is self.load:
            logging.debug("Load Clicked")
            self.io.load()

    def current_item_changed(self, current):
        # treeWidge 同步选中状态
        self.selectedItem = current

    def getItemName(self, item):
        return item.text(columnDict['itemName'])

    # def isParent(self, item):

    def hot_key_event(self, data):
        """热键处理函数"""
        if data == 12582913:
            if self.MainWindow.isMinimized():  # 判断窗口是否为最小化
                self.MainWindow.showNormal()  # 如果为最小化, 则恢复正常
            else:
                self.MainWindow.showMinimized()  # 将窗口设置为最小化
