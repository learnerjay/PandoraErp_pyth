import login
import datetime, re
from argon2 import PasswordHasher
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
     QDialog, QComboBox, QMessageBox
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QRegExp
from sqlalchemy import (Table, Column, Integer, String, MetaData,\
                          create_engine, func, ForeignKey)
from sqlalchemy.sql import select
import logging
logger = logging.getLogger(__name__)

def foutPostcode():
    logger.warning(">>> Entering foutPostcode()", extra={"event.action": "foutPostcode"})
    msg = QMessageBox()
    logger.debug("foutPostcode(): msg → %s", msg, extra={"event.action": "foutPostcode"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Foutieve postcode ingevoerd!')
    msg.setWindowTitle('POSTCODE!')
    logger.debug("<<< Exiting foutPostcode()", extra={"event.action": "foutPostcode"})
    msg.exec_()
  
def info():
    logger.warning(">>> Entering info()", extra={"event.action": "info"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Informatie over aanmaken nieuw account")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
            grid = QGridLayout()
            grid.setSpacing(20)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 0, 1, 1, Qt.AlignRight)
        
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 0, 0)
            
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Aanhef → %s", parent, self.Aanhef, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Voornaam → %s", parent, self.Voornaam, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Tussenvoegsel → %s", parent, self.Tussenvoegsel, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Achternaam → %s", parent, self.Achternaam, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Postcode → %s", parent, self.Postcode, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q6Edit → %s", parent, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q6Edit → %s", self, parent, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): font → %s", parent, font, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): font → %s", self, parent, font, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Huisnummer → %s", parent, self.Huisnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q7Edit → %s", parent, q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q7Edit → %s", self, parent, q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Toevoeging → %s", parent, self.Toevoeging, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.email → %s", parent, self.email, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q9Edit → %s", parent, q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q9Edit → %s", self, parent, q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Wachtwoord → %s", parent, self.Wachtwoord, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q10Edit → %s", parent, q10Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q10Edit → %s", self, parent, q10Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.ContrWachtwoord → %s", parent, self.ContrWachtwoord, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q11Edit → %s", parent, q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q11Edit → %s", self, parent, q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Telefoonnr → %s", parent, self.Telefoonnr, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q12Edit → %s", parent, q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q12Edit → %s", self, parent, q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Accountnummer → %s", parent, self.Accountnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q13Edit → %s", parent, q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q13Edit → %s", self, parent, q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Geboortedatum → %s", parent, self.Geboortedatum, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q14Edit → %s", parent, q14Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q14Edit → %s", self, parent, q14Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): helpBtn → %s", parent, helpBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): helpBtn → %s", self, parent, helpBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            infolbl = QLabel(
      '''

        Informatie over aanmaken nieuw account                                                  
                                                                                              
                                                                                               
        Verplichte invoervelden: 

        Voornaam en achternaam.                                                              
                                                                                               
        Postcode 4 cijfers en 2 letters zonder spatie.\t\t
        Huisnummer.            
                                                                                               
        Geldig emailadres.                                                                     
                                                                                               
        Wachtwoord minimaal 8 tekens.                                                          
        Wachtwoord controle identiek aan  wachtwoord.   

        Geboortedatum formaat jjjj-mm-dd                                       
        
        Optioneel:                                                                                       
        Telefoonnummer 10 cijfers, 1e cijfer een 0.                                            
    
  
     ''')
            grid.addWidget(infolbl, 0, 0)
            
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(self.close)  
            
            grid.addWidget(cancelBtn,  2, 0, 1, 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(90)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                
            infolbl.setStyleSheet("font: 10pt Comic Sans MS; color: black ; background-color: #D9E1DF")   
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 1, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(350, 250, 150, 100)
            
    window = Widget()
    window.exec_()

def password_check(password):
    logger.warning(">>> Entering password_check(password=<redacted>)", extra={"event.action": "password_check"})
    ph = PasswordHasher()
    logger.debug("password_check(password=<redacted>): ph → %s", ph, extra={"event.action": "password_check"})
    try:
        if ph.verify(ph.hash(password), password):  # True
            return(True)
    except Exception:
        logger.error("Exception in password_check(password=<redacted>)", exc_info=True, extra={"event.action": "password_check", "event.category": "process"})
        logger.debug("<<< Exiting password_check(password=<redacted>)", extra={"event.action": "password_check"})
        return(False)
 
def valid(item, valnr):
    logger.warning(">>> Entering valid(item=%s,valnr=%s)", item, valnr, extra={"event.action": "valid", "logrite.item": item, "logrite.valnr": valnr})
    if valnr == 1:
        # Postcode
        ab = re.compile("^([0-9]{4}[A-Za-z]{2})+$")
        logger.debug("valid(item=%s,valnr=%s): ab → %s", item, valnr, ab, extra={"event.action": "valid", "logrite.item": item, "logrite.valnr": valnr})
        if ab.match(item):
            return(True)
        else:
            return(False)
    elif valnr == 2:
        #huisnummer
        if item.isnumeric() and len(item) < 7:
            return(True)
        else:
            return(False)
    elif valnr == 3:
        #e-mail
        ab = re.compile("^([A-Za-z0-9._-]{1,}@(\\w+)(\\.(\\w+))(\\.(\\w+))?(\\.(\\w+))?)$")
        if ab.match(item):
            return(True)
        else:
            return(False)
    elif valnr == 6:
        #telefoonnummer
        if (len(item) == 10 and item.isnumeric and item[0] == '0') or item == '':
            return(True)
        else:
            logger.debug("<<< Exiting valid(item=%s,valnr=%s)", item, valnr, extra={"event.action": "valid", "logrite.item": item, "logrite.valnr": valnr})
            return(False) 
 
def windowSluit(self):
    logger.warning(">>> Entering windowSluit()", extra={"event.action": "windowSluit"})
    self.close()
    login.inlog()
    logger.debug("<<< Exiting windowSluit()", extra={"event.action": "windowSluit"})
     
def password_hash(password):
    logger.warning(">>> Entering password_hash(password=<redacted>)", extra={"event.action": "password_hash"})
    ph = PasswordHasher()
    logger.debug("password_hash(password=<redacted>): ph → %s", ph, extra={"event.action": "password_hash"})
    logger.debug("<<< Exiting password_hash(password=<redacted>)", extra={"event.action": "password_hash"})
    return(ph.hash(password))  # store hashpass in bisystem table  accounts,  field password
   
def geenGegevens():
    logger.warning(">>> Entering geenGegevens()", extra={"event.action": "geenGegevens"})
    msg = QMessageBox()
    logger.debug("geenGegevens(): msg → %s", msg, extra={"event.action": "geenGegevens"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Niet (alle) vereiste gegevens juist ingevuld!')
    msg.setWindowTitle('Gegevens!')
    logger.debug("<<< Exiting geenGegevens()", extra={"event.action": "geenGegevens"})
    msg.exec_()

def fout_email():
    logger.warning(">>> Entering fout_email()", extra={"event.action": "fout_email"})
    msg = QMessageBox()
    logger.debug("fout_email(): msg → %s", msg, extra={"event.action": "fout_email"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('ongeldig email adres!')
    msg.setWindowTitle('e-mailadres!')
    logger.debug("<<< Exiting fout_email()", extra={"event.action": "fout_email"})
    msg.exec_()

def foutTelnr():
    logger.warning(">>> Entering foutTelnr()", extra={"event.action": "foutTelnr"})
    msg = QMessageBox()
    logger.debug("foutTelnr(): msg → %s", msg, extra={"event.action": "foutTelnr"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('geen 10 cijfers!')
    msg.setWindowTitle('Telefoonnummer!')
    logger.debug("<<< Exiting foutTelnr()", extra={"event.action": "foutTelnr"})
    msg.exec_()

def accountBestaat():
    logger.warning(">>> Entering accountBestaat()", extra={"event.action": "accountBestaat"})
    msg = QMessageBox()
    logger.debug("accountBestaat(): msg → %s", msg, extra={"event.action": "accountBestaat"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Reeds bestaand account!')
    msg.setWindowTitle('Account')
    logger.debug("<<< Exiting accountBestaat()", extra={"event.action": "accountBestaat"})
    msg.exec_()

def dontMatch():
    logger.warning(">>> Entering dontMatch()", extra={"event.action": "dontMatch"})
    msg = QMessageBox()
    logger.debug("dontMatch(): msg → %s", msg, extra={"event.action": "dontMatch"})
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Wachtwoord niet identiek\nen/of minder dan 8 tekens!')
    msg.setWindowTitle('Wachtwoord!')
    logger.debug("<<< Exiting dontMatch()", extra={"event.action": "dontMatch"})
    msg.exec_()

def maak11proef(basisnr):
   logger.warning(">>> Entering maak11proef(basisnr=%s)", basisnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   basisnr = str(basisnr)
   basisnr = str((int(basisnr[0:8]))+int(1))
   logger.debug("maak11proef(basisnr=%s): basisnr → %s", basisnr, basisnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   total = 0                       
   logger.debug("maak11proef(basisnr=%s): total → %s", basisnr, total, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   for i in range(int(8)):
       total += int(basisnr[i])*(int(9)-i)
   checkdigit = total % 11 %10
   logger.debug("maak11proef(basisnr=%s): checkdigit → %s", basisnr, checkdigit, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   basisuitnr = basisnr+str(checkdigit)
   logger.debug("maak11proef(basisnr=%s): basisuitnr → %s", basisnr, basisuitnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   logger.debug("<<< Exiting maak11proef(basisnr=%s)", basisnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   return basisuitnr

def bepaalAccountnr():
    logger.warning(">>> Entering bepaalAccountnr()", extra={"event.action": "bepaalAccountnr"})
    metadata = MetaData()
    logger.debug("bepaalAccountnr(): metadata → %s", metadata, extra={"event.action": "bepaalAccountnr"})
    accounts = Table('accounts', metadata,
        Column('accountID', Integer(), primary_key=True))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("bepaalAccountnr(): engine → %s", engine, extra={"event.action": "bepaalAccountnr"})
    conn = engine.connect()
    logger.debug("bepaalAccountnr(): conn → %s", conn, extra={"event.action": "bepaalAccountnr"})
    
    try:
        maccountnr=(conn.execute(select([func.max(accounts.c.accountID,\
            type_=Integer)])).scalar())
        logger.debug("bepaalAccountnr(): type_ → %s", type_, extra={"event.action": "bepaalAccountnr"})
        maccountnr=int(maak11proef(maccountnr))
    except:
        maccountnr = 100000010
        logger.debug("bepaalAccountnr(): maccountnr → %s", maccountnr, extra={"event.action": "bepaalAccountnr"})
        logger.error("Exception in bepaalAccountnr()", exc_info=True, extra={"event.action": "bepaalAccountnr", "event.category": "process"})
    conn.close
    logger.debug("<<< Exiting bepaalAccountnr()", extra={"event.action": "bepaalAccountnr"})
    return(maccountnr)
   
def Invoer():
    logger.warning(">>> Entering Invoer()", extra={"event.action": "Invoer"})
    msg = QMessageBox()
    logger.debug("Invoer(): msg → %s", msg, extra={"event.action": "Invoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Invoer gelukt!')
    msg.setWindowTitle('Accountgegevens')
    logger.debug("<<< Exiting Invoer()", extra={"event.action": "Invoer"})
    msg.exec_()
    
def nieuwAccount(self):
    logger.warning(">>> Entering nieuwAccount()", extra={"event.action": "nieuwAccount"})
    self.close()
    logger.error("Exception in nieuwAccount()", exc_info=True, extra={"event.action": "nieuwAccount", "event.category": "process"})
    class Widget(QDialog):
        logger.debug("<<< Exiting nieuwAccount()", extra={"event.action": "nieuwAccount"})
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Invoer account")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                                  
            self.setFont(QFont('Arial', 10))
                
            self.Aanhef = QLabel()
            q2Edit = QComboBox()
            q2Edit.setFixedWidth(80)
            q2Edit.setFont(QFont("Arial",10))
            q2Edit.setStyleSheet("color: black;  background-color: gainsboro")
            q2Edit.addItem(' ')
            q2Edit.addItem('Dhr. ')
            q2Edit.addItem('Mevr. ')
            q2Edit.activated[str].connect(self.q2Changed)
            
            self.Voornaam = QLabel()
            q3Edit = QLineEdit()
            q3Edit.setFixedWidth(200)
            q3Edit.setFont(QFont("Arial",10))
            q3Edit.textChanged.connect(self.q3Changed)
            reg_ex = QRegExp("^.{1,30}$")
            input_validator = QRegExpValidator(reg_ex, q3Edit)
            q3Edit.setValidator(input_validator)
            
            self.Tussenvoegsel = QLabel()
            q4Edit = QLineEdit()
            q4Edit.setFixedWidth(80)
            q4Edit.setFont(QFont("Arial",10))
            q4Edit.textChanged.connect(self.q4Changed)
            reg_ex = QRegExp("^.{1,10}$")
            input_validator = QRegExpValidator(reg_ex, q3Edit)
            q4Edit.setValidator(input_validator)
            
            self.Achternaam = QLabel()
            q5Edit = QLineEdit()
            q5Edit.setFixedWidth(540)
            q5Edit.setFont(QFont("Arial",10))
            q5Edit.textChanged.connect(self.q5Changed)
            reg_ex = QRegExp("^.{1,50}$")
            input_validator = QRegExpValidator(reg_ex, q5Edit)
            q5Edit.setValidator(input_validator)
    
            self.Postcode = QLabel()
            q6Edit = QLineEdit()
            q6Edit.setFixedWidth(80)
            font = QFont("Arial",10)
            font.setCapitalization(QFont.AllUppercase)
            q6Edit.setFont(font)
            q6Edit.textChanged.connect(self.q6Changed)
            reg_ex = QRegExp("^[0-9]{4}[A-Za-z]{2}$")
            input_validator = QRegExpValidator(reg_ex, q6Edit)
            q6Edit.setValidator(input_validator)
            
            self.Huisnummer = QLabel()
            q7Edit = QLineEdit()
            q7Edit.setFixedWidth(60)
            q7Edit.setFont(QFont("Arial",10))
            q7Edit.textChanged.connect(self.q7Changed)
            reg_ex = QRegExp("^[0-9]{1,5}$")
            input_validator = QRegExpValidator(reg_ex, q7Edit)
            q7Edit.setValidator(input_validator)
    
            self.Toevoeging = QLabel()
            q8Edit = QLineEdit()
            q8Edit.setFixedWidth(80)
            q8Edit.setFont(QFont("Arial",10))
            q8Edit.textChanged.connect(self.q8Changed)
            reg_ex = QRegExp("^[A-Za-z0-9-]{0,8}")
            input_validator = QRegExpValidator(reg_ex, q8Edit)
            q8Edit.setValidator(input_validator)
               
            self.email = QLabel()
            q9Edit = QLineEdit()
            q9Edit.setFixedWidth(300)
            q9Edit.setFont(QFont("Arial",10))
            q9Edit.textChanged.connect(self.q9Changed)
            reg_ex = QRegExp("^([A-Za-z0-9._-]{1,}@(\\w+)(\\.(\\w+))(\\.(\\w+))?(\\.(\\w+))?)$")
            input_validator = QRegExpValidator(reg_ex, q9Edit)
            q9Edit.setValidator(input_validator)
       
            self.Wachtwoord = QLabel()
            q10Edit = QLineEdit()
            q10Edit.setFixedWidth(300)
            q10Edit.setFont(QFont("Arial",10))
            q10Edit.setEchoMode(QLineEdit.Password)
            q10Edit.textChanged.connect(self.q10Changed)
            
            self.ContrWachtwoord = QLabel()
            q11Edit = QLineEdit()
            q11Edit.setFixedWidth(300)
            q11Edit.setFont(QFont("Arial",10))
            q11Edit.setEchoMode(QLineEdit.Password)
            q11Edit.textChanged.connect(self.q11Changed)
    
            self.Telefoonnr = QLabel()
            q12Edit = QLineEdit()
            q12Edit.setFixedWidth(100)
            q12Edit.setFont(QFont("Arial",10))
            q12Edit.textChanged.connect(self.q12Changed)
            reg_ex = QRegExp("^[0]{1}[0-9]{9}$")
            input_validator = QRegExpValidator(reg_ex, q12Edit)
            q12Edit.setValidator(input_validator)
            
            self.Accountnummer = QLabel()
            q13Edit = QLineEdit(str(bepaalAccountnr()))
            q13Edit.setFixedWidth(100)
            q13Edit.setDisabled(True)
            q13Edit.setStyleSheet("QLineEdit { background-color: ; color: black }")
            q13Edit.setFont(QFont("Arial",10))
            q13Edit.textChanged.connect(self.q13Changed)
            
            self.Geboortedatum = QLabel()
            q14Edit = QLineEdit()
            q14Edit.setFixedWidth(100)
            q14Edit.setFont(QFont("Arial",10))
            q14Edit.textChanged.connect(self.q14Changed)
            reg_ex = QRegExp('^[1-2]{1}[09]{1}[0-9]{2}-[0-1]{1}[0-9]{1}-[0-3]{1}[0-9]{1}$')
            input_validator = QRegExpValidator(reg_ex, q14Edit)
            q14Edit.setValidator(input_validator)  
            
            grid = QGridLayout()
            grid.setSpacing(20)
            
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 1, 0)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 2, 1, 1, Qt.AlignRight)
    
            self.setFont(QFont('Arial', 10))
            grid.addWidget(QLabel('Nieuw account invoeren'), 1, 1)
                        
            grid.addWidget(QLabel('                                  *'), 2, 0) 
            grid.addWidget(QLabel('Verplichte velden'), 2, 1)   
                         
            grid.addWidget(QLabel('Aanhef'), 3, 0)
            grid.addWidget(q2Edit, 3, 1)
             
            grid.addWidget(QLabel('Voornaam                   *'), 4, 0)
            grid.addWidget(q3Edit, 4, 1)  
     
            grid.addWidget(QLabel('Tussenvoegel'), 5, 0)
            grid.addWidget(q4Edit, 5 , 1) 
             
            grid.addWidget(QLabel('Achternaam                *'), 6, 0)
            grid.addWidget(q5Edit, 6, 1, 1 , 2) 
            
            grid.addWidget(QLabel('Geboortedatum           *'), 7, 0)
            grid.addWidget(QLabel('                             formaat: jjjj-mm-dd'), 7, 1, 1, 2 )
            grid.addWidget(q14Edit, 7, 1)
                 
            grid.addWidget(QLabel('Postcode                    *'), 8, 0)
            grid.addWidget(q6Edit, 8, 1)
     
            grid.addWidget(QLabel('Huisnummer                *'), 9, 0)
            grid.addWidget(q7Edit, 9, 1)
            
            grid.addWidget(QLabel('Toevoeging'), 9, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(q8Edit, 9, 2)
    
            grid.addWidget(QLabel('e-mail                         *'), 10, 0)
            grid.addWidget(q9Edit, 10, 1, 1 ,2)
        
            grid.addWidget(QLabel('Wachtwoord                *'), 11, 0)
            grid.addWidget(q10Edit, 11, 1, 1 ,2) 
            
            grid.addWidget(QLabel('Wachtwoord controle    *'), 12, 0)
            grid.addWidget(q11Edit, 12, 1, 1, 2) 
    
            grid.addWidget(QLabel('Telefoonnummer'), 13, 0)
            grid.addWidget(q12Edit, 13, 1) 
           
            grid.addWidget(QLabel('Accountnummer'), 14, 0)
            grid.addWidget(q13Edit, 14, 1) 
                                
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 16, 0, 1, 3, Qt.AlignCenter)
            
            applyBtn = QPushButton('Invoeren')
            applyBtn.clicked.connect(self.accept)
                       
            grid.addWidget(applyBtn, 14, 2, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: windowSluit(self))
        
            grid.addWidget(cancelBtn, 13, 2 , 1, 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            helpBtn = QPushButton('Info')
            helpBtn.clicked.connect(lambda: info())
          
            grid.addWidget(helpBtn, 12, 2 , 1, 1, Qt.AlignRight)
            helpBtn.setFont(QFont("Arial",10))
            helpBtn.setFixedWidth(100)
            helpBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            self.setLayout(grid)
            self.setGeometry(400, 150, 350, 300)
                  
        def q2Changed(self, text):
            logger.warning(">>> Entering q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
            self.Aanhef.setText(text)
            logger.debug("<<< Exiting q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
          
        def q3Changed(self, text):
            logger.warning(">>> Entering q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
            self.Voornaam.setText(text)
            logger.debug("<<< Exiting q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
            
        def q4Changed(self, text):
            logger.warning(">>> Entering q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
            self.Tussenvoegsel.setText(text)
            logger.debug("<<< Exiting q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
            
        def q5Changed(self, text):
            logger.warning(">>> Entering q5Changed(text=%s)", text, extra={"event.action": "q5Changed", "logrite.text": text})
            self.Achternaam.setText(text)
            logger.debug("<<< Exiting q5Changed(text=%s)", text, extra={"event.action": "q5Changed", "logrite.text": text})
    
        def q6Changed(self, text):
            logger.warning(">>> Entering q6Changed(text=%s)", text, extra={"event.action": "q6Changed", "logrite.text": text})
            self.Postcode.setText(text)
            logger.debug("<<< Exiting q6Changed(text=%s)", text, extra={"event.action": "q6Changed", "logrite.text": text})
                  
        def q7Changed(self, text):
            logger.warning(">>> Entering q7Changed(text=%s)", text, extra={"event.action": "q7Changed", "logrite.text": text})
            self.Huisnummer.setText(text)
            logger.debug("<<< Exiting q7Changed(text=%s)", text, extra={"event.action": "q7Changed", "logrite.text": text})
    
        def q8Changed(self, text):
            logger.warning(">>> Entering q8Changed(text=%s)", text, extra={"event.action": "q8Changed", "logrite.text": text})
            self.Toevoeging.setText(text)
            logger.debug("<<< Exiting q8Changed(text=%s)", text, extra={"event.action": "q8Changed", "logrite.text": text})
    
        def q9Changed(self, text):
            logger.warning(">>> Entering q9Changed(text=%s)", text, extra={"event.action": "q9Changed", "logrite.text": text})
            logger.debug("q9Changed(self=%s,text=%s): email → %s", self, text, email, extra={"event.action": "q9Changed", "logrite.text": text})
            self.email.setText(text)
            logger.debug("<<< Exiting q9Changed(text=%s)", text, extra={"event.action": "q9Changed", "logrite.text": text})
       
        def q10Changed(self, text):
            logger.warning(">>> Entering q10Changed(text=%s)", text, extra={"event.action": "q10Changed", "logrite.text": text})
            self.Wachtwoord.setText(text)
            logger.debug("<<< Exiting q10Changed(text=%s)", text, extra={"event.action": "q10Changed", "logrite.text": text})
            
        def q11Changed(self, text):
            logger.warning(">>> Entering q11Changed(text=%s)", text, extra={"event.action": "q11Changed", "logrite.text": text})
            self.ContrWachtwoord.setText(text)
            logger.debug("<<< Exiting q11Changed(text=%s)", text, extra={"event.action": "q11Changed", "logrite.text": text})
        
        def q12Changed(self, text):
            logger.warning(">>> Entering q12Changed(text=%s)", text, extra={"event.action": "q12Changed", "logrite.text": text})
            self.Telefoonnr.setText(text)
            logger.debug("<<< Exiting q12Changed(text=%s)", text, extra={"event.action": "q12Changed", "logrite.text": text})
            
        def q13Changed(self, text):
            logger.warning(">>> Entering q13Changed(text=%s)", text, extra={"event.action": "q13Changed", "logrite.text": text})
            self.Accountnummer.setText(text)
            logger.debug("<<< Exiting q13Changed(text=%s)", text, extra={"event.action": "q13Changed", "logrite.text": text})
            
        def q14Changed(self, text):
            logger.warning(">>> Entering q14Changed(text=%s)", text, extra={"event.action": "q14Changed", "logrite.text": text})
            self.Geboortedatum.setText(text)
            logger.debug("<<< Exiting q14Changed(text=%s)", text, extra={"event.action": "q14Changed", "logrite.text": text})
            
        def returnAanhef(self):
            logger.warning(">>> Entering returnAanhef()", extra={"event.action": "returnAanhef"})
            logger.debug("<<< Exiting returnAanhef()", extra={"event.action": "returnAanhef"})
            return self.Aanhef.text()
        
        def returnVoornaam(self):
            logger.warning(">>> Entering returnVoornaam()", extra={"event.action": "returnVoornaam"})
            logger.debug("<<< Exiting returnVoornaam()", extra={"event.action": "returnVoornaam"})
            return self.Voornaam.text()
        
        def returnTussenvoegsel(self):
            logger.warning(">>> Entering returnTussenvoegsel()", extra={"event.action": "returnTussenvoegsel"})
            logger.debug("<<< Exiting returnTussenvoegsel()", extra={"event.action": "returnTussenvoegsel"})
            return self.Tussenvoegsel.text()
    
        def returnAchternaam(self):
            logger.warning(">>> Entering returnAchternaam()", extra={"event.action": "returnAchternaam"})
            logger.debug("<<< Exiting returnAchternaam()", extra={"event.action": "returnAchternaam"})
            return self.Achternaam.text()
    
        def returnPostcode(self):
            logger.warning(">>> Entering returnPostcode()", extra={"event.action": "returnPostcode"})
            logger.debug("<<< Exiting returnPostcode()", extra={"event.action": "returnPostcode"})
            return self.Postcode.text()
        
        def returnHuisnummer(self):
            logger.warning(">>> Entering returnHuisnummer()", extra={"event.action": "returnHuisnummer"})
            logger.debug("<<< Exiting returnHuisnummer()", extra={"event.action": "returnHuisnummer"})
            return self.Huisnummer.text()
    
        def returnToevoeging(self):
            logger.warning(">>> Entering returnToevoeging()", extra={"event.action": "returnToevoeging"})
            logger.debug("<<< Exiting returnToevoeging()", extra={"event.action": "returnToevoeging"})
            return self.Toevoeging.text()
        
        def returnemail(self):
            logger.warning(">>> Entering returnemail()", extra={"event.action": "returnemail"})
            logger.debug("<<< Exiting returnemail()", extra={"event.action": "returnemail"})
            return self.email.text()   
        
        def returnWachtwoord(self):
            logger.warning(">>> Entering returnWachtwoord()", extra={"event.action": "returnWachtwoord"})
            logger.debug("<<< Exiting returnWachtwoord()", extra={"event.action": "returnWachtwoord"})
            return self.Wachtwoord.text()
    
        def returnContrWachtwoord(self):
            logger.warning(">>> Entering returnContrWachtwoord()", extra={"event.action": "returnContrWachtwoord"})
            logger.debug("<<< Exiting returnContrWachtwoord()", extra={"event.action": "returnContrWachtwoord"})
            return self.ContrWachtwoord.text()   
    
        def returnTelefoonnummer(self):
            logger.warning(">>> Entering returnTelefoonnummer()", extra={"event.action": "returnTelefoonnummer"})
            logger.debug("<<< Exiting returnTelefoonnummer()", extra={"event.action": "returnTelefoonnummer"})
            return self.Telefoonnr.text()   
    
        def returnAccountnummer(self):
            logger.warning(">>> Entering returnAccountnummer()", extra={"event.action": "returnAccountnummer"})
            logger.debug("<<< Exiting returnAccountnummer()", extra={"event.action": "returnAccountnummer"})
            return self.Accountnummer.text() 
      
        def returnGeboortedatum(self):
            logger.warning(">>> Entering returnGeboortedatum()", extra={"event.action": "returnGeboortedatum"})
            logger.debug("<<< Exiting returnGeboortedatum()", extra={"event.action": "returnGeboortedatum"})
            return self.Geboortedatum.text() 
         
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnAanhef(), dialog.returnVoornaam(),\
                    dialog.returnTussenvoegsel(), dialog.returnAchternaam(),\
                    dialog.returnPostcode(), dialog.returnHuisnummer(),\
                    dialog.returnToevoeging(), dialog.returnemail(),\
                    dialog.returnWachtwoord(), dialog.returnContrWachtwoord(),\
                    dialog.returnTelefoonnummer(),dialog.returnAccountnummer(),\
                    dialog.returnGeboortedatum()]
                    
    window = Widget()
    data = window.getData()

    if data[1] and data[3] and valid(data[4], 1) and valid(data[5],2)\
         and valid(data[7],3) and data[12] and password_check(data[8]) and valid(data[10],6):
        if data[0]:
            maanhef = data[0]
        else:
            maanhef = ' '
        mvoornaam = (data[1]).title()
        mtussenv = (data[2]).lower()
        if mtussenv:
            mtussenv =  mtussenv+' '
        machternaam = (data[3]).title()
        mpostcode = (data[4]).upper()
        mhuisnr = int(data[5])
        mtoev = (data[6])
        if mtoev:
            mtoev = '-'+mtoev
        m_email = (data[7])
        password = (data[8])
        old_pass = (data[9])
        if (password == old_pass) and (len(password) > 7):
            mpassword = password_hash(data[8])
        else:
            dontMatch()
            nieuwAccount(self)
        mtelnr = (data[10])
        if data[12]:
            mgebdatum = data[12]
        import postcode
        mstrpl = postcode.checkpostcode(mpostcode,mhuisnr)
        if mstrpl[0]:
            metadata = MetaData()
            accounts = Table('accounts', metadata,
                Column('accountID', Integer(), primary_key=True),
                Column('aanhef', String(8)),
                Column('voornaam', String(30), nullable=False), 
                Column('achternaam', String(50), nullable=False),
                Column('tussenvoegsel', String(10)),
                Column('telnr', String(10)),
                Column('email', String, nullable=False),
                Column('huisnummer', String(5), nullable=False),
                Column('postcode', String(6), nullable=False),       
                Column('toevoeging', String),
                Column('password', String, nullable=False),
                Column('account_count', Integer(), nullable=False),
                Column('account_created', String),
                Column('geboortedatum', String))
                
            klanten = Table('klanten', metadata,
                Column('klantID', Integer(), primary_key=True),
                Column('accountID', None, ForeignKey('accounts.c.accountID')),
                Column('klant_status', Integer()))
                         
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            metadata.create_all(engine)
            conn = engine.connect()
            maccountnr=bepaalAccountnr()
            try:
                mklantnr=(conn.execute(select([func.max(klanten.c.klantID,\
                    type_=Integer)])).scalar())
                mklantnr += 1
            except:
                mklantnr = 1
                
            maccdatum = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))[0:10]
            metadata.create_all(engine)
            insacc = accounts.insert().values(
            accountID=maccountnr,  
            aanhef=maanhef,
            voornaam=mvoornaam,
            tussenvoegsel=mtussenv,
            achternaam=machternaam,
            postcode=mpostcode.upper(),
            huisnummer=mhuisnr,
            toevoeging=mtoev,
            email=m_email,
            password=mpassword,
            account_count=1,
            telnr=mtelnr,
            account_created = maccdatum,
            geboortedatum = mgebdatum)
              
            insklant = klanten.insert().values(
            klantID = mklantnr,
            accountID = maccountnr,
            klant_status = 9)
                     
            conn = engine.connect()
            s = select([accounts]).where(accounts.c.email == m_email)
            result = conn.execute(s).first()
            if result:
                accountBestaat()
                login.inlog()
            else:
                result = conn.execute(insacc)
                insacc.bind = engine
                result.inserted_primary_key
                result = conn.execute(insklant)
                insklant.bind = engine
                result.inserted_primary_key
                conn.close()
                Invoer()
                login.inlog()
        else:
            foutPostcode()
            self.close
            nieuwAccount(self) 
    else:
        geenGegevens()
        self.close()
        nieuwAccount(self)