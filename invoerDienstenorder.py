from login import hoofdMenu
import datetime
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
                QDialog, QMessageBox ,QComboBox 
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QRegExp
from sqlalchemy import (Table, Column, Integer, String, Float, ForeignKey, \
                        MetaData, create_engine, func)
from sqlalchemy.sql import select, insert, and_
import logging
logger = logging.getLogger(__name__)

def invoerGelukt():
    logger.warning(">>> Entering invoerGelukt()", extra={"event.action": "invoerGelukt"})
    msg = QMessageBox()
    logger.debug("invoerGelukt(): msg → %s", msg, extra={"event.action": "invoerGelukt"})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))        
    msg.setIcon(QMessageBox.Information)
    msg.setText('Import service order successful!')
    msg.setWindowTitle('Purchase order services')
    logger.debug("<<< Exiting invoerGelukt()", extra={"event.action": "invoerGelukt"})
    msg.exec_()
    
def foutInvoer():
    logger.warning(">>> Entering foutInvoer()", extra={"event.action": "foutInvoer"})
    msg = QMessageBox()
    logger.debug("foutInvoer(): msg → %s", msg, extra={"event.action": "foutInvoer"})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))        
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Incorrect insert. Re-enter data!')
    msg.setWindowTitle('Purchase order services')
    logger.debug("<<< Exiting foutInvoer()", extra={"event.action": "foutInvoer"})
    msg.exec_() 
    
def invoerBestaat():
    logger.warning(">>> Entering invoerBestaat()", extra={"event.action": "invoerBestaat"})
    msg = QMessageBox()
    logger.debug("invoerBestaat(): msg → %s", msg, extra={"event.action": "invoerBestaat"})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))        
    msg.setIcon(QMessageBox.Warning)
    msg.setText('The service in question has already been processed!')
    msg.setWindowTitle('Purchase order services')
    logger.debug("<<< Exiting invoerBestaat()", extra={"event.action": "invoerBestaat"})
    msg.exec_() 

def geenRegels():
    logger.warning(">>> Entering geenRegels()", extra={"event.action": "geenRegels"})
    msg = QMessageBox()
    logger.debug("geenRegels(): msg → %s", msg, extra={"event.action": "geenRegels"})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))        
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No calculation lines of the relevant service available!')
    msg.setWindowTitle('Purchase order services')
    logger.debug("<<< Exiting geenRegels()", extra={"event.action": "geenRegels"})
    msg.exec_()     
    
def sluitRegels(m_email, mlevnr, mwerknr, mregel, self):
    logger.warning(">>> Entering sluitRegels(m_email=%s,mlevnr=%s,mwerknr=%s,mregel=%s)", m_email, mlevnr, mwerknr, mregel, extra={"event.action": "sluitRegels", "logrite.mlevnr": mlevnr, "logrite.mwerknr": mwerknr, "logrite.mregel": mregel})
    self.close()
    zoekLeverancier(m_email, mlevnr, mwerknr, mregel)
    logger.debug("<<< Exiting sluitRegels(m_email=%s,mlevnr=%s,mwerknr=%s,mregel=%s)", m_email, mlevnr, mwerknr, mregel, extra={"event.action": "sluitRegels", "logrite.mlevnr": mlevnr, "logrite.mwerknr": mwerknr, "logrite.mregel": mregel})

def foutLeverancier():
    logger.warning(">>> Entering foutLeverancier()", extra={"event.action": "foutLeverancier"})
    msg = QMessageBox()
    logger.debug("foutLeverancier(): msg → %s", msg, extra={"event.action": "foutLeverancier"})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))        
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Supplier/Work number\nnot found!')
    msg.setWindowTitle('Purchase order services')
    logger.debug("<<< Exiting foutLeverancier()", extra={"event.action": "foutLeverancier"})
    msg.exec_()
        
def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
                 
def _11check(mlevnr):
    logger.warning(">>> Entering _11check(mlevnr=%s)", mlevnr, extra={"event.action": "_11check", "logrite.mlevnr": mlevnr})
    number = str(mlevnr)
    logger.debug("_11check(mlevnr=%s): number → %s", mlevnr, number, extra={"event.action": "_11check", "logrite.mlevnr": mlevnr})
    total = 0       
    fullnumber = number                       
    logger.debug("_11check(mlevnr=%s): total → %s", mlevnr, total, extra={"event.action": "_11check", "logrite.mlevnr": mlevnr})
    for i in range(8):
        total += int(fullnumber[i])*(9-i)
        logger.debug("_11check(mlevnr=%s): fullnumber → %s", mlevnr, fullnumber, extra={"event.action": "_11check", "logrite.mlevnr": mlevnr})
        checkdigit = total % 11 % 10
    if checkdigit == int(fullnumber[8]):
        return True
    else:
        logger.debug("<<< Exiting _11check(mlevnr=%s)", mlevnr, extra={"event.action": "_11check", "logrite.mlevnr": mlevnr})
        return False
 
