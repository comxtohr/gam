import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

app = QtGui.QApplication(sys.argv)
app.setApplicationName('Gmail Attachment Manager')
winNewMail = QtGui.QWidget()
winNewMail.setFixedSize(800,600)
winNewMail.move(300,300)
winNewMail.setWindowTitle('New Mail')

lblFrom = QtGui.QLabel('From:', winNewMail)
lblUserAddress = QtGui.QLabel('somhtong@gmail.com', winNewMail)
lblTo = QtGui.QLabel('To:', winNewMail)
lblSubj = QtGui.QLabel('Subject:', winNewMail)
lblAttach = QtGui.QLabel('Attach:',winNewMail)
leTo = QtGui.QLineEdit(winNewMail)
leSubl = QtGui.QLineEdit(winNewMail)
leAttach = QtGui.QLineEdit(winNewMail)
teContent = QtGui.QTextEdit(winNewMail)
btnSend = QtGui.QPushButton('Send', winNewMail)

leTo.resize(735,20)
leSubl.resize(735,20)
leAttach.resize(735,20)
teContent.resize(790,465)
btnSend.resize(80,35)

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

winNewMail.show()
sys.exit(app.exec_())