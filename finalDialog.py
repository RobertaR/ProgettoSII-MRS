#### PROGETTO SII - MOVIE RECOMMENDER SYSTEM

#### ROBERTA ROMANO

from bs4 import BeautifulSoup
import urllib
import urllib2
import webbrowser

from PyQt4 import QtCore, QtGui
from ClassUsers_Items import *
import sys
import ManageTheDialogs


current_user = []
d = Dataset()

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FinalDialog(object):
    def setupUi(self, Dialog):
        final_list = ManageTheDialogs.getFinalListMovies()
        #print "film trovati: " + final_list[0].title + ", genre: " + printGenres(final_list[0]) + "- " + final_list[1].title + ", genre: " + printGenres(final_list[1]) + "- " + final_list[2].title + ", genre: " + printGenres(final_list[2]) + "- " + final_list[3].title + ", genre: " + printGenres(final_list[3]) + "- " + final_list[4].title + ", genre: " + printGenres(final_list[4])
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(751, 631)
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(70, 10, 601, 121))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        ################## TABLE ###########################
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(70, 150, 601, 247))

        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(5)
        ############## ROWS and COLUMNS ####################
        item1 = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item1)
        item2 = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item2)
        item3 = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item3)
        item4 = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item4)
        item5 = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item5)
        item6 = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item6)
        item7 = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item7)
        item8 = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item8)
        item9 = QtGui.QTableWidgetItem()

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 580, 301, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(350, 580, 51, 31))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(610, 566, 99, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.spinBox.setRange(1,5)    

        self.retranslateUi(Dialog, final_list)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def retranslateUi(self, Dialog, final_list):
        d.load_current_user("data/us.user", current_user)
                
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))

        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Congratulations " + current_user[len(current_user)-1].name + "!!</span></p>\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">We found users which have similar preferences.</span></p>\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">You may be interested to see this 5 movies:</span></p></body></html>", None))
        
        item1 = self.tableWidget.verticalHeaderItem(0)
        item1.setText(_translate("Dialog", "1.", None))
        item2 = self.tableWidget.verticalHeaderItem(1)
        item2.setText(_translate("Dialog", "2.", None))
        item3 = self.tableWidget.verticalHeaderItem(2)
        item3.setText(_translate("Dialog", "3.", None))
        item4 = self.tableWidget.verticalHeaderItem(3)
        item4.setText(_translate("Dialog", "4.", None))
        item5 = self.tableWidget.verticalHeaderItem(4)
        item5.setText(_translate("Dialog", "5.", None))
        item6 = self.tableWidget.horizontalHeaderItem(0)
        item6.setText(_translate("Dialog", "Genre", None))
        item7 = self.tableWidget.horizontalHeaderItem(1)
        item7.setText(_translate("Dialog", "Movie", None))
        item8 = self.tableWidget.horizontalHeaderItem(2)
        item8.setText(_translate("Dialog", "Trailer", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.tableWidget.setColumnWidth(0, 210)
        self.tableWidget.setColumnWidth(1, 210)
        self.tableWidget.setColumnWidth(2, 157)

        #create the table with genres, title and trailer
        for index in range(5):
            self.tableWidget.setRowHeight(index, 44)
            # 1. genres
            str_genres_row1 = printGenres(final_list[index])
            item1 = QtGui.QTableWidgetItem(str_genres_row1)
            self.tableWidget.setItem(index,0,item1)  
            # 2. titles
            item2 = QtGui.QTableWidgetItem(str(final_list[index].title))
            self.tableWidget.setItem(index,1,item2)

#################### BUTTON - SEE THE TRAILER ###############################
        self.btn_sell1 = QtGui.QPushButton('See the Trailer!')
        self.btn_sell1.clicked.connect(lambda: self.open_webbrowser_trailer(final_list[0]))
        self.tableWidget.setCellWidget(0, 2, self.btn_sell1)

        self.btn_sell2 = QtGui.QPushButton('See the Trailer!')
        self.btn_sell2.clicked.connect(lambda: self.open_webbrowser_trailer(final_list[1]))
        self.tableWidget.setCellWidget(1, 2, self.btn_sell2)

        self.btn_sell3 = QtGui.QPushButton('See the Trailer!')
        self.btn_sell3.clicked.connect(lambda: self.open_webbrowser_trailer(final_list[2]))
        self.tableWidget.setCellWidget(2, 2, self.btn_sell3)

        self.btn_sell4 = QtGui.QPushButton('See the Trailer!')
        self.btn_sell4.clicked.connect(lambda: self.open_webbrowser_trailer(final_list[3]))
        self.tableWidget.setCellWidget(3, 2, self.btn_sell4)

        self.btn_sell5 = QtGui.QPushButton('See the Trailer!')
        self.btn_sell5.clicked.connect(lambda: self.open_webbrowser_trailer(final_list[4]))
        self.tableWidget.setCellWidget(4, 2, self.btn_sell5)


        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">Please give us your feedback: </span></p></body></html>", None))

        self.pushButton.setText(_translate("Dialog", "Close", None))
        self.pushButton.clicked.connect(lambda: self.closeDialogAndSaveTheFeedback())


    def open_webbrowser_trailer(self, movie):
        button = QtGui.qApp.focusWidget()
        index = self.tableWidget.indexAt(button.pos())
        if index.isValid():
            url = movie.imdb_url

            print movie.imdb_url
            print movie.title

            link_name = ""
            r = urllib2.Request(url, headers={ 'User-Agent': 'Chrome/52.0.2743.82' })
            html = urllib2.urlopen(r).read()
            soup = BeautifulSoup(html, "lxml")

            mydivs = soup.find_all("a", class_= "slate_button" )

            if len(mydivs) > 0:
                hrefVideo = mydivs[0].get("href")
                if hrefVideo !="":
                    webbrowser.open("http://www.imdb.com" + hrefVideo)
                    #open new information window
                    QtGui.QMessageBox.information(QtGui.QWidget(), "Information message", "A new window is opened in the current browser session to see the Trailer!")
                else:
                    webbrowser.open(url)
                    QtGui.QMessageBox.information(QtGui.QWidget(), "Information message", "Sorry no trailer available\nWe redirect you on the imdb Web Page!")
            else:
                webbrowser.open(url)
                QtGui.QMessageBox.information(QtGui.QWidget(), "Information message", "Sorry no trailer available\nWe redirect you on the imdb Web Page!")


    def closeDialogAndSaveTheFeedback(self):
        a = self.spinBox.value()
        currentUserFile = open('data/us.user', 'a')
        currentUserFile.write("|" + str(a))
        currentUserFile.close()

        sys.exit()


def printGenres(movie):
    genres_name =  movie.getGenres()
    str_for_table = ""
    for g in genres_name:
        if g == genres_name[len(genres_name)-1]:
            str_for_table = str_for_table + str(g) 
        else:
            str_for_table = str_for_table + str(g) + ", "

    return str_for_table

def main():
#if __name__ == '__main__': 
    #app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_FinalDialog()
    ui.setupUi(Form)
    Form.show()
    #sys.exit()
    sys.exit(app.exec_())

#main()
