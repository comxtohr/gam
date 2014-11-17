import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class GUINewMail(QtGui.QWidget):
  
  def __init__(self):
    super(GUINewMail, self).__init__()
    self.initUI()

  def initUI(self):
    self.setFixedSize(800,600)
    self.move(300,300)
    self.setWindowTitle('New Mail')

    lblFrom = QtGui.QLabel('From:', self)
    lblUserAddress = QtGui.QLabel('somhtong@gmail.com', self)
    lblTo = QtGui.QLabel('To:', self)
    lblSubj = QtGui.QLabel('Subject:', self)
    lblAttach = QtGui.QLabel('Attach:',self)
    leTo = QtGui.QLineEdit(self)
    leSubl = QtGui.QLineEdit(self)
    leAttach = QtGui.QLineEdit(self)
    teContent = QtGui.QTextEdit(self)
    btnSend = QtGui.QPushButton('Send', self)
    btnSelect = QtGui.QPushButton('Select From Existed', self)

    leTo.resize(735,20)
    leSubl.resize(735,20)
    leAttach.resize(590,20)
    teContent.resize(790,465)
    btnSend.resize(80,35)
    btnSelect.resize(150,35)

    lblFrom.move(18,10)
    lblUserAddress.move(62,10)
    lblTo.move(34,40)
    lblSubj.move(5,70)
    lblAttach.move(11,100)
    leTo.move(60,35)
    leSubl.move(60,65)
    leAttach.move(60,95)
    teContent.move(5,130)
    btnSend.move(720, 0)
    btnSelect.move(650,90)

    self.show()

def main():
  app = QtGui.QApplication(sys.argv)
  winNewMail = GUINewMail()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()
