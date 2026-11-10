from login import hoofdMenu
import datetime
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap, QIcon, QMovie
from PyQt5.QtCore import Qt, QRegExp, QSize
from PyQt5.QtWidgets import QLabel, QPushButton,QGridLayout,\
     QMessageBox, QDialog, QLineEdit, QCheckBox
from sqlalchemy import (Table, Column, Integer, String, MetaData, create_engine, Float)
from sqlalchemy.sql import select, update
import logging
logger = logging.getLogger(__name__)

def _11check(mwerknr):
    logger.warning(">>> Entering _11check(mwerknr=%s)", mwerknr, extra={"event.action": "_11check", "logrite.mwerknr": mwerknr})
    number = str(mwerknr)
    logger.debug("_11check(mwerknr=%s): number → %s", mwerknr, number, extra={"event.action": "_11check", "logrite.mwerknr": mwerknr})
    total = 0       
    fullnumber = number                       
    logger.debug("_11check(mwerknr=%s): total → %s", mwerknr, total, extra={"event.action": "_11check", "logrite.mwerknr": mwerknr})
    for i in range(8):
        total += int(fullnumber[i])*(9-i)
        logger.debug("_11check(mwerknr=%s): fullnumber → %s", mwerknr, fullnumber, extra={"event.action": "_11check", "logrite.mwerknr": mwerknr})
        checkdigit = total % 11 % 10
    if checkdigit == int(fullnumber[8]):
        return True
    else:
        logger.debug("<<< Exiting _11check(mwerknr=%s)", mwerknr, extra={"event.action": "_11check", "logrite.mwerknr": mwerknr})
        return False
    
def jaarweek():
    logger.warning(">>> Entering jaarweek()", extra={"event.action": "jaarweek"})
    dt = datetime.datetime.now()
    logger.debug("jaarweek(): dt → %s", dt, extra={"event.action": "jaarweek"})
    week = str('0'+str(dt.isocalendar()[1]))[-2:]
    logger.debug("jaarweek(): week → %s", week, extra={"event.action": "jaarweek"})
    jaar = str(dt.isocalendar()[0])
    jrwk = jaar+week
    logger.debug("jaarweek(): jaar → %s", jaar, extra={"event.action": "jaarweek"})
    logger.debug("jaarweek(): jrwk → %s", jrwk, extra={"event.action": "jaarweek"})
    logger.debug("<<< Exiting jaarweek()", extra={"event.action": "jaarweek"})
    return(jrwk)
    
def foutInvoer():
        logger.warning(">>> Entering foutInvoer()", extra={"event.action": "foutInvoer"})
        msg = QMessageBox()
        logger.debug("foutInvoer(): msg → %s", msg, extra={"event.action": "foutInvoer"})
        msg.setStyleSheet("color: black;  background-color: gainsboro")
        msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
        msg.setIcon(QMessageBox.Critical)
        msg.setText('Vereiste velden\nniet allen ingevoerd!')
        msg.setWindowTitle('Onjuiste invoer')
        logger.debug("<<< Exiting foutInvoer()", extra={"event.action": "foutInvoer"})
        msg.exec_()
      