def maak11proef(basisnr):
   logger.warning(">>> Entering maak11proef(basisnr=%s)", basisnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   basisnr = str(basisnr)
   basisnr = str((int(basisnr[0:8]))+int(1))
   logger.debug("maak11proef(basisnr=%s): basisnr → %s", basisnr, basisnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   total = 0                       
   logger.debug("maak11proef(basisnr=%s): total → %s", basisnr, total, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   for i in range(int(8)):
       total += int(basisnr[i])*(int(9)-i)
   checkdigit = total % 11 % 10
   logger.debug("maak11proef(basisnr=%s): checkdigit → %s", basisnr, checkdigit, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   basisuitnr = basisnr+str(checkdigit)
   logger.debug("maak11proef(basisnr=%s): basisuitnr → %s", basisnr, basisuitnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   logger.debug("<<< Exiting maak11proef(basisnr=%s)", basisnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   return basisuitnr

def zoekLeverancier(m_email, mlevnr, mwerknr, mregel):
    logger.warning(">>> Entering zoekLeverancier(m_email=%s,mlevnr=%s,mwerknr=%s,mregel=%s)", m_email, mlevnr, mwerknr, mregel, extra={"event.action": "zoekLeverancier", "logrite.mlevnr": mlevnr, "logrite.mwerknr": mwerknr, "logrite.mregel": mregel})
    metadata = MetaData()
    logger.debug("zoekLeverancier(m_email=%s,mlevnr=%s,mwerknr=%s,mregel=%s): metadata → %s", m_email, mlevnr, mwerknr, mregel, metadata, extra={"event.action": "zoekLeverancier", "logrite.mlevnr": mlevnr, "logrite.mwerknr": mwerknr, "logrite.mregel": mregel})
    leveranciers = Table('leveranciers', metadata,
        Column('leverancierID', Integer(), primary_key=True),
        Column('bedrijfsnaam', String),
        Column('rechtsvorm', String),
        Column('postcode', String),
        Column('huisnummer', String),
        Column('toevoeging', String))
    werken = Table('werken', metadata,
        Column('werknummerID', Integer, primary_key=True))
            
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("zoekLeverancier(m_email=%s,mlevnr=%s,mwerknr=%s,mregel=%s): engine → %s", m_email, mlevnr, mwerknr, mregel, engine, extra={"event.action": "zoekLeverancier", "logrite.mlevnr": mlevnr, "logrite.mwerknr": mwerknr, "logrite.mregel": mregel})
    conn = engine.connect()
    logger.debug("zoekLeverancier(m_email=%s,mlevnr=%s,mwerknr=%s,mregel=%s): conn → %s", m_email, mlevnr, mwerknr, mregel, conn, extra={"event.action": "zoekLeverancier", "logrite.mlevnr": mlevnr, "logrite.mwerknr": mwerknr, "logrite.mregel": mregel})

    class Widget(QDialog):
        logger.debug("<<< Exiting zoekLeverancier(m_email=%s,mlevnr=%s,mwerknr=%s,mregel=%s)", m_email, mlevnr, mwerknr, mregel, extra={"event.action": "zoekLeverancier", "logrite.mlevnr": mlevnr, "logrite.mwerknr": mwerknr, "logrite.mregel": mregel})
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Insert purchase orders services")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                            
            self.Leveranciernummer = QLabel()
            levEdit = QLineEdit(str(mlevnr))
            levEdit.setFixedWidth(100)
            levEdit.setFont(QFont("Arial",10))
            levEdit.textChanged.connect(self.levChanged)
            reg_ex = QRegExp('^[3]{1}[0-9]{8}$')
            input_validator = QRegExpValidator(reg_ex, levEdit)
            levEdit.setValidator(input_validator)
                            
            self.Werknummer = QLabel()
            werknEdit = QLineEdit(str(mwerknr))
            werknEdit.setFixedWidth(100)
            werknEdit.setFont(QFont("Arial",10))
            werknEdit.textChanged.connect(self.werknChanged)
            reg_ex = QRegExp('^[8]{1}[0-9]{8}$')
            input_validator = QRegExpValidator(reg_ex, levEdit)
            werknEdit.setValidator(input_validator)
            
            grid = QGridLayout()
            grid.setSpacing(20)
    
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 2, 1, 1, Qt.AlignRight)
    
            self.setFont(QFont('Arial', 10))
            grid.addWidget(QLabel('Supplier\nWork number\nServices'), 0, 1)
    
            grid.addWidget(QLabel('Supplier'), 1, 0)
            grid.addWidget(levEdit, 1, 1)
            
            grid.addWidget(QLabel('Work number'), 2, 0)
            grid.addWidget(werknEdit, 2, 1)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved - dj.jansen@casema.nl'), 3, 0, 1 ,3, Qt.AlignCenter)
       
            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
         
            applyBtn = QPushButton('Search')
            applyBtn.clicked.connect(self.accept)
                  
            grid.addWidget(applyBtn, 2, 2)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(120)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
        
            grid.addWidget(cancelBtn, 1, 2)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(120)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            self.setLayout(grid)
            self.setGeometry(600, 400, 150, 150)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Inkoopordernummer → %s", parent, self.Inkoopordernummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): inkorderEdit → %s", parent, inkorderEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): inkorderEdit → %s", self, parent, inkorderEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Werknummer → %s", parent, self.Werknummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): werknEdit → %s", parent, werknEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): werknEdit → %s", self, parent, werknEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Diensten → %s", parent, self.Diensten, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.OrderregelPrijs → %s", parent, self.OrderregelPrijs, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q1Edit → %s", parent, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q1Edit → %s", self, parent, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Omschrijving → %s", parent, self.Omschrijving, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.GeplandeStart → %s", parent, self.GeplandeStart, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.GeplandGereed → %s", parent, self.GeplandGereed, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl8 → %s", parent, lbl8, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl8 → %s", self, parent, lbl8, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl4 → %s", parent, lbl4, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl4 → %s", self, parent, lbl4, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl5 → %s", parent, lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl5 → %s", self, parent, lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl6 → %s", parent, lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl6 → %s", self, parent, lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl7 → %s", parent, lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl7 → %s", self, parent, lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): sluitBtn → %s", parent, sluitBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): sluitBtn → %s", self, parent, sluitBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
    
        def levChanged(self, text):
            logger.warning(">>> Entering levChanged(text=%s)", text, extra={"event.action": "levChanged", "logrite.text": text})
            self.Leveranciernummer.setText(text)
            logger.debug("<<< Exiting levChanged(text=%s)", text, extra={"event.action": "levChanged", "logrite.text": text})
            
        def werknChanged(self, text):
            self.Werknummer.setText(text)
            logger.warning(">>> Entering werknChanged(text=%s)", text, extra={"event.action": "werknChanged", "logrite.text": text})
            logger.debug("<<< Exiting werknChanged(text=%s)", text, extra={"event.action": "werknChanged", "logrite.text": text})
    
        def returnLeveranciernummer(self):
            logger.warning(">>> Entering returnLeveranciernummer()", extra={"event.action": "returnLeveranciernummer"})
            logger.debug("<<< Exiting returnLeveranciernummer()", extra={"event.action": "returnLeveranciernummer"})
            return self.Leveranciernummer.text()
        
        def returnWerknummer(self):
            return self.Werknummer.text()
    
        logger.warning(">>> Entering returnWerknummer()", extra={"event.action": "returnWerknummer"})
        logger.debug("<<< Exiting returnWerknummer()", extra={"event.action": "returnWerknummer"})
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnLeveranciernummer(), dialog.returnWerknummer()]
       
    window = Widget()
    data = window.getData()
    if data[0] and data[1] and len(data[0]) == 9 and len(data[1]) == 9\
           and _11check(data[0]) and  _11check(data[1]):
        mlevnr = int(data[0])
        mwerknr = int(data[1])
    sel = select([leveranciers, werken]).where(and_(leveranciers.c.leverancierID\
                == mlevnr, werken.c.werknummerID == mwerknr))
    rplev = conn.execute(sel).first()
    mregel = 1
    if rplev:
        inkoopRegels(m_email, rplev, mregel)
    else:
        foutLeverancier()
        zoekLeverancier(m_email, mlevnr, mwerknr , mregel)
            
def bepaalInkoopOrdernr(mregel):
    logger.warning(">>> Entering bepaalInkoopOrdernr(mregel=%s)", mregel, extra={"event.action": "bepaalInkoopOrdernr", "logrite.mregel": mregel})
    metadata = MetaData()
    logger.debug("bepaalInkoopOrdernr(mregel=%s): metadata → %s", mregel, metadata, extra={"event.action": "bepaalInkoopOrdernr", "logrite.mregel": mregel})
    orders_inkoop = Table('orders_inkoop', metadata,
        Column('orderinkoopID', Integer, primary_key=True),
        Column('leverancierID', None, ForeignKey('leveranciers.c.leverancierID')))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("bepaalInkoopOrdernr(mregel=%s): engine → %s", mregel, engine, extra={"event.action": "bepaalInkoopOrdernr", "logrite.mregel": mregel})
    conn = engine.connect()
    logger.debug("bepaalInkoopOrdernr(mregel=%s): conn → %s", mregel, conn, extra={"event.action": "bepaalInkoopOrdernr", "logrite.mregel": mregel})
    
    morderinkoopnr=(conn.execute(select([func.max(orders_inkoop.c.orderinkoopID, type_=Integer)\
                                   .label('morderinkoopnr')])).scalar())
    if mregel == 1:
       morderinkoopnr=int(maak11proef(morderinkoopnr))
       logger.debug("bepaalInkoopOrdernr(mregel=%s): morderinkoopnr → %s", mregel, morderinkoopnr, extra={"event.action": "bepaalInkoopOrdernr", "logrite.mregel": mregel})
    logger.debug("<<< Exiting bepaalInkoopOrdernr(mregel=%s)", mregel, extra={"event.action": "bepaalInkoopOrdernr", "logrite.mregel": mregel})
    return(morderinkoopnr)
   
def Inkooporder(m_email, rplev, mregel):
    logger.warning(">>> Entering Inkooporder(m_email=%s,rplev=%s,mregel=%s)", m_email, rplev, mregel, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    mlevnr = int(rplev[0])
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mlevnr → %s", m_email, rplev, mregel, mlevnr, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    mwerknr = int(rplev[6])
    mbedrnaam = rplev[1]
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mwerknr → %s", m_email, rplev, mregel, mwerknr, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    mrechtsvorm = rplev[2]
    mpostcode = rplev[3]
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mbedrnaam → %s", m_email, rplev, mregel, mbedrnaam, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mrechtsvorm → %s", m_email, rplev, mregel, mrechtsvorm, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mpostcode → %s", m_email, rplev, mregel, mpostcode, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    mhuisnr = int(rplev[4])
    if rplev[5]:
        mtoev = rplev[5]
    else:
        logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mhuisnr → %s", m_email, rplev, mregel, mhuisnr, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
        mtoev=''
        logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mtoev → %s", m_email, rplev, mregel, mtoev, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    import postcode
    mstrplts = postcode.checkpostcode(mpostcode, mhuisnr)
    mstraat = mstrplts[0]
    mplaats = mstrplts[1]
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mstrplts → %s", m_email, rplev, mregel, mstrplts, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mplaats → %s", m_email, rplev, mregel, mplaats, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    minkordnr = bepaalInkoopOrdernr(mregel)
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mstraat → %s", m_email, rplev, mregel, mstraat, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    logger.debug("<<< Exiting Inkooporder(m_email=%s,rplev=%s,mregel=%s)", m_email, rplev, mregel, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    return(minkordnr, mlevnr, mbedrnaam, mrechtsvorm, mstraat, mhuisnr,\
               mtoev, mpostcode, mplaats, mwerknr)
      
def inkoopRegels(m_email, rplev, mregel):
    logger.warning(">>> Entering inkoopRegels(m_email=%s,rplev=%s,mregel=%s)", m_email, rplev, mregel, extra={"event.action": "inkoopRegels", "logrite.rplev": rplev, "logrite.mregel": mregel})
    minkgeg = Inkooporder(m_email, rplev, mregel)
    logger.debug("inkoopRegels(m_email=%s,rplev=%s,mregel=%s): minkgeg → %s", m_email, rplev, mregel, minkgeg, extra={"event.action": "inkoopRegels", "logrite.rplev": rplev, "logrite.mregel": mregel})
    minkordnr = minkgeg[0]
    mlevnr = minkgeg[1]
    logger.debug("inkoopRegels(m_email=%s,rplev=%s,mregel=%s): minkordnr → %s", m_email, rplev, mregel, minkordnr, extra={"event.action": "inkoopRegels", "logrite.rplev": rplev, "logrite.mregel": mregel})
    logger.debug("inkoopRegels(m_email=%s,rplev=%s,mregel=%s): mlevnr → %s", m_email, rplev, mregel, mlevnr, extra={"event.action": "inkoopRegels", "logrite.rplev": rplev, "logrite.mregel": mregel})
    mwerknr = minkgeg[9]
    logger.debug("inkoopRegels(m_email=%s,rplev=%s,mregel=%s): mwerknr → %s", m_email, rplev, mregel, mwerknr, extra={"event.action": "inkoopRegels", "logrite.rplev": rplev, "logrite.mregel": mregel})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug("<<< Exiting inkoopRegels(m_email=%s,rplev=%s,mregel=%s)", m_email, rplev, mregel, extra={"event.action": "inkoopRegels", "logrite.rplev": rplev, "logrite.mregel": mregel})
            self.setWindowTitle("Insert purchase order provisional items work")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                       
            self.Inkoopordernummer = QLabel()
            inkorderEdit = QLineEdit(str(minkordnr))
            inkorderEdit.setDisabled(True)
            inkorderEdit.setAlignment(Qt.AlignRight)
            inkorderEdit.setFixedWidth(100)
            inkorderEdit.setFont(QFont("Arial",10))
            inkorderEdit.textChanged.connect(self.inkorderChanged) 
        
            self.Werknummer = QLabel()
            werknEdit = QLineEdit(str(mwerknr))
            werknEdit.setFixedWidth(100)
            werknEdit.setAlignment(Qt.AlignRight)
            werknEdit.setDisabled(True)
            werknEdit.setFont(QFont("Arial",10))
            werknEdit.textChanged.connect(self.werknChanged)
                            
            self.Diensten= QLabel()
            k0Edit = QComboBox()
            k0Edit.setFixedWidth(300)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('          Provisional items work')
            k0Edit.addItem('1. Hiring')
            k0Edit.addItem('2. Direction')
            k0Edit.addItem('3. Housing')
            k0Edit.addItem('5. Earth-moving')
            k0Edit.addItem('7. Transport')
            k0Edit.addItem('8. Remaining')
            k0Edit.activated[str].connect(self.k0Changed)
            
            self.OrderregelPrijs = QLabel()
            q1Edit = QLineEdit()
            q1Edit.setFixedWidth(130)
            q1Edit.setFont(QFont("Arial",10))
            q1Edit.textChanged.connect(self.q1Changed) 
            q1Edit.setDisabled(True)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q1Edit)
            q1Edit.setValidator(input_validator)
             
            self.Omschrijving = QLabel()
            q2Edit = QLineEdit()
            q2Edit.setFixedWidth(400)
            q2Edit.setFont(QFont("Arial",10))
            q2Edit.textChanged.connect(self.q2Changed) 
            reg_ex = QRegExp("^.{0,50}$")
            input_validator = QRegExpValidator(reg_ex,q2Edit)
            q2Edit.setValidator(input_validator)    
        
            self.GeplandeStart = QLabel()
            q3Edit = QLineEdit()
            q3Edit.setCursorPosition(0)
            q3Edit.setFixedWidth(130)
            q3Edit.setFont(QFont("Arial",10))
            q3Edit.textChanged.connect(self.q3Changed) 
            reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
            input_validator = QRegExpValidator(reg_ex, q3Edit)
            q3Edit.setValidator(input_validator)  
            
            self.GeplandGereed = QLabel()
            q4Edit = QLineEdit()
            q4Edit.setCursorPosition(0)
            q4Edit.setFixedWidth(130)
            q4Edit.setFont(QFont("Arial",10))
            q4Edit.textChanged.connect(self.q4Changed) 
            reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
            input_validator = QRegExpValidator(reg_ex, q4Edit)
            q4Edit.setValidator(input_validator)  
                        
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl ,1, 0)
            
            self.setFont(QFont('Arial', 10))
            grid.addWidget(QLabel('Order for\nSupplier: '+str(minkgeg[1])\
            +',\n'+minkgeg[2]+' '+minkgeg[3]+',\n'+minkgeg[4]+' '+str(minkgeg[5])\
            +minkgeg[6]+',\n'+minkgeg[7]+' '+minkgeg[8]+'.\nOrder line '+str(mregel)), 1, 1, 1, 3)
                                             
            lbl1 = QLabel('Order number')
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 5, 0)
            grid.addWidget(inkorderEdit, 5, 1)
            
            grid.addWidget(QLabel('Work number'), 6, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(werknEdit, 6, 1)  
 
            lbl8 = QLabel('Type of order  *')
            lbl8.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl8, 7, 0)
            grid.addWidget(k0Edit, 7, 1)
             
            '''
            lbl4 = QLabel('Contract price')  
            lbl4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl4, 8, 0)
            grid.addWidget(q1Edit, 8, 1)
            '''
            
            lbl5 = QLabel('Description  *')  
            lbl5.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl5, 9, 0)
            grid.addWidget(q2Edit, 9, 1, 1 , 3)
            
            lbl6 = QLabel('Planned start yyyy-mm-dd  *')  
            lbl6.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl6, 10, 0)
            grid.addWidget(q3Edit, 10, 1)
            
            lbl7 = QLabel('Planned ready yyyy-mm-dd  *')  
            lbl7.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl7, 11, 0)
            grid.addWidget(q4Edit, 11, 1)
            grid.addWidget(QLabel('* Required insert'), 11, 2, 1, 2)
                   
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved - dj.jansen@casema.nl'), 13, 0, 1, 4, Qt.AlignCenter)
         
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 3, 1 , 1, Qt.AlignRight)
                       
            self.setLayout(grid)
            self.setGeometry(600, 150, 150, 150)
    
            applyBtn = QPushButton('Insert')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 12, 3, 1 , 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            sluitBtn = QPushButton('Close')
            sluitBtn.clicked.connect(lambda: sluitRegels(m_email, mlevnr, mwerknr, mregel, self))
    
            grid.addWidget(sluitBtn, 12, 2)
            sluitBtn.setFont(QFont("Arial",10))
            sluitBtn.setFixedWidth(100)
            sluitBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                                                                                        
        def inkorderChanged(self, text):
            logger.warning(">>> Entering inkorderChanged(text=%s)", text, extra={"event.action": "inkorderChanged", "logrite.text": text})
            self.Inkoopordernummer.setText(text)
            logger.debug("<<< Exiting inkorderChanged(text=%s)", text, extra={"event.action": "inkorderChanged", "logrite.text": text})
            
        def werknChanged(self, text):
            self.Werknummer.setText(text)
         
        def q1Changed(self,text):
            logger.warning(">>> Entering q1Changed(text=%s)", text, extra={"event.action": "q1Changed", "logrite.text": text})
            self.OrderregelPrijs.setText(text)
            logger.debug("<<< Exiting q1Changed(text=%s)", text, extra={"event.action": "q1Changed", "logrite.text": text})
            
        def q2Changed(self,text):
            logger.warning(">>> Entering q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
            self.Omschrijving.setText(text)
            logger.debug("<<< Exiting q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
        
        def q3Changed(self,text):
            logger.warning(">>> Entering q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
            self.GeplandeStart.setText(text)
            logger.debug("<<< Exiting q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
            
        def q4Changed(self,text):
            logger.warning(">>> Entering q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
            self.GeplandGereed.setText(text)
            logger.debug("<<< Exiting q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
                  
        def k0Changed(self,text):
            logger.warning(">>> Entering k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            self.Diensten.setText(text)  
            logger.debug("<<< Exiting k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
                       
        def returninkorder(self):
            logger.warning(">>> Entering returninkorder()", extra={"event.action": "returninkorder"})
            logger.debug("<<< Exiting returninkorder()", extra={"event.action": "returninkorder"})
            return self.Inkoopordernummer.text()
        
        def returnWerknummer(self):
            logger.warning(">>> Entering returnWerknummer()", extra={"event.action": "returnWerknummer"})
            return self.Werknummer.text()    
                 
        def returnq1(self):
            logger.warning(">>> Entering returnq1()", extra={"event.action": "returnq1"})
            logger.debug("<<< Exiting returnq1()", extra={"event.action": "returnq1"})
            return self.Omschrijving.text()
        
        def returnq2(self):
            logger.warning(">>> Entering returnq2()", extra={"event.action": "returnq2"})
            logger.debug("<<< Exiting returnq2()", extra={"event.action": "returnq2"})
            return self.OrderregelPrijs.text()
        
        def returnq3(self):
            logger.warning(">>> Entering returnq3()", extra={"event.action": "returnq3"})
            logger.debug("<<< Exiting returnq3()", extra={"event.action": "returnq3"})
            return self.GeplandeStart.text()
        
        def returnq4(self):
            logger.warning(">>> Entering returnq4()", extra={"event.action": "returnq4"})
            logger.debug("<<< Exiting returnq4()", extra={"event.action": "returnq4"})
            return self.GeplandGereed.text()
                      
        def returnk0(self):
            logger.warning(">>> Entering returnk0()", extra={"event.action": "returnk0"})
            logger.debug("<<< Exiting returnk0()", extra={"event.action": "returnk0"})
            return self.Diensten.text() 
       
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            return [dialog.returnk0(), dialog.returnq1(),\
                    dialog.returnq2(), dialog.returnq3(), dialog.returnq4()]  
   
    window = Widget()
    data = window.getData()
         
    if data[0] and data[1] and data[3] and data[4]:
        soort = data[0]
        momschr = data[1]
        geplstart = data[3]
        geplgereed = data[4]
    else:
        foutInvoer()
        inkoopRegels(m_email, rplev, mregel)
          
    metadata = MetaData()
    orders_inkoop_diensten = Table('orders_inkoop_diensten', metadata,
        Column('orddienstlevID', Integer(), primary_key=True),
        Column('orderinkoopID', None, ForeignKey('orders_inkoop.orderinkoopID')),
        Column('werknummerID', None, ForeignKey('werken.werknummerID')),
        Column('werkomschr', String),
        Column('omschrijving', String),
        Column('aanneemsom', Float),
        Column('plan_start', String),
        Column('werk_start', String),
        Column('plan_gereed', String),
        Column('werk_gereed', String),
        Column('acceptatie_gereed', Float),
        Column('acceptatie_datum', String),
        Column('regel', Integer))
    calculaties = Table('calculaties', metadata,
        Column('calcID', Integer(), primary_key=True), 
        Column('koppelnummer', Integer),
        Column('inhuur', Float),            
        Column('uren_inhuur', Float),
        Column('leiding', Float),
        Column('huisvesting', Float),
        Column('kabelwerk', Float),
        Column('grondverzet', Float),
        Column('betonwerk', Float),
        Column('vervoer', Float),
        Column('overig', Float),
        Column('verwerkt', Integer))
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()

    selcal = select([calculaties]).where(calculaties.c.koppelnummer == mwerknr)
    seldienst = select([orders_inkoop_diensten]).where(and_(orders_inkoop_diensten.c.werknummerID == mwerknr,\
      orders_inkoop_diensten.c.werkomschr.like(soort+'%')))
    rpdienst = conn.execute(seldienst).first()
    rpcal = conn.execute(selcal)

    if mregel == 1 and data[0] and not rpdienst:
        datum = str(datetime.datetime.now())
        mbestdatum = (datum[0:4]+'-'+datum[8:10]+'-'+datum[5:7])
        metadata = MetaData()
        orders_inkoop = Table('orders_inkoop', metadata,
            Column('orderinkoopID', Integer(), primary_key=True),
            Column('leverancierID', None, ForeignKey('leveranciers.c.leverancierID')),
            Column('besteldatum', String),
            Column('status', Integer))
        engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
        conn = engine.connect()
        mbestdatum = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))[0:10]
        ins = insert(orders_inkoop).values(orderinkoopID = minkordnr, leverancierID =\
                    mlevnr, besteldatum = mbestdatum, status = 1)
        conn.execute(ins)

    flag = 0    
    if soort[0] == '1' and not rpdienst:
        minh_uren = 0
        minhuur = 0
        for row in rpcal:
            if row[2]:
                minh_uren += row[3]
                minhuur += row[2]
                flag = 1
        if flag:
            mdienstnr=(conn.execute(select([func.max(orders_inkoop_diensten.c.orddienstlevID,\
                type_=Integer).label('mdienstnr')])).scalar())
            mdienstnr += 1
            insrgl = insert(orders_inkoop_diensten).values(orddienstlevID = mdienstnr,\
                 orderinkoopID = minkordnr, werknummerID = mwerknr,\
                 werkomschr = soort+' '+str(round(minh_uren,2))+' uren', omschrijving = momschr,\
                 aanneemsom = minhuur, plan_start = geplstart, plan_gereed = geplgereed, regel = mregel)
            conn.execute(insrgl)
            mregel += 1
            invoerGelukt()
    elif soort[0] == '2' and not rpdienst: 
        mleiding = 0
        for row in rpcal:
            if row[4]:
                mleiding += row[4]
                flag = 1
        if flag:
            mdienstnr=(conn.execute(select([func.max(orders_inkoop_diensten.c.orddienstlevID,\
                type_=Integer).label('mdienstnr')])).scalar())
            mdienstnr += 1
            insrgl = insert(orders_inkoop_diensten).values(orddienstlevID = mdienstnr,\
                 orderinkoopID = minkordnr, werknummerID = mwerknr,\
                 werkomschr = soort, omschrijving = momschr, aanneemsom = mleiding,\
                 plan_start = geplstart, plan_gereed = geplgereed, regel = mregel)
            conn.execute(insrgl)
            mregel += 1
            invoerGelukt()
    elif soort[0] == '3' and not rpdienst:
        mhuisvesting = 0
        for row in rpcal:
            if row[5]:
                mhuisvesting += row[5]
                flag = 1
        if flag:
            mdienstnr=(conn.execute(select([func.max(orders_inkoop_diensten.c.orddienstlevID,\
                type_=Integer).label('mdienstnr')])).scalar())
            mdienstnr += 1
            insrgl = insert(orders_inkoop_diensten).values(orddienstlevID = mdienstnr,\
                 orderinkoopID = minkordnr, werknummerID = mwerknr,\
                 werkomschr = soort, omschrijving = momschr, aanneemsom = mhuisvesting,\
                 plan_start = geplstart, plan_gereed = geplgereed, regel = mregel)
            conn.execute(insrgl)
            mregel += 1
            invoerGelukt()
    elif soort[0] == '5' and not rpdienst:
        mgrondverzet = 0
        for row in rpcal:
            if row[7]:
                mgrondverzet += row[7]
                flag = 1
        if flag:
            mdienstnr=(conn.execute(select([func.max(orders_inkoop_diensten.c.orddienstlevID,\
                type_=Integer).label('mdienstnr')])).scalar())
            mdienstnr += 1
            insrgl = insert(orders_inkoop_diensten).values(orddienstlevID = mdienstnr,\
                 orderinkoopID = minkordnr, werknummerID = mwerknr,\
                 werkomschr = soort , omschrijving = momschr, aanneemsom = mgrondverzet,\
                 plan_start = geplstart, plan_gereed = geplgereed, regel = mregel)
            conn.execute(insrgl)
            mregel += 1
            invoerGelukt()
    elif soort[0] == '7' and not rpdienst:
        mvervoer = 0
        for row in rpcal:
            if row[9]:
                mvervoer += row[9]
                flag = 1
        if flag:
            mdienstnr=(conn.execute(select([func.max(orders_inkoop_diensten.c.orddienstlevID,\
                type_=Integer).label('mdienstnr')])).scalar())
            mdienstnr += 1
            insrgl = insert(orders_inkoop_diensten).values(orddienstlevID = mdienstnr,\
                 orderinkoopID = minkordnr, werknummerID = mwerknr,\
                 werkomschr = soort, omschrijving = momschr, aanneemsom = mvervoer,\
                 plan_start = geplstart, plan_gereed = geplgereed, regel = mregel)
            conn.execute(insrgl)
            mregel += 1
            invoerGelukt()
    elif soort[0] == '8' and not rpdienst:
        moverig = 0
        for row in rpcal:
            if row[10]:
                moverig += row[10]
                flag = 1
        if flag:
            mdienstnr=(conn.execute(select([func.max(orders_inkoop_diensten.c.orddienstlevID,\
                type_=Integer).label('mdienstnr')])).scalar())
            mdienstnr += 1
            insrgl = insert(orders_inkoop_diensten).values(orddienstlevID = mdienstnr,\
                 orderinkoopID = minkordnr, werknummerID = mwerknr,\
                 werkomschr = soort, omschrijving = momschr, aanneemsom = moverig,\
                 plan_start = geplstart, plan_gereed = geplgereed, regel = mregel)
            conn.execute(insrgl)
            mregel += 1
            invoerGelukt()
    elif rpdienst:
        invoerBestaat()
    if flag == 0 and not rpdienst:
        geenRegels()
    inkoopRegels(m_email, rplev, mregel)