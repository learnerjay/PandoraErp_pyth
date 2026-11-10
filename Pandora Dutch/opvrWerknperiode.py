from login import hoofdMenu
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
               QDialog, QMessageBox
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QRegExp
from sqlalchemy import (Table, Column, Integer, String, Float, Boolean,\
                        ForeignKey,  MetaData, create_engine)
from sqlalchemy.sql import select, and_
import logging
logger = logging.getLogger(__name__)

def geenBetaalgeg():
    logger.warning(">>> Entering geenBetaalgeg()", extra={"event.action": "geenBetaalgeg"})
    msg = QMessageBox()
    logger.debug("geenBetaalgeg(): msg → %s", msg, extra={"event.action": "geenBetaalgeg"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen betaalgegevens voor\ndeze periode gevonden!')
    msg.setWindowTitle('Werknemers periodegegevens opvragen')
    logger.debug("<<< Exiting geenBetaalgeg()", extra={"event.action": "geenBetaalgeg"})
    msg.exec_()
    
def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    
def ongInvoer():
    logger.warning(">>> Entering ongInvoer()", extra={"event.action": "ongInvoer"})
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg, extra={"event.action": "ongInvoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Foutieve invoer\nzoekterm opnieuw invoeren s.v.p.!')
    msg.setWindowTitle('Werknemers periodegegevens opvragen')               
    logger.debug("<<< Exiting ongInvoer()", extra={"event.action": "ongInvoer"})
    msg.exec_() 

def geenRecord():
    logger.warning(">>> Entering geenRecord()", extra={"event.action": "geenRecord"})
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg, extra={"event.action": "geenRecord"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen urenmutaties van deze persoon gevonden\nin deze periode maak een andere selektie s.v.p.!')
    msg.setWindowTitle('Werknemers periodegegevens opvragen')               
    logger.debug("<<< Exiting geenRecord()", extra={"event.action": "geenRecord"})
    msg.exec_() 
    
def foutWerknemer():
    logger.warning(">>> Entering foutWerknemer()", extra={"event.action": "foutWerknemer"})
    msg = QMessageBox()
    logger.debug("foutWerknemer(): msg → %s", msg, extra={"event.action": "foutWerknemer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Werknemer niet gevonden\nen/of geen geldige periode opgegeven!')
    msg.setWindowTitle('Werknemers periodegegevens opvragen')
    logger.debug("<<< Exiting foutWerknemer()", extra={"event.action": "foutWerknemer"})
    msg.exec_()
               
def _11check(minput):
    logger.warning(">>> Entering _11check(minput=%s)", minput, extra={"event.action": "_11check", "logrite.minput": minput})
    number = str(minput)
    logger.debug("_11check(minput=%s): number → %s", minput, number, extra={"event.action": "_11check", "logrite.minput": minput})
    total = 0       
    fullnumber = number                       
    logger.debug("_11check(minput=%s): total → %s", minput, total, extra={"event.action": "_11check", "logrite.minput": minput})
    for i in range(8):
        total += int(fullnumber[i])*(9-i)
        logger.debug("_11check(minput=%s): fullnumber → %s", minput, fullnumber, extra={"event.action": "_11check", "logrite.minput": minput})
        checkdigit = total % 11
    if checkdigit == 10:
        checkdigit = 0
    if checkdigit == int(fullnumber[8]):
        return True
    else:
        logger.debug("<<< Exiting _11check(minput=%s)", minput, extra={"event.action": "_11check", "logrite.minput": minput})
        return False 
    
def zoekWerknemer(m_email):     
    logger.warning(">>> Entering zoekWerknemer(m_email=%s)", m_email, extra={"event.action": "zoekWerknemer"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle('Periodegegevens opvragen')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    
            self.setFont(QFont('Arial', 10))
    
            self.Werknemer = QLabel()
            werknemerEdit = QLineEdit()
            werknemerEdit.setFixedWidth(100)
            werknemerEdit.setFont(QFont("Arial",10))
            werknemerEdit.textChanged.connect(self.werknemerChanged)
            reg_ex = QRegExp('^[1]{1}[0-9]{8}$')
            input_validator = QRegExpValidator(reg_ex, werknemerEdit)
            werknemerEdit.setValidator(input_validator)
            
            self.Betaalperiode = QLabel()
            betEdit = QLineEdit()
            betEdit.setFixedWidth(100)
            betEdit.setFont(QFont("Arial",10))
            betEdit.textChanged.connect(self.betChanged)
            reg_ex = QRegExp('^[2]{1}[01]{1}[0-9]{2}[-][0-1]{1}[0-9]{1}$')
            input_validator = QRegExpValidator(reg_ex, betEdit)
            betEdit.setValidator(input_validator)
                            
            grid = QGridLayout()
            grid.setSpacing(20)
    
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
    
            self.setFont(QFont('Arial', 10))
     
            grid.addWidget(QLabel('Account-werknemer'), 1, 0)
            grid.addWidget(werknemerEdit, 1, 1)
            
            grid.addWidget(QLabel('Betaalperiode jjjj-mm'), 2, 0)
            grid.addWidget(betEdit, 2, 1)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1, 2)
              
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
         
            applyBtn = QPushButton('Zoeken')
            applyBtn.clicked.connect(self.accept)
                  
            grid.addWidget(applyBtn, 3, 1)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
         
            grid.addWidget(cancelBtn, 3, 0, 1, 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            self.setLayout(grid)
            self.setGeometry(400, 300, 150, 150)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Accountnummer → %s", parent, self.Accountnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Loontabelnummer → %s", parent, self.Loontabelnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Loontrede → %s", parent, self.Loontrede, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Loonheffing → %s", parent, self.Loonheffing, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q6Edit → %s", parent, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q6Edit → %s", self, parent, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Reiskostenvergoeding → %s", parent, self.Reiskostenvergoeding, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Pensioen → %s", parent, self.Pensioen, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q9Edit → %s", parent, q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q9Edit → %s", self, parent, q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Reserveringvakantie → %s", parent, self.Reserveringvakantie, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q10Edit → %s", parent, q10Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q10Edit → %s", self, parent, q10Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Werkgeverpensioenpremie → %s", parent, self.Werkgeverpensioenpremie, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q11Edit → %s", parent, q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q11Edit → %s", self, parent, q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Auto → %s", parent, self.Auto, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q18Edit → %s", parent, q18Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q18Edit → %s", self, parent, q18Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Periodiekeuitkering → %s", parent, self.Periodiekeuitkering, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q12Edit → %s", parent, q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q12Edit → %s", self, parent, q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Overigeinhoudingen → %s", parent, self.Overigeinhoudingen, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q13Edit → %s", parent, q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q13Edit → %s", self, parent, q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Overigevergoedingen → %s", parent, self.Overigevergoedingen, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q19Edit → %s", parent, q19Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q19Edit → %s", self, parent, q19Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Indienst → %s", parent, self.Indienst, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q14Edit → %s", parent, q14Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q14Edit → %s", self, parent, q14Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Brutoloon → %s", parent, self.Brutoloon, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q15Edit → %s", parent, q15Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q15Edit → %s", self, parent, q15Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Verlofsaldo → %s", parent, self.Verlofsaldo, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q16Edit → %s", parent, q16Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q16Edit → %s", self, parent, q16Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.ExtraVerlof → %s", parent, self.ExtraVerlof, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q17Edit → %s", parent, q17Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q17Edit → %s", self, parent, q17Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
    
        def werknemerChanged(self, text):
            logger.warning(">>> Entering werknemerChanged(text=%s)", text, extra={"event.action": "werknemerChanged", "logrite.text": text})
            self.Werknemer.setText(text)
            logger.debug("<<< Exiting werknemerChanged(text=%s)", text, extra={"event.action": "werknemerChanged", "logrite.text": text})
            
        def betChanged(self, text):
            logger.warning(">>> Entering betChanged(text=%s)", text, extra={"event.action": "betChanged", "logrite.text": text})
            self.Betaalperiode.setText(text)
            logger.debug("<<< Exiting betChanged(text=%s)", text, extra={"event.action": "betChanged", "logrite.text": text})
    
        def returnWerknemer(self):
            logger.warning(">>> Entering returnWerknemer()", extra={"event.action": "returnWerknemer"})
            logger.debug("<<< Exiting returnWerknemer()", extra={"event.action": "returnWerknemer"})
            return self.Werknemer.text()
        
        def returnBetaalperiode(self):
            logger.warning(">>> Entering returnBetaalperiode()", extra={"event.action": "returnBetaalperiode"})
            logger.debug("<<< Exiting returnBetaalperiode()", extra={"event.action": "returnBetaalperiode"})
            return self.Betaalperiode.text()
    
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnWerknemer(), dialog.returnBetaalperiode()]
       
    window = Widget()
    data = window.getData()
    if data[0]:
        maccountnr = data[0]
    else:
        foutWerknemer()
        zoekWerknemer(m_email)
    if data[1]:
        mbetaalper = data[1]
    else:
        mbetaalper = '2000-01'
               
    metadata = MetaData()

    werknemers = Table('werknemers', metadata,
        Column('werknemerID', Integer(), primary_key=True),
        Column('accountID', None, ForeignKey('accounts.accountID')))
   
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    sel = select([werknemers]).where(werknemers.c.accountID == maccountnr)
    rpwerkn = conn.execute(sel).first()
     
    if (len(str(maccountnr)) == 9 and _11check(maccountnr) and rpwerkn)\
          and (len(mbetaalper) == 7):
        maccountnr = rpwerkn[1]
        mwerknmrnr = rpwerkn[0]
        opvrWerknperiode(mwerknmrnr,mbetaalper, m_email)
    else:
        foutWerknemer()
        zoekWerknemer(m_email)

def opvrWerknperiode(mwerknmrnr,mbetaalper, m_email):
    logger.warning(">>> Entering opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s)", mwerknmrnr, mbetaalper, m_email, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mbegin = str(mbetaalper[0:8]+'-'+'01')
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mbegin → %s", mwerknmrnr, mbetaalper, m_email, mbegin, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mtot = str(mbetaalper[0:8]+'-'+'31')
    midx = int(mbetaalper[5:7])
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mtot → %s", mwerknmrnr, mbetaalper, m_email, mtot, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mbet = ['Januari','Februari',' Maart', 'April', 'Mei', 'Juni', 'Juli',\
                'Augustus','September', 'Oktober', 'November', 'December']
    mbetmaand = str(mbet[midx-1])
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): midx → %s", mwerknmrnr, mbetaalper, m_email, midx, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mbetjr = str(mbetaalper[0:4])

    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mbet → %s", mwerknmrnr, mbetaalper, m_email, mbet, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    metadata = MetaData()   
    werknemers = Table('werknemers', metadata,
        Column('werknemerID', Integer(), primary_key=True),
        Column('accountID', None, ForeignKey('accounts.accountID')),
        Column('loonID', None, ForeignKey('lonen.loonID')), 
        Column('loontrede', Integer),
        Column('reiskosten_vergoeding', Float),
        Column('loonheffing', Float),
        Column('pensioenpremie', Float),
        Column('reservering_vakantietoeslag', Float),
        Column('werkgevers_pensioenpremie', Float),
        Column('periodieke_uitkeringen', Float),
        Column('overige_inhoudingen', Float),
        Column('overige_vergoedingen', Float),
        Column('bedrijfsauto', Float),
        Column('indienst', String),
        Column('verlofsaldo', Float),
        Column('extraverlof', Float)) 
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mbetmaand → %s", mwerknmrnr, mbetaalper, m_email, mbetmaand, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    lonen = Table('lonen', metadata,
        Column('loonID', Integer, primary_key=True),
        Column('tabelloon', Float),
        Column('reisuur', Float),
        Column('maandloon', Float)) 
    wrkwnrln = Table('wrkwnrln', metadata,
        Column('wrkwnrurenID', Integer, primary_key=True),
        Column('werknemerID', None, ForeignKey('werknemers.werknemerID')),
        Column('boekdatum', String),
        Column('aantaluren', Float),
        Column('soort', String),
        Column('meerwerkstatus', Boolean),
        Column('bruto_loonbedrag', Float))
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mbetjr → %s", mwerknmrnr, mbetaalper, m_email, mbetjr, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    accounts = Table('accounts', metadata,
        Column('accountID', Integer, primary_key=True),
        Column('voornaam', String),
        Column('achternaam', String),
        Column('geboortedatum', String))
         
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): metadata → %s", mwerknmrnr, mbetaalper, m_email, metadata, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): engine → %s", mwerknmrnr, mbetaalper, m_email, engine, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    sel = select([werknemers, lonen, wrkwnrln, accounts]).where(and_\
      (werknemers.c.werknemerID == mwerknmrnr, werknemers.c.loonID ==\
       lonen.c.loonID, accounts.c.accountID == werknemers.c.accountID))
    rpwerkn = conn.execute(sel).first()
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): conn → %s", mwerknmrnr, mbetaalper, m_email, conn, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mwerknmrnr = rpwerkn[0]
    maccountnr = rpwerkn[1]
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): sel → %s", mwerknmrnr, mbetaalper, m_email, sel, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mloonnr = rpwerkn[2]
    mtrede = rpwerkn[3]*0.03
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): rpwerkn → %s", mwerknmrnr, mbetaalper, m_email, rpwerkn, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mreisk = float(rpwerkn[4])
   
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): maccountnr → %s", mwerknmrnr, mbetaalper, m_email, maccountnr, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mloonnr → %s", mwerknmrnr, mbetaalper, m_email, mloonnr, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mtrede → %s", mwerknmrnr, mbetaalper, m_email, mtrede, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mreisk → %s", mwerknmrnr, mbetaalper, m_email, mreisk, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    #mloonh = (uurloon*40*13)/3 #tabelloon.loonheffing
    if rpwerkn[2] < 37:
        mbruto = rpwerkn[17]*520/3*(1+mtrede)
        muurl = rpwerkn[17]*(1+mtrede)
    else:
        mbruto =  rpwerkn[19]*(1+mtrede)
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mbruto → %s", mwerknmrnr, mbetaalper, m_email, mbruto, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
        muurl = mbruto*3/520
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): muurl → %s", mwerknmrnr, mbetaalper, m_email, muurl, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    #loonheffing pensioenpremie
    metadata =  MetaData()
    params = Table('params', metadata,
        Column('paramID', Integer, primary_key=True),
        Column('tarief', Float),
        Column('item', String),
        Column('lock', Boolean),
        Column('ondergrens', Float),
        Column('bovengrens', Float))
        
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    selpar = select([params]).order_by(params.c.paramID)
    rppar = con.execute(selpar).fetchall()
    
    mauto = rpwerkn[12]*12
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): con → %s", mwerknmrnr, mbetaalper, m_email, con, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
     #pensioenpremie
    if rpwerkn[2] < 37:
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): selpar → %s", mwerknmrnr, mbetaalper, m_email, selpar, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
        mbruto = rpwerkn[17]*520/3*(1+mtrede)
        muurl = rpwerkn[17]*(1+mtrede)
    else:
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): rppar → %s", mwerknmrnr, mbetaalper, m_email, rppar, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mauto → %s", mwerknmrnr, mbetaalper, m_email, mauto, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
        mbruto =  rpwerkn[2]*(1+mtrede)
        muurl = mbruto*3/520
    
    mjaarink = mbruto*12.96
    mpensink = mjaarink
    if mpensink >  rppar[44][5]:
        mpensprjr = (rppar[44][5]-rppar[44][4])*rppar[44][1]
    else:
        mpensprjr = (mpensink-rppar[44][4])*rppar[44][1]
    mpenspr = (mpensprjr)/12.96/3
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mjaarink → %s", mwerknmrnr, mbetaalper, m_email, mjaarink, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mpensink → %s", mwerknmrnr, mbetaalper, m_email, mpensink, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mpensprjr → %s", mwerknmrnr, mbetaalper, m_email, mpensprjr, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mpensprwg = mpenspr*2
    mresvak = mbruto*.08
    mbelink = mjaarink-mpensprjr+(mauto*12)

    mwerkg_WAO_IVA_WGA = rppar[69][1]*mjaarink/12.96
    mwerkg_AWF = rppar[70][1]*mjaarink/12.96 
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mpenspr → %s", mwerknmrnr, mbetaalper, m_email, mpenspr, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mwerkg_ZVW = rppar[71][1]*mjaarink/12.96
    # Bijzonder tarief bepalen
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mpensprwg → %s", mwerknmrnr, mbetaalper, m_email, mpensprwg, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mresvak → %s", mwerknmrnr, mbetaalper, m_email, mresvak, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    if mbelink > 0 and mbelink <= 6512:
        mbyz = 0.3655
    elif mbelink > 6512 and mbelink <= 10226:
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mbelink → %s", mwerknmrnr, mbetaalper, m_email, mbelink, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
        mbyz = 0.3479
    elif mbelink > 10226 and mbelink <=18937:
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mwerkg_AWF → %s", mwerknmrnr, mbetaalper, m_email, mwerkg_AWF, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mwerkg_WAO_IVA_WGA → %s", mwerknmrnr, mbetaalper, m_email, mwerkg_WAO_IVA_WGA, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mwerkg_ZVW → %s", mwerknmrnr, mbetaalper, m_email, mwerkg_ZVW, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
        mbyz = 0.0849
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mbyz → %s", mwerknmrnr, mbetaalper, m_email, mbyz, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    elif mbelink > 18937 and mbelink <= 20143:
        mbyz = 0.3655
    elif mbelink > 20143 and mbelink <= 22029:
        mbyz = 0.4553
    elif mbelink > 22029 and  mbelink <= 33113:
        mbyz = 0.4553
    elif mbelink > 33113 and mbelink <= 33995:
        mbyz = 0.4913
    elif mbelink > 33995 and mbelink <= 34405:
        mbyz = 0.4913
    elif mbelink > 34405 and mbelink <= 68508:
        mbyz = 0.4913
    elif mbelink > 68508 and mbelink <= 133232:
        mbyz = 0.5555
    elif mbelink > 133232:
        mbyz = 0.5195

    mloonh = rpwerkn[5]
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mloonh → %s", mwerknmrnr, mbetaalper, m_email, mloonh, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mbyztar = mbyz*100
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mbyztar → %s", mwerknmrnr, mbetaalper, m_email, mbyztar, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    #mwerkglasten = float(rpwerkn[8])
    mperiodiek = float(rpwerkn[9])
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mperiodiek → %s", mwerknmrnr, mbetaalper, m_email, mperiodiek, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    moverig = float(rpwerkn[10])
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): moverig → %s", mwerknmrnr, mbetaalper, m_email, moverig, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mindienst = rpwerkn[13]
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mindienst → %s", mwerknmrnr, mbetaalper, m_email, mindienst, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mverlofsaldo = rpwerkn[14]
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mverlofsaldo → %s", mwerknmrnr, mbetaalper, m_email, mverlofsaldo, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mextraverlof = rpwerkn[15]
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mextraverlof → %s", mwerknmrnr, mbetaalper, m_email, mextraverlof, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mvoorn = rpwerkn[28]
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mvoorn → %s", mwerknmrnr, mbetaalper, m_email, mvoorn, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    machtern = rpwerkn[29]
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): machtern → %s", mwerknmrnr, mbetaalper, m_email, machtern, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mgeboren = str(rpwerkn[30])[8:10]+str(rpwerkn[30])[4:7]+'-'+str(rpwerkn[30])[0:4]
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mgeboren → %s", mwerknmrnr, mbetaalper, m_email, mgeboren, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
   
    if rpwerkn[18]:
        mreisuurl = round(rpwerkn[18],2)
    else:
        mreisuurl = 0
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mreisuurl → %s", mwerknmrnr, mbetaalper, m_email, mreisuurl, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})

    selwrkwnrln = select([wrkwnrln]).where(and_(wrkwnrln.c.werknemerID == mwerknmrnr,\
     werknemers.c.werknemerID == wrkwnrln.c.werknemerID,\
     (wrkwnrln.c.boekdatum >= mbegin), (wrkwnrln.c.boekdatum <= mtot)))
    if conn.execute(selwrkwnrln).fetchone():
        rpwrkwnrln = conn.execute(selwrkwnrln)
    else:
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): rpwrkwnrln → %s", mwerknmrnr, mbetaalper, m_email, rpwrkwnrln, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
        geenRecord()
        zoekWerknemer(m_email)
    mreisuren = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mreisuren → %s", mwerknmrnr, mbetaalper, m_email, mreisuren, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    muren = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): muren → %s", mwerknmrnr, mbetaalper, m_email, muren, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    muren125 = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): muren125 → %s", mwerknmrnr, mbetaalper, m_email, muren125, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    muren150 = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): muren150 → %s", mwerknmrnr, mbetaalper, m_email, muren150, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    muren200 = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): muren200 → %s", mwerknmrnr, mbetaalper, m_email, muren200, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mverlof = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mverlof → %s", mwerknmrnr, mbetaalper, m_email, mverlof, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mziek = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mziek → %s", mwerknmrnr, mbetaalper, m_email, mziek, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mfeest = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mfeest → %s", mwerknmrnr, mbetaalper, m_email, mfeest, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mdokter = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mdokter → %s", mwerknmrnr, mbetaalper, m_email, mdokter, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mgverzuim = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mgverzuim → %s", mwerknmrnr, mbetaalper, m_email, mgverzuim, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    moverzuim = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): moverzuim → %s", mwerknmrnr, mbetaalper, m_email, moverzuim, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    muurlbedr = 0
    muurl125bedr = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): muurlbedr → %s", mwerknmrnr, mbetaalper, m_email, muurlbedr, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    muurl150bedr = 0
    muurl200bedr = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): muurl125bedr → %s", mwerknmrnr, mbetaalper, m_email, muurl125bedr, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mreisbedr = 0
    mverlofbedr = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): muurl150bedr → %s", mwerknmrnr, mbetaalper, m_email, muurl150bedr, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mziekbedr = 0
    mfeestbedr = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): muurl200bedr → %s", mwerknmrnr, mbetaalper, m_email, muurl200bedr, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    mdokterbedr = 0
    mgverzuimbedr = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mreisbedr → %s", mwerknmrnr, mbetaalper, m_email, mreisbedr, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
    moverzuimbedr = 0
    for row in rpwrkwnrln:
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mverlofbedr → %s", mwerknmrnr, mbetaalper, m_email, mverlofbedr, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
        if row[4] == 'Reis':
            mreisuren = mreisuren + float(row[3])
            logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mziekbedr → %s", mwerknmrnr, mbetaalper, m_email, mziekbedr, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
        if row[4] == '100%':
            muren = muren + float(row[3])
            logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mfeestbedr → %s", mwerknmrnr, mbetaalper, m_email, mfeestbedr, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
        if row[4] == '125%':
            muren125 = muren125 + float(row[3])
            logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mdokterbedr → %s", mwerknmrnr, mbetaalper, m_email, mdokterbedr, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
        if row[4] == '150%':
            muren150 = muren150 + float(row[3])
            logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mgverzuimbedr → %s", mwerknmrnr, mbetaalper, m_email, mgverzuimbedr, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
        if row[4] == '200%':
            muren200 = muren200 + float(row[3])
            logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): moverzuimbedr → %s", mwerknmrnr, mbetaalper, m_email, moverzuimbedr, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
        if row[4] == 'Verlof':
            mverlof = mverlof + float(row[3])
        if row[4] == 'Extra verlof':
            mextraverlof = mextraverlof + float(row[3])
        if row[4] == 'Ziekte':
            mziek = mziek + float(row[3])
        if row[4] == 'Feestdag':
            mfeest = mfeest + float(row[3])
        if row[4] == 'Dokter':
            mdokter = mdokter + float(row[3])
        if row[4] == 'Geoorl. Verzuim':
            mgverzuim = mgverzuim + float(row[3])
        if row[4] == 'Ong. Verzuim':
            moverzuim = moverzuim + float(row[3])
            
        mreisuurl = rpwerkn[18]
        muurl = (rpwerkn[17]+rpwerkn[17]/100*row[3])
            
        mreisbedr = round(float(str(mreisuren*mreisuurl)),2)
        muurlbedr = round(float(str(muren*muurl)),2)
        muurl125bedr = round(float(str(muren125*muurl*1.25)),2)
        muurl150bedr = round(float(str(muren150*muurl*1.5)),2)
        muurl200bedr = round(float(str(muren200*muurl*2)),2)
        mverlofbedr =  round(float(str(mverlof*muurl)),2)
        mziekbedr = round(float(str(mziek*muurl)),2)
        mfeestbedr = round(float(str(mfeest*muurl)),2)
        mdokterbedr = round(float(str(mdokter*muurl)),2)
        mgverzuimbedr = round(float(str(mgverzuim*muurl)),2)
        moverzuimbedr = round(float(str(moverzuim*muurl)),2)
                                       
    class Widget(QDialog):
         logger.debug("<<< Exiting opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s)", mwerknmrnr, mbetaalper, m_email, extra={"event.action": "opvrWerknperiode", "logrite.mwerknmrnr": mwerknmrnr, "logrite.mbetaalper": mbetaalper})
         def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Werknemerperiodegegevens opvragen")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                                  
            self.setFont(QFont('Arial', 10))
                
            self.Accountnummer = QLabel()
            q2Edit = QLineEdit(str(maccountnr))
            q2Edit.setFixedWidth(100)
            q2Edit.setAlignment(Qt.AlignRight)
            q2Edit.setDisabled(True)
            q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q2Edit.setDisabled(True)
                        
            self.Loontabelnummer = QLabel()
            q4Edit = QLineEdit(str(mloonnr))
            q4Edit.setAlignment(Qt.AlignRight)
            q4Edit.setFixedWidth(30)
            q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q4Edit.setDisabled(True)
            
            self.Loontrede = QLabel()
            q5Edit = QLineEdit(str(int(mtrede/0.03)))
            q5Edit.setFixedWidth(30)
            q5Edit.setAlignment(Qt.AlignRight)
            q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q5Edit.setDisabled(True)
           
            self.Loonheffing = QLabel()
            q6Edit = QLineEdit('{:12.2f}'.format(mloonh))
            q6Edit.setFixedWidth(100)
            q6Edit.setAlignment(Qt.AlignRight)
            q6Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q6Edit.setDisabled(True)
                              
            self.Reiskostenvergoeding = QLabel()
            q8Edit = QLineEdit('{:12.2f}'.format(mreisk))
            q8Edit.setFixedWidth(100)
            q8Edit.setAlignment(Qt.AlignRight)
            q8Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q8Edit.setDisabled(True)
       
            self.Pensioen = QLabel()
            q9Edit = QLineEdit('{:12.2f}'.format(mpenspr))
            q9Edit.setFixedWidth(100)
            q9Edit.setAlignment(Qt.AlignRight)
            q9Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q9Edit.setDisabled(True)
            
            self.Reserveringvakantie = QLabel()
            q10Edit = QLineEdit('{:12.2f}'.format(mresvak))
            q10Edit.setAlignment(Qt.AlignRight)
            q10Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q10Edit.setFixedWidth(100)
            q10Edit.setDisabled(True)
               
            self.Werkgeverpensioenpremie = QLabel()
            q11Edit = QLineEdit('{:12.2f}'.format( mpensprwg))
            q11Edit.setFixedWidth(100)
            q11Edit.setAlignment(Qt.AlignRight)
            q11Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q11Edit.setDisabled(True)
            
            self.Auto = QLabel()
            q18Edit = QLineEdit('{:12.2f}'.format(mauto/12))
            q18Edit.setFixedWidth(100)
            q18Edit.setAlignment(Qt.AlignRight)
            q18Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q18Edit.setDisabled(True)
             
            self.Periodiekeuitkering = QLabel()
            q12Edit = QLineEdit('{:12.2f}'.format(mperiodiek))
            q12Edit.setFixedWidth(100)
            q12Edit.setAlignment(Qt.AlignRight)
            q12Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q12Edit.setDisabled(True)
            
            self.Overigeinhoudingen = QLabel()
            q13Edit = QLineEdit('{:12.2f}'.format(moverig))
            q13Edit.setFixedWidth(100)
            q13Edit.setAlignment(Qt.AlignRight)
            q13Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q13Edit.setDisabled(True)
  
            self.Overigevergoedingen = QLabel()
            q19Edit = QLineEdit('{:12.2f}'.format(moverig))
            q19Edit.setFixedWidth(100)
            q19Edit.setAlignment(Qt.AlignRight)
            q19Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q19Edit.setDisabled(True)
    
            self.Indienst = QLabel()
            q14Edit = QLineEdit(mindienst)
            q14Edit.setFixedWidth(100)
            q14Edit.setAlignment(Qt.AlignRight)
            q14Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q14Edit.setDisabled(True)
                        
            self.Brutoloon = QLabel()
            q15Edit = QLineEdit('{:12.2f}'.format(mbruto))
            q15Edit.setDisabled(True)
            q15Edit.setAlignment(Qt.AlignRight)
            q15Edit.setFixedWidth(100)
            q15Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                        
            self.Verlofsaldo = QLabel()
            q16Edit = QLineEdit('{:12.2f}'.format(mverlofsaldo))
            q16Edit.setDisabled(True)
            q16Edit.setAlignment(Qt.AlignRight)
            q16Edit.setFixedWidth(100)
            q16Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            
            self.ExtraVerlof = QLabel()
            q17Edit = QLineEdit('{:12.2f}'.format(mextraverlof))
            q17Edit.setFixedWidth(100)
            q17Edit.setAlignment(Qt.AlignRight)
            q17Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q17Edit.setDisabled(True)
             
            grid = QGridLayout()
            grid.setSpacing(20)
            
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl ,1 , 0)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 3, 1, 1, Qt.AlignRight)
    
            self.setFont(QFont('Arial', 10))
            grid.addWidget(QLabel('Opvragen werknemergegevens van\n'+mvoorn+\
                ' '+machtern+'\nGeboren: '+mgeboren), 1, 1, 1, 3)
            
            grid.addWidget(QLabel('Bruto maandloon'), 3, 2)
            grid.addWidget(q15Edit, 3, 3) 
                                                
            grid.addWidget(QLabel('Accountnummer'), 3, 0)
            grid.addWidget(q2Edit, 3, 1)
            
            grid.addWidget(QLabel('Loontabel'), 7, 0)
            grid.addWidget(q4Edit, 7 , 1) 
             
            grid.addWidget(QLabel('Loontrede'), 8, 0)
            grid.addWidget(q5Edit, 8, 1)
                            
            grid.addWidget(QLabel('Loonheffing'), 4, 2)
            grid.addWidget(q6Edit, 4, 3)
                          
            grid.addWidget(QLabel('Reiskostenvergoeding'), 6, 0)
            grid.addWidget(q8Edit, 6, 1)
             
            grid.addWidget(QLabel('Pensioenafdracht'), 5, 2)
            grid.addWidget(q9Edit, 5, 3)
            
            grid.addWidget(QLabel('Reservering vakantiegeld      '), 5, 0)
            grid.addWidget(q10Edit, 5, 1)  
     
            grid.addWidget(QLabel('Werkgeversdeel pensioenpremie'), 6, 2)
            grid.addWidget(q11Edit, 6, 3)
                   
            grid.addWidget(QLabel('Periodieke uitkering belast'), 4, 0)
            grid.addWidget(q12Edit, 4, 1) 
            
            grid.addWidget(QLabel('Overige inhoudingen onbelast'), 7, 2)
            grid.addWidget(q13Edit, 7, 3) 
            
            grid.addWidget(QLabel('Bijtelling Bedrijfsauto'), 8, 2)
            grid.addWidget(q18Edit, 8, 3) 
            
            grid.addWidget(QLabel('Werkgeversdeel Arbeidsongeschiktheid'), 9, 2)
            grid.addWidget(QLabel('{:12.2f}'.format(mwerkg_WAO_IVA_WGA)), 9, 3, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('Werkgeversdeel Werkloosheidswet'), 10, 2)
            grid.addWidget(QLabel('{:12.2f}'.format(mwerkg_AWF)), 10, 3, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('Werkgeversdeel Zorgverzekering'), 11, 2)
            grid.addWidget(QLabel('{:12.2f}'.format(mwerkg_ZVW)), 11, 3, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('Bijzonder tarief   % '), 12, 2)
            grid.addWidget(QLabel('{:12.2f}'.format(mbyztar)), 12, 3, 1, 1, Qt.AlignRight)
            
            grid.addWidget(QLabel('Overige Vergoedingen onbelast'), 11, 0)
            grid.addWidget(q19Edit, 11, 1) 
       
            grid.addWidget(QLabel('Datum indiensttreding'), 12, 0)
            grid.addWidget(q14Edit, 12, 1) 
            
            grid.addWidget(QLabel('Verlofsaldo in uren'), 9, 0)
            grid.addWidget(q16Edit, 9, 1)
            
            grid.addWidget(QLabel('Extra verlof in uren'), 10, 0)
            grid.addWidget(q17Edit, 10, 1)
            
            grid.addWidget(QLabel('Uurloon'), 21, 0)
            grid.addWidget(QLabel('{:12.2f}'.format(muurl)), 21, 1, 1, 1, Qt.AlignRight) 
            grid.addWidget(QLabel('Reisuurloon'), 21, 2)
            grid.addWidget(QLabel('{:12.2f}'.format(mreisuurl)), 21, 3, 1 ,1, Qt.AlignRight)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 22, 0, 1, 3, Qt.AlignCenter)
            grid.addWidget(QLabel('Periode gegevens van '+mbetmaand+' '+mbetjr), 13, 1, 1, 2)
            grid.addWidget(QLabel('Uren'), 14, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('Bedragen'), 14, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('Uren'), 14, 2, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('Bedragen'), 14, 3, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('Werkuren 125%'), 15, 2)
            grid.addWidget(QLabel('{:12.2f}'.format(muren125)), 15, 2, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('{:12.2f}'.format(muurl125bedr)), 15, 3, 1, 1, Qt.AlignRight) 
            grid.addWidget(QLabel('Werkuren 150%'), 16, 2)
            grid.addWidget(QLabel('{:12.2f}'.format(muren150)), 16, 2, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('{:12.2f}'.format(muurl150bedr)), 16, 3, 1, 1, Qt.AlignRight) 
            grid.addWidget(QLabel('Werkuren 200%'), 17, 2)
            grid.addWidget(QLabel('{:12.2f}'.format(muren200)), 17, 2, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('{:12.2f}'.format(muurl200bedr)), 17, 3, 1, 1, Qt.AlignRight) 
            grid.addWidget(QLabel('Reisuren'), 15, 0)
            grid.addWidget(QLabel('{:12.2f}'.format(mreisuren)), 15, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('{:12.2f}'.format(mreisbedr)), 15, 1, 1, 1, Qt.AlignRight) 
            grid.addWidget(QLabel('Te betalen uren'), 16, 0) 
            grid.addWidget(QLabel('173.3'), 16, 0, 1, 1, Qt.AlignRight) 
            grid.addWidget(QLabel('Werkuren 100%'), 17 ,0)
            grid.addWidget(QLabel('{:12.2f}'.format(muren)), 17, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('{:12.2f}'.format(muurlbedr)), 17, 1, 1, 1, Qt.AlignRight) 
            grid.addWidget(QLabel('Verlof'), 18, 0)
            grid.addWidget(QLabel('{:12.2f}'.format(mverlof)), 18, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('{:12.2f}'.format(mverlofbedr)), 18, 1, 1, 1, Qt.AlignRight) 
            grid.addWidget(QLabel('Ziekte'), 18, 2)
            grid.addWidget(QLabel('{:12.2f}'.format(mziek)), 18, 2, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('{:12.2f}'.format(mziekbedr)), 18, 3, 1, 1, Qt.AlignRight) 
            grid.addWidget(QLabel('Feestdag'), 19, 0)
            grid.addWidget(QLabel('{:12.2f}'.format(mfeest)), 19, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('{:12.2f}'.format(mfeestbedr)), 19, 1, 1, 1, Qt.AlignRight) 
            grid.addWidget(QLabel('Dokter'), 19, 2)
            grid.addWidget(QLabel('{:12.2f}'.format(mdokter)), 19, 2, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('{:12.2f}'.format(mdokterbedr)), 19, 3, 1, 1, Qt.AlignRight) 
            grid.addWidget(QLabel('Geoorloofd verzuim'), 20, 0)
            grid.addWidget(QLabel('{:12.2f}'.format(mgverzuim)), 20, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('{:12.2f}'.format(mgverzuimbedr)), 20, 1, 1, 1, Qt.AlignRight) 
            grid.addWidget(QLabel('Ongeoorloofd verzuim'), 20, 2)
            grid.addWidget(QLabel('{:12.2f}'.format(moverzuim)), 20, 2, 1, 1, Qt.AlignRight)
            grid.addWidget(QLabel('{:12.2f}'.format(moverzuimbedr)), 20, 3, 1, 1, Qt.AlignRight) 
            
            self.setLayout(grid)
            self.setGeometry(400, 50, 350, 300)
                     
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(self.close)
        
            grid.addWidget(cancelBtn, 22, 3, 1, 1, Qt.AlignRight)
            cancelBtn.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
  
    window = Widget()
    window.exec_()
    zoekWerknemer(m_email)
