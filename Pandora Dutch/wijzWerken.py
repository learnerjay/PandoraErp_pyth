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
    logger.debug(">>> Entering _11check(mwerknr=%s)", mwerknr)
    number = str(mwerknr)
    logger.debug("_11check(mwerknr=%s): number → %s", mwerknr, number)
    total = 0       
    fullnumber = number                       
    logger.debug("_11check(mwerknr=%s): total → %s", mwerknr, total)
    for i in range(8):
        total += int(fullnumber[i])*(9-i)
        logger.debug("_11check(mwerknr=%s): fullnumber → %s", mwerknr, fullnumber)
        checkdigit = total % 11 % 10
    if checkdigit == int(fullnumber[8]):
        return True
    else:
        logger.debug("<<< Exiting _11check(mwerknr=%s)", mwerknr)
        return False
    
def jaarweek():
    logger.debug(">>> Entering jaarweek()")
    dt = datetime.datetime.now()
    logger.debug("jaarweek(): dt → %s", dt)
    week = str('0'+str(dt.isocalendar()[1]))[-2:]
    logger.debug("jaarweek(): week → %s", week)
    jaar = str(dt.isocalendar()[0])
    jrwk = jaar+week
    logger.debug("jaarweek(): jrwk → %s", jrwk)
    logger.debug("jaarweek(): jaar → %s", jaar)
    logger.debug("<<< Exiting jaarweek()")
    return(jrwk)
    
def foutInvoer():
        logger.debug(">>> Entering foutInvoer()")
        msg = QMessageBox()
        logger.debug("foutInvoer(): msg → %s", msg)
        msg.setStyleSheet("color: black;  background-color: gainsboro")
        msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
        msg.setIcon(QMessageBox.Critical)
        msg.setText('Vereiste velden\nniet allen ingevoerd!')
        msg.setWindowTitle('Onjuiste invoer')
        logger.debug("<<< Exiting foutInvoer()")
        msg.exec_()
      
