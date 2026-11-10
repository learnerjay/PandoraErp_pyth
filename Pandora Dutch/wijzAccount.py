from login import hoofdMenu
from validZt import zt
from argon2 import PasswordHasher
from postcode import checkpostcode
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
     QDialog, QMessageBox, QComboBox
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QRegExp
import logging
logger = logging.getLogger(__name__)

def hash_password(password):
    logger.warning(">>> Entering hash_password(password=<redacted>)", extra={"event.action": "hash_password"})
    ph = PasswordHasher()
    logger.debug("hash_password(password=<redacted>): ph → %s", ph, extra={"event.action": "hash_password"})
    logger.debug("<<< Exiting hash_password(password=<redacted>)", extra={"event.action": "hash_password"})
    return(ph.hash(password))

def check_password(hashed_password, user_password):
    logger.warning(">>> Entering check_password(hashed_password=<redacted>,user_password=<redacted>)", extra={"event.action": "check_password"})
    ph = PasswordHasher()
    logger.debug("check_password(hashed_password=<redacted>,user_password=<redacted>): ph → %s", ph, extra={"event.action": "check_password"})
    try:
        if ph.verify(hashed_password, user_password) and (len(user_password) > 7):  # True
            return(True)
    except Exception:
        logger.error("Exception in check_password(hashed_password=<redacted>,user_password=<redacted>)", exc_info=True, extra={"event.action": "check_password", "event.category": "process"})
        logger.debug("<<< Exiting check_password(hashed_password=<redacted>,user_password=<redacted>)", extra={"event.action": "check_password"})
        return(False)
    
