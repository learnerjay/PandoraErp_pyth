from login import hoofdMenu
import  datetime
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
                         QDialog, QMessageBox
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap, QIcon
from PyQt5.QtCore import QRegExp, Qt
from sqlalchemy import (Table, Column, Integer, ForeignKey, MetaData,\
                        create_engine, func, String)
from sqlalchemy.sql import select, and_
import logging
logger = logging.getLogger(__name__)
 
def geenRecord():
    logger.warning(">>> Entering geenRecord()", extra={"event.action": "geenRecord"})
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg, extra={"event.action": "geenRecord"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No record found\ncreate another selection please!')
    msg.setWindowTitle('Link account')               
    logger.debug("<<< Exiting geenRecord()", extra={"event.action": "geenRecord"})
    msg.exec_() 
    
def geenGeboortedatum():
    logger.warning(">>> Entering geenGeboortedatum()", extra={"event.action": "geenGeboortedatum"})
    msg = QMessageBox()
    logger.debug("geenGeboortedatum(): msg → %s", msg, extra={"event.action": "geenGeboortedatum"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No date of birth filled in\nfill in a date of birth first\nbefore linking an employee!')
    msg.setWindowTitle('Link account')               
    logger.debug("<<< Exiting geenGeboortedatum()", extra={"event.action": "geenGeboortedatum"})
    msg.exec_() 
    
def foutAdmin():
    logger.warning(">>> Entering foutAdmin()", extra={"event.action": "foutAdmin"})
    msg = QMessageBox()
    logger.debug("foutAdmin(): msg → %s", msg, extra={"event.action": "foutAdmin"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Administrator privileges\ncannot be modified!')
    msg.setWindowTitle('Link account')
    logger.debug("<<< Exiting foutAdmin()", extra={"event.action": "foutAdmin"})
    msg.exec_()
        
def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    
def koppelOK():
    logger.warning(">>> Entering koppelOK()", extra={"event.action": "koppelOK"})
    msg = QMessageBox()
    logger.debug("koppelOK(): msg → %s", msg, extra={"event.action": "koppelOK"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Linking successful!')
    msg.setWindowTitle('Link account')
    logger.debug("<<< Exiting koppelOK()", extra={"event.action": "koppelOK"})
    msg.exec_()
   
def koppelBestaat():
    logger.warning(">>> Entering koppelBestaat()", extra={"event.action": "koppelBestaat"})
    msg = QMessageBox()
    logger.debug("koppelBestaat(): msg → %s", msg, extra={"event.action": "koppelBestaat"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Link already exist!')
    msg.setWindowTitle('Link account')
    logger.debug("<<< Exiting koppelBestaat()", extra={"event.action": "koppelBestaat"})
    msg.exec_()  
       
def foutAccountnr():
    logger.warning(">>> Entering foutAccountnr()", extra={"event.action": "foutAccountnr"})
    msg = QMessageBox()
    logger.debug("foutAccountnr(): msg → %s", msg, extra={"event.action": "foutAccountnr"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Account not found.')
    msg.setWindowTitle('Link account')
    logger.debug("<<< Exiting foutAccountnr()", extra={"event.action": "foutAccountnr"})
    msg.exec_()
    
def foutLeveranciernr():
    logger.warning(">>> Entering foutLeveranciernr()", extra={"event.action": "foutLeveranciernr"})
    msg = QMessageBox()
    logger.debug("foutLeveranciernr(): msg → %s", msg, extra={"event.action": "foutLeveranciernr"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Supplier not found!')
    msg.setWindowTitle('Link account')
    logger.debug("<<< Exiting foutLeveranciernr()", extra={"event.action": "foutLeveranciernr"})
    msg.exec_()
    
def foutClient():
    logger.warning(">>> Entering foutClient()", extra={"event.action": "foutClient"})
    msg = QMessageBox()
    logger.debug("foutClient(): msg → %s", msg, extra={"event.action": "foutClient"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Client not found.')
    msg.setWindowTitle('Link account')
    logger.debug("<<< Exiting foutClient()", extra={"event.action": "foutClient"})
    msg.exec_()
                 
def _11check(minnr):
    logger.warning(">>> Entering _11check(minnr=%s)", minnr, extra={"event.action": "_11check", "logrite.minnr": minnr})
    number = str(minnr)
    logger.debug("_11check(minnr=%s): number → %s", minnr, number, extra={"event.action": "_11check", "logrite.minnr": minnr})
    total = 0       
    fullnumber = number                       
    logger.debug("_11check(minnr=%s): total → %s", minnr, total, extra={"event.action": "_11check", "logrite.minnr": minnr})
    for i in range(8):
        total += int(fullnumber[i])*(9-i)
        logger.debug("_11check(minnr=%s): fullnumber → %s", minnr, fullnumber, extra={"event.action": "_11check", "logrite.minnr": minnr})
        checkdigit = total % 11
    if checkdigit == 10:
        checkdigit = 0
    if checkdigit == int(fullnumber[8]):
        return True
    else:
        logger.debug("<<< Exiting _11check(minnr=%s)", minnr, extra={"event.action": "_11check", "logrite.minnr": minnr})
        return False

def zoekAccount(m_email, flag):     
    logger.warning(">>> Entering zoekAccount(m_email=%s,flag=%s)", m_email, flag, extra={"event.action": "zoekAccount", "logrite.flag": flag})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Link account")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Accountnummer = QLabel()
            logger.debug("__init__(parent=%s): self.Accountnummer → %s", parent, self.Accountnummer, extra={"event.action": "__init__"})
            accEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): accEdit → %s", self, parent, accEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): accEdit → %s", parent, accEdit, extra={"event.action": "__init__"})
            accEdit.setFixedWidth(100)
            accEdit.setFont(QFont("Arial",10))
            accEdit.textChanged.connect(self.accChanged)
            reg_ex = QRegExp('^[1]{1}[0-9]{8}$')
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            input_validator = QRegExpValidator(reg_ex, accEdit)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            accEdit.setValidator(input_validator)
                            
            grid = QGridLayout()
            grid.setSpacing(20)
    
            lbl = QLabel()
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0)
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
                
            self.setFont(QFont('Arial', 10))
 
            grid.addWidget(QLabel('Account number'), 1, 0)
            grid.addWidget(accEdit, 1, 1)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 2, Qt.AlignCenter)
        
            cancelBtn = QPushButton('Close')
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
         
            applyBtn = QPushButton('Link')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
                  
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
        
            grid.addWidget(cancelBtn, 2, 0, 1, 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
    
        def accChanged(self, text):
            logger.warning(">>> Entering accChanged(text=%s)", text, extra={"event.action": "accChanged", "logrite.text": text})
            self.Accountnummer.setText(text)
            logger.debug("<<< Exiting accChanged(text=%s)", text, extra={"event.action": "accChanged", "logrite.text": text})
    
        def returnAccountnummer(self):
            logger.warning(">>> Entering returnAccountnummer()", extra={"event.action": "returnAccountnummer"})
            logger.debug("<<< Exiting returnAccountnummer()", extra={"event.action": "returnAccountnummer"})
            return self.Accountnummer.text()
    
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnAccountnummer()]
   
    window = Widget()
    data = window.getData()
    if data[0]:
        maccountnr = int(data[0])
    else:
        maccountnr = 1
    metadata = MetaData()
    accounts = Table('accounts', metadata,
        Column('accountID', Integer(), primary_key=True),
        Column('geboortedatum', String))           
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    
    sel = select([accounts]).where(accounts.c.accountID == maccountnr)
    rp = conn.execute(sel).first()
    if maccountnr == 100000010:
        foutAdmin()
        zoekAccount(m_email, flag)
    elif len(str(maccountnr)) == 9 and _11check(maccountnr) and rp:
        maccountnr = int(maccountnr)
        mgebdat = rp[1]
        if flag == 0 and mgebdat:
            koppelWerknemer(m_email, maccountnr, mgebdat, flag)
        elif flag == 1:
            koppelKoper(m_email, maccountnr, flag)
        elif flag == 2:
            koppelLeverancier(m_email, maccountnr, flag)
        else:
            geenGeboortedatum()
            zoekAccount(m_email, flag)
    else:
        foutAccountnr()
        zoekAccount(m_email, flag)
        
def koppelLeverancier(m_email, maccountnr, flag):
    logger.warning(">>> Entering koppelLeverancier(m_email=%s,maccountnr=%s,flag=%s)", m_email, maccountnr, flag, extra={"event.action": "koppelLeverancier", "logrite.maccountnr": maccountnr, "logrite.flag": flag})
    class Widget(QDialog):
       logger.error("Exception in koppelLeverancier(m_email=%s,maccountnr=%s,flag=%s)", m_email, maccountnr, flag, exc_info=True, extra={"event.action": "koppelLeverancier", "event.category": "process", "logrite.maccountnr": maccountnr, "logrite.flag": flag})
       def __init__(self, parent=None):
           super(Widget, self).__init__(parent)
           self.setWindowTitle("Link account to supplier.")
           self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
           self.setFont(QFont('Arial', 10))
    
           self.Leveranciernummer = QLabel()
           levEdit = QLineEdit()
           levEdit.setFixedWidth(100)
           levEdit.setFont(QFont("Arial",10))
           levEdit.textChanged.connect(self.levChanged)
           reg_ex = QRegExp('^[3]{1}[0-9]{8}$')
           input_validator = QRegExpValidator(reg_ex, levEdit)
           levEdit.setValidator(input_validator)
                           
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
     
           grid.addWidget(QLabel('Supplier number'), 1, 0)
           grid.addWidget(levEdit, 1, 1)
    
           grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 2, Qt.AlignCenter)
    
           cancelBtn = QPushButton('Close')
           cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
         
           applyBtn = QPushButton('Link')
           applyBtn.clicked.connect(self.accept)
                  
           grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
           applyBtn.setFont(QFont("Arial",10))
           applyBtn.setFixedWidth(100)
           applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
        
           grid.addWidget(cancelBtn, 2, 0, 1, 1, Qt.AlignRight)
           cancelBtn.setFont(QFont("Arial",10))
           cancelBtn.setFixedWidth(100)
           cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
           
           self.setLayout(grid)
           self.setGeometry(500, 300, 150, 150)
   
       def levChanged(self, text):
           logger.warning(">>> Entering levChanged(text=%s)", text, extra={"event.action": "levChanged", "logrite.text": text})
           self.Leveranciernummer.setText(text)
           logger.debug("<<< Exiting levChanged(text=%s)", text, extra={"event.action": "levChanged", "logrite.text": text})
    
       def returnLeveranciernummer(self):
           logger.warning(">>> Entering returnLeveranciernummer()", extra={"event.action": "returnLeveranciernummer"})
           logger.debug("<<< Exiting returnLeveranciernummer()", extra={"event.action": "returnLeveranciernummer"})
           return self.Leveranciernummer.text()
    
       @staticmethod
       def getData(parent=None):
           logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
           dialog = Widget(parent)
           dialog.exec_()
           return [dialog.returnLeveranciernummer()]
       
    window = Widget()
    data = window.getData()
    if data[0]:
        mlevnr = int(data[0])
    else:
        mlevnr = 1
        
    metadata = MetaData()
    leveranciers = Table('leveranciers', metadata,
        Column('leverancierID', Integer, primary_key=True))
    lev_accounts = Table('lev_accounts', metadata,
        Column('levaccID', Integer(), primary_key=True),
        Column('leverancierID', None, ForeignKey('leveranciers.leverancierID')),
        Column('accountID', None, ForeignKey('accounts.accountID')))
          
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    
    s = select([leveranciers]).where(leveranciers.c.leverancierID == mlevnr)
    if conn.execute(s).fetchone():
        rp = conn.execute(s)
    else:
        geenRecord()
        zoekAccount(m_email, flag)
    
    if len(str(mlevnr)) == 9 and _11check(mlevnr):
        mlevnr = int(mlevnr)
    else:
        mlevnr = 1
        foutLeveranciernr()
        zoekAccount(m_email, flag)   
          
    s = select([lev_accounts]).where(and_(lev_accounts.c.accountID == maccountnr,
             lev_accounts.c.leverancierID == mlevnr, lev_accounts.c.accountID ==\
             maccountnr))
     
    rp = conn.execute(s)
    if rp:
        regels = 0
        for record in rp:
            regels += 1
        if regels == 0:
            try:
                mlevaccnr = (conn.execute(select([func.max(lev_accounts.c.levaccID,\
                        type_=Integer)])).scalar())
                mlevaccnr += 1
            except:
                mlevaccnr = 1
            ins = lev_accounts.insert().values(levaccID = mlevaccnr, accountID = maccountnr,\
                        leverancierID = mlevnr)
            conn.execute(ins)
            conn.close()
            koppelOK()
            zoekAccount(m_email, flag)
        else:
            koppelBestaat()
            zoekAccount(m_email, flag)
     
def koppelKoper(m_email, maccountnr, flag):
    logger.warning(">>> Entering koppelKoper(m_email=%s,maccountnr=%s,flag=%s)", m_email, maccountnr, flag, extra={"event.action": "koppelKoper", "logrite.maccountnr": maccountnr, "logrite.flag": flag})
    class Widget(QDialog):
       logger.error("Exception in koppelKoper(m_email=%s,maccountnr=%s,flag=%s)", m_email, maccountnr, flag, exc_info=True, extra={"event.action": "koppelKoper", "event.category": "process", "logrite.maccountnr": maccountnr, "logrite.flag": flag})
       def __init__(self, parent=None):
           super(Widget, self).__init__(parent)
           self.setWindowTitle("Link account / buyer.")
           self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
           self.setFont(QFont('Arial', 10))
    
           self.Clientnummer = QLabel()
           kbedrEdit = QLineEdit()
           kbedrEdit.setFixedWidth(100)
           kbedrEdit.setFont(QFont("Arial",10))
           kbedrEdit.textChanged.connect(self.kbedrChanged)
           reg_ex = QRegExp('^[6]{1}[0-9]{8}$')
           input_validator = QRegExpValidator(reg_ex, kbedrEdit)
           kbedrEdit.setValidator(input_validator)
                           
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
    
           grid.addWidget(QLabel('Client number'), 1, 0)
           grid.addWidget(kbedrEdit, 1, 1)
           grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 2, Qt.AlignCenter)
    
           cancelBtn = QPushButton('Close')
           cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
         
           applyBtn = QPushButton('Link')
           applyBtn.clicked.connect(self.accept)
                  
           grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
           applyBtn.setFont(QFont("Arial",10))
           applyBtn.setFixedWidth(100)
           applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
        
           grid.addWidget(cancelBtn, 2, 0, 1, 1, Qt.AlignRight)
           cancelBtn.setFont(QFont("Arial",10))
           cancelBtn.setFixedWidth(100)
           cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
           
           self.setLayout(grid)
           self.setGeometry(500, 300, 150, 150)
   
       def kbedrChanged(self, text):
           logger.warning(">>> Entering kbedrChanged(text=%s)", text, extra={"event.action": "kbedrChanged", "logrite.text": text})
           self.Clientnummer.setText(text)
           logger.debug("<<< Exiting kbedrChanged(text=%s)", text, extra={"event.action": "kbedrChanged", "logrite.text": text})
    
       def returnClientnummer(self):
           logger.warning(">>> Entering returnClientnummer()", extra={"event.action": "returnClientnummer"})
           logger.debug("<<< Exiting returnClientnummer()", extra={"event.action": "returnClientnummer"})
           return self.Clientnummer.text()
    
       @staticmethod
       def getData(parent=None):
           dialog = Widget(parent)
           dialog.exec_()
           return [dialog.returnClientnummer()]
       
    window = Widget()
    data = window.getData()
    if data[0]:
        mclientnr = int(data[0])
    else:
        mclientnr = 1
        
    metadata = MetaData()
    kopers = Table('kopers', metadata,
        Column('koperID', Integer, primary_key=True))
    koper_accounts = Table('koper_accounts', metadata,
        Column('koperaccID', Integer(), primary_key=True),
        Column('koperID', None, ForeignKey('kopers.koperID')),
        Column('accountID', None, ForeignKey('accounts.accountID')))
          
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    s = select([kopers]).where(kopers.c.koperID == mclientnr)
    if conn.execute(s).fetchone():
        rp = conn.execute(s)
    else:
        geenRecord()
        zoekAccount(m_email, flag)

    s = select([koper_accounts]).where(and_(koper_accounts.c.accountID == maccountnr,
             koper_accounts.c.koperID == int(mclientnr)))
    rp = conn.execute(s)
    if rp:
        regels = 0
        for record in rp:
            regels += 1
        if regels == 0:
            try:
                mclientaccnr = (conn.execute(select([func.max(koper_accounts.c.koperaccID,\
                    type_=Integer)])).scalar())
                mclientaccnr += 1
            except:
                mclientaccnr = 1
            ins = koper_accounts.insert().values(koperaccID = mclientaccnr, accountID = maccountnr,\
                                koperID = mclientnr)
            conn.execute(ins)
            koppelOK()
            zoekAccount(m_email, flag)
        else:
            koppelBestaat()
            zoekAccount(m_email, flag)
 
def koppelWerknemer(m_email, maccountnr, mgebdat, flag):
    logger.warning(">>> Entering koppelWerknemer(m_email=%s,maccountnr=%s,mgebdat=%s,flag=%s)", m_email, maccountnr, mgebdat, flag, extra={"event.action": "koppelWerknemer", "logrite.maccountnr": maccountnr, "logrite.mgebdat": mgebdat, "logrite.flag": flag})
    metadata = MetaData()
    logger.debug("koppelWerknemer(m_email=%s,maccountnr=%s,mgebdat=%s,flag=%s): metadata → %s", m_email, maccountnr, mgebdat, flag, metadata, extra={"event.action": "koppelWerknemer", "logrite.maccountnr": maccountnr, "logrite.mgebdat": mgebdat, "logrite.flag": flag})
    werknemers = Table('werknemers', metadata,
        Column('werknemerID', Integer(), primary_key=True),
        Column('accountID', None, ForeignKey('accounts.accountID')),
        Column('indienst', String))
      
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("koppelWerknemer(m_email=%s,maccountnr=%s,mgebdat=%s,flag=%s): engine → %s", m_email, maccountnr, mgebdat, flag, engine, extra={"event.action": "koppelWerknemer", "logrite.maccountnr": maccountnr, "logrite.mgebdat": mgebdat, "logrite.flag": flag})
    conn = engine.connect()
    logger.debug("koppelWerknemer(m_email=%s,maccountnr=%s,mgebdat=%s,flag=%s): conn → %s", m_email, maccountnr, mgebdat, flag, conn, extra={"event.action": "koppelWerknemer", "logrite.maccountnr": maccountnr, "logrite.mgebdat": mgebdat, "logrite.flag": flag})
    try:
        mwerknemernr =(conn.execute(select([func.max(werknemers.c.werknemerID,\
            type_=Integer)])).scalar())
        mwerknemernr += 1
    except:
        logger.debug("koppelWerknemer(m_email=%s,maccountnr=%s,mgebdat=%s,flag=%s): type_ → %s", m_email, maccountnr, mgebdat, flag, type_, extra={"event.action": "koppelWerknemer", "logrite.maccountnr": maccountnr, "logrite.mgebdat": mgebdat, "logrite.flag": flag})
        mwerknemernr = 1
        logger.debug("koppelWerknemer(m_email=%s,maccountnr=%s,mgebdat=%s,flag=%s): mwerknemernr → %s", m_email, maccountnr, mgebdat, flag, mwerknemernr, extra={"event.action": "koppelWerknemer", "logrite.maccountnr": maccountnr, "logrite.mgebdat": mgebdat, "logrite.flag": flag})
    sel = select([werknemers]).where(werknemers.c.accountID == maccountnr)
    logger.debug("koppelWerknemer(m_email=%s,maccountnr=%s,mgebdat=%s,flag=%s): sel → %s", m_email, maccountnr, mgebdat, flag, sel, extra={"event.action": "koppelWerknemer", "logrite.maccountnr": maccountnr, "logrite.mgebdat": mgebdat, "logrite.flag": flag})
    logger.error("Exception in koppelWerknemer(m_email=%s,maccountnr=%s,mgebdat=%s,flag=%s)", m_email, maccountnr, mgebdat, flag, exc_info=True, extra={"event.action": "koppelWerknemer", "event.category": "process", "logrite.maccountnr": maccountnr, "logrite.mgebdat": mgebdat, "logrite.flag": flag})
    if conn.execute(sel).fetchone():
        koppelBestaat()
        zoekAccount(m_email, flag)
    else:
        rp = conn.execute(sel)
        logger.debug("koppelWerknemer(m_email=%s,maccountnr=%s,mgebdat=%s,flag=%s): rp → %s", m_email, maccountnr, mgebdat, flag, rp, extra={"event.action": "koppelWerknemer", "logrite.maccountnr": maccountnr, "logrite.mgebdat": mgebdat, "logrite.flag": flag})
        koppelOK()
    mindienst = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))[0:10]
    logger.debug("koppelWerknemer(m_email=%s,maccountnr=%s,mgebdat=%s,flag=%s): mindienst → %s", m_email, maccountnr, mgebdat, flag, mindienst, extra={"event.action": "koppelWerknemer", "logrite.maccountnr": maccountnr, "logrite.mgebdat": mgebdat, "logrite.flag": flag})
    if rp:
        regels = 0
        for record in rp:
            regels += 1
        if regels == 0 :
            ins = werknemers.insert().values(werknemerID=mwerknemernr,accountID =\
            maccountnr, indienst = mindienst)
            conn.execute(ins)
            zoekAccount(m_email, flag)
        else:
            koppelBestaat()
            logger.debug("<<< Exiting koppelWerknemer(m_email=%s,maccountnr=%s,mgebdat=%s,flag=%s)", m_email, maccountnr, mgebdat, flag, extra={"event.action": "koppelWerknemer", "logrite.maccountnr": maccountnr, "logrite.mgebdat": mgebdat, "logrite.flag": flag})
            zoekAccount(m_email, flag) 