def foutWerknr():
    logger.debug(">>> Entering foutWerknr()")
    msg = QMessageBox()
    logger.debug("foutWerknr(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Werknummer niet gevonden\nWerknummer bestaat niet!')
    msg.setWindowTitle('Wijzi werken!')
    logger.debug("<<< Exiting foutWerknr()")
    msg.exec_()
    
def werkGereed():
    logger.debug(">>> Entering werkGereed()")
    msg = QMessageBox()
    logger.debug("werkGereed(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Werk is gereed\nboeken is niet meer mogelijk!')
    msg.setWindowTitle('Wijzig werken!')
    logger.debug("<<< Exiting werkGereed()")
    msg.exec_()
    
def updateOK():
    logger.debug(">>> Entering updateOK()")
    msg = QMessageBox()
    logger.debug("updateOK(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('De gegevens zijn aangepast!')
    msg.setWindowTitle('Wijzig werken!')
    logger.debug("<<< Exiting updateOK()")
    msg.exec_()
       
def winSluit(self, m_email):
    logger.debug(">>> Entering winSluit(m_email=%s)", m_email)
    self.close()
    zoekWerk(m_email)
    logger.debug("<<< Exiting winSluit(m_email=%s)", m_email)
    
def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)
             
def zoekWerk(m_email):
    logger.debug(">>> Entering zoekWerk(m_email=%s)", m_email)
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
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator)
            logger.debug("__init__(parent=%s): q1Edit → %s", parent, q1Edit)
            logger.debug("__init__(parent=%s): self.Omschrijving → %s", parent, self.Omschrijving)
            logger.debug("__init__(self=%s,parent=%s): q1Edit → %s", self, parent, q1Edit)
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex)
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator)
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit)
            logger.debug("__init__(parent=%s): self.Aanneemsom → %s", parent, self.Aanneemsom)
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit)
            logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit)
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit)
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit)
            logger.debug("__init__(parent=%s): self.mutPaid → %s", parent, self.mutPaid)
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit)
            logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit)
            logger.debug("__init__(parent=%s): self.Huisvesting → %s", parent, self.Huisvesting)
            logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit)
            logger.debug("__init__(parent=%s): q5aEdit → %s", parent, q5aEdit)
            logger.debug("__init__(self=%s,parent=%s): q5aEdit → %s", self, parent, q5aEdit)
            logger.debug("__init__(parent=%s): q5bEdit → %s", parent, q5bEdit)
            logger.debug("__init__(parent=%s): self.housing → %s", parent, self.housing)
            logger.debug("__init__(self=%s,parent=%s): q5bEdit → %s", self, parent, q5bEdit)
            logger.debug("__init__(parent=%s): q6Edit → %s", parent, q6Edit)
            logger.debug("__init__(parent=%s): self.Leiding → %s", parent, self.Leiding)
            logger.debug("__init__(self=%s,parent=%s): q6Edit → %s", self, parent, q6Edit)
            logger.debug("__init__(parent=%s): q6aEdit → %s", parent, q6aEdit)
            logger.debug("__init__(self=%s,parent=%s): q6aEdit → %s", self, parent, q6aEdit)
            logger.debug("__init__(parent=%s): q6bEdit → %s", parent, q6bEdit)
            logger.debug("__init__(parent=%s): self.direction → %s", parent, self.direction)
            logger.debug("__init__(self=%s,parent=%s): q6bEdit → %s", self, parent, q6bEdit)
            logger.debug("__init__(parent=%s): q7Edit → %s", parent, q7Edit)
            logger.debug("__init__(parent=%s): self.Inhuur → %s", parent, self.Inhuur)
            logger.debug("__init__(self=%s,parent=%s): q7Edit → %s", self, parent, q7Edit)
            logger.debug("__init__(parent=%s): q7aEdit → %s", parent, q7aEdit)
            logger.debug("__init__(self=%s,parent=%s): q7aEdit → %s", self, parent, q7aEdit)
            logger.debug("__init__(parent=%s): q7bEdit → %s", parent, q7bEdit)
            logger.debug("__init__(parent=%s): self.hiring → %s", parent, self.hiring)
            logger.debug("__init__(self=%s,parent=%s): q7bEdit → %s", self, parent, q7bEdit)
            logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit)
            logger.debug("__init__(parent=%s): self.Vervoer → %s", parent, self.Vervoer)
            logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit)
            logger.debug("__init__(parent=%s): q8aEdit → %s", parent, q8aEdit)
            logger.debug("__init__(self=%s,parent=%s): q8aEdit → %s", self, parent, q8aEdit)
            logger.debug("__init__(parent=%s): q8bEdit → %s", parent, q8bEdit)
            logger.debug("__init__(parent=%s): self.transport → %s", parent, self.transport)
            logger.debug("__init__(self=%s,parent=%s): q8bEdit → %s", self, parent, q8bEdit)
            logger.debug("__init__(parent=%s): q11Edit → %s", parent, q11Edit)
            logger.debug("__init__(parent=%s): self.Grondverzet → %s", parent, self.Grondverzet)
            logger.debug("__init__(self=%s,parent=%s): q11Edit → %s", self, parent, q11Edit)
            logger.debug("__init__(parent=%s): q11aEdit → %s", parent, q11aEdit)
            logger.debug("__init__(self=%s,parent=%s): q11aEdit → %s", self, parent, q11aEdit)
            logger.debug("__init__(parent=%s): q11bEdit → %s", parent, q11bEdit)
            logger.debug("__init__(parent=%s): self.earthmoving → %s", parent, self.earthmoving)
            logger.debug("__init__(self=%s,parent=%s): q11bEdit → %s", self, parent, q11bEdit)
            logger.debug("__init__(parent=%s): self.Overig → %s", parent, self.Overig)
            logger.debug("__init__(self=%s,parent=%s): q12Edit → %s", self, parent, q12Edit)
            logger.debug("__init__(parent=%s): q12Edit → %s", parent, q12Edit)
            logger.debug("__init__(self=%s,parent=%s): q12aEdit → %s", self, parent, q12aEdit)
            logger.debug("__init__(parent=%s): q12aEdit → %s", parent, q12aEdit)
            logger.debug("__init__(parent=%s): self.remaining → %s", parent, self.remaining)
            logger.debug("__init__(self=%s,parent=%s): q12bEdit → %s", self, parent, q12bEdit)
            logger.debug("__init__(parent=%s): q12bEdit → %s", parent, q12bEdit)
            logger.debug("__init__(parent=%s): self.StartWerk → %s", parent, self.StartWerk)
            logger.debug("__init__(self=%s,parent=%s): q23Edit → %s", self, parent, q23Edit)
            logger.debug("__init__(parent=%s): q23Edit → %s", parent, q23Edit)
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid)
            logger.debug("__init__(parent=%s): grid → %s", parent, grid)
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1)
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1)
            logger.debug("__init__(self=%s,parent=%s): lbl2 → %s", self, parent, lbl2)
            logger.debug("__init__(parent=%s): lbl2 → %s", parent, lbl2)
            logger.debug("__init__(self=%s,parent=%s): lbl3 → %s", self, parent, lbl3)
            logger.debug("__init__(parent=%s): lbl3 → %s", parent, lbl3)
            logger.debug("__init__(parent=%s): lbl4 → %s", parent, lbl4)
            logger.debug("__init__(self=%s,parent=%s): lbl4 → %s", self, parent, lbl4)
            logger.debug("__init__(parent=%s): lbl5 → %s", parent, lbl5)
            logger.debug("__init__(self=%s,parent=%s): lbl5 → %s", self, parent, lbl5)
            logger.debug("__init__(parent=%s): lbl6 → %s", parent, lbl6)
            logger.debug("__init__(self=%s,parent=%s): lbl6 → %s", self, parent, lbl6)
            logger.debug("__init__(parent=%s): lbl7a → %s", parent, lbl7a)
            logger.debug("__init__(self=%s,parent=%s): lbl7a → %s", self, parent, lbl7a)
            logger.debug("__init__(parent=%s): lbl7b → %s", parent, lbl7b)
            logger.debug("__init__(self=%s,parent=%s): lbl7b → %s", self, parent, lbl7b)
            logger.debug("__init__(parent=%s): lbl7c → %s", parent, lbl7c)
            logger.debug("__init__(self=%s,parent=%s): lbl7c → %s", self, parent, lbl7c)
            logger.debug("__init__(parent=%s): lbl7 → %s", parent, lbl7)
            logger.debug("__init__(self=%s,parent=%s): lbl7 → %s", self, parent, lbl7)
            logger.debug("__init__(parent=%s): lbl8 → %s", parent, lbl8)
            logger.debug("__init__(self=%s,parent=%s): lbl8 → %s", self, parent, lbl8)
            logger.debug("__init__(parent=%s): lbl9 → %s", parent, lbl9)
            logger.debug("__init__(self=%s,parent=%s): lbl9 → %s", self, parent, lbl9)
            logger.debug("__init__(parent=%s): lbl10 → %s", parent, lbl10)
            logger.debug("__init__(self=%s,parent=%s): lbl10 → %s", self, parent, lbl10)
            logger.debug("__init__(parent=%s): lbl13 → %s", parent, lbl13)
            logger.debug("__init__(self=%s,parent=%s): lbl13 → %s", self, parent, lbl13)
            logger.debug("__init__(parent=%s): lbl14 → %s", parent, lbl14)
            logger.debug("__init__(self=%s,parent=%s): lbl14 → %s", self, parent, lbl14)
            logger.debug("__init__(parent=%s): lblwk → %s", parent, lblwk)
            logger.debug("__init__(self=%s,parent=%s): lblwk → %s", self, parent, lblwk)
            logger.debug("__init__(parent=%s): lblst → %s", parent, lblst)
            logger.debug("__init__(self=%s,parent=%s): lblst → %s", self, parent, lblst)
            logger.debug("__init__(parent=%s): lbl25 → %s", parent, lbl25)
            logger.debug("__init__(self=%s,parent=%s): lbl25 → %s", self, parent, lbl25)
            logger.debug("__init__(parent=%s): lbl27 → %s", parent, lbl27)
            logger.debug("__init__(self=%s,parent=%s): lbl27 → %s", self, parent, lbl27)
            logger.debug("__init__(parent=%s): lbl28 → %s", parent, lbl28)
            logger.debug("__init__(self=%s,parent=%s): lbl28 → %s", self, parent, lbl28)
            logger.debug("__init__(parent=%s): cBox2 → %s", parent, cBox2)
            logger.debug("__init__(self=%s,parent=%s): cBox2 → %s", self, parent, cBox2)
            logger.debug("__init__(parent=%s): cBox1 → %s", parent, cBox1)
            logger.debug("__init__(self=%s,parent=%s): cBox1 → %s", self, parent, cBox1)
            logger.debug("__init__(parent=%s): cBox → %s", parent, cBox)
            logger.debug("__init__(self=%s,parent=%s): cBox → %s", self, parent, cBox)
            logger.debug("__init__(parent=%s): movie → %s", parent, movie)
            logger.debug("__init__(parent=%s): pyqt → %s", parent, pyqt)
            logger.debug("__init__(self=%s,parent=%s): pyqt → %s", self, parent, pyqt)
            logger.debug("__init__(self=%s,parent=%s): movie → %s", self, parent, movie)
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn)
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
    
        def werknChanged(self, text):
            logger.debug(">>> Entering werknChanged(text=%s)", text)
            logger.debug("werknChanged(self=%s,text=%s): Werknummer → %s", self, text, Werknummer)
            self.Werknummer.setText(text)
            logger.debug("<<< Exiting werknChanged(text=%s)", text)
    
        def returnwerkn(self):
            logger.debug(">>> Entering returnwerkn()")
            logger.debug("<<< Exiting returnwerkn()")
            return self.Werknummer.text()
    
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            logger.debug(">>> Entering getData(parent=%s)", parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            logger.debug("<<< Exiting getData(parent=%s)", parent)
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
    logger.debug(">>> Entering wijzWerk(mwerknr=%s,m_email=%s)", mwerknr, m_email)
    metadata = MetaData()
    logger.debug("wijzWerk(mwerknr=%s,m_email=%s): metadata → %s", mwerknr, m_email, metadata)
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
    logger.debug("wijzWerk(mwerknr=%s,m_email=%s): engine → %s", mwerknr, m_email, engine)
    conn = engine.connect()
    selwerk = select([werken]).where(werken.c.werknummerID == mwerknr)
    logger.debug("wijzWerk(mwerknr=%s,m_email=%s): conn → %s", mwerknr, m_email, conn)
    rpwerk = conn.execute(selwerk).first()
                                          
    logger.debug("wijzWerk(mwerknr=%s,m_email=%s): selwerk → %s", mwerknr, m_email, selwerk)
    logger.debug("wijzWerk(mwerknr=%s,m_email=%s): rpwerk → %s", mwerknr, m_email, rpwerk)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug("<<< Exiting wijzWerk(mwerknr=%s,m_email=%s)", mwerknr, m_email)
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
            logger.debug(">>> Entering q1Changed(text=%s)", text)
            logger.debug("q1Changed(self=%s,text=%s): Omschrijving → %s", self, text, Omschrijving)
            self.Omschrijving.setText(text)
            logger.debug("<<< Exiting q1Changed(text=%s)", text)
    
        def q2Changed(self,text):
            logger.debug(">>> Entering q2Changed(text=%s)", text)
            logger.debug("q2Changed(self=%s,text=%s): Aanneemsom → %s", self, text, Aanneemsom)
            self.Aanneemsom.setText(text)
            logger.debug("<<< Exiting q2Changed(text=%s)", text)

        def q4Changed(self, text):
            logger.debug(">>> Entering q4Changed(text=%s)", text)
            logger.debug("q4Changed(self=%s,text=%s): mutPaid → %s", self, text, mutPaid)
            self.mutPaid.setText(text)
            logger.debug("<<< Exiting q4Changed(text=%s)", text)

        def q5Changed(self,text):
            logger.debug(">>> Entering q5Changed(text=%s)", text)
            logger.debug("q5Changed(self=%s,text=%s): Huisvesting → %s", self, text, Huisvesting)
            self.Huisvesting.setText(text)
            logger.debug("<<< Exiting q5Changed(text=%s)", text)

        def q5bChanged(self,text):
            logger.debug(">>> Entering q5bChanged(text=%s)", text)
            logger.debug("q5bChanged(self=%s,text=%s): housing → %s", self, text, housing)
            self.housing.setText(text)
            logger.debug("<<< Exiting q5bChanged(text=%s)", text)

        def q6Changed(self,text):
            logger.debug(">>> Entering q6Changed(text=%s)", text)
            logger.debug("q6Changed(self=%s,text=%s): Leiding → %s", self, text, Leiding)
            self.Leiding.setText(text)
            logger.debug("<<< Exiting q6Changed(text=%s)", text)

        def q6bChanged(self,text):
            logger.debug(">>> Entering q6bChanged(text=%s)", text)
            logger.debug("q6bChanged(self=%s,text=%s): direction → %s", self, text, direction)
            self.direction.setText(text)
            logger.debug("<<< Exiting q6bChanged(text=%s)", text)
            
        def q7Changed(self,text):
            logger.debug(">>> Entering q7Changed(text=%s)", text)
            logger.debug("q7Changed(self=%s,text=%s): Inhuur → %s", self, text, Inhuur)
            self.Inhuur.setText(text)
            logger.debug("<<< Exiting q7Changed(text=%s)", text)

        def q7bChanged(self,text):
            logger.debug(">>> Entering q7bChanged(text=%s)", text)
            logger.debug("q7bChanged(self=%s,text=%s): hiring → %s", self, text, hiring)
            self.hiring.setText(text)
            logger.debug("<<< Exiting q7bChanged(text=%s)", text)
            
        def q8Changed(self,text):
            logger.debug(">>> Entering q8Changed(text=%s)", text)
            logger.debug("q8Changed(self=%s,text=%s): Vervoer → %s", self, text, Vervoer)
            self.Vervoer.setText(text)
            logger.debug("<<< Exiting q8Changed(text=%s)", text)

        def q8bChanged(self,text):
            logger.debug(">>> Entering q8bChanged(text=%s)", text)
            logger.debug("q8bChanged(self=%s,text=%s): transport → %s", self, text, transport)
            self.transport.setText(text)
            logger.debug("<<< Exiting q8bChanged(text=%s)", text)
        
        def q11Changed(self,text):
            logger.debug(">>> Entering q11Changed(text=%s)", text)
            logger.debug("q11Changed(self=%s,text=%s): Grondverzet → %s", self, text, Grondverzet)
            self.Grondverzet.setText(text)
            logger.debug("<<< Exiting q11Changed(text=%s)", text)

        def q11bChanged(self,text):
            logger.debug(">>> Entering q11bChanged(text=%s)", text)
            logger.debug("q11bChanged(self=%s,text=%s): earthmoving → %s", self, text, earthmoving)
            self.earthmoving.setText(text)
            logger.debug("<<< Exiting q11bChanged(text=%s)", text)
            
        def q12Changed(self,text):
            logger.debug(">>> Entering q12Changed(text=%s)", text)
            logger.debug("q12Changed(self=%s,text=%s): Overig → %s", self, text, Overig)
            self.Overig.setText(text)
            logger.debug("<<< Exiting q12Changed(text=%s)", text)

        def q12bChanged(self,text):
            logger.debug(">>> Entering q12bChanged(text=%s)", text)
            logger.debug("q12bChanged(self=%s,text=%s): remaining → %s", self, text, remaining)
            self.remaining.setText(text)
            logger.debug("<<< Exiting q12bChanged(text=%s)", text)

        def q23Changed(self,text):
            logger.debug(">>> Entering q23Changed(text=%s)", text)
            logger.debug("q23Changed(self=%s,text=%s): Startwerk → %s", self, text, Startwerk)
            self.Startwerk.setText(text)
            logger.debug("<<< Exiting q23Changed(text=%s)", text)

        state = False
        def cBoxChanged(self, state):
            logger.debug(">>> Entering cBoxChanged(state=%s)", state)
            logger.debug("cBoxChanged(state=%s): self.state → %s", state, self.state)
            logger.debug("cBoxChanged(self=%s,state=%s): self.state → %s", self, state, self.state)
            if state == Qt.Checked:
                self.state = True
                logger.debug("<<< Exiting cBoxChanged(state=%s)", state)

        state1 = False  
        def cBox1Changed(self, state1):
            logger.debug(">>> Entering cBox1Changed(state1=%s)", state1)
            logger.debug("cBox1Changed(self=%s,state1=%s): self.state1 → %s", self, state1, self.state1)
            if state1 == Qt.Checked:
                logger.debug("<<< Exiting cBox1Changed(state1=%s)", state1)
                self.state1 = True

        state2 = False  
        def cBox2Changed(self, state2):
            logger.debug(">>> Entering cBox2Changed(state2=%s)", state2)
            logger.debug("cBox2Changed(self=%s,state2=%s): self.state2 → %s", self, state2, self.state2)
            if state2 == Qt.Checked:
                logger.debug("<<< Exiting cBox2Changed(state2=%s)", state2)
                self.state2 = True

        def returnq1(self):
            logger.debug(">>> Entering returnq1()")
            logger.debug("<<< Exiting returnq1()")
            return self.Omschrijving.text()
        
        def returnq2(self):
            logger.debug(">>> Entering returnq2()")
            logger.debug("<<< Exiting returnq2()")
            return self.Aanneemsom.text()

        def returnq4(self):
            logger.debug(">>> Entering returnq4()")
            logger.debug("<<< Exiting returnq4()")
            return  self.mutPaid.text()
        
        def returnq5(self):
            logger.debug(">>> Entering returnq5()")
            logger.debug("<<< Exiting returnq5()")
            return self.Huisvesting.text()

        def returnq5b(self):
            logger.debug(">>> Entering returnq5b()")
            logger.debug("<<< Exiting returnq5b()")
            return self.housing.text()
    
        def returnq6(self):
            logger.debug(">>> Entering returnq6()")
            logger.debug("<<< Exiting returnq6()")
            return self.Leiding.text()

        def returnq6b(self):
            logger.debug(">>> Entering returnq6b()")
            logger.debug("<<< Exiting returnq6b()")
            return self.direction.text()
        
        def returnq7(self):
            logger.debug(">>> Entering returnq7()")
            logger.debug("<<< Exiting returnq7()")
            return self.Inhuur.text()

        def returnq7b(self):
            logger.debug(">>> Entering returnq7b()")
            logger.debug("<<< Exiting returnq7b()")
            return self.hiring.text()
              
        def returnq8(self):
            logger.debug(">>> Entering returnq8()")
            logger.debug("<<< Exiting returnq8()")
            return self.Vervoer.text()

        def returnq8b(self):
            logger.debug(">>> Entering returnq8b()")
            logger.debug("<<< Exiting returnq8b()")
            return self.transport.text()

        def returnq11(self):
            logger.debug(">>> Entering returnq11()")
            logger.debug("<<< Exiting returnq11()")
            return self.Grondverzet.text()

        def returnq11b(self):
            logger.debug(">>> Entering returnq11b()")
            logger.debug("<<< Exiting returnq11b()")
            return self.earthmoving.text()
        
        def returnq12(self):
            logger.debug(">>> Entering returnq12()")
            logger.debug("<<< Exiting returnq12()")
            return self.Overig.text()

        def returnq12b(self):
            logger.debug(">>> Entering returnq12b()")
            logger.debug("<<< Exiting returnq12b()")
            return self.remaining.text()
        
        def returnq23(self):
            logger.debug(">>> Entering returnq23()")
            logger.debug("<<< Exiting returnq23()")
            return self.StartWerk.text()

        def returncBox(self):
            logger.debug(">>> Entering returncBox()")
            logger.debug("<<< Exiting returncBox()")
            return self.state
        
        def returncBox1(self):
            logger.debug(">>> Entering returncBox1()")
            logger.debug("<<< Exiting returncBox1()")
            return self.state1
        
        def returncBox2(self):
            logger.debug(">>> Entering returncBox2()")
            logger.debug("<<< Exiting returncBox2()")
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