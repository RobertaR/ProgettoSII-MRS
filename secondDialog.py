#### PROGETTO SII - MOVIE RECOMMENDER SYSTEM

#### ROBERTA ROMANO

from bs4 import BeautifulSoup
import urllib
import urllib2
import webbrowser

from PyQt4 import QtCore, QtGui
import sys
import ManageTheDialogs

movies = ManageTheDialogs.getMovies()

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        movie = movies[0]
        description = openDescription()

        ##################### STRUTTURA ####################################
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 647)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 10, 621, 23))
        self.progressBar.setProperty("value", 1)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(-10, 0, 661, 651))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 659, 649))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(280, 480, 81, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.RateNumber = QtGui.QSpinBox(self.scrollAreaWidgetContents)
        self.RateNumber.setGeometry(QtCore.QRect(280, 510, 81, 31))
        self.RateNumber.setObjectName(_fromUtf8("RateNumber"))
        self.textBrowser = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(80, 80, 501, 41))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_2.setGeometry(QtCore.QRect(80, 130, 501, 261))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.scrollAreaWidgetContents)
        self.commandLinkButton.setGeometry(QtCore.QRect(240, 40, 191, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(170, 420, 81, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_3.setGeometry(QtCore.QRect(260, 420, 256, 31))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(480, 590, 121, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.scrollArea.raise_()
        self.progressBar.raise_()

        self.retranslateUi(Dialog, movie, description)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        ##################### RATING ##########################################
        self.RateNumber.setRange(1,5)        
        
    def retranslateUi(self, Dialog, movie, description):
        genre_m = movie.getGenres()
        Dialog.setWindowTitle(_translate("Dialog", "MovieRecommenderSystem", None))
        ##################### PROGRESS BAR ####################################
        self.progressBar.setProperty("value", 10*(10 - len(movies)))
        ##################### COMMAND LINK ####################################
        self.commandLinkButton.setText(_translate("Dialog", "See the Trailer!", None))
        self.commandLinkButton.clicked.connect(self.open_webbrowser)

        self.pushButton.setText(_translate("Dialog", "Next", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Rate:</span></p></body></html>", None))
        ##################### TITLE ###########################################
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">" + movie.title + "</span></p></body></html>", None))

        ##################### DESCRIPTION #####################################
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">" + description + "</span></p></body></html>", None))

        ##################### GENRE ###########################################
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Genre:</span></p></body></html>", None))

        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">" + str(genre_m[0]) + "</span></p></body></html>", None))

        ##################### NEXT ############################################
        self.pushButton.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.nextButton)


    def nextButton(self):
        ### SALVA RATING ###
        a = self.RateNumber.value()
        ManageTheDialogs.addValues(movies[0], a)


    def open_webbrowser(self):
        url = movies[0].imdb_url
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

def openDescription():
    url = movies[0].imdb_url

    r = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
    html = urllib2.urlopen(r).read()

    soup = BeautifulSoup(html, "lxml")
    mydivs = soup.find_all("div", class_= "summary_text" )

    if len(mydivs) > 0:
        if mydivs[0].a == None:
            count = 0
            description = mydivs[0].getText()
            for lettera in description:
                if lettera == " " or lettera == "\n":
                    count += 1
                else:
                    description = description[count:]
                    break
        else:
            hrefSummary = mydivs[0].a
            req = urllib2.Request("http://www.imdb.com" + hrefSummary.get("href"), headers={ 'User-Agent': 'Mozilla/5.0' })
            summary = urllib2.urlopen(req).read()
            soupSumm = BeautifulSoup(summary, "lxml")
            plotSumm = soupSumm.find_all("p", class_= "plotSummary" )

            if len(plotSumm) > 0:
                description = plotSumm[0].getText()
    else:
        description = "no description available"

    return description


def main():
#if __name__ == '__main__': 
    #app1 = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
