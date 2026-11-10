from login import hoofdMenu
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
                           QDialog, QMessageBox
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap, QIcon
from PyQt5.QtCore import QRegExp, Qt
from sqlalchemy import (Table, Column, Integer, String, MetaData,\
                            create_engine, update)
from sqlalchemy.sql import select
import logging
logger = logging.getLogger(__name__)
  
def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    
def wijzWindow(self, m_email):
    logger.warning(">>> Entering wijzWindow(m_email=%s)", m_email, extra={"event.action": "wijzWindow"})
    self.close()
    zoekKoper(m_email)
    logger.debug("<<< Exiting wijzWindow(m_email=%s)", m_email, extra={"event.action": "wijzWindow"})
       
def foutTelnr():
    logger.warning(">>> Entering foutTelnr()", extra={"event.action": "foutTelnr"})
    msg = QMessageBox()
    logger.debug("foutTelnr(): msg → %s", msg, extra={"event.action": "foutTelnr"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('no 10 digits!')
    msg.setWindowTitle('Sales company')
    logger.debug("<<< Exiting foutTelnr()", extra={"event.action": "foutTelnr"})
    msg.exec_()
    
def foutKopernr():
    logger.warning(">>> Entering foutKopernr()", extra={"event.action": "foutKopernr"})
    msg = QMessageBox()
    logger.debug("foutKopernr(): msg → %s", msg, extra={"event.action": "foutKopernr"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Company not found')
    msg.setWindowTitle('Sales company')
    logger.debug("<<< Exiting foutKopernr()", extra={"event.action": "foutKopernr"})
    msg.exec_()
         
def updateOK():
    logger.warning(">>> Entering updateOK()", extra={"event.action": "updateOK"})
    msg = QMessageBox()
    logger.debug("updateOK(): msg → %s", msg, extra={"event.action": "updateOK"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Your data has been adjusted!')
    msg.setWindowTitle('Sales company')
    logger.debug("<<< Exiting updateOK()", extra={"event.action": "updateOK"})
    msg.exec_()
           
def zoekKoper(m_email):     
    logger.warning(">>> Entering zoekKoper(m_email=%s)", m_email, extra={"event.action": "zoekKoper"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Modify sales company.")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Bedrijfsnummer = QLabel()
            levEdit = QLineEdit()
            levEdit.setFixedWidth(100)
            levEdit.setFont(QFont("Arial",10))
            levEdit.textChanged.connect(self.levChanged)
            reg_ex = QRegExp('^[6]{1}[0-9]{8}$')
            input_validator = QRegExpValidator(reg_ex, levEdit)
            levEdit.setValidator(input_validator)
                            
            grid = QGridLayout()
            grid.setSpacing(20)
    
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 2, Qt.AlignRight)
         
            grid.addWidget(QLabel('Sales company'), 1, 1)
            grid.addWidget(levEdit, 1, 2)
       
            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
         
            applyBtn = QPushButton('Search')
            applyBtn.clicked.connect(self.accept)
                  
            grid.addWidget(applyBtn, 2, 2, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
        
            grid.addWidget(cancelBtn, 2, 1, 1, 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 3, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(500, 100, 150, 150)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Bedrijfsnaam → %s", parent, self.Bedrijfsnaam, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Afdeling → %s", parent, self.Afdeling, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q16Edit → %s", parent, q16Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q16Edit → %s", self, parent, q16Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Rechtsvorm → %s", parent, self.Rechtsvorm, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.BTWnummer → %s", parent, self.BTWnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.KvKnummer → %s", parent, self.KvKnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Straat → %s", parent, self.Straat, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q1Edit → %s", parent, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q1Edit → %s", self, parent, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Huisnummer → %s", parent, self.Huisnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q7Edit → %s", parent, q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q7Edit → %s", self, parent, q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Toevoeging → %s", parent, self.Toevoeging, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Postcode → %s", parent, self.Postcode, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q6Edit → %s", self, parent, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q6Edit → %s", parent, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): font → %s", self, parent, font, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): font → %s", parent, font, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Woonplaats → %s", parent, self.Woonplaats, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q15Edit → %s", self, parent, q15Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q15Edit → %s", parent, q15Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Telefoonnr → %s", parent, self.Telefoonnr, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q13Edit → %s", self, parent, q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q13Edit → %s", parent, q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Bedrijfverkoopnummer → %s", parent, self.Bedrijfverkoopnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q14Edit → %s", self, parent, q14Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q14Edit → %s", parent, q14Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
    
        def levChanged(self, text):
            logger.warning(">>> Entering levChanged(text=%s)", text, extra={"event.action": "levChanged", "logrite.text": text})
            self.Bedrijfsnummer.setText(text)
            logger.debug("<<< Exiting levChanged(text=%s)", text, extra={"event.action": "levChanged", "logrite.text": text})
    
        def returnBedrijfsnummer(self):
            logger.warning(">>> Entering returnBedrijfsnummer()", extra={"event.action": "returnBedrijfsnummer"})
            logger.debug("<<< Exiting returnBedrijfsnummer()", extra={"event.action": "returnBedrijfsnummer"})
            return self.Bedrijfsnummer.text()
    
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnBedrijfsnummer()]
       
    window = Widget()
    data = window.getData()
    if data[0]:
        mkopernr = int(data[0])
    else:
          mkopernr = 0
    
    metadata = MetaData()

    kopers = Table('kopers', metadata,
        Column('koperID', Integer(), primary_key=True))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    s = select([kopers]).where(kopers.c.koperID == mkopernr)
    rpkop = conn.execute(s).first()
    
    if rpkop:
        updateKoper(m_email, mkopernr)
    else:
        foutKopernr()
        zoekKoper(m_email)
        
def updateKoper(m_email, mkopernr):
    logger.warning(">>> Entering updateKoper(m_email=%s,mkopernr=%s)", m_email, mkopernr, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
    metadata = MetaData()
    logger.debug("updateKoper(m_email=%s,mkopernr=%s): metadata → %s", m_email, mkopernr, metadata, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
    kopers= Table('kopers', metadata,
        Column('koperID', Integer(), primary_key=True),
        Column('bedrijfsnaam', String),
        Column('rechtsvorm', String),
        Column('btwnummer', String),
        Column('kvknummer', String),
        Column('telnr', String),
        Column('huisnummer', String),
        Column('toevoeging', String),
        Column('postcode', String),
        Column('afdeling', String))       
              
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("updateKoper(m_email=%s,mkopernr=%s): engine → %s", m_email, mkopernr, engine, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
    conn = engine.connect()
    logger.debug("updateKoper(m_email=%s,mkopernr=%s): conn → %s", m_email, mkopernr, conn, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
    sel = select([kopers]).where(kopers.c.koperID == mkopernr)
    rpkop = conn.execute(sel).first()
    logger.debug("updateKoper(m_email=%s,mkopernr=%s): sel → %s", m_email, mkopernr, sel, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
    logger.debug("updateKoper(m_email=%s,mkopernr=%s): rpkop → %s", m_email, mkopernr, rpkop, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
    if rpkop:
        mkopernr = rpkop[0]
        mbedrnaam = rpkop[1]
        logger.debug("updateKoper(m_email=%s,mkopernr=%s): mbedrnaam → %s", m_email, mkopernr, mbedrnaam, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
        mrechtsvorm = rpkop[2]
        logger.debug("updateKoper(m_email=%s,mkopernr=%s): mrechtsvorm → %s", m_email, mkopernr, mrechtsvorm, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
        mbtwnr = rpkop[3]
        logger.debug("updateKoper(m_email=%s,mkopernr=%s): mbtwnr → %s", m_email, mkopernr, mbtwnr, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
        mkvknr = rpkop[4]
        logger.debug("updateKoper(m_email=%s,mkopernr=%s): mkvknr → %s", m_email, mkopernr, mkvknr, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
        mtelnr = rpkop[5]
        logger.debug("updateKoper(m_email=%s,mkopernr=%s): mtelnr → %s", m_email, mkopernr, mtelnr, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
        mhuisnr = rpkop[6]
        mhuisnr = int(mhuisnr)
        logger.debug("updateKoper(m_email=%s,mkopernr=%s): mhuisnr → %s", m_email, mkopernr, mhuisnr, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
        mtoev = rpkop[7]
        mpostcode = rpkop[8]
        mafdeling = rpkop[9]
        logger.debug("updateKoper(m_email=%s,mkopernr=%s): mtoev → %s", m_email, mkopernr, mtoev, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
        logger.debug("updateKoper(m_email=%s,mkopernr=%s): mpostcode → %s", m_email, mkopernr, mpostcode, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
        logger.debug("updateKoper(m_email=%s,mkopernr=%s): mafdeling → %s", m_email, mkopernr, mafdeling, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
        logger.debug("updateKoper(m_email=%s,mkopernr=%s): mstrtplts → %s", m_email, mkopernr, mstrtplts, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
        import postcode
        mstrtplts = postcode.checkpostcode(mpostcode,mhuisnr)
        mstraat = mstrtplts[0]
        mplaats = mstrtplts[1]
                                
        logger.debug("updateKoper(m_email=%s,mkopernr=%s): mstraat → %s", m_email, mkopernr, mstraat, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
        logger.debug("updateKoper(m_email=%s,mkopernr=%s): mplaats → %s", m_email, mkopernr, mplaats, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug("<<< Exiting updateKoper(m_email=%s,mkopernr=%s)", m_email, mkopernr, extra={"event.action": "updateKoper", "logrite.mkopernr": mkopernr})
            self.setWindowTitle("Modify sales company")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                                  
            self.setFont(QFont('Arial', 10))
                  
            self.Bedrijfsnaam = QLabel()
            q3Edit = QLineEdit(mbedrnaam)
            q3Edit.setText(mbedrnaam)
            q3Edit.setFixedWidth(540)
            q3Edit.setFont(QFont("Arial",10))
            q3Edit.textChanged.connect(self.q3Changed)
            reg_ex = QRegExp("^[^0-9]{1,50}$")
            input_validator = QRegExpValidator(reg_ex, q3Edit)
            q3Edit.setValidator(input_validator)
            
            self.Afdeling = QLabel()
            q16Edit = QLineEdit()
            q16Edit.setText(mafdeling)
            q16Edit.setFixedWidth(540)
            q16Edit.setFont(QFont("Arial",10))
            q16Edit.textChanged.connect(self.q16Changed)
            reg_ex = QRegExp("^.{1,50}$")
            input_validator = QRegExpValidator(reg_ex, q16Edit)
            q16Edit.setValidator(input_validator)
                
            self.Rechtsvorm = QLabel()
            q5Edit = QLineEdit()
            q5Edit.setText(mrechtsvorm)
            q5Edit.setFixedWidth(100)
            q5Edit.setFont(QFont("Arial",10))
            q5Edit.textChanged.connect(self.q5Changed)
            reg_ex = QRegExp("^[^0-9]{1,30}$")
            input_validator = QRegExpValidator(reg_ex, q5Edit)
            q5Edit.setValidator(input_validator)
            
            self.BTWnummer =  QLabel()
            q2Edit = QLineEdit()
            q2Edit.setText(str(mbtwnr))
            q2Edit.setDisabled(True)
            q2Edit.setFixedWidth(170)
            q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q2Edit.setFont(QFont("Arial",10))
            q2Edit.textChanged.connect(self.q2Changed)
            reg_ex = QRegExp("^[A-Za-z]{2}[0-9]{9}[Bb]{1}[0-9]{2}$")
            input_validator = QRegExpValidator(reg_ex, q2Edit)
            q2Edit.setValidator(input_validator)
            
            self.KvKnummer =  QLabel()
            q4Edit = QLineEdit()
            q4Edit.setText(str(mkvknr))
            q4Edit.setFixedWidth(110)
            q4Edit.setDisabled(True)
            q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q4Edit.setFont(QFont("Arial",10))
            q4Edit.textChanged.connect(self.q4Changed)
            reg_ex = QRegExp("^[0-9]{8}$")
            input_validator = QRegExpValidator(reg_ex, q4Edit)
            q4Edit.setValidator(input_validator)
            
            self.Straat =  QLabel()
            q1Edit = QLineEdit()
            q1Edit.setText(mstraat)
            q1Edit.setFixedWidth(540)
            q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q1Edit.setDisabled(True)
    
            self.Huisnummer = QLabel()
            q7Edit = QLineEdit()
            q7Edit.setText(str(mhuisnr))
            q7Edit.setAlignment(Qt.AlignRight)
            q7Edit.setFixedWidth(60)
            q7Edit.setFont(QFont("Arial",10))
            q7Edit.textChanged.connect(self.q7Changed)
            reg_ex = QRegExp("^[0-9]{1,5}$")
            input_validator = QRegExpValidator(reg_ex, q7Edit)
            q7Edit.setValidator(input_validator)
        
            self.Toevoeging = QLabel()
            q8Edit = QLineEdit('')
            q8Edit.setFixedWidth(80)
            q8Edit.setFont(QFont("Arial",10))
            q8Edit.textChanged.connect(self.q8Changed)
            q8Edit.setText(mtoev)
            reg_ex = QRegExp("^[A-Za-z0-9-#]{0,10}")
            input_validator = QRegExpValidator(reg_ex, q8Edit)
            q8Edit.setValidator(input_validator)
            
            self.Postcode = QLabel()
            q6Edit = QLineEdit()
            q6Edit.setText(mpostcode)
            q6Edit.setFixedWidth(80)
            font = QFont("Arial",10)
            font.setCapitalization(QFont.AllUppercase)
            q6Edit.setFont(font)
            q6Edit.textChanged.connect(self.q6Changed)
            reg_ex = QRegExp("^[0-9]{4}[A-Za-z]{2}$")
            input_validator = QRegExpValidator(reg_ex, q6Edit)
            q6Edit.setValidator(input_validator)
               
            self.Woonplaats =  QLabel()
            q15Edit = QLineEdit()
            q15Edit.setText(mplaats)
            q15Edit.setFixedWidth(400)
            q15Edit.setDisabled(True)
            q15Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
               
            self.Telefoonnr = QLabel()
            q13Edit = QLineEdit('')
            q13Edit.setFixedWidth(120)
            q13Edit.setFont(QFont("Arial",10))
            q13Edit.textChanged.connect(self.q13Changed)
            q13Edit.setText(mtelnr)
            reg_ex = QRegExp("^[0]{1}[0-9]{9}$")
            input_validator = QRegExpValidator(reg_ex, q13Edit)
            q13Edit.setValidator(input_validator)
            
            self.Bedrijfverkoopnummer =  QLabel()
            q14Edit = QLineEdit()
            q14Edit.setText(str(mkopernr))
            q14Edit.setAlignment(Qt.AlignRight)
            q14Edit.setFixedWidth(120)
            q14Edit.setDisabled(True)
            q14Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q14Edit.setFont(QFont("Arial",10))
            q14Edit.textChanged.connect(self.q14Changed)
            
            grid = QGridLayout()
            grid.setSpacing(20)
            
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 2, Qt.AlignRight)
   
            self.setFont(QFont('Arial', 10))
            grid.addWidget(QLabel('Modifications sales company'), 0, 1)
                        
            grid.addWidget(QLabel('                                  *'), 1, 0) 
            grid.addWidget(QLabel('Required fields'), 1, 1)   
                         
            grid.addWidget(QLabel('Company name           *'), 2, 0)
            grid.addWidget(q3Edit, 2, 1, 1, 3) 
            
            grid.addWidget(QLabel('Department name/Room/\nContact person'), 3, 0)
            grid.addWidget(q16Edit, 3, 1, 1, 3)  
                 
            grid.addWidget(QLabel('Legal status                *'), 4, 0)
            grid.addWidget(q5Edit, 4, 1) 
            
            grid.addWidget(QLabel('VAT number  *'), 4, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(q2Edit, 4, 2) 
            
            grid.addWidget(QLabel('KvK number                *'), 5, 0)
            grid.addWidget(q4Edit, 5, 1) 
            
            grid.addWidget(QLabel('Street'),6, 0)
            grid.addWidget(q1Edit, 6, 1, 1, 3)
     
            grid.addWidget(QLabel('House number            *'), 7, 0)
            grid.addWidget(q7Edit, 7, 1)
    
            grid.addWidget(QLabel('Suffix'), 7, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(q8Edit, 7, 2)
            
            grid.addWidget(QLabel('Zipcode Residence     *'), 8, 0)
            grid.addWidget(q6Edit, 8, 1)
            
            grid.addWidget(q15Edit, 8, 1, 1, 2, Qt.AlignRight) 
     
            grid.addWidget(QLabel('Telephone number      *'), 9, 0)
            grid.addWidget(q13Edit, 9, 1) 
            
            grid.addWidget(QLabel('Sales Company number'), 10, 0)
            grid.addWidget(q14Edit, 10, 1) 
                                
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 11, 1)
              
            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: wijzWindow(self,m_email))
            
            applyBtn = QPushButton('Modify')
            applyBtn.clicked.connect(self.accept)
                       
            grid.addWidget(applyBtn, 10, 2, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
        
            grid.addWidget(cancelBtn, 9, 2, 1, 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
               
            self.setLayout(grid)
            self.setGeometry(500, 100, 150, 150)
          
        def q3Changed(self, text):
            logger.warning(">>> Entering q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
            self.Bedrijfsnaam.setText(text)
            logger.debug("<<< Exiting q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
            
        def q16Changed(self, text):
            logger.warning(">>> Entering q16Changed(text=%s)", text, extra={"event.action": "q16Changed", "logrite.text": text})
            self.Afdeling.setText(text)
            logger.debug("<<< Exiting q16Changed(text=%s)", text, extra={"event.action": "q16Changed", "logrite.text": text})
                   
        def q5Changed(self, text):
            logger.warning(">>> Entering q5Changed(text=%s)", text, extra={"event.action": "q5Changed", "logrite.text": text})
            self.Rechtsvorm.setText(text)
            logger.debug("<<< Exiting q5Changed(text=%s)", text, extra={"event.action": "q5Changed", "logrite.text": text})
            
        def q2Changed(self, text):
            logger.warning(">>> Entering q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
            self.BTWnummer.setText(text)      
            logger.debug("<<< Exiting q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
            
        def q4Changed(self, text):
            logger.warning(">>> Entering q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
            self.KvKnummer.setText(text)
            logger.debug("<<< Exiting q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
      
        def q1Changed(self, text):
            logger.warning(">>> Entering q1Changed(text=%s)", text, extra={"event.action": "q1Changed", "logrite.text": text})
            self.Straat.setText(text)
            logger.debug("<<< Exiting q1Changed(text=%s)", text, extra={"event.action": "q1Changed", "logrite.text": text})
                  
        def q7Changed(self, text):
            logger.warning(">>> Entering q7Changed(text=%s)", text, extra={"event.action": "q7Changed", "logrite.text": text})
            self.Huisnummer.setText(text)
            logger.debug("<<< Exiting q7Changed(text=%s)", text, extra={"event.action": "q7Changed", "logrite.text": text})
    
        def q8Changed(self, text):
            logger.warning(">>> Entering q8Changed(text=%s)", text, extra={"event.action": "q8Changed", "logrite.text": text})
            self.Toevoeging.setText(text)          
            logger.debug("<<< Exiting q8Changed(text=%s)", text, extra={"event.action": "q8Changed", "logrite.text": text})
    
        def q6Changed(self, text):
            logger.warning(">>> Entering q6Changed(text=%s)", text, extra={"event.action": "q6Changed", "logrite.text": text})
            self.Postcode.setText(text)
            logger.debug("<<< Exiting q6Changed(text=%s)", text, extra={"event.action": "q6Changed", "logrite.text": text})
            
        def q15Changed(self, text):
            logger.warning(">>> Entering q15Changed(text=%s)", text, extra={"event.action": "q15Changed", "logrite.text": text})
            self.Woonplaats.setText(text)
            logger.debug("<<< Exiting q15Changed(text=%s)", text, extra={"event.action": "q15Changed", "logrite.text": text})
              
        def q13Changed(self, text):
            logger.warning(">>> Entering q13Changed(text=%s)", text, extra={"event.action": "q13Changed", "logrite.text": text})
            self.Telefoonnr.setText(text)
            logger.debug("<<< Exiting q13Changed(text=%s)", text, extra={"event.action": "q13Changed", "logrite.text": text})
            
        def q14Changed(self, text):
            logger.warning(">>> Entering q14Changed(text=%s)", text, extra={"event.action": "q14Changed", "logrite.text": text})
            self.Bedrijfverkoopnummer.setText(text)
            logger.debug("<<< Exiting q14Changed(text=%s)", text, extra={"event.action": "q14Changed", "logrite.text": text})
                
        def returnBedrijfsnaam(self):
            logger.warning(">>> Entering returnBedrijfsnaam()", extra={"event.action": "returnBedrijfsnaam"})
            logger.debug("<<< Exiting returnBedrijfsnaam()", extra={"event.action": "returnBedrijfsnaam"})
            return self.Bedrijfsnaam.text()
        
        def returnAfdeling(self):
            logger.warning(">>> Entering returnAfdeling()", extra={"event.action": "returnAfdeling"})
            logger.debug("<<< Exiting returnAfdeling()", extra={"event.action": "returnAfdeling"})
            return self.Afdeling.text()
        
        def returnRechtsvorm(self):
            logger.warning(">>> Entering returnRechtsvorm()", extra={"event.action": "returnRechtsvorm"})
            logger.debug("<<< Exiting returnRechtsvorm()", extra={"event.action": "returnRechtsvorm"})
            return self.Rechtsvorm.text()
    
        def returnBTWnummer(self):
            logger.warning(">>> Entering returnBTWnummer()", extra={"event.action": "returnBTWnummer"})
            logger.debug("<<< Exiting returnBTWnummer()", extra={"event.action": "returnBTWnummer"})
            return self.BTWnummer.text()
        
        def returnKvKnummer(self):
            logger.warning(">>> Entering returnKvKnummer()", extra={"event.action": "returnKvKnummer"})
            logger.debug("<<< Exiting returnKvKnummer()", extra={"event.action": "returnKvKnummer"})
            return self.KvKnummer.text()
        
        def returnStraat(self):
            logger.warning(">>> Entering returnStraat()", extra={"event.action": "returnStraat"})
            logger.debug("<<< Exiting returnStraat()", extra={"event.action": "returnStraat"})
            return self.Straat.text()
   
        def returnHuisnummer(self):
            logger.warning(">>> Entering returnHuisnummer()", extra={"event.action": "returnHuisnummer"})
            logger.debug("<<< Exiting returnHuisnummer()", extra={"event.action": "returnHuisnummer"})
            return self.Huisnummer.text()
    
        def returnToevoeging(self):
            logger.warning(">>> Entering returnToevoeging()", extra={"event.action": "returnToevoeging"})
            logger.debug("<<< Exiting returnToevoeging()", extra={"event.action": "returnToevoeging"})
            return self.Toevoeging.text()
    
        def returnPostcode(self):
            logger.warning(">>> Entering returnPostcode()", extra={"event.action": "returnPostcode"})
            logger.debug("<<< Exiting returnPostcode()", extra={"event.action": "returnPostcode"})
            return self.Postcode.text()
        
        def returnWoonplaats(self):
            logger.warning(">>> Entering returnWoonplaats()", extra={"event.action": "returnWoonplaats"})
            logger.debug("<<< Exiting returnWoonplaats()", extra={"event.action": "returnWoonplaats"})
            return self.Woonplaats.text()
           
        def returnTelefoonnummer(self):
            logger.warning(">>> Entering returnTelefoonnummer()", extra={"event.action": "returnTelefoonnummer"})
            logger.debug("<<< Exiting returnTelefoonnummer()", extra={"event.action": "returnTelefoonnummer"})
            return self.Telefoonnr.text()   
    
        def returnBedrijfverkoopnummer(self):
            logger.warning(">>> Entering returnBedrijfverkoopnummer()", extra={"event.action": "returnBedrijfverkoopnummer"})
            logger.debug("<<< Exiting returnBedrijfverkoopnummer()", extra={"event.action": "returnBedrijfverkoopnummer"})
            return self.Bedrijfverkoopnummer.text() 
         
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            return [dialog.returnBedrijfsnaam(), dialog.returnRechtsvorm(),\
                    dialog.returnBTWnummer(), dialog.returnKvKnummer(),\
                    dialog.returnStraat(),dialog.returnHuisnummer(),\
                    dialog.returnToevoeging(), dialog.returnPostcode(),\
                    dialog.returnWoonplaats(), dialog.returnTelefoonnummer(),\
                    dialog.returnBedrijfverkoopnummer(), dialog.returnAfdeling()]
                
    window = Widget()
    data = window.getData()
    if data[0]:
        mbedrnaam = (data[0])
    else:
        mbedrnaam = rpkop[1]
    if data[1]:
        mrechtsvorm = (data[1]).upper()
    else:
        mrechtsvorm = rpkop[2]
    if data[2]:
        mbtwnr = data[2].upper()
    else:
        mbtwnr = rpkop[3]
    if data[3]:
        mkvknr = data[3]
    else:
        mkvknr = rpkop[4]
    if data[7]:
        mpostcode = data[7].upper()
    else:
        mpostcode = rpkop[8]
    if data[5]:
        mhuisnr = data[5]
    else:
        mhuisnr = rpkop[6]
    mhuisnr = int(mhuisnr)
    if data[6]:
        mtoev = '-'+data[6]
    else:
        mtoev = ''
    if data[9]:
        mtelnr = data[9]
    else:
        mtelnr = ''
    if not (len(mtelnr) == 10 or mtelnr == ''):
        foutTelnr()
        hoofdMenu(m_email) 
    if data[11]:
        mafdeling = data[11]
    else:
        mafdeling = rpkop[9]
                                            
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    u = update(kopers).where(kopers.c.koperID == mkopernr).\
     values(bedrijfsnaam = mbedrnaam, rechtsvorm = mrechtsvorm, btwnummer =\
           mbtwnr, kvknummer = mkvknr, telnr = mtelnr, postcode = mpostcode,\
           huisnummer = mhuisnr, toevoeging = mtoev, afdeling = mafdeling)  
    conn.execute(u) 
    conn.close()
    updateOK()  
    zoekKoper(m_email)