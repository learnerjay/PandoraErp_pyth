from login import hoofdMenu
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
                             QDialog, QMessageBox
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QRegExp
from sqlalchemy import (Table, Column, Integer, String, Float, Boolean,\
                        ForeignKey,  MetaData, create_engine)
from sqlalchemy.sql import select, and_, update
import logging
logger = logging.getLogger(__name__)

def geenBetaalgeg():
    logger.warning(">>> Entering geenBetaalgeg()", extra={"event.action": "geenBetaalgeg"})
    msg = QMessageBox()
    logger.debug("geenBetaalgeg(): msg → %s", msg, extra={"event.action": "geenBetaalgeg"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen betaalgegevens voor\ndeze periode gevonden!')
    msg.setWindowTitle('Gegevens!')
    logger.debug("<<< Exiting geenBetaalgeg()", extra={"event.action": "geenBetaalgeg"})
    msg.exec_()
    
def wijzSluit(self, m_email):
    logger.warning(">>> Entering wijzSluit(m_email=%s)", m_email, extra={"event.action": "wijzSluit"})
    self.close()
    zoekWerknemer(m_email)
    logger.debug("<<< Exiting wijzSluit(m_email=%s)", m_email, extra={"event.action": "wijzSluit"})
    
def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    
def info():
    logger.warning(">>> Entering info()", extra={"event.action": "info"})
    class Widget(QDialog):
        def __init__(self):
            logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
            QDialog.__init__(self)
            self.setWindowTitle("Informatie vervangend werk")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setFont(QFont("Arial", 10))
            grid = QGridLayout()
            logger.debug("__init__(): grid → %s", grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): grid → %s", self, grid, extra={"event.action": "__init__"})
            grid.setSpacing(20)
            
            logo = QLabel()
            logger.debug("__init__(): logo → %s", logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): logo → %s", self, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lblinfo → %s", self, lblinfo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logger.debug("__init__(self=%s): pixmap → %s", self, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(): pixmap → %s", pixmap, extra={"event.action": "__init__"})
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 3, 1, 1, Qt.AlignRight)
            
            logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})
            lblinfo = QLabel('Vervangend werk.')
            grid.addWidget(lblinfo, 0, 0, 1, 4, Qt.AlignCenter)
            lblinfo.setStyleSheet("color:rgb(45, 83, 115); font: 25pt Comic Sans MS")
        
            lbl = QLabel()
            logger.debug("__init__(): lbl → %s", lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl → %s", self, lbl, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 0, 0)
            lblinfo = QLabel(
        '''
        Indien een werknemer vervangend werk moet verrichten in een andere discipline,
        dient het nieuwe loontabelnummer van deze discipline  te worden ingevuld 
        in het veld Loontabel.
        Bij het veld Orig blijft dan het oude loontabelnummer staan, waarmee zijn of haar\t
        loon wordt bepaald.
        De werkloongegevens voor doorboeking naar de werken worden
        berekend met het gewijzigde loontabelnummer.
        Bij het hervatten van het oorspronkelijk werk, dient het loontabelnummer 
        te worden teruggewijzigd naar de inhoud van het veld Orig, zodat beide velden
        weer gelijk zijn en de oorspronkelijke situatie is hersteld.
        ''')
                
            grid.addWidget(lblinfo, 1, 0, 1, 4, Qt.AlignCenter)
            lblinfo.setStyleSheet("font: 10pt Comic Sans MS; color: black ; background-color: #D9E1DF") 
            
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(self.close)  
            
            grid.addWidget(cancelBtn,  3, 0, 1, 4, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(90)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 4, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setMinimumWidth(650)
            self.setGeometry(550, 300, 900, 150)
            
    window = Widget()
    window.exec_()
    
def foutWerknemer():
    logger.warning(">>> Entering foutWerknemer()", extra={"event.action": "foutWerknemer"})
    msg = QMessageBox()
    logger.debug("foutWerknemer(): msg → %s", msg, extra={"event.action": "foutWerknemer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Werknemer niet gevonden!')
    msg.setWindowTitle('WERKNEMER')
    logger.debug("<<< Exiting foutWerknemer()", extra={"event.action": "foutWerknemer"})
    msg.exec_()
               
def updateOK():
    logger.warning(">>> Entering updateOK()", extra={"event.action": "updateOK"})
    msg = QMessageBox()
    logger.debug("updateOK(): msg → %s", msg, extra={"event.action": "updateOK"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Je gegevens zijn aangepast!')
    msg.setWindowTitle('Gegevens!')
    logger.debug("<<< Exiting updateOK()", extra={"event.action": "updateOK"})
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
            self.setWindowTitle("Werknemergegevens wijzigen.")
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
                                         
            grid = QGridLayout()
            grid.setSpacing(20)
    
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
    
            self.setFont(QFont('Arial', 10))
     
            grid.addWidget(QLabel('Account-werknemer'), 1, 0)
            grid.addWidget(werknemerEdit, 1, 1)
                       
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
         
            applyBtn = QPushButton('Zoeken')
            applyBtn.clicked.connect(self.accept)
                  
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
        
            grid.addWidget(cancelBtn, 2, 0, 1, 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'),3,0,1,2, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(400, 300, 150, 150)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Accountnummer → %s", parent, self.Accountnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Loontabelnummer → %s", parent, self.Loontabelnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.wnrTabelnummer → %s", parent, self.wnrTabelnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): o4Edit → %s", parent, o4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): o4Edit → %s", self, parent, o4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Loontrede → %s", parent, self.Loontrede, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Reiskostenvergoeding → %s", parent, self.Reiskostenvergoeding, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit, extra={"event.action": "__init__"})
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
            logger.debug("__init__(self=%s,parent=%s): q19Edit → %s", self, parent, q19Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q19Edit → %s", parent, q19Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Indienst → %s", parent, self.Indienst, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q14Edit → %s", self, parent, q14Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q14Edit → %s", parent, q14Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Brutoloon → %s", parent, self.Brutoloon, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q15Edit → %s", self, parent, q15Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q15Edit → %s", parent, q15Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Verlofsaldo → %s", parent, self.Verlofsaldo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q16Edit → %s", self, parent, q16Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q16Edit → %s", parent, q16Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.ExtraVerlof → %s", parent, self.ExtraVerlof, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q17Edit → %s", self, parent, q17Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q17Edit → %s", parent, q17Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): infoBtn → %s", parent, infoBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): infoBtn → %s", self, parent, infoBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
    
        def werknemerChanged(self, text):
            logger.warning(">>> Entering werknemerChanged(text=%s)", text, extra={"event.action": "werknemerChanged", "logrite.text": text})
            self.Werknemer.setText(text)
            logger.debug("<<< Exiting werknemerChanged(text=%s)", text, extra={"event.action": "werknemerChanged", "logrite.text": text})
         
        def returnWerknemer(self):
            logger.warning(">>> Entering returnWerknemer()", extra={"event.action": "returnWerknemer"})
            logger.debug("<<< Exiting returnWerknemer()", extra={"event.action": "returnWerknemer"})
            return self.Werknemer.text()
        
  
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnWerknemer()]
    
    window = Widget()
    data = window.getData()
    if data[0]:
        maccountnr = data[0]
    else:
        foutWerknemer()
        return(0, 0)
                
    metadata = MetaData()

    werknemers = Table('werknemers', metadata,
        Column('werknemerID', Integer(), primary_key=True),
        Column('accountID', None, ForeignKey('accounts.accountID')))
   
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    sel = select([werknemers]).where(werknemers.c.accountID == maccountnr)
    rpwerkn = conn.execute(sel).first()
    
    if (len(str(maccountnr)) == 9 and _11check(maccountnr) and rpwerkn):
        maccountnr = rpwerkn[1]
        mwerknmr = rpwerkn[0]
        updateWerknemer(m_email, mwerknmr)
    else:
        foutWerknemer()
        zoekWerknemer(m_email)

def updateWerknemer(m_email, mwerknmr):
    logger.warning(">>> Entering updateWerknemer(m_email=%s,mwerknmr=%s)", m_email, mwerknmr, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    metadata = MetaData()   
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): metadata → %s", m_email, mwerknmr, metadata, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    werknemers = Table('werknemers', metadata,
        Column('werknemerID', Integer(), primary_key=True),
        Column('accountID', None, ForeignKey('accounts.accountID')),
        Column('loonID', None, ForeignKey('lonen.loonID')), 
        Column('loontrede', Integer),
        Column('reiskosten_vergoeding', Float),
        Column('periodieke_uitkeringen', Float),
        Column('overige_inhoudingen', Float),
        Column('overige_vergoedingen', Float),
        Column('bedrijfsauto', Float),
        Column('indienst', String),
        Column('verlofsaldo', Float),
        Column('extraverlof', Float),
        Column('wnrloonID', Integer))
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
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): sel → %s", m_email, mwerknmr, sel, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    accounts = Table('accounts', metadata,
        Column('accountID', Integer, primary_key=True),
        Column('voornaam', String),
        Column('achternaam', String),
        Column('geboortedatum', String))
         
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): engine → %s", m_email, mwerknmr, engine, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    conn = engine.connect()
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): conn → %s", m_email, mwerknmr, conn, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    sel = select([werknemers, lonen, wrkwnrln, accounts]).where(and_\
      (werknemers.c.werknemerID == mwerknmr, werknemers.c.loonID ==\
       lonen.c.loonID, accounts.c.accountID == werknemers.c.accountID))
    rpwerkn = conn.execute(sel).first()
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): rpwerkn → %s", m_email, mwerknmr, rpwerkn, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    mwerknmr = rpwerkn[0]
    maccountnr = rpwerkn[1]
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): maccountnr → %s", m_email, mwerknmr, maccountnr, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    mloonnr = rpwerkn[2]
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): mloonnr → %s", m_email, mwerknmr, mloonnr, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    if not rpwerkn[12]:
        mwnrloonnr = mloonnr
    else:
        mwnrloonnr = rpwerkn[12]
        logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): mwnrloonnr → %s", m_email, mwerknmr, mwnrloonnr, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    mtrede = rpwerkn[3]*0.03
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): mtrede → %s", m_email, mwerknmr, mtrede, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    mreisk = rpwerkn[4]
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): mreisk → %s", m_email, mwerknmr, mreisk, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    mauto = rpwerkn[8]      
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): mauto → %s", m_email, mwerknmr, mauto, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    mperiodiek = rpwerkn[5]
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): mperiodiek → %s", m_email, mwerknmr, mperiodiek, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    moveriginh = rpwerkn[6]
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): moveriginh → %s", m_email, mwerknmr, moveriginh, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    moverigverg = rpwerkn[7]
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): moverigverg → %s", m_email, mwerknmr, moverigverg, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    mindienst = rpwerkn[9]
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): mindienst → %s", m_email, mwerknmr, mindienst, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    mverlofsaldo = rpwerkn[10]
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): mverlofsaldo → %s", m_email, mwerknmr, mverlofsaldo, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    mextraverlof = rpwerkn[11]
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): mextraverlof → %s", m_email, mwerknmr, mextraverlof, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    mvoorn = rpwerkn[25]
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): mvoorn → %s", m_email, mwerknmr, mvoorn, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    machtern = rpwerkn[26]
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): machtern → %s", m_email, mwerknmr, machtern, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    mgeboren = rpwerkn[27]
    logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): mgeboren → %s", m_email, mwerknmr, mgeboren, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
        
    if rpwerkn[2] < 37:
        mbruto = rpwerkn[14]*520/3*(1+mtrede)
        logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): mbruto → %s", m_email, mwerknmr, mbruto, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
        muurl = rpwerkn[14]*(1+mtrede)
    else:
        mbruto =  rpwerkn[16]*(1+mtrede)
        muurl = mbruto*3/520
        logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): muurl → %s", m_email, mwerknmr, muurl, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
    if rpwerkn[14]:
        mreisuurl = round(rpwerkn[14],2)
    else:
        mreisuurl = 0
        logger.debug("updateWerknemer(m_email=%s,mwerknmr=%s): mreisuurl → %s", m_email, mwerknmr, mreisuurl, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
                                         
    class Widget(QDialog):
         logger.debug("<<< Exiting updateWerknemer(m_email=%s,mwerknmr=%s)", m_email, mwerknmr, extra={"event.action": "updateWerknemer", "logrite.mwerknmr": mwerknmr})
         def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Werknemersgegevens aanpassen")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                                  
            self.setFont(QFont('Arial', 10))
                
            self.Accountnummer = QLabel()
            q2Edit = QLineEdit(str(maccountnr))
            q2Edit.setFixedWidth(100)
            q2Edit.setAlignment(Qt.AlignRight)
            q2Edit.setDisabled(True)
            q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q2Edit.textChanged.connect(self.q2Changed)
                        
            self.Loontabelnummer = QLabel()
            q4Edit = QLineEdit(str(mloonnr))
            q4Edit.setFixedWidth(30)
            q4Edit.setFont(QFont("Arial",10))
            q4Edit.textChanged.connect(self.q4Changed)
            reg_ex = QRegExp("^[0-9]{1,2}$")
            input_validator = QRegExpValidator(reg_ex, q4Edit)
            q4Edit.setValidator(input_validator)
            
            self.wnrTabelnummer = QLabel()
            o4Edit = QLineEdit(str(mwnrloonnr))
            o4Edit.setFixedWidth(30)
            o4Edit.setFont(QFont("Arial",10))
            o4Edit.textChanged.connect(self.o4Changed)
            reg_ex = QRegExp("^[0-9]{1,2}$")
            input_validator = QRegExpValidator(reg_ex, o4Edit)
            o4Edit.setValidator(input_validator)
            
            self.Loontrede = QLabel()
            q5Edit = QLineEdit(str(int(mtrede/0.03)))
            q5Edit.setFixedWidth(30)
            q5Edit.setFont(QFont("Arial",10))
            q5Edit.textChanged.connect(self.q5Changed)
            reg_ex = QRegExp("^[0-9]{1,2}$")
            input_validator = QRegExpValidator(reg_ex, q5Edit)
            q5Edit.setValidator(input_validator)
                                     
            self.Reiskostenvergoeding = QLabel()
            q8Edit = QLineEdit(str(round(mreisk,2)))
            q8Edit.setFixedWidth(100)
            q8Edit.setFont(QFont("Arial",10))
            q8Edit.setAlignment(Qt.AlignRight)
            q8Edit.textChanged.connect(self.q8Changed)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q8Edit)
            q8Edit.setValidator(input_validator)
                                              
            self.Auto = QLabel()
            q18Edit = QLineEdit(str(round(mauto,2)))
            q18Edit.setFixedWidth(100)
            q18Edit.setFont(QFont("Arial",10))
            q18Edit.setAlignment(Qt.AlignRight)
            q18Edit.textChanged.connect(self.q18Changed)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q18Edit)
            q18Edit.setValidator(input_validator)
             
            self.Periodiekeuitkering = QLabel()
            q12Edit = QLineEdit(str(round(mperiodiek,2)))
            q12Edit.setFixedWidth(100)
            q12Edit.setAlignment(Qt.AlignRight)
            q12Edit.setFont(QFont("Arial",10))
            q12Edit.setAlignment(Qt.AlignRight)
            q12Edit.textChanged.connect(self.q12Changed)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q12Edit)
            q12Edit.setValidator(input_validator)
            
            self.Overigeinhoudingen = QLabel()
            q13Edit = QLineEdit(str(round(moveriginh,2)))
            q13Edit.setFixedWidth(100)
            q13Edit.setAlignment(Qt.AlignRight)
            q13Edit.setFont(QFont("Arial",10))
            q13Edit.setAlignment(Qt.AlignRight)
            q13Edit.textChanged.connect(self.q13Changed)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q13Edit)
            q13Edit.setValidator(input_validator)
  
            self.Overigevergoedingen = QLabel()
            q19Edit = QLineEdit(str(round(moverigverg,2)))
            q19Edit.setFixedWidth(100)
            q19Edit.setAlignment(Qt.AlignRight)
            q19Edit.setFont(QFont("Arial",10))
            q19Edit.setAlignment(Qt.AlignRight)
            q19Edit.textChanged.connect(self.q19Changed)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q19Edit)
            q19Edit.setValidator(input_validator)
    
            self.Indienst = QLabel()
            q14Edit = QLineEdit(mindienst)
            q14Edit.setFixedWidth(100)
            q14Edit.setFont(QFont("Arial",10))
            q14Edit.textChanged.connect(self.q14Changed)
            reg_ex = QRegExp('^[1-2]{1}[09]{1}[0-9]{2}-[0-1]{1}[0-9]{1}-[0-3]{1}[0-9]{1}$')
            input_validator = QRegExpValidator(reg_ex, q14Edit)
            q14Edit.setValidator(input_validator)
                        
            self.Brutoloon = QLabel()
            q15Edit = QLineEdit('{:12.2f}'.format(mbruto))
            q15Edit.setDisabled(True)
            q15Edit.setFixedWidth(100)
            q15Edit.setAlignment(Qt.AlignRight)
            q15Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q15Edit.textChanged.connect(self.q15Changed)
            
            self.Verlofsaldo = QLabel()
            q16Edit = QLineEdit('{:12.2f}'.format(mverlofsaldo))
            q16Edit.setDisabled(True)
            q16Edit.setFixedWidth(100)
            q16Edit.setAlignment(Qt.AlignRight)
            q16Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q16Edit.textChanged.connect(self.q16Changed)

            self.ExtraVerlof = QLabel()
            q17Edit = QLineEdit(str(round(mextraverlof,2)))
            q17Edit.setFixedWidth(100)
            q17Edit.setAlignment(Qt.AlignRight)
            q17Edit.setFont(QFont("Arial",10))
            q17Edit.textChanged.connect(self.q17Changed)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q17Edit)
            q17Edit.setValidator(input_validator)
             
            grid = QGridLayout()
            grid.setSpacing(20)
            
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl ,1 , 0)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 4, 1, 1, Qt.AlignCenter)
    
            self.setFont(QFont('Arial', 10))
            grid.addWidget(QLabel('Aanpassen werknemergegevens van\n'+mvoorn+\
                ' '+machtern+'\nGeboren: '+mgeboren), 1, 1, 1, 3)
            
            grid.addWidget(QLabel('Bruto maandloon'), 3, 2)
            grid.addWidget(q15Edit, 3, 3) 
                                                
            grid.addWidget(QLabel('Accountnummer'), 3, 0)
            grid.addWidget(q2Edit, 3, 1)
            
            grid.addWidget(QLabel('Loontabel'), 6, 0)
            grid.addWidget(q4Edit, 6 , 1) 
            
            grid.addWidget(QLabel('Orig'), 6, 1, 1, 1, Qt.AlignCenter)
            grid.addWidget(o4Edit, 6, 1, 1, 1, Qt.AlignRight)
             
            grid.addWidget(QLabel('Loontrede'), 7, 0)
            grid.addWidget(q5Edit, 7, 1)
                                                      
            grid.addWidget(QLabel('Reiskostenvergoeding'), 4, 2)
            grid.addWidget(q8Edit, 4, 3)
                                      
            grid.addWidget(QLabel('Periodieke uitkering belast'), 5, 0)
            grid.addWidget(q12Edit, 5, 1) 
            
            grid.addWidget(QLabel('Overige inhoudingen onbelast'), 5, 2)
            grid.addWidget(q13Edit, 5, 3) 
            
            grid.addWidget(QLabel('Bijtelling Bedrijfsauto'), 4, 0)
            grid.addWidget(q18Edit, 4, 1) 
                           
            grid.addWidget(QLabel('Overige Vergoedingen\nonbelast'), 6, 2)
            grid.addWidget(q19Edit, 6, 3) 
       
            grid.addWidget(QLabel('Datum indiensttreding'), 8, 0)
            grid.addWidget(q14Edit, 8, 1) 
            
            grid.addWidget(QLabel('Verlofsaldo in uren'), 7, 2)
            grid.addWidget(q16Edit, 7, 3)
            
            grid.addWidget(QLabel('Extra verlof in uren'), 8, 2)
            grid.addWidget(q17Edit, 8, 3)
            
            grid.addWidget(QLabel('Uurloon'), 9, 0)
            grid.addWidget(QLabel(str(round(muurl, 2))), 9, 1, 1, 1, Qt.AlignRight) 
            grid.addWidget(QLabel('Reisuurloon'), 9, 2)
            grid.addWidget(QLabel(str(round(mreisuurl, 2))), 9, 3)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 10, 1, 1, 2)
            self.setLayout(grid)
            self.setGeometry(400, 250, 350, 300)
                         
            applyBtn = QPushButton('Wijzigen')
            applyBtn.clicked.connect(self.accept)
                       
            grid.addWidget(applyBtn, 10, 4)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: wijzSluit(self, m_email))
        
            grid.addWidget(cancelBtn, 9, 4)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            infoBtn = QPushButton('Informatie')
            infoBtn.clicked.connect(lambda: info())
        
            grid.addWidget(infoBtn, 8, 4)
            infoBtn.setFont(QFont("Arial",10))
            infoBtn.setFixedWidth(100)
            infoBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                                
         def q2Changed(self, text):
            logger.warning(">>> Entering q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
            self.Accountnummer.setText(text)
            logger.debug("<<< Exiting q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
                       
         def q4Changed(self, text):
            logger.warning(">>> Entering q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
            self.Loontabelnummer.setText(text)
            logger.debug("<<< Exiting q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})

         def o4Changed(self, text):
            logger.warning(">>> Entering o4Changed(text=%s)", text, extra={"event.action": "o4Changed", "logrite.text": text})
            logger.debug("o4Changed(self=%s,text=%s): wnrTabelnummer → %s", self, text, wnrTabelnummer, extra={"event.action": "o4Changed", "logrite.text": text})
            self.wnrTabelnummer.setText(text)
            logger.debug("<<< Exiting o4Changed(text=%s)", text, extra={"event.action": "o4Changed", "logrite.text": text})
            
         def q5Changed(self, text):
            logger.warning(">>> Entering q5Changed(text=%s)", text, extra={"event.action": "q5Changed", "logrite.text": text})
            self.Loontrede.setText(text)
            logger.debug("<<< Exiting q5Changed(text=%s)", text, extra={"event.action": "q5Changed", "logrite.text": text})
                              
         def q8Changed(self, text):
            logger.warning(">>> Entering q8Changed(text=%s)", text, extra={"event.action": "q8Changed", "logrite.text": text})
            self.Reiskostenvergoeding.setText(text)
            logger.debug("<<< Exiting q8Changed(text=%s)", text, extra={"event.action": "q8Changed", "logrite.text": text})
        
         def q12Changed(self, text):
            logger.warning(">>> Entering q12Changed(text=%s)", text, extra={"event.action": "q12Changed", "logrite.text": text})
            self.Periodiekeuitkering.setText(text)
            logger.debug("<<< Exiting q12Changed(text=%s)", text, extra={"event.action": "q12Changed", "logrite.text": text})
            
         def q13Changed(self, text):
            logger.warning(">>> Entering q13Changed(text=%s)", text, extra={"event.action": "q13Changed", "logrite.text": text})
            self.Overigeinhoudingen.setText(text)
            logger.debug("<<< Exiting q13Changed(text=%s)", text, extra={"event.action": "q13Changed", "logrite.text": text})
            
         def q14Changed(self, text):
            logger.warning(">>> Entering q14Changed(text=%s)", text, extra={"event.action": "q14Changed", "logrite.text": text})
            self.Indienst.setText(text)
            logger.debug("<<< Exiting q14Changed(text=%s)", text, extra={"event.action": "q14Changed", "logrite.text": text})
        
         def q15Changed(self, text):
            logger.warning(">>> Entering q15Changed(text=%s)", text, extra={"event.action": "q15Changed", "logrite.text": text})
            self.Brutoloon.setText(text)
            logger.debug("<<< Exiting q15Changed(text=%s)", text, extra={"event.action": "q15Changed", "logrite.text": text})
            
         def q16Changed(self, text):
            logger.warning(">>> Entering q16Changed(text=%s)", text, extra={"event.action": "q16Changed", "logrite.text": text})
            self.Verlofsaldo.setText(text)
            logger.debug("<<< Exiting q16Changed(text=%s)", text, extra={"event.action": "q16Changed", "logrite.text": text})
            
         def q17Changed(self, text):
            logger.warning(">>> Entering q17Changed(text=%s)", text, extra={"event.action": "q17Changed", "logrite.text": text})
            self.ExtraVerlof.setText(text)
            logger.debug("<<< Exiting q17Changed(text=%s)", text, extra={"event.action": "q17Changed", "logrite.text": text})
       
         def q18Changed(self, text):
            logger.warning(">>> Entering q18Changed(text=%s)", text, extra={"event.action": "q18Changed", "logrite.text": text})
            self.Auto.setText(text)
            logger.debug("<<< Exiting q18Changed(text=%s)", text, extra={"event.action": "q18Changed", "logrite.text": text})
            
         def q19Changed(self, text):
            logger.warning(">>> Entering q19Changed(text=%s)", text, extra={"event.action": "q19Changed", "logrite.text": text})
            self.Overigevergoedingen.setText(text)
            logger.debug("<<< Exiting q19Changed(text=%s)", text, extra={"event.action": "q19Changed", "logrite.text": text})
            
         def returnAccountnummer(self):
            logger.warning(">>> Entering returnAccountnummer()", extra={"event.action": "returnAccountnummer"})
            logger.debug("<<< Exiting returnAccountnummer()", extra={"event.action": "returnAccountnummer"})
            return self.Accountnummer.text()
        
         def returnLoontabelnummer(self):
            logger.warning(">>> Entering returnLoontabelnummer()", extra={"event.action": "returnLoontabelnummer"})
            logger.debug("<<< Exiting returnLoontabelnummer()", extra={"event.action": "returnLoontabelnummer"})
            return self.Loontabelnummer.text()
        
         def returnWnrLoonnummer(self):
            logger.warning(">>> Entering returnWnrLoonnummer()", extra={"event.action": "returnWnrLoonnummer"})
            logger.debug("<<< Exiting returnWnrLoonnummer()", extra={"event.action": "returnWnrLoonnummer"})
            return self.wnrTabelnummer.text()
    
         def returnLoontrede(self):
            logger.warning(">>> Entering returnLoontrede()", extra={"event.action": "returnLoontrede"})
            logger.debug("<<< Exiting returnLoontrede()", extra={"event.action": "returnLoontrede"})
            return self.Loontrede.text()
     
         def returnReiskostenvergoeding(self):
            logger.warning(">>> Entering returnReiskostenvergoeding()", extra={"event.action": "returnReiskostenvergoeding"})
            logger.debug("<<< Exiting returnReiskostenvergoeding()", extra={"event.action": "returnReiskostenvergoeding"})
            return self.Reiskostenvergoeding.text()
                              
         def returnPeriodiekeuitkering(self):
            logger.warning(">>> Entering returnPeriodiekeuitkering()", extra={"event.action": "returnPeriodiekeuitkering"})
            logger.debug("<<< Exiting returnPeriodiekeuitkering()", extra={"event.action": "returnPeriodiekeuitkering"})
            return self.Periodiekeuitkering.text()
    
         def returnOverigeinhoudingen(self):
            logger.warning(">>> Entering returnOverigeinhoudingen()", extra={"event.action": "returnOverigeinhoudingen"})
            logger.debug("<<< Exiting returnOverigeinhoudingen()", extra={"event.action": "returnOverigeinhoudingen"})
            return self.Overigeinhoudingen.text()   
 
         def returnIndienst(self):
            logger.warning(">>> Entering returnIndienst()", extra={"event.action": "returnIndienst"})
            logger.debug("<<< Exiting returnIndienst()", extra={"event.action": "returnIndienst"})
            return self.Indienst.text()   
    
         def returnBrutoloon(self):
            logger.warning(">>> Entering returnBrutoloon()", extra={"event.action": "returnBrutoloon"})
            logger.debug("<<< Exiting returnBrutoloon()", extra={"event.action": "returnBrutoloon"})
            return self.Brutoloon.text() 
        
         def returnVerlofsaldo(self):
            logger.warning(">>> Entering returnVerlofsaldo()", extra={"event.action": "returnVerlofsaldo"})
            logger.debug("<<< Exiting returnVerlofsaldo()", extra={"event.action": "returnVerlofsaldo"})
            return self.Verlofsaldo.text() 

         def returnExtraVerlof(self):
            logger.warning(">>> Entering returnExtraVerlof()", extra={"event.action": "returnExtraVerlof"})
            logger.debug("<<< Exiting returnExtraVerlof()", extra={"event.action": "returnExtraVerlof"})
            return self.ExtraVerlof.text() 
        
         def returnAuto(self):
            logger.warning(">>> Entering returnAuto()", extra={"event.action": "returnAuto"})
            logger.debug("<<< Exiting returnAuto()", extra={"event.action": "returnAuto"})
            return self.Auto.text() 
        
         def returnOverigevergoedingen(self):
            logger.warning(">>> Entering returnOverigevergoedingen()", extra={"event.action": "returnOverigevergoedingen"})
            logger.debug("<<< Exiting returnOverigevergoedingen()", extra={"event.action": "returnOverigevergoedingen"})
            return self.Overigevergoedingen.text() 
                
         @staticmethod
         def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            return [dialog.returnAccountnummer(), dialog.returnLoontabelnummer(),\
               dialog.returnWnrLoonnummer(),dialog.returnLoontrede(),\
               dialog.returnReiskostenvergoeding(), dialog.returnPeriodiekeuitkering(),\
               dialog.returnOverigeinhoudingen(),dialog.returnIndienst(),\
               dialog.returnBrutoloon(), dialog.returnVerlofsaldo(),\
               dialog.returnExtraVerlof(), dialog.returnAuto(), dialog.returnOverigevergoedingen()]   

    window = Widget()
    data = window.getData()
    if data[1]:
        mloontabel = int(data[1])
    else:
        mloontabel = rpwerkn[2]
    if data[2]:
        mwnrloonnr = int(data[2])
    elif not rpwerkn[12]:
        mwnrloonnr = rpwerkn[2]
    elif not data[2]: 
        mwnrloonnr = rpwerkn[12]
    if data[3]:
        mtrede = int(data[2])
    else:
        mtrede = rpwerkn[3]
    if data[4]:
        mreisk = float(data[3])
    else:
        mreisk = rpwerkn[4]
    if data[5]:
        mperiod = float(data[4])
    else:
        mperiod = rpwerkn[5]
    if data[6]:
        moverig = float(data[5])
    else:
        moverig = rpwerkn[6]
    if data[7]:
        mindienst = data[6]
    else:
        mindienst = rpwerkn[9]
    if data[9]:
        mextraverlof = data[9]
    else:
        mextraverlof = rpwerkn[11]
    if data[10]:
        mauto = data[10]
    else:
        mauto = rpwerkn[8]
    if data[12]:
        movverg = data[11]
    else:
        movverg = rpwerkn[7]
        
    u = update(werknemers).where(werknemers.c.werknemerID == mwerknmr).\
    values(loonID = mloontabel, wnrloonID = mwnrloonnr, loontrede = mtrede, reiskosten_vergoeding = mreisk,\
        periodieke_uitkeringen=mperiod, overige_inhoudingen=moverig,\
        indienst = mindienst, extraverlof = mextraverlof, bedrijfsauto = mauto,\
        overige_vergoedingen = movverg)  
    conn.execute(u)
    conn.close()
    updateOK()
    zoekWerknemer(m_email)