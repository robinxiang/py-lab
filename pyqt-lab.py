# -*- coding: utf-8 -*-
"""
Created on Fri May 08 10:02:17 2015

@author: xiangtao
"""
import sys
from PySide import QtGui

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    
    #定义界面及控件    
    def initUI(self):               
        
        #状态栏
        self.statusBar().showMessage(u'准备好')
        self.setGeometry(300, 300, 250, 150)
        #窗口标题        
        self.setWindowTitle(u'状态栏')    
        #显示窗体        
        self.show()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()