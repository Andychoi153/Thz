#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we select a file with a
QtGui.QFileDialog and display its contents
in a QtGui.QTextEdit.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""
import untitled1
import sys
import matplotlib.pyplot as plt
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)       
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()
        
    def showDialog(self):

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
                '/scan')
        
        x, y = untitled1.import_data(fname)
           
        plt.subplot(2,1,1)
        plt.plot(x,y)
        plt.title('Thz data/FFT')
        plt.xlabel('Time (ps)')    
        plt.ylabel('Amplitude (arb. units)')
        
#    x, y = adding_up_zeros(x, y)    
        fermi = untitled1.fermi_function(x,y)
        yf, xf = untitled1.fft(x,y, fermi)    
        plt.subplot(2,1,2)    
        plt.plot(xf[0:(xf.size/2)], abs(yf[0:(yf.size/2)]))
        plt.xlabel('Furie frequency(Hz)')    
        plt.show()
             
        f = open(fname, 'r')
        
        with f:        
            data = f.read()
            self.textEdit.setText(data) 
                                                        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
