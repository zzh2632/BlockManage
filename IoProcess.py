import xml.etree.cElementTree as ET
import xml.dom.minidom
import logging
import time
from InheritItemTest import MyItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from config import *
import os


class IoProcess(object):
    def __init__(self, root):
        self.root = root
        print(columnDict)

    def save(self):
        # XML 结构
        # <item>
        #   <property></>
        #   <children>
        #       <item>
        #       <item>
        #   </>
        # </>
        rootNode = ET.Element('root')  # 创建根节点
        # 深度优先遍历建树，存入xml
        stack = []

        def depthTraversal(item, parentNode):
            # 入栈
            stack.append(item)
            # print(item.text(0))
            # 获取节点信息
            infoTurple = self.getItemInfo(item)
            # 存储到xml, parentNode 为 <children>
            parentNode = self.insertChildXML(parentNode, infoTurple)
            # 获取子列表
            children = []
            for i in range(item.childCount()):
                # children.extend(item.child(child))
                depthTraversal(item.child(i), parentNode)
            stack.pop()
            return

        depthTraversal(self.root, rootNode)
        # 有缩进的输出XML文件

        xmlString = xml.dom.minidom.parseString(ET.tostring(rootNode, 'utf-8')).toprettyxml()
        logging.info(xmlString)

        # 选择保存位置
        cwd = os.getcwd()
        file_name, filetype = QFileDialog.getSaveFileName(None, "创建文件", cwd, "Archive Files(*.xml)")

        with open(file_name, 'wb') as f:
            f.write(xmlString.encode('utf-8'))
        logging.info("Saved: {}".format(time.strftime("%m-%d-%H_%M_%S", time.localtime())))
        pass

    def load(self):
        # 根据时间排序存档
        # saveFileList = os.listdir(output_dir)
        # saveFileLatest = saveFileList[-1]
        cwd = os.getcwd()
        file_choose, filetype = QFileDialog.getOpenFileName(None, "选取文件", cwd, "Archive Files(*.xml)")
        if file_choose == "":
            logging.debug("Cancel Selecting")
            return
        tree = ET.ElementTree(file=file_choose)
        rootNode = tree.getroot().getchildren()[0]
        stack = []

        # 深度遍历
        def depthTraversal(node, parentItem):
            # 入栈
            stack.append(node)
            print(node.getchildren()[0].text)
            # 获取节点信息
            infoTurple = self.getNodeInfo(node)
            # 建树
            if infoTurple[0] != '根':
                parentItem = self.insertChildTree(parentItem, infoTurple)
            else:
                self.root.setText(columnDict['block'], infoTurple[0])
                self.root.setText(columnDict['des'], infoTurple[1])
                self.root.setText(columnDict['remark'], infoTurple[2])
                self.root.setText(columnDict['link'], infoTurple[3])
                self.root.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable)
                if infoTurple[2] == "√":
                    self.root.isItemComplete = True
            # 获取子列表
            childNodeList = node.getchildren()[4].getchildren()
            for childNode in childNodeList:
                depthTraversal(childNode, parentItem)
            stack.pop()
            return

        depthTraversal(rootNode, self.root)
        self.root.setExpanded(1)
        pass

    def getItemInfo(self, item):
        # {'itemName': 0, 'completeness': 1, 'isComplete': 2, 'time': 3}
        block = item.text(columnDict['block'])
        des = item.text(columnDict['des'])
        remark = item.text(columnDict['remark'])
        link = item.text(columnDict['link'])
        return block, des, remark, link

    def getNodeInfo(self, node):
        block = node.getchildren()[columnDict['block']].text
        des = node.getchildren()[columnDict['des']].text
        remark = node.getchildren()[columnDict['remark']].text
        link = node.getchildren()[columnDict['link']].text
        return block, des, remark, link

    def insertChildXML(self, parentNode, infoTurple):
        # 添加<item>
        # parentNode: XML 中父节点的 <children>
        itemNode = ET.SubElement(parentNode, 'item')
        # 按属性存储到xml
        itemNameNode = ET.SubElement(itemNode, 'block')  # 创建子节点
        itemNameNode.text = infoTurple[columnDict['block']]
        completenessNode = ET.SubElement(itemNode, 'des')
        completenessNode.text = infoTurple[columnDict['des']]
        isCompleteNode = ET.SubElement(itemNode, 'remark')
        isCompleteNode.text = infoTurple[columnDict['remark']]
        timeNode = ET.SubElement(itemNode, 'link')
        timeNode.text = infoTurple[columnDict['link']]
        childrenNode = ET.SubElement(itemNode, 'children')
        return childrenNode

    def insertChildTree(self, parentItem, infoTurple):
        childItem = MyItem(parentItem)
        childItem.setExpanded(1)
        block = infoTurple[0]
        des = infoTurple[1]
        remark = infoTurple[2]
        link = infoTurple[3]
        childItem.setText(columnDict['block'], block)
        childItem.setText(columnDict['des'], des)
        childItem.setText(columnDict['remark'], remark)
        childItem.setText(columnDict['link'], link)
        childItem.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable)

        if remark == "√":
            childItem.isItemComplete = True
        return childItem
