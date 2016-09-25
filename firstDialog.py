#### PROGETTO SII - MOVIE RECOMMENDER SYSTEM

#### ROBERTA ROMANO

from PyQt4 import QtCore, QtGui
import sys
import secondDialog
import ManageTheDialogs

app = QtGui.QApplication(sys.argv)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return self
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MovieRecommenderSystem(object):
    def setupUi(self, MovieRecommenderSystem):
        MovieRecommenderSystem.setObjectName(_fromUtf8("MovieRecommenderSystem"))
        MovieRecommenderSystem.resize(651, 535)
        self.pushButton_2 = QtGui.QPushButton(MovieRecommenderSystem)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 480, 111, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.ready_to_start = QtGui.QTextBrowser(MovieRecommenderSystem)
        self.ready_to_start.setGeometry(QtCore.QRect(90, 410, 461, 51))
        self.ready_to_start.setObjectName(_fromUtf8("ready_to_start"))
        self.educationEdit = QtGui.QComboBox(MovieRecommenderSystem)
        self.educationEdit.setGeometry(QtCore.QRect(200, 350, 211, 31))
        self.educationEdit.setObjectName(_fromUtf8("educationEdit"))
        self.sexEdit = QtGui.QComboBox(MovieRecommenderSystem)
        self.sexEdit.setGeometry(QtCore.QRect(200, 230, 71, 31))
        self.sexEdit.setObjectName(_fromUtf8("sexEdit"))
        self.nameEdit = QtGui.QLineEdit(MovieRecommenderSystem)
        self.nameEdit.setGeometry(QtCore.QRect(200, 100, 231, 41))
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.ageEdit = QtGui.QSpinBox(MovieRecommenderSystem)
        self.ageEdit.setGeometry(QtCore.QRect(200, 170, 71, 31))
        self.ageEdit.setObjectName(_fromUtf8("spinBox_3"))
        self.ageEdit.setProperty("value", 20)
        self.occupationEdit = QtGui.QComboBox(MovieRecommenderSystem)
        self.occupationEdit.setGeometry(QtCore.QRect(200, 290, 211, 31))
        self.occupationEdit.setObjectName(_fromUtf8("occupationEdit"))
        self.insert_your_data = QtGui.QTextBrowser(MovieRecommenderSystem)
        self.insert_your_data.setGeometry(QtCore.QRect(170, 20, 291, 41))
        self.insert_your_data.setObjectName(_fromUtf8("insert_your_data"))
        self.label = QtGui.QLabel(MovieRecommenderSystem)
        self.label.setGeometry(QtCore.QRect(80, 110, 61, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(MovieRecommenderSystem)
        self.label_2.setGeometry(QtCore.QRect(80, 170, 91, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(MovieRecommenderSystem)
        self.label_3.setGeometry(QtCore.QRect(80, 230, 91, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(MovieRecommenderSystem)
        self.label_4.setGeometry(QtCore.QRect(80, 290, 111, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(MovieRecommenderSystem)
        self.label_5.setGeometry(QtCore.QRect(80, 350, 111, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(MovieRecommenderSystem)
        QtCore.QMetaObject.connectSlotsByName(MovieRecommenderSystem)
   
        self.sexEdit.addItems(["F","M"])  
        self.occupationEdit.addItems(["student", "administrator","artist","doctor","educator","engineer","entertainment","executive","healthcare", "housewife","homemaker","lawyer","librarian","marketing","none","programmer","retired","salesman","scientist","technician","writer","other"]) 
        self.educationEdit.addItems(["None", "Secondary", "Degree", "PhD"]) 

    def retranslateUi(self, MovieRecommenderSystem):
        MovieRecommenderSystem.setWindowTitle(_translate("MovieRecommenderSystem", "Dialog", None))
        self.pushButton_2.setText(_translate("MovieRecommenderSystem", "Start!", None))
        self.ready_to_start.setHtml(_translate("MovieRecommenderSystem", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">Are you ready to start? </span></p></body></html>", None))
        self.insert_your_data.setHtml(_translate("MovieRecommenderSystem", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Insert your data :</span></p></body></html>", None))
        
        self.label.setText(_translate("MovieRecommenderSystem", "<html><head/><body><p><span style=\" font-size:14pt;\">Name:</span></p></body></html>", None))
        self.label_2.setText(_translate("MovieRecommenderSystem", "<html><head/><body><p><span style=\" font-size:14pt;\">Age:</span></p></body></html>", None))
        self.label_3.setText(_translate("MovieRecommenderSystem", "<html><head/><body><p><span style=\" font-size:14pt;\">Sex:</span></p></body></html>", None))
        self.label_4.setText(_translate("MovieRecommenderSystem", "<html><head/><body><p><span style=\" font-size:14pt;\">Occupation:</span></p></body></html>", None))
        self.label_5.setText(_translate("MovieRecommenderSystem", "<html><head/><body><p><span style=\" font-size:14pt;\">Education:</span></p></body></html>", None))

        self.pushButton_2.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.mbutton1)
        
    def mbutton1(self):
        currentUserFile = open('data/us.user', 'a')

        name = str(self.nameEdit.text())
        age = str(self.ageEdit.value())
        sex = str(self.sexEdit.currentText())
        occupation = str(self.occupationEdit.currentText())
        education = str(self.educationEdit.currentText())

        currentUserFile.write("\n" + name + "|" + age + "|" + sex + "|" + occupation + "|" + education)
        currentUserFile.close()
        
        ManageTheDialogs.load_a_newDialog()

if __name__ == '__main__':
#def main():
    #choose 10 movies at the beginning
    Form = QtGui.QWidget()
    ui = Ui_MovieRecommenderSystem()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    

#main()