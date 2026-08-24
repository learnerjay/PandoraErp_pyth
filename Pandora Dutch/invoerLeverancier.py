from login import hoofdMenu
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
                            QDialog, QMessageBox
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap, QIcon
from PyQt5.QtCore import  QRegExp, Qt
from sqlalchemy import (Table, Column, Integer, String, MetaData,\
                             create_engine, func)
from sqlalchemy.sql import select
import logging
logger = logging.getLogger(__name__)

def foutPostcode():
    logger.debug(">>> Entering foutPostcode()")
    msg = QMessageBox()
    logger.debug("foutPostcode(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Foutieve postcode ingevoerd!')
    msg.setWindowTitle('Postcode')
    logger.debug("<<< Exiting foutPostcode()")
    msg.exec_()

def geenGegevens():
    logger.debug(">>> Entering geenGegevens()")
    msg = QMessageBox()
    logger.debug("geenGegevens(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Niet (alle) vereiste gegevens ingevuld!')
    msg.setWindowTitle('Gegevens!')
    logger.debug("<<< Exiting geenGegevens()")
    msg.exec_()
    
def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)
    
def fout_email():
    logger.debug(">>> Entering fout_email()")
    msg = QMessageBox()
    logger.debug("fout_email(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('ongeldig email adres!')
    msg.setWindowTitle('e-mailadres!')
    logger.debug("<<< Exiting fout_email()")
    msg.exec_()

def foutTelnr():
    logger.debug(">>> Entering foutTelnr()")
    msg = QMessageBox()
    logger.debug("foutTelnr(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('geen 10 cijfers!')
    msg.setWindowTitle('Telefoonnummer!')
    logger.debug("<<< Exiting foutTelnr()")
    msg.exec_()

def dontMatch():
    logger.debug(">>> Entering dontMatch()")
    msg = QMessageBox()
    logger.debug("dontMatch(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Wachtwoord niet identiek\nen/of minder dan 8 tekens!')
    msg.setWindowTitle('Wachtwoord!')
    logger.debug("<<< Exiting dontMatch()")
    msg.exec_()
 
def leverancierBestaat():
    logger.debug(">>> Entering leverancierBestaat()")
    msg = QMessageBox()
    logger.debug("leverancierBestaat(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Leverancier is al aanweizg!')
    msg.setWindowTitle('Account')
    logger.debug("<<< Exiting leverancierBestaat()")
    msg.exec_()

def maak11proef(basisnr):
   logger.debug(">>> Entering maak11proef(basisnr=%s)", basisnr)
   basisnr = str(basisnr)
   basisnr = str((int(basisnr[0:8]))+int(1))
   logger.debug("maak11proef(basisnr=%s): basisnr → %s", basisnr, basisnr)
   total = 0                       
   logger.debug("maak11proef(basisnr=%s): total → %s", basisnr, total)
   for i in range(int(8)):
       total += int(basisnr[i])*(int(9)-i)
   checkdigit = total % 11 % 10
   logger.debug("maak11proef(basisnr=%s): checkdigit → %s", basisnr, checkdigit)
   basisuitnr = basisnr+str(checkdigit)
   logger.debug("maak11proef(basisnr=%s): basisuitnr → %s", basisnr, basisuitnr)
   logger.debug("<<< Exiting maak11proef(basisnr=%s)", basisnr)
   logger.debug("bepaalLeverancier(m_email=%s): leveranciers → %s", m_email, leveranciers)
   logger.debug("bepaalLeverancier(m_email=%s): engine → %s", m_email, engine)
   return basisuitnr

def bepaalLeverancier(m_email):
    logger.debug(">>> Entering bepaalLeverancier(m_email=%s)", m_email)
    metadata = MetaData()
    logger.debug("bepaalLeverancier(m_email=%s): metadata → %s", m_email, metadata)
    leveranciers = Table('leveranciers', metadata,
        Column('leverancierID', Integer(), primary_key=True))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    try:
        logger.debug("bepaalLeverancier(m_email=%s): conn → %s", m_email, conn)
        mlevnr=(conn.execute(select([func.max(leveranciers.c.leverancierID,\
            type_=Integer)])).scalar())
        mlevnr=int(maak11proef(mlevnr))
        logger.debug("bepaalLeverancier(m_email=%s): mlevnr → %s", m_email, mlevnr)
        logger.debug("bepaalLeverancier(m_email=%s): type_ → %s", m_email, type_)
        conn.close
    except:
        mlevnr = 300000005
    invLeverancier(mlevnr, m_email)
    logger.error("Exception in bepaalLeverancier(m_email=%s)", m_email, exc_info=True)
    logger.debug("<<< Exiting bepaalLeverancier(m_email=%s)", m_email)
   
def Invoer():
    logger.debug(">>> Entering Invoer()")
    msg = QMessageBox()
    logger.debug("Invoer(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Invoer gelukt!')
    msg.setWindowTitle('Leveranciergegevens')
    logger.debug("<<< Exiting Invoer()")
    msg.exec_()

def invLeverancier(mlevnr, m_email):                                 
    logger.debug(">>> Entering invLeverancier(mlevnr=%s,m_email=%s)", mlevnr, m_email)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            logger.debug("__init__(parent=%s): font → %s", parent, font)
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator)
            self.setWindowTitle("Invoer leverancier")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                                  
            self.setFont(QFont('Arial', 10))
                  
            self.Bedrijfsnaam = QLabel()
            logger.debug("__init__(parent=%s): self.Bedrijfsnaam → %s", parent, self.Bedrijfsnaam)
            q3Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit)
            logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit)
            q3Edit.setFixedWidth(540)
            q3Edit.setFont(QFont("Arial",10))
            q3Edit.textChanged.connect(self.q3Changed)
            reg_ex = QRegExp("^.{1,50}$")
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex)
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex)
            input_validator = QRegExpValidator(reg_ex, q3Edit)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator)
            q3Edit.setValidator(input_validator)
            
            self.Rechtsvorm = QLabel()
            logger.debug("__init__(parent=%s): self.Rechtsvorm → %s", parent, self.Rechtsvorm)
            q5Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit)
            logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit)
            q5Edit.setFixedWidth(200)
            q5Edit.setFont(QFont("Arial",10))
            q5Edit.textChanged.connect(self.q5Changed)
            reg_ex = QRegExp("^.{1,30}$")
            input_validator = QRegExpValidator(reg_ex, q5Edit)
            q5Edit.setValidator(input_validator)
            
            self.BTWnummer =  QLabel()
            logger.debug("__init__(parent=%s): self.BTWnummer → %s", parent, self.BTWnummer)
            q2Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit)
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit)
            q2Edit.setFixedWidth(170)
            q2Edit.setText("")
            q2Edit.setFont(QFont("Arial",10))
            q2Edit.textChanged.connect(self.q2Changed)
            reg_ex = QRegExp("^[NLnl]{2}[0-9]{9}[Bb]{1}[0-9]{2}$")
            input_validator = QRegExpValidator(reg_ex, q2Edit)
            q2Edit.setValidator(input_validator)
            
            self.KvKnummer =  QLabel()
            logger.debug("__init__(parent=%s): self.KvKnummer → %s", parent, self.KvKnummer)
            q4Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit)
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit)
            q4Edit.setFixedWidth(120)
            q4Edit.setFont(QFont("Arial",10))
            q4Edit.textChanged.connect(self.q4Changed)
            reg_ex = QRegExp("^[0-9]{8}$")
            input_validator = QRegExpValidator(reg_ex, q4Edit)
            q4Edit.setValidator(input_validator)
       
            self.Postcode = QLabel()
            logger.debug("__init__(parent=%s): self.Postcode → %s", parent, self.Postcode)
            q6Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q6Edit → %s", self, parent, q6Edit)
            logger.debug("__init__(parent=%s): q6Edit → %s", parent, q6Edit)
            q6Edit.setFixedWidth(80)
            font = QFont("Arial",10)
            logger.debug("__init__(self=%s,parent=%s): font → %s", self, parent, font)
            font.setCapitalization(QFont.AllUppercase)
            q6Edit.setFont(font)
            q6Edit.textChanged.connect(self.q6Changed)
            reg_ex = QRegExp("^[0-9]{4}[A-Za-z]{2}$")
            input_validator = QRegExpValidator(reg_ex, q6Edit)
            q6Edit.setValidator(input_validator)
            
            self.Huisnummer = QLabel()
            logger.debug("__init__(parent=%s): self.Huisnummer → %s", parent, self.Huisnummer)
            q7Edit = QLineEdit()
            logger.debug("__init__(parent=%s): q7Edit → %s", parent, q7Edit)
            logger.debug("__init__(self=%s,parent=%s): q7Edit → %s", self, parent, q7Edit)
            q7Edit.setFixedWidth(60)
            q7Edit.setFont(QFont("Arial",10))
            q7Edit.textChanged.connect(self.q7Changed)
            reg_ex = QRegExp("^[0-9]{1,5}$")
            input_validator = QRegExpValidator(reg_ex, q7Edit)
            q7Edit.setValidator(input_validator)
    
            self.Toevoeging = QLabel()
            q8Edit = QLineEdit()
            logger.debug("__init__(parent=%s): self.Toevoeging → %s", parent, self.Toevoeging)
            logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit)
            logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit)
            q8Edit.setFixedWidth(80)
            q8Edit.setFont(QFont("Arial",10))
            q8Edit.textChanged.connect(self.q8Changed)
            reg_ex = QRegExp("^[A-Za-z0-9-]{0,10}")
            input_validator = QRegExpValidator(reg_ex, q8Edit)
            q8Edit.setValidator(input_validator)
               
            self.Telefoonnr = QLabel()
            q12Edit = QLineEdit()
            q12Edit.setFixedWidth(120)
            logger.debug("__init__(parent=%s): self.Telefoonnr → %s", parent, self.Telefoonnr)
            logger.debug("__init__(self=%s,parent=%s): q12Edit → %s", self, parent, q12Edit)
            logger.debug("__init__(parent=%s): q12Edit → %s", parent, q12Edit)
            q12Edit.setFont(QFont("Arial",10))
            q12Edit.textChanged.connect(self.q12Changed)
            reg_ex = QRegExp("^[0]{1}[0-9]{9}$")
            input_validator = QRegExpValidator(reg_ex, q12Edit)
            q12Edit.setValidator(input_validator)
            
            self.Leveranciernummer =  QLabel()
            q13Edit = QLineEdit(str(mlevnr))
            q13Edit.setFixedWidth(110)
            q13Edit.setStyleSheet("color: black")
            logger.debug("__init__(parent=%s): self.Leveranciernummer → %s", parent, self.Leveranciernummer)
            logger.debug("__init__(self=%s,parent=%s): q13Edit → %s", self, parent, q13Edit)
            logger.debug("__init__(parent=%s): q13Edit → %s", parent, q13Edit)
            q13Edit.setAlignment(Qt.AlignRight)
            q13Edit.setDisabled(True)
            q13Edit.setFont(QFont("Arial",10))
             
            grid = QGridLayout()
            grid.setSpacing(20)
            
            lbl = QLabel()
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid)
            logger.debug("__init__(parent=%s): grid → %s", parent, grid)
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0)
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl)
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap)
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 2, 1, 2, Qt.AlignRight)
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
    
            self.setFont(QFont('Arial', 10))
            grid.addWidget(QLabel('Nieuwe leverancier invoeren'), 0, 1, 1, 2,Qt.AlignCenter)
                        
            grid.addWidget(QLabel('                              *'), 1, 0) 
            grid.addWidget(QLabel('Verplichte velden'), 1, 1)   
                         
            grid.addWidget(QLabel('Bedrijfsnaam           *'), 2, 0)
            grid.addWidget(q3Edit, 2, 1, 1, 3)  
                 
            grid.addWidget(QLabel('Rechtsvorm             *'), 3, 0)
            grid.addWidget(q5Edit, 3, 1) 
            
            grid.addWidget(QLabel('BTWnummer   *'), 3, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(q2Edit, 3, 2) 
            
            grid.addWidget(QLabel('KvKnummer             *'), 4, 0)
            grid.addWidget(q4Edit, 4, 1) 
                 
            grid.addWidget(QLabel('Postcode  *'), 4, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(q6Edit, 4, 2)
     
            grid.addWidget(QLabel('Huisnummer            *'), 5, 0)
            grid.addWidget(q7Edit, 5, 1)
    
            grid.addWidget(QLabel('Toevoeging'), 5, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(q8Edit, 5, 2)
      
            grid.addWidget(QLabel('Telefoonnummer      *'), 6, 0)
            grid.addWidget(q12Edit, 6, 1) 
            
            grid.addWidget(QLabel('Leveranciernummer'), 7, 0)
            grid.addWidget(q13Edit, 7, 1) 
                                
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 8, 1)
              
            cancelBtn = QPushButton('Sluiten')
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn)
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn)
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
            
            applyBtn = QPushButton('Invoeren')
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            applyBtn.clicked.connect(self.accept)
                       
            grid.addWidget(applyBtn, 7, 2, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
        
            grid.addWidget(cancelBtn, 6, 2, 1, 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            self.setLayout(grid)
            self.setGeometry(500, 100, 150, 150)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
          
        def q3Changed(self, text):
            logger.debug(">>> Entering q3Changed(text=%s)", text)
            logger.debug("q3Changed(self=%s,text=%s): Bedrijfsnaam → %s", self, text, Bedrijfsnaam)
            self.Bedrijfsnaam.setText(text)
            logger.debug("<<< Exiting q3Changed(text=%s)", text)
                    
        def q5Changed(self, text):
            logger.debug(">>> Entering q5Changed(text=%s)", text)
            logger.debug("q5Changed(self=%s,text=%s): Rechtsvorm → %s", self, text, Rechtsvorm)
            self.Rechtsvorm.setText(text)
            logger.debug("<<< Exiting q5Changed(text=%s)", text)
            
        def q2Changed(self, text):
            logger.debug(">>> Entering q2Changed(text=%s)", text)
            logger.debug("q2Changed(self=%s,text=%s): BTWnummer → %s", self, text, BTWnummer)
            self.BTWnummer.setText(text)      
            logger.debug("<<< Exiting q2Changed(text=%s)", text)
            
        def q4Changed(self, text):
            logger.debug(">>> Entering q4Changed(text=%s)", text)
            logger.debug("q4Changed(self=%s,text=%s): KvKnummer → %s", self, text, KvKnummer)
            self.KvKnummer.setText(text)
            logger.debug("<<< Exiting q4Changed(text=%s)", text)
    
        def q6Changed(self, text):
            logger.debug(">>> Entering q6Changed(text=%s)", text)
            logger.debug("q6Changed(self=%s,text=%s): Postcode → %s", self, text, Postcode)
            self.Postcode.setText(text)
            logger.debug("<<< Exiting q6Changed(text=%s)", text)
                  
        def q7Changed(self, text):
            logger.debug(">>> Entering q7Changed(text=%s)", text)
            logger.debug("q7Changed(self=%s,text=%s): Huisnummer → %s", self, text, Huisnummer)
            self.Huisnummer.setText(text)
            logger.debug("<<< Exiting q7Changed(text=%s)", text)
    
        def q8Changed(self, text):
            logger.debug(">>> Entering q8Changed(text=%s)", text)
            logger.debug("q8Changed(self=%s,text=%s): Toevoeging → %s", self, text, Toevoeging)
            self.Toevoeging.setText(text)
            logger.debug("<<< Exiting q8Changed(text=%s)", text)
        
        def q12Changed(self, text):
            logger.debug(">>> Entering q12Changed(text=%s)", text)
            logger.debug("q12Changed(self=%s,text=%s): Telefoonnr → %s", self, text, Telefoonnr)
            self.Telefoonnr.setText(text)
            logger.debug("<<< Exiting q12Changed(text=%s)", text)
            
        def returnBedrijfsnaam(self):
            logger.debug(">>> Entering returnBedrijfsnaam()")
            logger.debug("<<< Exiting returnBedrijfsnaam()")
            return self.Bedrijfsnaam.text()
        
        def returnRechtsvorm(self):
            logger.debug(">>> Entering returnRechtsvorm()")
            logger.debug("<<< Exiting returnRechtsvorm()")
            return self.Rechtsvorm.text()
    
        def returnBTWnummer(self):
            logger.debug(">>> Entering returnBTWnummer()")
            logger.debug("<<< Exiting returnBTWnummer()")
            return self.BTWnummer.text()
        
        def returnKvKnummer(self):
            logger.debug(">>> Entering returnKvKnummer()")
            logger.debug("<<< Exiting returnKvKnummer()")
            return self.KvKnummer.text()
    
        def returnPostcode(self):
            logger.debug(">>> Entering returnPostcode()")
            logger.debug("<<< Exiting returnPostcode()")
            return self.Postcode.text()
        
        def returnHuisnummer(self):
            logger.debug(">>> Entering returnHuisnummer()")
            logger.debug("<<< Exiting returnHuisnummer()")
            return self.Huisnummer.text()
    
        def returnToevoeging(self):
            logger.debug(">>> Entering returnToevoeging()")
            logger.debug("<<< Exiting returnToevoeging()")
            return self.Toevoeging.text()
        
        def returnTelefoonnummer(self):
            logger.debug(">>> Entering returnTelefoonnummer()")
            logger.debug("<<< Exiting returnTelefoonnummer()")
            return self.Telefoonnr.text()   
    
         
        @staticmethod
        def getData(parent=None):
            logger.debug(">>> Entering getData(parent=%s)", parent)
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent)
            return [dialog.returnBedrijfsnaam(), dialog.returnRechtsvorm(),\
                    dialog.returnBTWnummer(), dialog.returnKvKnummer(),\
                    dialog.returnPostcode(), dialog.returnHuisnummer(),\
                    dialog.returnToevoeging(), dialog.returnTelefoonnummer()]
               
    window = Widget()
    data = window.getData()
    mbedrijfsnaam = (data[0]).title()
    mrechtsvorm = (data[1]).upper()
    mbtwnr = data[2].upper()
    mkvknr = data[3]
    mpostcode = (data[4]).upper()
    mhuisnr = data[5]
    if not (mbedrijfsnaam and mrechtsvorm and mpostcode and mhuisnr):
        geenGegevens()
        bepaalLeverancier(m_email)
    mhuisnr = int(mhuisnr)
    mtoev = (data[6])
    if mtoev:
        mtoev = '-'+mtoev
    mtelnr = (data[7])
    if data[7]:
        if len(mtelnr) < 10:
            foutTelnr()
            bepaalLeverancier(m_email)
    else:
            geenGegevens()
            bepaalLeverancier(m_email)
    import postcode
    if postcode.checkpostcode(mpostcode,mhuisnr)[0]:
        metadata = MetaData()

        leveranciers = Table('leveranciers', metadata,
            Column('leverancierID', Integer(), primary_key=True),
            Column('bedrijfsnaam', String),
            Column('rechtsvorm', String),
            Column('btwnummer', String),
            Column('kvknummer', String),
            Column('telnr', String(10)),
            Column('huisnummer', String(5), nullable=False),
            Column('postcode', String(6), nullable=False),       
            Column('toevoeging', String))
                        
        engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
        conn = engine.connect()
                                             
        conn = engine.connect()
        s = select([leveranciers.c.leverancierID]).\
                where(leveranciers.c.leverancierID == mlevnr)
        result = conn.execute(s).first()
        
        if result:
            conn.close()
            leverancierBestaat()
            bepaalLeverancier(m_email)
        else:
            inslev = leveranciers.insert().values(
            leverancierID=mlevnr,  
            bedrijfsnaam=mbedrijfsnaam,
            rechtsvorm=mrechtsvorm,
            btwnummer=mbtwnr,
            kvknummer=mkvknr,
            postcode=mpostcode,
            huisnummer=mhuisnr,
            toevoeging=mtoev,
            telnr=mtelnr)
            result = conn.execute(inslev)
            inslev.bind = engine
            result.inserted_primary_key
            conn.close()
            Invoer()
    else:
           foutPostcode()
    bepaalLeverancier(m_email)