def foutWerknr():
    logger.warning(">>> Entering foutWerknr()", extra={"event.action": "foutWerknr"})
    msg = QMessageBox()
    logger.debug("foutWerknr(): msg → %s", msg, extra={"event.action": "foutWerknr"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Werknummer niet gevonden\nWerknummer bestaat niet!')
    msg.setWindowTitle('Wijzi werken!')
    logger.debug("<<< Exiting foutWerknr()", extra={"event.action": "foutWerknr"})
    msg.exec_()
    
def werkGereed():
    logger.warning(">>> Entering werkGereed()", extra={"event.action": "werkGereed"})
    msg = QMessageBox()
    logger.debug("werkGereed(): msg → %s", msg, extra={"event.action": "werkGereed"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Werk is gereed\nboeken is niet meer mogelijk!')
    msg.setWindowTitle('Wijzig werken!')
    logger.debug("<<< Exiting werkGereed()", extra={"event.action": "werkGereed"})
    msg.exec_()
    
def updateOK():
    logger.warning(">>> Entering updateOK()", extra={"event.action": "updateOK"})
    msg = QMessageBox()
    logger.debug("updateOK(): msg → %s", msg, extra={"event.action": "updateOK"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('De gegevens zijn aangepast!')
    msg.setWindowTitle('Wijzig werken!')
    logger.debug("<<< Exiting updateOK()", extra={"event.action": "updateOK"})
    msg.exec_()
       
def winSluit(self, m_email):
    logger.warning(">>> Entering winSluit(m_email=%s)", m_email, extra={"event.action": "winSluit"})
    self.close()
    zoekWerk(m_email)
    logger.debug("<<< Exiting winSluit(m_email=%s)", m_email, extra={"event.action": "winSluit"})
    
def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
             
def zoekWerk(m_email):
    logger.warning(">>> Entering zoekWerk(m_email=%s)", m_email, extra={"event.action": "zoekWerk"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Modify works.")
            self.setWindowFlags(self.windowFlags() | Qt.WindowSystemMenuHint |
                                Qt.WindowMinMaxButtonsHint)
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Werknummer = QLabel()
            werknEdit = QLineEdit()
            werknEdit.setFixedWidth(100)
            werknEdit.setFont(QFont("Arial",10))
            werknEdit.textChanged.connect(self.werknChanged)
            reg_ex = QRegExp('^[8]{1}[0-9]{8}$')
            input_validator = QRegExpValidator(reg_ex, werknEdit)
            werknEdit.setValidator(input_validator)
                            
            grid = QGridLayout()
            grid.setSpacing(20)

            pyqt = QLabel()
            movie = QMovie('./images/logos/pyqt.gif')
            pyqt.setMovie(movie)
            movie.setScaledSize(QSize(240, 80))
            movie.start()
            grid.addWidget(pyqt, 0, 0, 1, 2)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1 ,1, Qt.AlignRight)
    
            self.setFont(QFont('Arial', 10))
         
            grid.addWidget(QLabel('Werknummer'), 1, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(werknEdit, 1, 1)
            
            applyBtn = QPushButton('Zoeken')
            applyBtn.clicked.connect(self.accept)
                     
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
       
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
           
            grid.addWidget(cancelBtn, 2, 0, 1, 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
           
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1 , 2, Qt.AlignCenter)
                        
            self.setLayout(grid)
            self.setGeometry(600, 300, 150, 150)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Omschrijving → %s", parent, self.Omschrijving, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q1Edit → %s", parent, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q1Edit → %s", self, parent, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Aanneemsom → %s", parent, self.Aanneemsom, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.mutPaid → %s", parent, self.mutPaid, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Huisvesting → %s", parent, self.Huisvesting, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q5aEdit → %s", parent, q5aEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q5aEdit → %s", self, parent, q5aEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.housing → %s", parent, self.housing, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q5bEdit → %s", parent, q5bEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q5bEdit → %s", self, parent, q5bEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Leiding → %s", parent, self.Leiding, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q6Edit → %s", parent, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q6Edit → %s", self, parent, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q6aEdit → %s", parent, q6aEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q6aEdit → %s", self, parent, q6aEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.direction → %s", parent, self.direction, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q6bEdit → %s", parent, q6bEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q6bEdit → %s", self, parent, q6bEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Inhuur → %s", parent, self.Inhuur, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q7Edit → %s", parent, q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q7Edit → %s", self, parent, q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q7aEdit → %s", parent, q7aEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q7aEdit → %s", self, parent, q7aEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.hiring → %s", parent, self.hiring, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q7bEdit → %s", parent, q7bEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q7bEdit → %s", self, parent, q7bEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Vervoer → %s", parent, self.Vervoer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q8aEdit → %s", parent, q8aEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q8aEdit → %s", self, parent, q8aEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.transport → %s", parent, self.transport, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q8bEdit → %s", parent, q8bEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q8bEdit → %s", self, parent, q8bEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Grondverzet → %s", parent, self.Grondverzet, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q11Edit → %s", parent, q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q11Edit → %s", self, parent, q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q11aEdit → %s", parent, q11aEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q11aEdit → %s", self, parent, q11aEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.earthmoving → %s", parent, self.earthmoving, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q11bEdit → %s", parent, q11bEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q11bEdit → %s", self, parent, q11bEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Overig → %s", parent, self.Overig, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q12Edit → %s", self, parent, q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q12Edit → %s", parent, q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q12aEdit → %s", self, parent, q12aEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q12aEdit → %s", parent, q12aEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.remaining → %s", parent, self.remaining, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q12bEdit → %s", self, parent, q12bEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q12bEdit → %s", parent, q12bEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.StartWerk → %s", parent, self.StartWerk, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q23Edit → %s", self, parent, q23Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q23Edit → %s", parent, q23Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl2 → %s", self, parent, lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl2 → %s", parent, lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl3 → %s", self, parent, lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl3 → %s", parent, lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl4 → %s", parent, lbl4, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl4 → %s", self, parent, lbl4, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl5 → %s", parent, lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl5 → %s", self, parent, lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl6 → %s", parent, lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl6 → %s", self, parent, lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl7a → %s", parent, lbl7a, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl7a → %s", self, parent, lbl7a, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl7b → %s", parent, lbl7b, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl7b → %s", self, parent, lbl7b, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl7c → %s", parent, lbl7c, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl7c → %s", self, parent, lbl7c, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl7 → %s", parent, lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl7 → %s", self, parent, lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl8 → %s", parent, lbl8, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl8 → %s", self, parent, lbl8, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl9 → %s", parent, lbl9, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl9 → %s", self, parent, lbl9, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl10 → %s", parent, lbl10, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl10 → %s", self, parent, lbl10, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl13 → %s", parent, lbl13, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl13 → %s", self, parent, lbl13, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl14 → %s", parent, lbl14, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl14 → %s", self, parent, lbl14, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lblwk → %s", parent, lblwk, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lblwk → %s", self, parent, lblwk, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lblst → %s", parent, lblst, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lblst → %s", self, parent, lblst, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl25 → %s", parent, lbl25, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl25 → %s", self, parent, lbl25, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl27 → %s", parent, lbl27, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl27 → %s", self, parent, lbl27, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl28 → %s", parent, lbl28, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl28 → %s", self, parent, lbl28, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): cBox2 → %s", parent, cBox2, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cBox2 → %s", self, parent, cBox2, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): cBox1 → %s", parent, cBox1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cBox1 → %s", self, parent, cBox1, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): cBox → %s", parent, cBox, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cBox → %s", self, parent, cBox, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pyqt → %s", parent, pyqt, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): pyqt → %s", self, parent, pyqt, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): movie → %s", parent, movie, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): movie → %s", self, parent, movie, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
    
        def werknChanged(self, text):
            logger.warning(">>> Entering werknChanged(text=%s)", text, extra={"event.action": "werknChanged", "logrite.text": text})
            self.Werknummer.setText(text)
            logger.debug("<<< Exiting werknChanged(text=%s)", text, extra={"event.action": "werknChanged", "logrite.text": text})
    
        def returnwerkn(self):
            logger.warning(">>> Entering returnwerkn()", extra={"event.action": "returnwerkn"})
            logger.debug("<<< Exiting returnwerkn()", extra={"event.action": "returnwerkn"})
            return self.Werknummer.text()
    
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnwerkn()]
    
    window = Widget()
    data = window.getData()
    import validZt
    if validZt.zt(data[0], 8):
        mwerknr = int(data[0])
    else:
        foutWerknr()
        zoekWerk(m_email)
        
    metadata = MetaData()
    werken = Table('werken', metadata,
        Column('werknummerID', Integer(), primary_key=True),
        Column('voortgangstatus', String))
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    s = select([werken]).where(werken.c.werknummerID == mwerknr)
    rp = conn.execute(s).first()
    if not rp:
        foutWerknr()
        zoekWerk(m_email)
    elif rp[1] == 'H':
        werkGereed()
        zoekWerk(m_email)
    else:
        wijzWerk(mwerknr, m_email)
 
def wijzWerk(mwerknr, m_email):
    logger.warning(">>> Entering wijzWerk(mwerknr=%s,m_email=%s)", mwerknr, m_email, extra={"event.action": "wijzWerk", "logrite.mwerknr": mwerknr})
    metadata = MetaData()
    logger.debug("wijzWerk(mwerknr=%s,m_email=%s): metadata → %s", mwerknr, m_email, metadata, extra={"event.action": "wijzWerk", "logrite.mwerknr": mwerknr})
    werken = Table('werken', metadata,
        Column('werknummerID', Integer(), primary_key=True),
        Column('werkomschrijving', String(50)),
        Column('voortgangstatus', String(1)),
        Column('statusweek',  String(6)),
        Column('aanneemsom', Float),
        Column('begr_materialen', Float),
        Column('begr_materieel', Float),
        Column('begr_huisv', Float),
        Column('begr_leiding', Float),
        Column('begr_inhuur', Float),
        Column('begr_vervoer', Float),
        Column('begr_beton_bvl', Float),
        Column('begr_kabelwerk', Float),
        Column('begr_grondverzet', Float),
        Column('begr_overig', Float),
        Column('begr_constr_uren', Float),
        Column('begr_mont_uren', Float),
        Column('begr_retourlas_uren', Float),
        Column('begr_telecom_uren', Float),
        Column('begr_bfi_uren', Float),
        Column('begr_bvl_uren', Float),
        Column('begr_spoorleg_uren', Float),
        Column('begr_spoorlas_uren', Float),
        Column('begr_voeding_uren', Float),
        Column('begr_lonen', Float),
        Column('startweek', String),
        Column('betaald_bedrag', Float),
        Column('meerminderwerk', Float),
        Column('kosten_materialen', Float),
        Column('kosten_lonen', Float),
        Column('kosten_materieel', Float),
        Column('kosten_leiding', Float),
        Column('kosten_huisv', Float),
        Column('kosten_overig', Float),
        Column('kosten_vervoer', Float),
        Column('kosten_inhuur', Float),
        Column('beton_bvl', Float),
        Column('kabelwerk', Float),
        Column('grondverzet', Float),
        Column('opdracht_datum', String))
               
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("wijzWerk(mwerknr=%s,m_email=%s): engine → %s", mwerknr, m_email, engine, extra={"event.action": "wijzWerk", "logrite.mwerknr": mwerknr})
    conn = engine.connect()
    logger.debug("wijzWerk(mwerknr=%s,m_email=%s): conn → %s", mwerknr, m_email, conn, extra={"event.action": "wijzWerk", "logrite.mwerknr": mwerknr})
    selwerk = select([werken]).where(werken.c.werknummerID == mwerknr)
    rpwerk = conn.execute(selwerk).first()
    logger.debug("wijzWerk(mwerknr=%s,m_email=%s): selwerk → %s", mwerknr, m_email, selwerk, extra={"event.action": "wijzWerk", "logrite.mwerknr": mwerknr})
    logger.debug("wijzWerk(mwerknr=%s,m_email=%s): rpwerk → %s", mwerknr, m_email, rpwerk, extra={"event.action": "wijzWerk", "logrite.mwerknr": mwerknr})
                                          
    class Widget(QDialog):
        logger.debug("<<< Exiting wijzWerk(mwerknr=%s,m_email=%s)", mwerknr, m_email, extra={"event.action": "wijzWerk", "logrite.mwerknr": mwerknr})
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Wijzig begroting werk")
            self.setWindowFlags(self.windowFlags() | Qt.WindowSystemMenuHint |
                                Qt.WindowMinMaxButtonsHint)
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                                  
            self.setFont(QFont('Arial', 10))
                                               
            self.Omschrijving = QLabel()
            q1Edit = QLineEdit(rpwerk[1])
            q1Edit.setFont(QFont("Arial",10))
            q1Edit.textChanged.connect(self.q1Changed) 
            reg_ex = QRegExp("^.{0,49}$")
            input_validator = QRegExpValidator(reg_ex, q1Edit)
            q1Edit.setValidator(input_validator)
                            
            self.Aanneemsom = QLabel()
            q2Edit = QLineEdit(str(round(float(rpwerk[4]),2)))
            q2Edit.setFixedWidth(150)
            q2Edit.setAlignment(Qt.AlignRight)
            q2Edit.setFont(QFont("Arial",10))
            q2Edit.setDisabled(True)
            q2Edit.textChanged.connect(self.q2Changed)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q2Edit)
            q2Edit.setValidator(input_validator)

            # paid sum
            q3Edit = QLineEdit(str(round(float(rpwerk[26]), 2)))
            q3Edit.setFixedWidth(150)
            q3Edit.setAlignment(Qt.AlignRight)
            q3Edit.setFont(QFont("Arial", 10))
            q3Edit.setDisabled(True)

            self.mutPaid = QLabel()
            q4Edit = QLineEdit('0')
            q4Edit.setFixedWidth(150)
            q4Edit.setAlignment(Qt.AlignRight)
            q4Edit.setFont(QFont("Arial", 10))
            q4Edit.textChanged.connect(self.q4Changed)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q4Edit)
            q4Edit.setValidator(input_validator)

            self.Huisvesting = QLabel()
            q5Edit = QLineEdit(str(round(float(rpwerk[7]),2)))
            q5Edit.setFixedWidth(150)
            q5Edit.setAlignment(Qt.AlignRight)
            q5Edit.setFont(QFont("Arial",10))
            q5Edit.textChanged.connect(self.q5Changed) 
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q5Edit)
            q5Edit.setValidator(input_validator)

            # costs housing
            q5aEdit = QLineEdit(str(round(float(rpwerk[32]), 2)))
            q5aEdit.setFixedWidth(150)
            q5aEdit.setAlignment(Qt.AlignRight)
            q5aEdit.setFont(QFont("Arial", 10))
            q5aEdit.setDisabled(True)

            self.housing = QLabel() # mutate housing
            q5bEdit = QLineEdit('0')
            q5bEdit.setFixedWidth(150)
            q5bEdit.setAlignment(Qt.AlignRight)
            q5bEdit.setFont(QFont("Arial", 10))
            q5bEdit.textChanged.connect(self.q5bChanged)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q5bEdit)
            q5bEdit.setValidator(input_validator)
            
            self.Leiding = QLabel()
            q6Edit = QLineEdit(str(round(float(rpwerk[8]),2)))
            q6Edit.setFixedWidth(150)
            q6Edit.setAlignment(Qt.AlignRight)
            q6Edit.setFont(QFont("Arial",10))
            q6Edit.textChanged.connect(self.q6Changed) 
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q6Edit)
            q6Edit.setValidator(input_validator)

            # costs direction
            q6aEdit = QLineEdit(str(round(float(rpwerk[31]), 2)))
            q6aEdit.setFixedWidth(150)
            q6aEdit.setAlignment(Qt.AlignRight)
            q6aEdit.setFont(QFont("Arial", 10))
            q6aEdit.setDisabled(True)

            self.direction = QLabel() # mutate direction
            q6bEdit = QLineEdit('0')
            q6bEdit.setFixedWidth(150)
            q6bEdit.setAlignment(Qt.AlignRight)
            q6bEdit.setFont(QFont("Arial", 10))
            q6bEdit.textChanged.connect(self.q6bChanged)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q6bEdit)
            q6bEdit.setValidator(input_validator)

            self.Inhuur = QLabel()
            q7Edit = QLineEdit(str(round(float(rpwerk[9]),2)))
            q7Edit.setFixedWidth(150)
            q7Edit.setAlignment(Qt.AlignRight)
            q7Edit.setFont(QFont("Arial",10))
            q7Edit.textChanged.connect(self.q7Changed) 
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q7Edit)
            q7Edit.setValidator(input_validator)

            # costs hiring
            q7aEdit = QLineEdit(str(round(float(rpwerk[35]), 2)))
            q7aEdit.setFixedWidth(150)
            q7aEdit.setAlignment(Qt.AlignRight)
            q7aEdit.setFont(QFont("Arial", 10))
            q7aEdit.setDisabled(True)

            self.hiring = QLabel()  # mutate hiring
            q7bEdit = QLineEdit('0')
            q7bEdit.setFixedWidth(150)
            q7bEdit.setAlignment(Qt.AlignRight)
            q7bEdit.setFont(QFont("Arial", 10))
            q7bEdit.textChanged.connect(self.q7bChanged)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q7bEdit)
            q7bEdit.setValidator(input_validator)
            
            self.Vervoer = QLabel()
            q8Edit = QLineEdit(str(round(float(rpwerk[10]),2)))
            q8Edit.setFixedWidth(150)
            q8Edit.setAlignment(Qt.AlignRight)
            q8Edit.setFont(QFont("Arial",10))
            q8Edit.textChanged.connect(self.q8Changed) 
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q8Edit)
            q8Edit.setValidator(input_validator)

            # costs transport
            q8aEdit = QLineEdit(str(round(float(rpwerk[34]),2)))
            q8aEdit.setFixedWidth(150)
            q8aEdit.setAlignment(Qt.AlignRight)
            q8aEdit.setFont(QFont("Arial", 10))
            q8aEdit.setDisabled(True)

            self.transport = QLabel()      # mutate transport
            q8bEdit = QLineEdit('0')
            q8bEdit.setFixedWidth(150)
            q8bEdit.setAlignment(Qt.AlignRight)
            q8bEdit.setFont(QFont("Arial", 10))
            q8bEdit.textChanged.connect(self.q8bChanged)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q8bEdit)
            q8bEdit.setValidator(input_validator)

            self.Grondverzet = QLabel()
            q11Edit = QLineEdit(str(round(float(rpwerk[13]),2)))
            q11Edit.setFixedWidth(150)
            q11Edit.setAlignment(Qt.AlignRight)
            q11Edit.setFont(QFont("Arial",10))
            q11Edit.textChanged.connect(self.q11Changed) 
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q11Edit)
            q11Edit.setValidator(input_validator)

            # costs earthmoving
            q11aEdit = QLineEdit(str(round(float(rpwerk[38]), 2)))
            q11aEdit.setFixedWidth(150)
            q11aEdit.setAlignment(Qt.AlignRight)
            q11aEdit.setFont(QFont("Arial", 10))
            q11aEdit.setDisabled(True)

            self.earthmoving = QLabel()      # mutate earthmoving
            q11bEdit = QLineEdit('0')
            q11bEdit.setFixedWidth(150)
            q11bEdit.setAlignment(Qt.AlignRight)
            q11bEdit.setFont(QFont("Arial", 10))
            q11bEdit.textChanged.connect(self.q8bChanged)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q11bEdit)
            q11bEdit.setValidator(input_validator)
            
            self.Overig = QLabel()
            q12Edit = QLineEdit(str(round(float(rpwerk[14]),2)))
            q12Edit.setFixedWidth(150)
            q12Edit.setAlignment(Qt.AlignRight)
            q12Edit.setFont(QFont("Arial",10))
            q12Edit.textChanged.connect(self.q12Changed) 
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q12Edit)
            q12Edit.setValidator(input_validator)

            # costs remaining
            q12aEdit = QLineEdit(str(round(float(rpwerk[33]),2)))
            q12aEdit.setFixedWidth(150)
            q12aEdit.setAlignment(Qt.AlignRight)
            q12aEdit.setFont(QFont("Arial", 10))
            q12aEdit.setDisabled(True)

            self.remaining = QLabel()    # mutate remaining
            q12bEdit = QLineEdit('0')
            q12bEdit.setFixedWidth(150)
            q12bEdit.setAlignment(Qt.AlignRight)
            q12bEdit.setFont(QFont("Arial", 10))
            q12bEdit.textChanged.connect(self.q12bChanged)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q12bEdit)
            q12bEdit.setValidator(input_validator)

            self.StartWerk = QLabel()
            q23Edit = QLineEdit(str(rpwerk[25]))
            q23Edit.setFixedWidth(80)
            q23Edit.setFont(QFont("Arial",10))
            q23Edit.textChanged.connect(self.q23Changed) 
            reg_ex = QRegExp("^[2]{1}[0]{1}[0-9]{2}[0-5]{1}[0-9]{1}$")
            input_validator = QRegExpValidator(reg_ex, q23Edit)
            q23Edit.setValidator(input_validator)

            grid = QGridLayout()
            grid.setSpacing(20)
            
            lbl1 = QLabel('Werknummer')
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 1, 0)
            
            lbl2 = QLabel(str(mwerknr))
            grid.addWidget(lbl2, 1, 1)
                   
            lbl3 = QLabel('Omschrijving')
            lbl3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl3, 2, 0)
            grid.addWidget(q1Edit, 2, 1, 1, 3) # RowSpan 1 ,ColumnSpan 3
                                                 
            lbl4 = QLabel('Aanneemsom')
            lbl4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl4, 3, 0)
            grid.addWidget(q2Edit, 3, 1)

            lbl5 = QLabel('Betaald bedrag')
            grid.addWidget(lbl5, 6, 0)
            grid.addWidget(q3Edit, 6, 1)

            lbl6 = QLabel('Mutatie betaald bedrag')
            grid.addWidget(lbl6, 6, 2)
            grid.addWidget(q4Edit, 6, 3)

            lbl7a = QLabel('Stelpost / Bedrag stelpost')
            lbl7a.setStyleSheet("font: 12pt Comic Sans MS; color: #000000")
            grid.addWidget(lbl7a, 8, 0, 1, 2, Qt.AlignCenter)

            lbl7b = QLabel('Kosten stelposten')
            lbl7b.setStyleSheet("font: 12pt Comic Sans MS; color: #000000")
            grid.addWidget(lbl7b, 8, 2)

            lbl7c = QLabel('Muteren kosten')
            lbl7c.setStyleSheet("font: 12pt Comic Sans MS; color: #000000")
            grid.addWidget(lbl7c, 8, 3)

            lbl7 = QLabel('Huisvesting')
            lbl7.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl7, 9, 0)
            grid.addWidget(q5Edit, 9, 1)

            grid.addWidget(q5aEdit, 9, 2)
            grid.addWidget(q5bEdit, 9, 3)

            lbl8 = QLabel('Leiding')
            lbl8.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl8, 10, 0)
            grid.addWidget(q6Edit, 10, 1)
            grid.addWidget(q6aEdit, 10, 2)
            grid.addWidget(q6bEdit, 10, 3)
            
            lbl9 = QLabel('Inhuur')
            lbl9.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl9, 11, 0)
            grid.addWidget(q7Edit, 11, 1)
            grid.addWidget(q7aEdit, 11, 2)
            grid.addWidget(q7bEdit, 11, 3)
            
            lbl10 = QLabel('Transport')
            lbl10.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl10, 12, 0)
            grid.addWidget(q8Edit, 12, 1)
            grid.addWidget(q8aEdit, 12, 2)
            grid.addWidget(q8bEdit, 12, 3)

            lbl13 = QLabel('Grondverzet')
            lbl13.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl13, 13, 0)
            grid.addWidget(q11Edit, 13, 1)
            grid.addWidget(q11aEdit, 13, 2)
            grid.addWidget(q11bEdit, 13, 3)
            
            lbl14 = QLabel('Overig')
            lbl14.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl14, 14, 0)
            grid.addWidget(q12Edit, 14, 1)
            grid.addWidget(q12aEdit, 14, 2)
            grid.addWidget(q12bEdit, 14, 3)
            
            lblwk = QLabel('Status-Jaarweek')
            lblwk.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lblwk, 1,2)
            lblst = QLabel(rpwerk[2]+'  '+rpwerk[3])
            grid.addWidget(lblst,1,3)

            lbl25 = QLabel('Startweek werk')
            lbl25.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl25, 4, 2)
            grid.addWidget(q23Edit, 4, 3)

            lbl27 = QLabel('Order datum')
            grid.addWidget(lbl27, 4, 0, 1, 1, Qt.AlignRight)
            lbl28 =QLabel(rpwerk[39])
            grid.addWidget(lbl28, 4, 1)

            cBox2 = QCheckBox('Order')
            cBox2.stateChanged.connect(self.cBox2Changed)
            if rpwerk[39]:
                cBox2.setDisabled(True)
            grid.addWidget(cBox2, 5, 1)
            
            cBox1 = QCheckBox('Meer/minder\nwerk goedgekeurd')
            cBox1.stateChanged.connect(self.cBox1Changed)
            if rpwerk[2] != 'F':
                cBox1.setDisabled(True)
            grid.addWidget(cBox1, 5, 2)
            
            cBox = QCheckBox('Werk gereed')
            cBox.stateChanged.connect(self.cBoxChanged)
            if rpwerk[2] != 'G':
                cBox.setDisabled(True)
            grid.addWidget(cBox, 5, 3)

            pyqt = QLabel()
            movie = QMovie('./images/logos/pyqt.gif')
            pyqt.setMovie(movie)
            movie.setScaledSize(QSize(240, 80))
            movie.start()
            grid.addWidget(pyqt, 0, 0, 1, 2)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 3, 1, 1, Qt.AlignRight)
                                            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 19, 0, 1, 4, Qt.AlignCenter)
              
            self.setLayout(grid)
            self.setGeometry(600, 100, 150, 150)
    
            applyBtn = QPushButton('Wijzig')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 18, 3, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: winSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 18, 2, 1 , 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                       
        def q1Changed(self,text):
            logger.warning(">>> Entering q1Changed(text=%s)", text, extra={"event.action": "q1Changed", "logrite.text": text})
            self.Omschrijving.setText(text)
            logger.debug("<<< Exiting q1Changed(text=%s)", text, extra={"event.action": "q1Changed", "logrite.text": text})
    
        def q2Changed(self,text):
            logger.warning(">>> Entering q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
            self.Aanneemsom.setText(text)
            logger.debug("<<< Exiting q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})

        def q4Changed(self, text):
            logger.warning(">>> Entering q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
            logger.debug("q4Changed(self=%s,text=%s): mutPaid → %s", self, text, mutPaid, extra={"event.action": "q4Changed", "logrite.text": text})
            self.mutPaid.setText(text)
            logger.debug("<<< Exiting q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})

        def q5Changed(self,text):
            logger.warning(">>> Entering q5Changed(text=%s)", text, extra={"event.action": "q5Changed", "logrite.text": text})
            self.Huisvesting.setText(text)
            logger.debug("<<< Exiting q5Changed(text=%s)", text, extra={"event.action": "q5Changed", "logrite.text": text})

        def q5bChanged(self,text):
            logger.warning(">>> Entering q5bChanged(text=%s)", text, extra={"event.action": "q5bChanged", "logrite.text": text})
            logger.debug("q5bChanged(self=%s,text=%s): housing → %s", self, text, housing, extra={"event.action": "q5bChanged", "logrite.text": text})
            self.housing.setText(text)
            logger.debug("<<< Exiting q5bChanged(text=%s)", text, extra={"event.action": "q5bChanged", "logrite.text": text})

        def q6Changed(self,text):
            logger.warning(">>> Entering q6Changed(text=%s)", text, extra={"event.action": "q6Changed", "logrite.text": text})
            self.Leiding.setText(text)
            logger.debug("<<< Exiting q6Changed(text=%s)", text, extra={"event.action": "q6Changed", "logrite.text": text})

        def q6bChanged(self,text):
            logger.warning(">>> Entering q6bChanged(text=%s)", text, extra={"event.action": "q6bChanged", "logrite.text": text})
            logger.debug("q6bChanged(self=%s,text=%s): direction → %s", self, text, direction, extra={"event.action": "q6bChanged", "logrite.text": text})
            self.direction.setText(text)
            logger.debug("<<< Exiting q6bChanged(text=%s)", text, extra={"event.action": "q6bChanged", "logrite.text": text})
            
        def q7Changed(self,text):
            logger.warning(">>> Entering q7Changed(text=%s)", text, extra={"event.action": "q7Changed", "logrite.text": text})
            self.Inhuur.setText(text)
            logger.debug("<<< Exiting q7Changed(text=%s)", text, extra={"event.action": "q7Changed", "logrite.text": text})

        def q7bChanged(self,text):
            logger.warning(">>> Entering q7bChanged(text=%s)", text, extra={"event.action": "q7bChanged", "logrite.text": text})
            logger.debug("q7bChanged(self=%s,text=%s): hiring → %s", self, text, hiring, extra={"event.action": "q7bChanged", "logrite.text": text})
            self.hiring.setText(text)
            logger.debug("<<< Exiting q7bChanged(text=%s)", text, extra={"event.action": "q7bChanged", "logrite.text": text})
            
        def q8Changed(self,text):
            logger.warning(">>> Entering q8Changed(text=%s)", text, extra={"event.action": "q8Changed", "logrite.text": text})
            self.Vervoer.setText(text)
            logger.debug("<<< Exiting q8Changed(text=%s)", text, extra={"event.action": "q8Changed", "logrite.text": text})

        def q8bChanged(self,text):
            logger.warning(">>> Entering q8bChanged(text=%s)", text, extra={"event.action": "q8bChanged", "logrite.text": text})
            logger.debug("q8bChanged(self=%s,text=%s): transport → %s", self, text, transport, extra={"event.action": "q8bChanged", "logrite.text": text})
            self.transport.setText(text)
            logger.debug("<<< Exiting q8bChanged(text=%s)", text, extra={"event.action": "q8bChanged", "logrite.text": text})
        
        def q11Changed(self,text):
            logger.warning(">>> Entering q11Changed(text=%s)", text, extra={"event.action": "q11Changed", "logrite.text": text})
            self.Grondverzet.setText(text)
            logger.debug("<<< Exiting q11Changed(text=%s)", text, extra={"event.action": "q11Changed", "logrite.text": text})

        def q11bChanged(self,text):
            logger.warning(">>> Entering q11bChanged(text=%s)", text, extra={"event.action": "q11bChanged", "logrite.text": text})
            logger.debug("q11bChanged(self=%s,text=%s): earthmoving → %s", self, text, earthmoving, extra={"event.action": "q11bChanged", "logrite.text": text})
            self.earthmoving.setText(text)
            logger.debug("<<< Exiting q11bChanged(text=%s)", text, extra={"event.action": "q11bChanged", "logrite.text": text})
            
        def q12Changed(self,text):
            logger.warning(">>> Entering q12Changed(text=%s)", text, extra={"event.action": "q12Changed", "logrite.text": text})
            self.Overig.setText(text)
            logger.debug("<<< Exiting q12Changed(text=%s)", text, extra={"event.action": "q12Changed", "logrite.text": text})

        def q12bChanged(self,text):
            logger.warning(">>> Entering q12bChanged(text=%s)", text, extra={"event.action": "q12bChanged", "logrite.text": text})
            logger.debug("q12bChanged(self=%s,text=%s): remaining → %s", self, text, remaining, extra={"event.action": "q12bChanged", "logrite.text": text})
            self.remaining.setText(text)
            logger.debug("<<< Exiting q12bChanged(text=%s)", text, extra={"event.action": "q12bChanged", "logrite.text": text})

        def q23Changed(self,text):
            logger.warning(">>> Entering q23Changed(text=%s)", text, extra={"event.action": "q23Changed", "logrite.text": text})
            self.Startwerk.setText(text)
            logger.debug("<<< Exiting q23Changed(text=%s)", text, extra={"event.action": "q23Changed", "logrite.text": text})

        state = False
        def cBoxChanged(self, state):
            logger.warning(">>> Entering cBoxChanged(state=%s)", state, extra={"event.action": "cBoxChanged", "logrite.state": state})
            logger.debug("cBoxChanged(state=%s): self.state → %s", state, self.state, extra={"event.action": "cBoxChanged", "logrite.state": state})
            logger.debug("cBoxChanged(self=%s,state=%s): self.state → %s", self, state, self.state, extra={"event.action": "cBoxChanged", "logrite.state": state})
            if state == Qt.Checked:
                self.state = True
                logger.debug("<<< Exiting cBoxChanged(state=%s)", state, extra={"event.action": "cBoxChanged", "logrite.state": state})

        state1 = False  
        def cBox1Changed(self, state1):
            logger.warning(">>> Entering cBox1Changed(state1=%s)", state1, extra={"event.action": "cBox1Changed", "logrite.state1": state1})
            logger.debug("cBox1Changed(self=%s,state1=%s): self.state1 → %s", self, state1, self.state1, extra={"event.action": "cBox1Changed", "logrite.state1": state1})
            if state1 == Qt.Checked:
                logger.debug("<<< Exiting cBox1Changed(state1=%s)", state1, extra={"event.action": "cBox1Changed", "logrite.state1": state1})
                self.state1 = True

        state2 = False  
        def cBox2Changed(self, state2):
            logger.warning(">>> Entering cBox2Changed(state2=%s)", state2, extra={"event.action": "cBox2Changed", "logrite.state2": state2})
            logger.debug("cBox2Changed(self=%s,state2=%s): self.state2 → %s", self, state2, self.state2, extra={"event.action": "cBox2Changed", "logrite.state2": state2})
            if state2 == Qt.Checked:
                logger.debug("<<< Exiting cBox2Changed(state2=%s)", state2, extra={"event.action": "cBox2Changed", "logrite.state2": state2})
                self.state2 = True

        def returnq1(self):
            logger.warning(">>> Entering returnq1()", extra={"event.action": "returnq1"})
            logger.debug("<<< Exiting returnq1()", extra={"event.action": "returnq1"})
            return self.Omschrijving.text()
        
        def returnq2(self):
            logger.warning(">>> Entering returnq2()", extra={"event.action": "returnq2"})
            logger.debug("<<< Exiting returnq2()", extra={"event.action": "returnq2"})
            return self.Aanneemsom.text()

        def returnq4(self):
            logger.warning(">>> Entering returnq4()", extra={"event.action": "returnq4"})
            logger.debug("<<< Exiting returnq4()", extra={"event.action": "returnq4"})
            return  self.mutPaid.text()
        
        def returnq5(self):
            logger.warning(">>> Entering returnq5()", extra={"event.action": "returnq5"})
            logger.debug("<<< Exiting returnq5()", extra={"event.action": "returnq5"})
            return self.Huisvesting.text()

        def returnq5b(self):
            logger.warning(">>> Entering returnq5b()", extra={"event.action": "returnq5b"})
            logger.debug("<<< Exiting returnq5b()", extra={"event.action": "returnq5b"})
            return self.housing.text()
    
        def returnq6(self):
            logger.warning(">>> Entering returnq6()", extra={"event.action": "returnq6"})
            logger.debug("<<< Exiting returnq6()", extra={"event.action": "returnq6"})
            return self.Leiding.text()

        def returnq6b(self):
            logger.warning(">>> Entering returnq6b()", extra={"event.action": "returnq6b"})
            logger.debug("<<< Exiting returnq6b()", extra={"event.action": "returnq6b"})
            return self.direction.text()
        
        def returnq7(self):
            logger.warning(">>> Entering returnq7()", extra={"event.action": "returnq7"})
            logger.debug("<<< Exiting returnq7()", extra={"event.action": "returnq7"})
            return self.Inhuur.text()

        def returnq7b(self):
            logger.warning(">>> Entering returnq7b()", extra={"event.action": "returnq7b"})
            logger.debug("<<< Exiting returnq7b()", extra={"event.action": "returnq7b"})
            return self.hiring.text()
              
        def returnq8(self):
            logger.warning(">>> Entering returnq8()", extra={"event.action": "returnq8"})
            logger.debug("<<< Exiting returnq8()", extra={"event.action": "returnq8"})
            return self.Vervoer.text()

        def returnq8b(self):
            logger.warning(">>> Entering returnq8b()", extra={"event.action": "returnq8b"})
            logger.debug("<<< Exiting returnq8b()", extra={"event.action": "returnq8b"})
            return self.transport.text()

        def returnq11(self):
            logger.warning(">>> Entering returnq11()", extra={"event.action": "returnq11"})
            logger.debug("<<< Exiting returnq11()", extra={"event.action": "returnq11"})
            return self.Grondverzet.text()

        def returnq11b(self):
            logger.warning(">>> Entering returnq11b()", extra={"event.action": "returnq11b"})
            logger.debug("<<< Exiting returnq11b()", extra={"event.action": "returnq11b"})
            return self.earthmoving.text()
        
        def returnq12(self):
            logger.warning(">>> Entering returnq12()", extra={"event.action": "returnq12"})
            logger.debug("<<< Exiting returnq12()", extra={"event.action": "returnq12"})
            return self.Overig.text()

        def returnq12b(self):
            logger.warning(">>> Entering returnq12b()", extra={"event.action": "returnq12b"})
            logger.debug("<<< Exiting returnq12b()", extra={"event.action": "returnq12b"})
            return self.remaining.text()
        
        def returnq23(self):
            logger.warning(">>> Entering returnq23()", extra={"event.action": "returnq23"})
            logger.debug("<<< Exiting returnq23()", extra={"event.action": "returnq23"})
            return self.StartWerk.text()

        def returncBox(self):
            logger.warning(">>> Entering returncBox()", extra={"event.action": "returncBox"})
            logger.debug("<<< Exiting returncBox()", extra={"event.action": "returncBox"})
            return self.state
        
        def returncBox1(self):
            logger.warning(">>> Entering returncBox1()", extra={"event.action": "returncBox1"})
            logger.debug("<<< Exiting returncBox1()", extra={"event.action": "returncBox1"})
            return self.state1
        
        def returncBox2(self):
            logger.warning(">>> Entering returncBox2()", extra={"event.action": "returncBox2"})
            logger.debug("<<< Exiting returncBox2()", extra={"event.action": "returncBox2"})
            return self.state2
        
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            return [dialog.returnq1(), dialog.returnq2(),dialog.returnq4(),dialog.returnq5(), dialog.returnq5b(),\
                    dialog.returnq6(), dialog.returnq6b(), dialog.returnq7(),dialog.returnq7b(), dialog.returnq8(),\
                    dialog.returnq8b(), dialog.returnq11(), dialog.returnq11b(), dialog.returnq12(),dialog.returnq12b(),\
                    dialog.returnq23(), dialog.returncBox(), dialog.returncBox1(), dialog.returncBox2()]
                       
    window = Widget()
    data = window.getData()
    if data[0]:
        ms0 = str(data[0])  #werkomschrijving
    else:
        ms0 = rpwerk[1]
    if data[1]:
        mf1 = float(data[1]) # aanneemsom
    else:
        mf1 = rpwerk[4]
    if data[2]:
        mf2 = float(data[2])  # mut betaling
    else:
        mf2 = 0
    if data[3]:
        mf3 = float(data[3])  #begr  huisv
    else:
        mf3 = rpwerk[7]
    if data[4]:
        mf4 = float(data[4])  #mut huisv
    else:
        mf4 = 0
    if data[5]:
        mf5 = float(data[5])  #begr leiding
    else:
        mf5 = rpwerk[8]
    if data[6]:
        mf6 = float(data[6]) # mut leiding
    else:
        mf6 = 0
    if data[7]:
        mf7 = float(data[7]) # begr inhuur
    else:
        mf7 = rpwerk[9]
    if data[8]:
        mf8 = float(data[8]) #mut inhuur
    else:
        mf8 = 0
    if data[9]:
        mf9 = float(data[9]) #begr vervoer
    else:
        mf9 = rpwerk[10]
    if data[10]:
        mf10 = float(data[10])  # mut vervoer
    else:
        mf10 = 0
    if data[11]:
        mf11 = float(data[11]) #begr grondverzet
    else:
        mf11 = rpwerk[13]
    if data[12]:
        mf12 = float(data[12]) # mut grondverzet
    else:
        mf12 = 0
    if data[13]:
        mf13 = float(data[13]) # begr overig
    else:
        mf13 = rpwerk[14]
    if data[14]:
        mf14 = float(data[14]) # mut overig
    else:
        mf14 = 0
    if data[15]:
        mf15 = str(data[15])  # startweek
    else:
        mf15 = rpwerk[25]
    if data[17]:
        mvgangst = 'G'
        mstatwk = jaarweek()
    elif data[16]:
        mvgangst = 'H'
        mstatwk =  jaarweek()
    else:
        mvgangst = rpwerk[2]
        mstatwk = rpwerk[3]
    if data[18]:
        mopdrdatum = str(datetime.datetime.now())[0:10]
    else:
        mopdrdatum = rpwerk[39]
                   
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()        
    uwrk = update(werken).where(werken.c.werknummerID == mwerknr).values(\
        werkomschrijving = ms0, aanneemsom = mf1, betaald_bedrag = werken.c.betaald_bedrag + mf2, begr_huisv = mf3,\
        kosten_huisv = werken.c.kosten_huisv + mf4, begr_leiding = mf5, kosten_leiding = werken.c.kosten_leiding + mf6,\
        begr_inhuur = mf7, kosten_inhuur = werken.c.kosten_inhuur + mf8 , begr_vervoer = mf9,\
        kosten_vervoer = werken.c.kosten_vervoer + mf10, begr_grondverzet = mf11, grondverzet = werken.c.grondverzet + mf12,\
        begr_overig = mf13, kosten_overig = werken.c.kosten_overig + mf14, startweek = mf15, statusweek = mstatwk,\
        voortgangstatus = mvgangst, opdracht_datum = mopdrdatum)
    conn.execute(uwrk)
    conn.close()
    updateOK() 
    zoekWerk(m_email)