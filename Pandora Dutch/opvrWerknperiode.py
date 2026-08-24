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
    logger.debug(">>> Entering geenBetaalgeg()")
    msg = QMessageBox()
    logger.debug("geenBetaalgeg(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen betaalgegevens voor\ndeze periode gevonden!')
    msg.setWindowTitle('Werknemers periodegegevens opvragen')
    logger.debug("<<< Exiting geenBetaalgeg()")
    msg.exec_()
    
def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)
    
def ongInvoer():
    logger.debug(">>> Entering ongInvoer()")
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Foutieve invoer\nzoekterm opnieuw invoeren s.v.p.!')
    msg.setWindowTitle('Werknemers periodegegevens opvragen')               
    logger.debug("<<< Exiting ongInvoer()")
    msg.exec_() 

def geenRecord():
    logger.debug(">>> Entering geenRecord()")
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen urenmutaties van deze persoon gevonden\nin deze periode maak een andere selektie s.v.p.!')
    msg.setWindowTitle('Werknemers periodegegevens opvragen')               
    logger.debug("<<< Exiting geenRecord()")
    msg.exec_() 
    
def foutWerknemer():
    logger.debug(">>> Entering foutWerknemer()")
    msg = QMessageBox()
    logger.debug("foutWerknemer(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Werknemer niet gevonden\nen/of geen geldige periode opgegeven!')
    msg.setWindowTitle('Werknemers periodegegevens opvragen')
    logger.debug("<<< Exiting foutWerknemer()")
    msg.exec_()
               
def _11check(minput):
    logger.debug(">>> Entering _11check(minput=%s)", minput)
    number = str(minput)
    logger.debug("_11check(minput=%s): number → %s", minput, number)
    total = 0       
    fullnumber = number                       
    logger.debug("_11check(minput=%s): total → %s", minput, total)
    for i in range(8):
        total += int(fullnumber[i])*(9-i)
        logger.debug("_11check(minput=%s): fullnumber → %s", minput, fullnumber)
        checkdigit = total % 11
    if checkdigit == 10:
        checkdigit = 0
    if checkdigit == int(fullnumber[8]):
        return True
    else:
        logger.debug("<<< Exiting _11check(minput=%s)", minput)
        return False 
    
def zoekWerknemer(m_email):     
    logger.debug(">>> Entering zoekWerknemer(m_email=%s)", m_email)
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
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit)
            logger.debug("__init__(parent=%s): self.Accountnummer → %s", parent, self.Accountnummer)
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit)
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit)
            logger.debug("__init__(parent=%s): self.Loontabelnummer → %s", parent, self.Loontabelnummer)
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit)
            logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit)
            logger.debug("__init__(parent=%s): self.Loontrede → %s", parent, self.Loontrede)
            logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit)
            logger.debug("__init__(parent=%s): q6Edit → %s", parent, q6Edit)
            logger.debug("__init__(parent=%s): self.Loonheffing → %s", parent, self.Loonheffing)
            logger.debug("__init__(self=%s,parent=%s): q6Edit → %s", self, parent, q6Edit)
            logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit)
            logger.debug("__init__(parent=%s): self.Reiskostenvergoeding → %s", parent, self.Reiskostenvergoeding)
            logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit)
            logger.debug("__init__(parent=%s): q9Edit → %s", parent, q9Edit)
            logger.debug("__init__(parent=%s): self.Pensioen → %s", parent, self.Pensioen)
            logger.debug("__init__(self=%s,parent=%s): q9Edit → %s", self, parent, q9Edit)
            logger.debug("__init__(parent=%s): q10Edit → %s", parent, q10Edit)
            logger.debug("__init__(parent=%s): self.Reserveringvakantie → %s", parent, self.Reserveringvakantie)
            logger.debug("__init__(self=%s,parent=%s): q10Edit → %s", self, parent, q10Edit)
            logger.debug("__init__(parent=%s): q11Edit → %s", parent, q11Edit)
            logger.debug("__init__(parent=%s): self.Werkgeverpensioenpremie → %s", parent, self.Werkgeverpensioenpremie)
            logger.debug("__init__(self=%s,parent=%s): q11Edit → %s", self, parent, q11Edit)
            logger.debug("__init__(parent=%s): q18Edit → %s", parent, q18Edit)
            logger.debug("__init__(parent=%s): self.Auto → %s", parent, self.Auto)
            logger.debug("__init__(self=%s,parent=%s): q18Edit → %s", self, parent, q18Edit)
            logger.debug("__init__(parent=%s): q12Edit → %s", parent, q12Edit)
            logger.debug("__init__(parent=%s): self.Periodiekeuitkering → %s", parent, self.Periodiekeuitkering)
            logger.debug("__init__(self=%s,parent=%s): q12Edit → %s", self, parent, q12Edit)
            logger.debug("__init__(parent=%s): q13Edit → %s", parent, q13Edit)
            logger.debug("__init__(parent=%s): self.Overigeinhoudingen → %s", parent, self.Overigeinhoudingen)
            logger.debug("__init__(self=%s,parent=%s): q13Edit → %s", self, parent, q13Edit)
            logger.debug("__init__(parent=%s): q19Edit → %s", parent, q19Edit)
            logger.debug("__init__(parent=%s): self.Overigevergoedingen → %s", parent, self.Overigevergoedingen)
            logger.debug("__init__(self=%s,parent=%s): q19Edit → %s", self, parent, q19Edit)
            logger.debug("__init__(parent=%s): q14Edit → %s", parent, q14Edit)
            logger.debug("__init__(parent=%s): self.Indienst → %s", parent, self.Indienst)
            logger.debug("__init__(self=%s,parent=%s): q14Edit → %s", self, parent, q14Edit)
            logger.debug("__init__(parent=%s): q15Edit → %s", parent, q15Edit)
            logger.debug("__init__(parent=%s): self.Brutoloon → %s", parent, self.Brutoloon)
            logger.debug("__init__(self=%s,parent=%s): q15Edit → %s", self, parent, q15Edit)
            logger.debug("__init__(parent=%s): q16Edit → %s", parent, q16Edit)
            logger.debug("__init__(parent=%s): self.Verlofsaldo → %s", parent, self.Verlofsaldo)
            logger.debug("__init__(self=%s,parent=%s): q16Edit → %s", self, parent, q16Edit)
            logger.debug("__init__(parent=%s): q17Edit → %s", parent, q17Edit)
            logger.debug("__init__(parent=%s): self.ExtraVerlof → %s", parent, self.ExtraVerlof)
            logger.debug("__init__(self=%s,parent=%s): q17Edit → %s", self, parent, q17Edit)
            logger.debug("__init__(parent=%s): grid → %s", parent, grid)
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid)
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl)
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl)
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn)
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
    
        def werknemerChanged(self, text):
            logger.debug(">>> Entering werknemerChanged(text=%s)", text)
            logger.debug("werknemerChanged(self=%s,text=%s): Werknemer → %s", self, text, Werknemer)
            self.Werknemer.setText(text)
            logger.debug("<<< Exiting werknemerChanged(text=%s)", text)
            
        def betChanged(self, text):
            logger.debug(">>> Entering betChanged(text=%s)", text)
            logger.debug("betChanged(self=%s,text=%s): Betaalperiode → %s", self, text, Betaalperiode)
            self.Betaalperiode.setText(text)
            logger.debug("<<< Exiting betChanged(text=%s)", text)
    
        def returnWerknemer(self):
            logger.debug(">>> Entering returnWerknemer()")
            logger.debug("<<< Exiting returnWerknemer()")
            return self.Werknemer.text()
        
        def returnBetaalperiode(self):
            logger.debug(">>> Entering returnBetaalperiode()")
            logger.debug("<<< Exiting returnBetaalperiode()")
            return self.Betaalperiode.text()
    
        @staticmethod
        def getData(parent=None):
            logger.debug(">>> Entering getData(parent=%s)", parent)
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent)
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
    logger.debug(">>> Entering opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s)", mwerknmrnr, mbetaalper, m_email)
    mbegin = str(mbetaalper[0:8]+'-'+'01')
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mbegin → %s", mwerknmrnr, mbetaalper, m_email, mbegin)
    mtot = str(mbetaalper[0:8]+'-'+'31')
    midx = int(mbetaalper[5:7])
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mtot → %s", mwerknmrnr, mbetaalper, m_email, mtot)
    mbet = ['Januari','Februari',' Maart', 'April', 'Mei', 'Juni', 'Juli',\
                'Augustus','September', 'Oktober', 'November', 'December']
    mbetmaand = str(mbet[midx-1])
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): midx → %s", mwerknmrnr, mbetaalper, m_email, midx)
    mbetjr = str(mbetaalper[0:4])

    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mbet → %s", mwerknmrnr, mbetaalper, m_email, mbet)
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
    accounts = Table('accounts', metadata,
        Column('accountID', Integer, primary_key=True),
        Column('voornaam', String),
        Column('achternaam', String),
        Column('geboortedatum', String))
         
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): werknemers → %s", mwerknmrnr, mbetaalper, m_email, werknemers)
    sel = select([werknemers, lonen, wrkwnrln, accounts]).where(and_\
      (werknemers.c.werknemerID == mwerknmrnr, werknemers.c.loonID ==\
       lonen.c.loonID, accounts.c.accountID == werknemers.c.accountID))
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): lonen → %s", mwerknmrnr, mbetaalper, m_email, lonen)
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): wrkwnrln → %s", mwerknmrnr, mbetaalper, m_email, wrkwnrln)
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): accounts → %s", mwerknmrnr, mbetaalper, m_email, accounts)
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): engine → %s", mwerknmrnr, mbetaalper, m_email, engine)
    rpwerkn = conn.execute(sel).first()
    mwerknmrnr = rpwerkn[0]
    maccountnr = rpwerkn[1]
    mloonnr = rpwerkn[2]
    mtrede = rpwerkn[3]*0.03
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): conn → %s", mwerknmrnr, mbetaalper, m_email, conn)
    mreisk = float(rpwerkn[4])
   
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): sel → %s", mwerknmrnr, mbetaalper, m_email, sel)
    #mloonh = (uurloon*40*13)/3 #tabelloon.loonheffing
    if rpwerkn[2] < 37:
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): rpwerkn → %s", mwerknmrnr, mbetaalper, m_email, rpwerkn)
        mbruto = rpwerkn[17]*520/3*(1+mtrede)
        muurl = rpwerkn[17]*(1+mtrede)
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): maccountnr → %s", mwerknmrnr, mbetaalper, m_email, maccountnr)
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mloonnr → %s", mwerknmrnr, mbetaalper, m_email, mloonnr)
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mtrede → %s", mwerknmrnr, mbetaalper, m_email, mtrede)
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mreisk → %s", mwerknmrnr, mbetaalper, m_email, mreisk)
    else:
        mbruto =  rpwerkn[19]*(1+mtrede)
        muurl = mbruto*3/520
    #loonheffing pensioenpremie
    metadata =  MetaData()
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mbruto → %s", mwerknmrnr, mbetaalper, m_email, mbruto)
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
     #pensioenpremie
    if rpwerkn[2] < 37:
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): params → %s", mwerknmrnr, mbetaalper, m_email, params)
        mbruto = rpwerkn[17]*520/3*(1+mtrede)
        muurl = rpwerkn[17]*(1+mtrede)
    else:
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): con → %s", mwerknmrnr, mbetaalper, m_email, con)
        mbruto =  rpwerkn[2]*(1+mtrede)
        muurl = mbruto*3/520
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): selpar → %s", mwerknmrnr, mbetaalper, m_email, selpar)
    
    mjaarink = mbruto*12.96
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): rppar → %s", mwerknmrnr, mbetaalper, m_email, rppar)
    mpensink = mjaarink
    if mpensink >  rppar[44][5]:
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mauto → %s", mwerknmrnr, mbetaalper, m_email, mauto)
        mpensprjr = (rppar[44][5]-rppar[44][4])*rppar[44][1]
    else:
        mpensprjr = (mpensink-rppar[44][4])*rppar[44][1]
    mpenspr = (mpensprjr)/12.96/3
    mpensprwg = mpenspr*2
    mresvak = mbruto*.08
    mbelink = mjaarink-mpensprjr+(mauto*12)

    mwerkg_WAO_IVA_WGA = rppar[69][1]*mjaarink/12.96
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mjaarink → %s", mwerknmrnr, mbetaalper, m_email, mjaarink)
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mpensink → %s", mwerknmrnr, mbetaalper, m_email, mpensink)
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mpensprjr → %s", mwerknmrnr, mbetaalper, m_email, mpensprjr)
    mwerkg_AWF = rppar[70][1]*mjaarink/12.96 
    mwerkg_ZVW = rppar[71][1]*mjaarink/12.96
    # Bijzonder tarief bepalen
    if mbelink > 0 and mbelink <= 6512:
        mbyz = 0.3655
    elif mbelink > 6512 and mbelink <= 10226:
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mpenspr → %s", mwerknmrnr, mbetaalper, m_email, mpenspr)
        mbyz = 0.3479
    elif mbelink > 10226 and mbelink <=18937:
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mpensprwg → %s", mwerknmrnr, mbetaalper, m_email, mpensprwg)
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mresvak → %s", mwerknmrnr, mbetaalper, m_email, mresvak)
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mbelink → %s", mwerknmrnr, mbetaalper, m_email, mbelink)
        mbyz = 0.0849
    elif mbelink > 18937 and mbelink <= 20143:
        mbyz = 0.3655
    elif mbelink > 20143 and mbelink <= 22029:
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mwerkg_WAO_IVA_WGA → %s", mwerknmrnr, mbetaalper, m_email, mwerkg_WAO_IVA_WGA)
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mwerkg_AWF → %s", mwerknmrnr, mbetaalper, m_email, mwerkg_AWF)
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mwerkg_ZVW → %s", mwerknmrnr, mbetaalper, m_email, mwerkg_ZVW)
        mbyz = 0.4553
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mbyz → %s", mwerknmrnr, mbetaalper, m_email, mbyz)
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
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mloonh → %s", mwerknmrnr, mbetaalper, m_email, mloonh)
    mbyztar = mbyz*100
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mbyztar → %s", mwerknmrnr, mbetaalper, m_email, mbyztar)
    #mwerkglasten = float(rpwerkn[8])
    mperiodiek = float(rpwerkn[9])
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mperiodiek → %s", mwerknmrnr, mbetaalper, m_email, mperiodiek)
    moverig = float(rpwerkn[10])
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): moverig → %s", mwerknmrnr, mbetaalper, m_email, moverig)
    mindienst = rpwerkn[13]
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mindienst → %s", mwerknmrnr, mbetaalper, m_email, mindienst)
    mverlofsaldo = rpwerkn[14]
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mverlofsaldo → %s", mwerknmrnr, mbetaalper, m_email, mverlofsaldo)
    mextraverlof = rpwerkn[15]
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mextraverlof → %s", mwerknmrnr, mbetaalper, m_email, mextraverlof)
    mvoorn = rpwerkn[28]
    machtern = rpwerkn[29]
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mvoorn → %s", mwerknmrnr, mbetaalper, m_email, mvoorn)
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): machtern → %s", mwerknmrnr, mbetaalper, m_email, machtern)
    mgeboren = str(rpwerkn[30])[8:10]+str(rpwerkn[30])[4:7]+'-'+str(rpwerkn[30])[0:4]
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mgeboren → %s", mwerknmrnr, mbetaalper, m_email, mgeboren)
   
    if rpwerkn[18]:
        mreisuurl = round(rpwerkn[18],2)
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mreisuurl → %s", mwerknmrnr, mbetaalper, m_email, mreisuurl)
    else:
        mreisuurl = 0

    selwrkwnrln = select([wrkwnrln]).where(and_(wrkwnrln.c.werknemerID == mwerknmrnr,\
     werknemers.c.werknemerID == wrkwnrln.c.werknemerID,\
     (wrkwnrln.c.boekdatum >= mbegin), (wrkwnrln.c.boekdatum <= mtot)))
    if conn.execute(selwrkwnrln).fetchone():
        rpwrkwnrln = conn.execute(selwrkwnrln)
        logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): rpwrkwnrln → %s", mwerknmrnr, mbetaalper, m_email, rpwrkwnrln)
    else:
        geenRecord()
        zoekWerknemer(m_email)
    mreisuren = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mreisuren → %s", mwerknmrnr, mbetaalper, m_email, mreisuren)
    muren = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): muren → %s", mwerknmrnr, mbetaalper, m_email, muren)
    muren125 = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): muren125 → %s", mwerknmrnr, mbetaalper, m_email, muren125)
    muren150 = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): muren150 → %s", mwerknmrnr, mbetaalper, m_email, muren150)
    muren200 = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): muren200 → %s", mwerknmrnr, mbetaalper, m_email, muren200)
    mverlof = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mverlof → %s", mwerknmrnr, mbetaalper, m_email, mverlof)
    mziek = 0
    mfeest = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mziek → %s", mwerknmrnr, mbetaalper, m_email, mziek)
    mdokter = 0
    mgverzuim = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mfeest → %s", mwerknmrnr, mbetaalper, m_email, mfeest)
    moverzuim = 0
    muurlbedr = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mdokter → %s", mwerknmrnr, mbetaalper, m_email, mdokter)
    muurl125bedr = 0
    muurl150bedr = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mgverzuim → %s", mwerknmrnr, mbetaalper, m_email, mgverzuim)
    muurl200bedr = 0
    mreisbedr = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): moverzuim → %s", mwerknmrnr, mbetaalper, m_email, moverzuim)
    mverlofbedr = 0
    mziekbedr = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): muurlbedr → %s", mwerknmrnr, mbetaalper, m_email, muurlbedr)
    mfeestbedr = 0
    mdokterbedr = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): muurl125bedr → %s", mwerknmrnr, mbetaalper, m_email, muurl125bedr)
    mgverzuimbedr = 0
    moverzuimbedr = 0
    logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): muurl150bedr → %s", mwerknmrnr, mbetaalper, m_email, muurl150bedr)
    for row in rpwrkwnrln:
        if row[4] == 'Reis':
            logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): muurl200bedr → %s", mwerknmrnr, mbetaalper, m_email, muurl200bedr)
            mreisuren = mreisuren + float(row[3])
        if row[4] == '100%':
            logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mreisbedr → %s", mwerknmrnr, mbetaalper, m_email, mreisbedr)
            muren = muren + float(row[3])
        if row[4] == '125%':
            logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mverlofbedr → %s", mwerknmrnr, mbetaalper, m_email, mverlofbedr)
            muren125 = muren125 + float(row[3])
        if row[4] == '150%':
            logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mziekbedr → %s", mwerknmrnr, mbetaalper, m_email, mziekbedr)
            muren150 = muren150 + float(row[3])
        if row[4] == '200%':
            logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mfeestbedr → %s", mwerknmrnr, mbetaalper, m_email, mfeestbedr)
            muren200 = muren200 + float(row[3])
        if row[4] == 'Verlof':
            logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mdokterbedr → %s", mwerknmrnr, mbetaalper, m_email, mdokterbedr)
            mverlof = mverlof + float(row[3])
        if row[4] == 'Extra verlof':
            logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): mgverzuimbedr → %s", mwerknmrnr, mbetaalper, m_email, mgverzuimbedr)
            mextraverlof = mextraverlof + float(row[3])
        if row[4] == 'Ziekte':
            logger.debug("opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s): moverzuimbedr → %s", mwerknmrnr, mbetaalper, m_email, moverzuimbedr)
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
         logger.debug("<<< Exiting opvrWerknperiode(mwerknmrnr=%s,mbetaalper=%s,m_email=%s)", mwerknmrnr, mbetaalper, m_email)
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
