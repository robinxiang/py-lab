# -*- coding: utf-8 -*-
"""tWindow(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self)
        
        self.setWindowTitle(u"PyQt的Widget窗体")
        
        #定义按钮
        bt_QueDing=QtGui.QPushButton(u"确定(&O)")
        bt_QuXiao=QtGui.QPushButton(u"取消(&C)")
        
        #定义布局容器
        hbox=QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(bt_QueDing) #添加按钮到容易
        hbox.addWidget(bt_QuXiao)
        
        vbox=QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox) #将子容器添加到父容器
        
        self.setLayout(vbox) #设置窗体布局
        self.resize(300,150) #窗体大小

Created on Sun May 10 12:50:49 2015

@author: robin
"""

import sys
from PyQt4 import QtGui

#定义一个Widget的窗体类
class MyWidge
app=QtGui.QApplication(sys.argv)
ThisWindow=MyWidgetWindow()
ThisWindow.show()
sys.exit(app.exec_())