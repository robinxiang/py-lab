# -*- coding: utf-8 -*-
"""
Created on Sat May 09 23:00:24 2015

@author: robin
"""

import sys
from PyQt4 import QtGui,QtCore

#主窗口类
class MainWindow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle(u'PyQt学习') #设置窗口标题
        self.setWindowIcon(QtGui.QIcon('icons/hema.png')) #窗口图标
        
        #窗口的提示标签
        self.setToolTip(u'河马的PyQt<br>学习结果') #可以使用html标识
        QtGui.QToolTip.setFont(QtGui.QFont('宋体',9))
        
        #退出程序的按钮
        bt_quit=QtGui.QPushButton(u'关闭',self) #定义按钮文字
        bt_quit.setToolTip(u'退出程序') #按钮的提示标签
        bt_quit.setGeometry(10,30,60,35) #按钮在窗口中所在位置和大小设置
        #将窗口信号槽的退出时间绑定在按钮的点击事件中        
        self.connect(bt_quit,QtCore.SIGNAL('clicked()'),QtGui.qApp,QtCore.SLOT('quit()'))
        exit=QtGui.QAction(self)        
        self.connect(exit,QtCore.SIGNAL('triggered()'),QtCore.SLOT('close()'))
        
        #将窗口居中显示
        self.OverCenter()
        
        #窗口中显示状态栏
        self.statusBar().showMessage(u'就绪')
        
        #窗口中显示主菜单
        MainMenu=self.menuBar()
        #"文件"菜单做父菜单
        mu_file=MainMenu.addMenu(u'文件(&F)') 
        #定义“退出”子菜单
        mu_exit=QtGui.QAction(QtGui.QIcon('icons/exit.png'),u'退出',self)
        mu_exit.setShortcut('Ctrl+Q') #定义菜单快捷键
        mu_exit.setStatusTip(u'退出程序')#提示标签
        #菜单绑定信号槽
        mu_exit.connect(mu_exit,QtCore.SIGNAL('triggered()'),QtGui.qApp,
                        QtCore.SLOT('quit()'))
        #将定义的子菜单添加到父菜单中
        mu_file.addAction(mu_exit)
    
    #窗体居中显示的控制函数
    def OverCenter(self):
        screen=QtGui.QDesktopWidget().screenGeometry() #获取桌面的分辨率
        size=self.geometry() #获取窗口的大小
        #通过桌面的长宽和窗口的长宽，计算出窗口居中应该所在的位置
        self.move((screen.width()-size.width())/2,
                  (screen.height()-size.height())/2)
    
    #窗体的关闭事件，重新定义
    def closeEvent(self,event):
        reply=QtGui.QMessageBox.question(self,u'提示',u'您确定要退出吗？',
                                         QtGui.QMessageBox.Yes,
                                         QtGui.QMessageBox.No)
        if reply==QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


#App对象
app=QtGui.QApplication(sys.argv)
#窗体对象
window_main=MainWindow()
window_main.show()
sys.exit(app.exec_())