#!/usr/bin/python

# icons from http://openclipart.org/

import sys
from PyQt4 import QtGui, QtCore
import os
from os.path import expanduser

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        # name
        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("App Name")
        self.qleName = QtGui.QLineEdit(self)
        
        nameHBox = QtGui.QHBoxLayout()
        nameHBox.addWidget(self.lbl)
        nameHBox.addWidget(self.qleName)
        
        # url
        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("App URL")
        self.qleUrl = QtGui.QLineEdit(self)
        
        urlHBox = QtGui.QHBoxLayout()
        urlHBox.addWidget(self.lbl)
        urlHBox.addWidget(self.qleUrl)
        
        # icon
        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("App Icon")
        self.qleIcon = QtGui.QLineEdit(self)
        
        iconButton = QtGui.QPushButton("")
        iconButton.setIcon(QtGui.QIcon('folder.png'))
        iconButton.setIconSize(QtCore.QSize(24,24))
        iconButton.clicked.connect(self.showDialog)
        
        iconHBox = QtGui.QHBoxLayout()
        iconHBox.addWidget(self.lbl)
        iconHBox.addWidget(self.qleIcon)
        iconHBox.addWidget(iconButton)
        
#        qle.textChanged[str].connect(self.onChanged)
        
        # buttons
        okButton = QtGui.QPushButton("OK")
        okButton.clicked.connect(self.makeApp)
        
        cancelButton = QtGui.QPushButton("Cancel")
        cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        buttonsHBox = QtGui.QHBoxLayout()
        buttonsHBox.addStretch(1)
        buttonsHBox.addWidget(okButton)
        buttonsHBox.addWidget(cancelButton)

		# build layout
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(nameHBox)
        vbox.addLayout(urlHBox)
        vbox.addLayout(iconHBox)
        vbox.addStretch(1)
        vbox.addLayout(buttonsHBox)
        
        self.setLayout(vbox)    
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Web App Creator')   
        self.setWindowIcon(QtGui.QIcon('wand.png'))    
        
        self.center()
        self.show()
        
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def showDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', expanduser("~"))
        self.qleIcon.setText(fname)
        
    def makeApp(self):
    	r = os.system("./createWebApp.py -n " + self.qleName.text() + " -u " + self.qleUrl.text() + " -i " + self.qleIcon.text())
    	if r == 0:
    	    QtCore.QCoreApplication.instance().quit()
    	else:
    	    print("sorry, something went wrong :(")
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
