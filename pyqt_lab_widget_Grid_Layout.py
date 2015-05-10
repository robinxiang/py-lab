# -*- coding: utf-8 -*-
"""
Created on Sun May 10 15:25:03 2015
pyqt的网格化布局
@author: robin
"""

import sys
from PyQt4 import QtGui

class MyGridLayout(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self)
        
        self.setWindowTitle(u"PyQt的网格化布局窗口")
        
        #模拟计算器按钮的数组        
        ButtonNames=['Cls','Bck','','Close','7','8','9','/',
                     '4','5','6','*','1','2','3','-','0','.','=','+']
                     
        ButtonGrid=QtGui.QGridLayout()
        j=0
        pos=[(0,0),(0,1),(0,2),(0,3),
             (1,0),(1,1),(1,2),(1,3),
            (2,0),(2,1),(2,2),(2,3),
            (3,0),(3,1),(3,2),(3,3),
            (4,0),(4,1),(4,2),(4,3)]
            
        for i in ButtonNames:
            ButtonItem=QtGui.QPushButton(i)
            if j==2:
                ButtonGrid.addWidget(QtGui.QLabel(''),0,2) #如果没有指定按钮，则用label代替
            else:
                ButtonGrid.addWidget(ButtonItem,pos[j][0],pos[j][1])
            j=j+1
        self.setLayout(ButtonGrid)

app=QtGui.QApplication(sys.argv)
ThisWindow=MyGridLayout()
ThisWindow.show()
sys.exit(app.exec_())