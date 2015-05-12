# -*- coding: utf-8 -*-
"""
Created on Wed May 13 04:45:03 2015
pyqt输入对话框
@author: robin
"""
import sys
from PyQt4 import QtGui,QtCore

class LabWindow(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self)
        
        self.setGeometry(300,300,350,80)
        self.setWindowTitle(u"py输入框试验")
        
        btn_input=QtGui.QPushButton(u"输入对话")        
        btn_color=QtGui.QPushButton(u"颜色对话")
        btn_font=QtGui.QPushButton(u"字体对话")
        btn_file=QtGui.QPushButton(u"文件选择")
        
        self.label1=QtGui.QLineEdit(self) 
        
        vbox=QtGui.QVBoxLayout() #布局设置
        vbox.addWidget(btn_input) #弹出输入对话框的按钮
        vbox.addWidget(btn_color) #弹出颜色对话框的按钮 
        vbox.addWidget(btn_font) #弹出字体选择对话框
        vbox.addWidget(btn_file) #弹出文件选择对话框
        
        vbox.addWidget(self.label1) #显示反馈信息的按钮
        
        self.setLayout(vbox) #设置窗口布局

        
        #bt_input按钮的click()信号被激发调用showDialog函数
        self.connect(btn_input,QtCore.SIGNAL('clicked()'),self.ShowInputDialog)
        
        #bt_color按钮的click（）信号被假发，调用showColorDialog函数
        self.connect(btn_color,QtCore.SIGNAL('clicked()'),self.ShowColorDialog)

        #bt_font按钮的click（）信号被激发，调用showFontDialog函数
        self.connect(btn_font,QtCore.SIGNAL('clicked()'),self.ShowFontDialog)

        #bt_file按钮的click（）信号被激发，调用showFileDialog函数
        self.connect(btn_file,QtCore.SIGNAL('clicked()'),self.ShowFileDialog)
        
    
    #对话框的显示函数
    def ShowInputDialog(self):
        text,ok=QtGui.QInputDialog.getText(self,u'输入对话框',u'请输入信息:')
        if ok:
            self.label1.setText(unicode(text))
    
    #颜色选取对话框的函数
    def ShowColorDialog(self):
        col=QtGui.QColorDialog.getColor()
        if col.isValid():
            self.label1.setStyleSheet('QWidget {background-color:%s}'%col.name())
    
    #字体选取对话框的函数
    def ShowFontDialog(self):
        font,ok=QtGui.QFontDialog.getFont()
        
        if ok:
            self.label1.setFont(font)
            self.label1.setText(u"测试字体")
            
    #文件选择对话框函数
    def ShowFileDialog(self):
        filename=QtGui.QFileDialog.getOpenFileName(self,u'选择文件','./')
        self.label1.setText(filename)
            
app=QtGui.QApplication(sys.argv)
icon=LabWindow()
icon.show()
sys.exit(app.exec_())