def geenGegevens():
    logger.warning(">>> Entering geenGegevens()", extra={"event.action": "geenGegevens"})
    msg = QMessageBox()
    logger.debug("geenGegevens(): msg → %s", msg, extra={"event.action": "geenGegevens"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Niet (alle) vereiste gegevens ingevuld!')
    msg.setWindowTitle('Gegevens!')
    logger.debug("<<< Exiting geenGegevens()", extra={"event.action": "geenGegevens"})
    msg.exec_()
     
def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
      
def foutEmail():
    logger.warning(">>> Entering foutEmail()", extra={"event.action": "foutEmail"})
    msg = QMessageBox()
    logger.debug("foutEmail(): msg → %s", msg, extra={"event.action": "foutEmail"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Ongeldig email adres\nof wachtwoord ingevoerd!')
    msg.setWindowTitle('e-mailadres!')
    logger.debug("<<< Exiting foutEmail()", extra={"event.action": "foutEmail"})
    msg.exec_()
    
def foutWachtw():
    logger.warning(">>> Entering foutWachtw()", extra={"event.action": "foutWachtw"})
    msg = QMessageBox()
    logger.debug("foutWachtw(): msg → %s", msg, extra={"event.action": "foutWachtw"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText(('Wachtwoord gegevens\nniet juist ingevuld\nof minder dan 8 teksns'))
    msg.setWindowTitle('AANMELDING')               
    logger.debug("<<< Exiting foutWachtw()", extra={"event.action": "foutWachtw"})
    msg.exec_()

def foutPostcode():
    logger.warning(">>> Entering foutPostcode()", extra={"event.action": "foutPostcode"})
    msg = QMessageBox()
    logger.debug("foutPostcode(): msg → %s", msg, extra={"event.action": "foutPostcode"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText(('Poscode / huisnummer combinatie onjuist!'))
    msg.setWindowTitle('AANMELDING')               
    logger.debug("<<< Exiting foutPostcode()", extra={"event.action": "foutPostcode"})
    msg.exec_()
        
def geenToegang():
    logger.warning(">>> Entering geenToegang()", extra={"event.action": "geenToegang"})
    msg = QMessageBox()
    logger.debug("geenToegang(): msg → %s", msg, extra={"event.action": "geenToegang"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen toegang\nNeem contact op met beheerder!')
    msg.setWindowTitle('PERMISSIE')               
    logger.debug("<<< Exiting geenToegang()", extra={"event.action": "geenToegang"})
    msg.exec_()

def updateOK():
    logger.warning(">>> Entering updateOK()", extra={"event.action": "updateOK"})
    msg = QMessageBox()
    logger.debug("updateOK(): msg → %s", msg, extra={"event.action": "updateOK"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Je gegevens zijn aangepast!')
    msg.setWindowTitle('Gegevens!')
    logger.debug("<<< Exiting updateOK()", extra={"event.action": "updateOK"})
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

def dontMatch():
    logger.warning(">>> Entering dontMatch()", extra={"event.action": "dontMatch"})
    msg = QMessageBox()
    logger.debug("dontMatch(): msg → %s", msg, extra={"event.action": "dontMatch"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Wachtwoord ongewijzigd')
    msg.setWindowTitle('Wachtwoord!')
    logger.debug("<<< Exiting dontMatch()", extra={"event.action": "dontMatch"})
    msg.exec_()
    
def logoutGeg():
    logger.warning(">>> Entering logoutGeg()", extra={"event.action": "logoutGeg"})
    msg = QMessageBox()
    logger.debug("logoutGeg(): msg → %s", msg, extra={"event.action": "logoutGeg"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Je wordt nu uitgelogd\n log in met je nieuwe emailadres!')
    msg.setWindowTitle('EMAIL')
    msg.exec_()
    logger.debug("<<< Exiting logoutGeg()", extra={"event.action": "logoutGeg"})
    return(1)
   
def updateAccount(m_email):
    logger.warning(">>> Entering updateAccount(m_email=%s)", m_email, extra={"event.action": "updateAccount"})
    from sqlalchemy import (Table, Column, Integer, String, MetaData,\
                            create_engine, update)
    from sqlalchemy.sql import select
        
    metadata = MetaData()
    logger.debug("updateAccount(m_email=%s): metadata → %s", m_email, metadata, extra={"event.action": "updateAccount"})

    accounts = Table('accounts', metadata,
        Column('accountID', Integer(), primary_key=True),
        Column('aanhef', String(8)),
        Column('voornaam', String(30), nullable=False), 
        Column('tussenvoegsel', String(10)),
        Column('achternaam', String(50), nullable=False),
        Column('postcode', String(6), nullable=False),       
        Column('huisnummer', String(5), nullable=False),
        Column('toevoeging', String),
        Column('email', String, nullable=False),
        Column('password', String, nullable=False),
        Column('telnr', String(10)), 
        Column('account_count', Integer(), nullable=False),
        Column('geboortedatum', String))
     
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("updateAccount(m_email=%s): engine → %s", m_email, engine, extra={"event.action": "updateAccount"})
    conn = engine.connect()
    logger.debug("updateAccount(m_email=%s): conn → %s", m_email, conn, extra={"event.action": "updateAccount"})
    sel = select([accounts]).\
            where(accounts.c.email == m_email)
    logger.debug("updateAccount(m_email=%s): sel → %s", m_email, sel, extra={"event.action": "updateAccount"})
    rpaccount = conn.execute(sel).first()
    logger.debug("updateAccount(m_email=%s): rpaccount → %s", m_email, rpaccount, extra={"event.action": "updateAccount"})
    if rpaccount:
        maccountnr = rpaccount[0]
        logger.debug("updateAccount(m_email=%s): maccountnr → %s", m_email, maccountnr, extra={"event.action": "updateAccount"})
        maanhef = rpaccount[1]
        logger.debug("updateAccount(m_email=%s): maanhef → %s", m_email, maanhef, extra={"event.action": "updateAccount"})
        mvoornaam = rpaccount[2]
        logger.debug("updateAccount(m_email=%s): mvoornaam → %s", m_email, mvoornaam, extra={"event.action": "updateAccount"})
        mtussenv = rpaccount[3]
        logger.debug("updateAccount(m_email=%s): mtussenv → %s", m_email, mtussenv, extra={"event.action": "updateAccount"})
        machternaam = rpaccount[4]
        logger.debug("updateAccount(m_email=%s): machternaam → %s", m_email, machternaam, extra={"event.action": "updateAccount"})
        mpostcode = rpaccount[5]
        logger.debug("updateAccount(m_email=%s): mpostcode → %s", m_email, mpostcode, extra={"event.action": "updateAccount"})
        mhuisnr = rpaccount[6]
        mhuisnr = int(mhuisnr)
        logger.debug("updateAccount(m_email=%s): mhuisnr → %s", m_email, mhuisnr, extra={"event.action": "updateAccount"})
        mtoev = rpaccount[7]
        logger.debug("updateAccount(m_email=%s): mtoev → %s", m_email, mtoev, extra={"event.action": "updateAccount"})
        m_email = rpaccount[8]
        mtelnr = rpaccount[10]
        logger.debug("updateAccount(m_email=%s): mtelnr → %s", m_email, mtelnr, extra={"event.action": "updateAccount"})
        mcount = rpaccount[11]
        mcount = int(mcount)+1
        logger.debug("updateAccount(m_email=%s): mcount → %s", m_email, mcount, extra={"event.action": "updateAccount"})
        mgebdat = rpaccount[12]
        logger.debug("updateAccount(m_email=%s): mgebdat → %s", m_email, mgebdat, extra={"event.action": "updateAccount"})
        mstrtplts = checkpostcode(mpostcode,mhuisnr)
        logger.debug("updateAccount(m_email=%s): mstrtplts → %s", m_email, mstrtplts, extra={"event.action": "updateAccount"})
        mstraat = mstrtplts[0]
        mplaats = mstrtplts[1]
        logger.debug("updateAccount(m_email=%s): mstraat → %s", m_email, mstraat, extra={"event.action": "updateAccount"})
        logger.debug("updateAccount(m_email=%s): mplaats → %s", m_email, mplaats, extra={"event.action": "updateAccount"})
             
    class Widget(QDialog):
         logger.debug("<<< Exiting updateAccount(m_email=%s)", m_email, extra={"event.action": "updateAccount"})
         def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Bedrijfs Informatie Systeem")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                                  
            self.setFont(QFont('Arial', 10))
                
            self.Aanhef = QLabel()
            logger.debug("__init__(parent=%s): self.Aanhef → %s", parent, self.Aanhef, extra={"event.action": "__init__"})
            q2Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit, extra={"event.action": "__init__"})
            q2Edit.setFixedWidth(80)
            q2Edit.setFont(QFont("Arial",10))
            q2Edit.setStyleSheet("color: black;  background-color: gainsboro")
            q2Edit.addItem(' ')
            q2Edit.addItem('Dhr. ')
            q2Edit.addItem('Mevr. ')
            q2Edit.setCurrentIndex(q2Edit.findText(rpaccount[1]))
            q2Edit.activated[str].connect(self.q2Changed)
           
            self.Voornaam = QLabel()
            logger.debug("__init__(parent=%s): self.Voornaam → %s", parent, self.Voornaam, extra={"event.action": "__init__"})
            q3Edit = QLineEdit(mvoornaam)
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit, extra={"event.action": "__init__"})
            q3Edit.setFixedWidth(200)
            q3Edit.setFont(QFont("Arial",10))
            q3Edit.textChanged.connect(self.q3Changed)
            reg_ex = QRegExp("^[^0-9]{1,30}$")
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Tussenvoegsel → %s", parent, self.Tussenvoegsel, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit, extra={"event.action": "__init__"})
            input_validator = QRegExpValidator(reg_ex, q3Edit)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            q3Edit.setValidator(input_validator)
            
            self.Tussenvoegsel = QLabel()
            q4Edit = QLineEdit('')
            q4Edit.setFixedWidth(80)
            q4Edit.setFont(QFont("Arial",10))
            q4Edit.textChanged.connect(self.q4Changed)
            q4Edit.setText(mtussenv)
            reg_ex = QRegExp("^[^0-9]{1,10}$")
            input_validator = QRegExpValidator(reg_ex, q3Edit)
            q4Edit.setValidator(input_validator)
            
            self.Achternaam = QLabel()
            logger.debug("__init__(parent=%s): self.Achternaam → %s", parent, self.Achternaam, extra={"event.action": "__init__"})
            q5Edit = QLineEdit(machternaam)
            logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit, extra={"event.action": "__init__"})
            q5Edit.setFixedWidth(400)
            q5Edit.setFont(QFont("Arial",10))
            q5Edit.textChanged.connect(self.q5Changed)
            reg_ex = QRegExp("^[^0-9]{1,50}$")
            input_validator = QRegExpValidator(reg_ex, q5Edit)
            q5Edit.setValidator(input_validator)
      
            self.Straat = QLabel()
            logger.debug("__init__(parent=%s): self.Straat → %s", parent, self.Straat, extra={"event.action": "__init__"})
            q6Edit = QLineEdit(mstraat)
            logger.debug("__init__(self=%s,parent=%s): q6Edit → %s", self, parent, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q6Edit → %s", parent, q6Edit, extra={"event.action": "__init__"})
            q6Edit.setFixedWidth(500)
            q6Edit.setDisabled(True)
            q6Edit.setStyleSheet("QLineEdit { background-color: ; color: black }")
            q6Edit.setFont(QFont("Arial",10))
            q6Edit.textChanged.connect(self.q6Changed)
                       
            self.Huisnummer = QLabel()
            logger.debug("__init__(parent=%s): self.Huisnummer → %s", parent, self.Huisnummer, extra={"event.action": "__init__"})
            q7Edit = QLineEdit(str(mhuisnr))
            logger.debug("__init__(self=%s,parent=%s): q7Edit → %s", self, parent, q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q7Edit → %s", parent, q7Edit, extra={"event.action": "__init__"})
            q7Edit.setFixedWidth(60)
            q7Edit.setFont(QFont("Arial",10))
            q7Edit.textChanged.connect(self.q7Changed)
            reg_ex = QRegExp("^[0-9]{1,5}$")
            input_validator = QRegExpValidator(reg_ex, q7Edit)
            q7Edit.setValidator(input_validator)
    
            self.Toevoeging = QLabel()
            logger.debug("__init__(parent=%s): self.Toevoeging → %s", parent, self.Toevoeging, extra={"event.action": "__init__"})
            q8Edit = QLineEdit('')
            logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit, extra={"event.action": "__init__"})
            q8Edit.setFixedWidth(80)
            q8Edit.setFont(QFont("Arial",10))
            q8Edit.textChanged.connect(self.q8Changed)
            q8Edit.setText(mtoev)
            reg_ex = QRegExp("^[A-Za-z0-9-#]{0,10}")
            input_validator = QRegExpValidator(reg_ex, q8Edit)
            q8Edit.setValidator(input_validator)
       
            self.Postcode = QLabel()
            logger.debug("__init__(parent=%s): self.Postcode → %s", parent, self.Postcode, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): font → %s", parent, font, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): font → %s", self, parent, font, extra={"event.action": "__init__"})
            q9Edit = QLineEdit(mpostcode)
            logger.debug("__init__(self=%s,parent=%s): q9Edit → %s", self, parent, q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q9Edit → %s", parent, q9Edit, extra={"event.action": "__init__"})
            q9Edit.setFixedWidth(70)
            font = QFont("Arial",10)
            font.setCapitalization(QFont.AllUppercase)
            q9Edit.setFont(font)
            q9Edit.textChanged.connect(self.q9Changed)
            reg_ex = QRegExp("^[0-9]{4}[A-Za-z]{2}$")
            input_validator = QRegExpValidator(reg_ex, q9Edit)
            q9Edit.setValidator(input_validator)
            
            self.Woonplaats = QLabel()
            logger.debug("__init__(parent=%s): self.Woonplaats → %s", parent, self.Woonplaats, extra={"event.action": "__init__"})
            q10Edit = QLineEdit(mplaats)
            logger.debug("__init__(self=%s,parent=%s): q10Edit → %s", self, parent, q10Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q10Edit → %s", parent, q10Edit, extra={"event.action": "__init__"})
            q10Edit.setFixedWidth(500)
            q10Edit.setDisabled(True)
            q10Edit.setFont(QFont("Arial",10))
            q10Edit.setStyleSheet("QLineEdit { background-color: ; color: black }")
            q10Edit.textChanged.connect(self.q10Changed)
               
            self.email = QLabel()
            logger.debug("__init__(parent=%s): self.email → %s", parent, self.email, extra={"event.action": "__init__"})
            q11Edit = QLineEdit(m_email)
            logger.debug("__init__(self=%s,parent=%s): q11Edit → %s", self, parent, q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q11Edit → %s", parent, q11Edit, extra={"event.action": "__init__"})
            q11Edit.setFixedWidth(300)
            q11Edit.setFont(QFont("Arial",10))
            q11Edit.textChanged.connect(self.q11Changed)
            reg_ex = QRegExp("^([A-Za-z0-9._-]{1,}@(\\w+)(\\.(\\w+))(\\.(\\w+))?(\\.(\\w+))?)$")
            input_validator = QRegExpValidator(reg_ex, q11Edit)
            q11Edit.setValidator(input_validator)
            
            self.BestaandWachtwoord = QLabel()
            logger.debug("__init__(parent=%s): self.BestaandWachtwoord → %s", parent, self.BestaandWachtwoord, extra={"event.action": "__init__"})
            q12Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q12Edit → %s", self, parent, q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q12Edit → %s", parent, q12Edit, extra={"event.action": "__init__"})
            q12Edit.setFixedWidth(300)
            q12Edit.setFont(QFont("Arial",10))
            q12Edit.setEchoMode(QLineEdit.Password)
            q12Edit.textChanged.connect(self.q12Changed)
            
            self.NieuwWachtwoord = QLabel()
            logger.debug("__init__(parent=%s): self.NieuwWachtwoord → %s", parent, self.NieuwWachtwoord, extra={"event.action": "__init__"})
            q13Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q13Edit → %s", self, parent, q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q13Edit → %s", parent, q13Edit, extra={"event.action": "__init__"})
            q13Edit.setFixedWidth(300)
            q13Edit.setFont(QFont("Arial",10))
            q13Edit.setEchoMode(QLineEdit.Password)
            q13Edit.textChanged.connect(self.q13Changed)
  
            self.NieuwWachtwoordControle = QLabel()
            logger.debug("__init__(parent=%s): self.NieuwWachtwoordControle → %s", parent, self.NieuwWachtwoordControle, extra={"event.action": "__init__"})
            q14Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q14Edit → %s", self, parent, q14Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q14Edit → %s", parent, q14Edit, extra={"event.action": "__init__"})
            q14Edit.setFixedWidth(300)
            q14Edit.setFont(QFont("Arial",10))
            q14Edit.setEchoMode(QLineEdit.Password)
            q14Edit.textChanged.connect(self.q14Changed)
    
            self.Telefoonnr = QLabel()
            logger.debug("__init__(parent=%s): self.Telefoonnr → %s", parent, self.Telefoonnr, extra={"event.action": "__init__"})
            q15Edit = QLineEdit('')
            logger.debug("__init__(self=%s,parent=%s): q15Edit → %s", self, parent, q15Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q15Edit → %s", parent, q15Edit, extra={"event.action": "__init__"})
            q15Edit.setFixedWidth(100)
            q15Edit.setFont(QFont("Arial",10))
            q15Edit.textChanged.connect(self.q15Changed)
            q15Edit.setText(mtelnr)
            reg_ex = QRegExp("^[#0]{1}[0-9]{9}$")
            input_validator = QRegExpValidator(reg_ex, q15Edit)
            q15Edit.setValidator(input_validator)
            
            self.Accountnummer = QLabel()
            logger.debug("__init__(parent=%s): self.Accountnummer → %s", parent, self.Accountnummer, extra={"event.action": "__init__"})
            q16Edit = QLineEdit(str(maccountnr))
            logger.debug("__init__(self=%s,parent=%s): q16Edit → %s", self, parent, q16Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q16Edit → %s", parent, q16Edit, extra={"event.action": "__init__"})
            q16Edit.setFixedWidth(100)
            q16Edit.setDisabled(True)
            q16Edit.setStyleSheet("QLineEdit { background-color: ; color: black }")
            q16Edit.setFont(QFont("Arial",10))
            q16Edit.textChanged.connect(self.q16Changed)
            
            self.Geboortedatum = QLabel()
            logger.debug("__init__(parent=%s): self.Geboortedatum → %s", parent, self.Geboortedatum, extra={"event.action": "__init__"})
            q17Edit = QLineEdit(mgebdat)
            logger.debug("__init__(self=%s,parent=%s): q17Edit → %s", self, parent, q17Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q17Edit → %s", parent, q17Edit, extra={"event.action": "__init__"})
            q17Edit.setFixedWidth(100)
            q17Edit.setFont(QFont("Arial",10))
            q17Edit.textChanged.connect(self.q17Changed)
            reg_ex = QRegExp('^[1-2]{1}[09]{1}[0-9]{2}-[0-1]{1}[0-9]{1}-[0-3]{1}[0-9]{1}$')
            input_validator = QRegExpValidator(reg_ex, q17Edit)
            q17Edit.setValidator(input_validator)  
        
            grid = QGridLayout()
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            grid.setSpacing(20)
            
            lbl = QLabel()
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 1, 0)
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 2, 1, 1, Qt.AlignRight)
    
            self.setFont(QFont('Arial', 10))
            grid.addWidget(QLabel('Opvragen of aanpassen persoongegevens'), 1, 1)
                        
            grid.addWidget(QLabel('                                           *'), 2, 0) 
            grid.addWidget(QLabel('Verplichte velden'), 2, 1)   
                         
            grid.addWidget(QLabel('Aanhef'), 3, 0)
            grid.addWidget(q2Edit, 3, 1)
            
            grid.addWidget(QLabel('Voornaam                            *'), 4, 0)
            grid.addWidget(q3Edit, 4, 1)  
     
            grid.addWidget(QLabel('Tussenvoegsel'), 5, 0)
            grid.addWidget(q4Edit, 5 , 1) 
             
            grid.addWidget(QLabel('Achternaam                         *'), 6, 0)
            grid.addWidget(q5Edit, 6, 1, 1, 2)
            
            grid.addWidget(QLabel('Geboortedatum                     *'), 7, 0)
            grid.addWidget(QLabel('                       formaat: jjjj-mm-dd'), 7, 1, 1, 2 )
            grid.addWidget(q17Edit, 7, 1)
                 
            grid.addWidget(QLabel('Straat'), 8, 0)
            grid.addWidget(q6Edit, 8, 1, 1, 2) 
       
            grid.addWidget(QLabel('Huisnummer                        *'), 9, 0)
            grid.addWidget(q7Edit, 9, 1)
            
            grid.addWidget(QLabel('Toevoeging'), 9, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(q8Edit, 9, 2)
             
            grid.addWidget(QLabel('Postcode                            *'), 10, 0)
            grid.addWidget(q9Edit, 10, 1)
            
            grid.addWidget(QLabel('Woonplaats'), 11, 0)
            grid.addWidget(q10Edit, 11, 1, 1, 2)    
     
            grid.addWidget(QLabel('e-mail                                 *'), 12, 0)
            grid.addWidget(q11Edit, 12, 1, 1 ,2)
                   
            grid.addWidget(QLabel('Bestaand wachtwoord          *'), 13, 0)
            grid.addWidget(q12Edit, 13, 1, 1 ,2) 
            
            grid.addWidget(QLabel('Nieuw wachtwoord               *'), 14, 0)
            grid.addWidget(q13Edit, 14, 1, 1 ,2) 
    
            grid.addWidget(QLabel('Nieuw wachtwoord controle  *'), 15, 0)
            grid.addWidget(q14Edit, 15, 1, 1 ,2) 
    
            grid.addWidget(QLabel('Telefoonnummer'), 16, 0)
            grid.addWidget(q15Edit, 16, 1) 
            
            grid.addWidget(QLabel('Accountnummer'),17, 0)
            grid.addWidget(q16Edit, 17, 1, 1, 2) 
                        
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 18, 0, 1, 3, Qt.AlignCenter)
                                 
            self.setLayout(grid)
            self.setGeometry(500, 50, 350, 300)
            
            applyBtn = QPushButton('Wijzigen')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
                       
            grid.addWidget(applyBtn, 17, 2, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
                            
            cancelBtn = QPushButton('Sluiten')
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
       
            grid.addWidget(cancelBtn, 16, 2, 1, 1, Qt.AlignRight)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                                     
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
            self.Straat.setText(text)    
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
            self.Postcode.setText(text)
            logger.debug("<<< Exiting q9Changed(text=%s)", text, extra={"event.action": "q9Changed", "logrite.text": text})
       
         def q10Changed(self, text):
            logger.warning(">>> Entering q10Changed(text=%s)", text, extra={"event.action": "q10Changed", "logrite.text": text})
            self.Woonplaats.setText(text)             
            logger.debug("<<< Exiting q10Changed(text=%s)", text, extra={"event.action": "q10Changed", "logrite.text": text})
    
         def q11Changed(self, text):
            logger.warning(">>> Entering q11Changed(text=%s)", text, extra={"event.action": "q11Changed", "logrite.text": text})
            logger.debug("q11Changed(self=%s,text=%s): email → %s", self, text, email, extra={"event.action": "q11Changed", "logrite.text": text})
            self.email.setText(text)
            logger.debug("<<< Exiting q11Changed(text=%s)", text, extra={"event.action": "q11Changed", "logrite.text": text})
                   
         def q12Changed(self, text):
            logger.warning(">>> Entering q12Changed(text=%s)", text, extra={"event.action": "q12Changed", "logrite.text": text})
            self.BestaandWachtwoord.setText(text)
            logger.debug("<<< Exiting q12Changed(text=%s)", text, extra={"event.action": "q12Changed", "logrite.text": text})
            
         def q13Changed(self, text):
            logger.warning(">>> Entering q13Changed(text=%s)", text, extra={"event.action": "q13Changed", "logrite.text": text})
            self.NieuwWachtwoord.setText(text)
            logger.debug("<<< Exiting q13Changed(text=%s)", text, extra={"event.action": "q13Changed", "logrite.text": text})
            
         def q14Changed(self, text):
            logger.warning(">>> Entering q14Changed(text=%s)", text, extra={"event.action": "q14Changed", "logrite.text": text})
            self.NieuwWachtwoordControle.setText(text)
            logger.debug("<<< Exiting q14Changed(text=%s)", text, extra={"event.action": "q14Changed", "logrite.text": text})
        
         def q15Changed(self, text):
            logger.warning(">>> Entering q15Changed(text=%s)", text, extra={"event.action": "q15Changed", "logrite.text": text})
            self.Telefoonnr.setText(text)
            logger.debug("<<< Exiting q15Changed(text=%s)", text, extra={"event.action": "q15Changed", "logrite.text": text})
            
         def q16Changed(self, text):
            logger.warning(">>> Entering q16Changed(text=%s)", text, extra={"event.action": "q16Changed", "logrite.text": text})
            self.Accountnummer.setText(text)
            logger.debug("<<< Exiting q16Changed(text=%s)", text, extra={"event.action": "q16Changed", "logrite.text": text})
            
         def q17Changed(self, text):
            logger.warning(">>> Entering q17Changed(text=%s)", text, extra={"event.action": "q17Changed", "logrite.text": text})
            self.Geboortedatum.setText(text)
            logger.debug("<<< Exiting q17Changed(text=%s)", text, extra={"event.action": "q17Changed", "logrite.text": text})
      
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
        
         def returnemail(self):
            logger.warning(">>> Entering returnemail()", extra={"event.action": "returnemail"})
            logger.debug("<<< Exiting returnemail()", extra={"event.action": "returnemail"})
            return self.email.text()   
                
         def returnBestaandWachtwoord(self):
            logger.warning(">>> Entering returnBestaandWachtwoord()", extra={"event.action": "returnBestaandWachtwoord"})
            logger.debug("<<< Exiting returnBestaandWachtwoord()", extra={"event.action": "returnBestaandWachtwoord"})
            return self.BestaandWachtwoord.text()
    
         def returnNieuwWachtwoord(self):
            logger.warning(">>> Entering returnNieuwWachtwoord()", extra={"event.action": "returnNieuwWachtwoord"})
            logger.debug("<<< Exiting returnNieuwWachtwoord()", extra={"event.action": "returnNieuwWachtwoord"})
            return self.NieuwWachtwoord.text()   
 
         def returnNieuwWachtwoordControle(self):
            logger.warning(">>> Entering returnNieuwWachtwoordControle()", extra={"event.action": "returnNieuwWachtwoordControle"})
            logger.debug("<<< Exiting returnNieuwWachtwoordControle()", extra={"event.action": "returnNieuwWachtwoordControle"})
            return self.NieuwWachtwoordControle.text()   
    
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
                    dialog.returnStraat(), dialog.returnHuisnummer(),\
                    dialog.returnToevoeging(), dialog.returnPostcode(),\
                    dialog.returnWoonplaats(), dialog.returnemail(),\
                    dialog.returnBestaandWachtwoord(), dialog.returnNieuwWachtwoord(),\
                    dialog.returnNieuwWachtwoordControle(), dialog.returnTelefoonnummer(),\
                    dialog.returnAccountnummer(),dialog.returnGeboortedatum()]
     
    window = Widget()
    data = window.getData()
    if data[0]:
        maanhef = data[0]
    else:
        maanhef = rpaccount[1]
    if data[1]:
        mvoornaam = (data[1]).title()
    else:
        mvoornaam = rpaccount[2].title()
    if data[2]:
        mtussenv = data[2]
    else:
        mtussenv = ''
    if data[3]:
        machternaam = (data[3]).title()
    else:
        machternaam = rpaccount[4].title()
    if data[5]:
        mhuisnr = data[5]
    else:
        mhuisnr = rpaccount[6]
    if data[7]:
        mpostcode = data[7].upper()
    else:
        mpostcode = rpaccount[5]
    if  checkpostcode(mpostcode, int(mhuisnr))[0] == '':
        foutPostcode()
        hoofdMenu(m_email)
    if data[6]:
        mtoev = '-'+data[6]
    else:
        mtoev = ''
    if data[9]:
        if zt(data[9], 12):
            m_email = (data[9])
        else:
            foutEmail()
            hoofdMenu(m_email)
    else:
        m_email = rpaccount[8]
    mpassword = rpaccount[9]
    old_password = ''
    nw_password = ''
    contr_nwpass = ''
    if data[10] and data[11] and data[12]:
        old_password = data[10]
        nw_password = data[11]
        contr_nwpass = data[12]
        if check_password(mpassword, old_password) and len(nw_password) > 7 \
                                          and (nw_password == contr_nwpass):
            nw_passwd = hash_password(nw_password)
        else:
            foutWachtw()
            hoofdMenu(m_email)    
    else:
        nw_passwd = mpassword
        dontMatch()
    if data[13]:
        mtelnr = data[13]
    else:
        mtelnr = ''
    if not (len(mtelnr) == 10 or mtelnr == ''):
        foutTelnr()
        hoofdMenu(m_email)        
    if data[15]:
        mgebdat = data[15]
    else:
        mgebdat = rpaccount[12]
                   
    u = update(accounts).where(accounts.c.accountID == maccountnr).\
    values(aanhef = maanhef, voornaam = mvoornaam, tussenvoegsel =\
    mtussenv, achternaam = machternaam, huisnummer = int(mhuisnr),\
    toevoeging = mtoev, postcode = mpostcode, email = m_email, password =\
    nw_passwd, telnr = mtelnr, account_count = mcount, geboortedatum = mgebdat)  
    conn.execute(u)
    conn.close()
    updateOK()
    hoofdMenu(m_email)