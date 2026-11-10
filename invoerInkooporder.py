from login import hoofdMenu
import datetime
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
            QDialog, QMessageBox #,QDateEdit
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QRegExp
from sqlalchemy import (Table, Column, Integer, String, Float, Boolean, ForeignKey, \
                        MetaData, create_engine, select, insert, update, and_, func)
import logging
logger = logging.getLogger(__name__)
    
def foutInvoer():
    logger.warning(">>> Entering foutInvoer()", extra={"event.action": "foutInvoer"})
    msg = QMessageBox()
    logger.debug("foutInvoer(): msg → %s", msg, extra={"event.action": "foutInvoer"})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Mandatory Entry!')
    msg.setWindowTitle('Insert work orders')
    logger.debug("<<< Exiting foutInvoer()", extra={"event.action": "foutInvoer"})
    msg.exec_()
    
def foutLeverancier():
    logger.warning(">>> Entering foutLeverancier()", extra={"event.action": "foutLeverancier"})
    msg = QMessageBox()
    logger.debug("foutLeverancier(): msg → %s", msg, extra={"event.action": "foutLeverancier"})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))        
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Supplier not found!')
    msg.setWindowTitle('PURCHASE ORDER')
    logger.debug("<<< Exiting foutLeverancier()", extra={"event.action": "foutLeverancier"})
    msg.exec_()

def geenArtnr():
    logger.warning(">>> Entering geenArtnr()", extra={"event.action": "geenArtnr"})
    msg = QMessageBox()
    logger.debug("geenArtnr(): msg → %s", msg, extra={"event.action": "geenArtnr"})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No existing article found\nNew article number is created!')
    msg.setWindowTitle('Insert Article number')
    logger.debug("<<< Exiting geenArtnr()", extra={"event.action": "geenArtnr"})
    msg.exec_() 

def invoerOk(mregel):
    logger.warning(">>> Entering invoerOk(mregel=%s)", mregel, extra={"event.action": "invoerOk", "logrite.mregel": mregel})
    msg = QMessageBox()
    logger.debug("invoerOk(mregel=%s): msg → %s", mregel, msg, extra={"event.action": "invoerOk", "logrite.mregel": mregel})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Order line '+str(mregel)+' entered')
    msg.setWindowTitle('Order line purchase order')
    logger.debug("<<< Exiting invoerOk(mregel=%s)", mregel, extra={"event.action": "invoerOk", "logrite.mregel": mregel})
    msg.exec_()
    
def reedsBesteld():
    logger.warning(">>> Entering reedsBesteld()", extra={"event.action": "reedsBesteld"})
    msg = QMessageBox()
    logger.debug("reedsBesteld(): msg → %s", msg, extra={"event.action": "reedsBesteld"})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('This product is in the ordering process\nOrdering is possible again after delivery!')
    msg.setWindowTitle('Order line purchase order')
    logger.debug("<<< Exiting reedsBesteld()", extra={"event.action": "reedsBesteld"})
    msg.exec_()
    
def foutArtikel():
    logger.warning(">>> Entering foutArtikel()", extra={"event.action": "foutArtikel"})
    msg = QMessageBox()
    logger.debug("foutArtikel(): msg → %s", msg, extra={"event.action": "foutArtikel"})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Incorrect item number, or not all required data entered!')
    msg.setWindowTitle('Order line purchase order')
    logger.debug("<<< Exiting foutArtikel()", extra={"event.action": "foutArtikel"})
    msg.exec_()
        
def onvBesteld(aantal):
    logger.warning(">>> Entering onvBesteld(aantal=%s)", aantal, extra={"event.action": "onvBesteld", "logrite.aantal": aantal})
    msg = QMessageBox()
    logger.debug("onvBesteld(aantal=%s): msg → %s", aantal, msg, extra={"event.action": "onvBesteld", "logrite.aantal": aantal})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Critical)
    msg.setText('There are '+str(aantal)+' items less specified'+
     '\nto provide reservations minus stock!'+\
     '\nSee "Inventory Management Reservations"'+\
     '\nRe-enter the order line with increased quantity!')
    msg.setWindowTitle('Order line purchase order')
    logger.debug("<<< Exiting onvBesteld(aantal=%s)", aantal, extra={"event.action": "onvBesteld", "logrite.aantal": aantal})
    msg.exec_()
  
def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    
def sluitRegels(m_email, mlevnr, mregel, self):
    logger.warning(">>> Entering sluitRegels(m_email=%s,mlevnr=%s,mregel=%s)", m_email, mlevnr, mregel, extra={"event.action": "sluitRegels", "logrite.mlevnr": mlevnr, "logrite.mregel": mregel})
    self.close()
    zoekLeverancier(m_email, mlevnr, mregel)
    logger.debug("<<< Exiting sluitRegels(m_email=%s,mlevnr=%s,mregel=%s)", m_email, mlevnr, mregel, extra={"event.action": "sluitRegels", "logrite.mlevnr": mlevnr, "logrite.mregel": mregel})

def foutLeveranciernr():
    logger.warning(">>> Entering foutLeveranciernr()", extra={"event.action": "foutLeveranciernr"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            msg = QMessageBox()
            msg.setStyleSheet("color: black;  background-color: gainsboro")
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Supplier not found!')
            msg.setWindowTitle('Ordering purchase order')
            msg.exec_()
            
    window = Widget()
    window.show() 
                
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
   checkdigit = total % 11
   if checkdigit == 10:
            checkdigit = 0
   basisuitnr = basisnr+str(checkdigit)
   logger.debug("maak11proef(basisnr=%s): basisuitnr → %s", basisnr, basisuitnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   logger.debug("<<< Exiting maak11proef(basisnr=%s)", basisnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   return basisuitnr

def zoekLeverancier(m_email, mlevnr, mregel):
    logger.warning(">>> Entering zoekLeverancier(m_email=%s,mlevnr=%s,mregel=%s)", m_email, mlevnr, mregel, extra={"event.action": "zoekLeverancier", "logrite.mlevnr": mlevnr, "logrite.mregel": mregel})
    metadata = MetaData()
    logger.debug("zoekLeverancier(m_email=%s,mlevnr=%s,mregel=%s): metadata → %s", m_email, mlevnr, mregel, metadata, extra={"event.action": "zoekLeverancier", "logrite.mlevnr": mlevnr, "logrite.mregel": mregel})
    leveranciers = Table('leveranciers', metadata,
        Column('leverancierID', Integer(), primary_key=True),
        Column('bedrijfsnaam', String),
        Column('rechtsvorm', String),
        Column('postcode', String),
        Column('huisnummer', String),
        Column('toevoeging', String))
            
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("zoekLeverancier(m_email=%s,mlevnr=%s,mregel=%s): engine → %s", m_email, mlevnr, mregel, engine, extra={"event.action": "zoekLeverancier", "logrite.mlevnr": mlevnr, "logrite.mregel": mregel})
    conn = engine.connect()
    logger.debug("zoekLeverancier(m_email=%s,mlevnr=%s,mregel=%s): conn → %s", m_email, mlevnr, mregel, conn, extra={"event.action": "zoekLeverancier", "logrite.mlevnr": mlevnr, "logrite.mregel": mregel})

    class Widget(QDialog):
        logger.debug("<<< Exiting zoekLeverancier(m_email=%s,mlevnr=%s,mregel=%s)", m_email, mlevnr, mregel, extra={"event.action": "zoekLeverancier", "logrite.mlevnr": mlevnr, "logrite.mregel": mregel})
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Supplier search materials.")
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
                            
            grid = QGridLayout()
            grid.setSpacing(20)
    
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1 ,2)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 2, 1, 1, Qt.AlignRight)
    
            self.setFont(QFont('Arial', 10))
     
            grid.addWidget(QLabel('Supplier'), 2, 1)
            grid.addWidget(levEdit, 2, 2)
       
            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
         
            applyBtn = QPushButton('Search')
            applyBtn.clicked.connect(self.accept)
                    
            grid.addWidget(applyBtn, 3, 2, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
        
            grid.addWidget(cancelBtn, 3, 1, 1, 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1, 3, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(600, 300, 150, 150)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Inkoopordernummer → %s", parent, self.Inkoopordernummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): inkorderEdit → %s", parent, inkorderEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): inkorderEdit → %s", self, parent, inkorderEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.BestelregelArtikel → %s", parent, self.BestelregelArtikel, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): artEdit → %s", parent, artEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): artEdit → %s", self, parent, artEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.BestelHoeveelheid → %s", parent, self.BestelHoeveelheid, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): hoevEdit → %s", parent, hoevEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): hoevEdit → %s", self, parent, hoevEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Inkoopeenheidsprijs → %s", parent, self.Inkoopeenheidsprijs, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): prijsEdit → %s", parent, prijsEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): prijsEdit → %s", self, parent, prijsEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Levering_start → %s", parent, self.Levering_start, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): startEdit → %s", parent, startEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): startEdit → %s", self, parent, startEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Levering_end → %s", parent, self.Levering_end, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): endEdit → %s", parent, endEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): endEdit → %s", self, parent, endEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl2 → %s", parent, lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl2 → %s", self, parent, lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl3 → %s", parent, lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl3 → %s", self, parent, lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl4 → %s", parent, lbl4, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl4 → %s", self, parent, lbl4, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl5 → %s", parent, lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl5 → %s", self, parent, lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl6 → %s", parent, lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl6 → %s", self, parent, lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): sluitBtn → %s", parent, sluitBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): sluitBtn → %s", self, parent, sluitBtn, extra={"event.action": "__init__"})
    
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
            dialog = Widget(parent)
            dialog.exec_()
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnLeveranciernummer()]
       
    window = Widget()
    data = window.getData()
    if data[0] and len(data[0]) == 9 and _11check(data[0]):
        mlevnr = int(data[0])
    sel = select([leveranciers]).where(leveranciers.c.leverancierID == mlevnr)
    rplev = conn.execute(sel).first()
    mregel = 1
    if rplev:
        inkoopRegels(m_email, rplev, mregel)
    else:
        foutLeverancier()
        zoekLeverancier(m_email, mlevnr, mregel)
           
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
    
    try:
        morderinkoopnr=(conn.execute(select([func.max(orders_inkoop.c.orderinkoopID,\
            type_=Integer)])).scalar())
        logger.debug("bepaalInkoopOrdernr(mregel=%s): type_ → %s", mregel, type_, extra={"event.action": "bepaalInkoopOrdernr", "logrite.mregel": mregel})
        if mregel == 1:
            morderinkoopnr=int(maak11proef(morderinkoopnr))
    except:
        logger.debug("bepaalInkoopOrdernr(mregel=%s): morderinkoopnr → %s", mregel, morderinkoopnr, extra={"event.action": "bepaalInkoopOrdernr", "logrite.mregel": mregel})
        if mregel == 1:
            logger.error("Exception in bepaalInkoopOrdernr(mregel=%s)", mregel, exc_info=True, extra={"event.action": "bepaalInkoopOrdernr", "event.category": "process", "logrite.mregel": mregel})
            morderinkoopnr = 400000003
    logger.debug("<<< Exiting bepaalInkoopOrdernr(mregel=%s)", mregel, extra={"event.action": "bepaalInkoopOrdernr", "logrite.mregel": mregel})
    return(morderinkoopnr)
   
def Inkooporder(m_email, rplev, mregel):
    logger.warning(">>> Entering Inkooporder(m_email=%s,rplev=%s,mregel=%s)", m_email, rplev, mregel, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    mlevnr = int(rplev[0])
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mlevnr → %s", m_email, rplev, mregel, mlevnr, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    mbedrnaam = rplev[1]
    mrechtsvorm = rplev[2]
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mbedrnaam → %s", m_email, rplev, mregel, mbedrnaam, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mrechtsvorm → %s", m_email, rplev, mregel, mrechtsvorm, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    mpostcode = rplev[3]
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mpostcode → %s", m_email, rplev, mregel, mpostcode, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    mhuisnr = int(rplev[4])
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mhuisnr → %s", m_email, rplev, mregel, mhuisnr, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    if rplev[5]:
        mtoev = rplev[5]
    else:
        mtoev=''
        logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mtoev → %s", m_email, rplev, mregel, mtoev, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    import postcode
    mstrplts = postcode.checkpostcode(mpostcode, mhuisnr)
    mstraat = mstrplts[0]
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mstrplts → %s", m_email, rplev, mregel, mstrplts, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    mplaats = mstrplts[1]
    minkordnr = bepaalInkoopOrdernr(mregel)
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mstraat → %s", m_email, rplev, mregel, mstraat, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): minkordnr → %s", m_email, rplev, mregel, minkordnr, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mplaats → %s", m_email, rplev, mregel, mplaats, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    logger.debug("<<< Exiting Inkooporder(m_email=%s,rplev=%s,mregel=%s)", m_email, rplev, mregel, extra={"event.action": "Inkooporder", "logrite.rplev": rplev, "logrite.mregel": mregel})
    return(minkordnr, mlevnr, mbedrnaam, mrechtsvorm, mstraat, mhuisnr,\
               mtoev, mpostcode, mplaats)
    
def inkoopRegels(m_email, rplev, mregel):
    logger.warning(">>> Entering inkoopRegels(m_email=%s,rplev=%s,mregel=%s)", m_email, rplev, mregel, extra={"event.action": "inkoopRegels", "logrite.rplev": rplev, "logrite.mregel": mregel})
    minkgeg = Inkooporder(m_email, rplev, mregel)
    logger.debug("inkoopRegels(m_email=%s,rplev=%s,mregel=%s): minkgeg → %s", m_email, rplev, mregel, minkgeg, extra={"event.action": "inkoopRegels", "logrite.rplev": rplev, "logrite.mregel": mregel})
    minkordnr = minkgeg[0]
    mlevnr = minkgeg[1]
    logger.debug("inkoopRegels(m_email=%s,rplev=%s,mregel=%s): minkordnr → %s", m_email, rplev, mregel, minkordnr, extra={"event.action": "inkoopRegels", "logrite.rplev": rplev, "logrite.mregel": mregel})
    logger.debug("inkoopRegels(m_email=%s,rplev=%s,mregel=%s): mlevnr → %s", m_email, rplev, mregel, mlevnr, extra={"event.action": "inkoopRegels", "logrite.rplev": rplev, "logrite.mregel": mregel})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug("<<< Exiting inkoopRegels(m_email=%s,rplev=%s,mregel=%s)", m_email, rplev, mregel, extra={"event.action": "inkoopRegels", "logrite.rplev": rplev, "logrite.mregel": mregel})
            self.setWindowTitle('Enter purchase order order materials')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                       
            self.Inkoopordernummer = QLabel()
            inkorderEdit = QLineEdit(str(minkordnr))
            inkorderEdit.setStyleSheet("color: black ")
            inkorderEdit.setDisabled(True)
            inkorderEdit.setAlignment(Qt.AlignRight)
            inkorderEdit.setFixedWidth(130)
            inkorderEdit.setFont(QFont("Arial",10))
            inkorderEdit.textChanged.connect(self.inkorderChanged) 
            
            self.BestelregelArtikel = QLabel()
            artEdit = QLineEdit()
            artEdit.setFixedWidth(130)
            artEdit.setFont(QFont("Arial",10))
            artEdit.textChanged.connect(self.artChanged) 
            reg_ex = QRegExp("^[2]{1}[0-9]{8}$")
            input_validator = QRegExpValidator(reg_ex, artEdit)
            artEdit.setValidator(input_validator)
            
            self.BestelHoeveelheid = QLabel()
            hoevEdit = QLineEdit()
            hoevEdit.setFixedWidth(130)
            hoevEdit.setFont(QFont("Arial",10))
            hoevEdit.textChanged.connect(self.hoevChanged) 
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, hoevEdit)
            hoevEdit.setValidator(input_validator)
            
            self.Inkoopeenheidsprijs = QLabel()
            prijsEdit = QLineEdit()
            prijsEdit.setFixedWidth(130)
            prijsEdit.setFont(QFont("Arial",10))
            prijsEdit.textChanged.connect(self.prijsChanged) 
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, prijsEdit)
            prijsEdit.setValidator(input_validator)    
        
            self.Levering_start = QLabel()
            #levertEdit = QDateEdit(datetime.date)
            startEdit = QLineEdit('')
            startEdit.setCursorPosition(0)
            startEdit.setFixedWidth(130)
            startEdit.setFont(QFont("Arial",10))
            startEdit.textChanged.connect(self.startChanged) 
            reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
            input_validator = QRegExpValidator(reg_ex, startEdit)
            startEdit.setValidator(input_validator) 
            
            self.Levering_end = QLabel()
            #levertEdit = QDateEdit(datetime.date)
            endEdit = QLineEdit('')
            endEdit.setCursorPosition(0)
            endEdit.setFixedWidth(130)
            endEdit.setFont(QFont("Arial",10))
            endEdit.textChanged.connect(self.endChanged) 
            reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
            input_validator = QRegExpValidator(reg_ex, endEdit)
            endEdit.setValidator(input_validator)  
                        
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl ,0, 0)
            grid.addWidget(QLabel("Order articles"), 0, 1)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 2, 1, 1, Qt.AlignRight)
            
            self.setFont(QFont('Arial', 10))
            grid.addWidget(QLabel('Order for\nSupplier: '+str(minkgeg[1])+\
              ',\n'+minkgeg[2]+' '+minkgeg[3]+',\n'+minkgeg[4]+' '+str(minkgeg[5])+\
              minkgeg[6]+',\n'+minkgeg[7]+' '+minkgeg[8]+'.\nOrder line '+str(mregel)), 1, 1, 5, 2)
            
            grid.addWidget(QLabel("* Input required"), 6 , 2)
                                             
            lbl1 = QLabel('Order number')
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 6, 0)
            grid.addWidget(inkorderEdit, 6, 1)
                                          
            lbl2 = QLabel('Article number')
            lbl2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl2, 7, 0)
            grid.addWidget(artEdit, 7, 1)
            grid.addWidget(QLabel("*"), 7,2)
            
            lbl3 = QLabel('Order quantity')  
            lbl3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl3, 8, 0)
            grid.addWidget(hoevEdit,8, 1)
            grid.addWidget(QLabel("*"), 8,2)
                       
            lbl4 = QLabel('Purchase unit price')  
            lbl4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl4, 9, 0)
            grid.addWidget(prijsEdit,9, 1)
            grid.addWidget(QLabel("*"), 9,2)
            
            lbl5 = QLabel('Delivery starts yyyy-mm-dd')  
            lbl5.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl5, 10, 0)
            grid.addWidget(startEdit, 10, 1)
            grid.addWidget(QLabel("*"),10, 2)
            
            lbl6 = QLabel('Delivery ends yyyy-mm-dd')  
            lbl6.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl6, 11, 0)
            grid.addWidget(endEdit, 11, 1)
                        
            self.setLayout(grid)
            self.setGeometry(600, 300, 150, 150)
    
            applyBtn = QPushButton('Insert')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 12, 2, 1 , 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            sluitBtn = QPushButton('Close')
            sluitBtn.clicked.connect(lambda: sluitRegels(m_email, mlevnr, 0, self))
    
            grid.addWidget(sluitBtn, 12, 1, 1, 1, Qt.AlignRight)
            sluitBtn.setFont(QFont("Arial",10))
            sluitBtn.setFixedWidth(100)
            sluitBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 13, 0, 1, 3, Qt.AlignCenter)
                                                                                            
        def inkorderChanged(self, text):
            logger.warning(">>> Entering inkorderChanged(text=%s)", text, extra={"event.action": "inkorderChanged", "logrite.text": text})
            self.Inkoopordernummer.setText(text)
            logger.debug("<<< Exiting inkorderChanged(text=%s)", text, extra={"event.action": "inkorderChanged", "logrite.text": text})
            
        def artChanged(self,text):
            logger.warning(">>> Entering artChanged(text=%s)", text, extra={"event.action": "artChanged", "logrite.text": text})
            self.BestelregelArtikel.setText(text)
            logger.debug("<<< Exiting artChanged(text=%s)", text, extra={"event.action": "artChanged", "logrite.text": text})
            
        def hoevChanged(self,text):
            logger.warning(">>> Entering hoevChanged(text=%s)", text, extra={"event.action": "hoevChanged", "logrite.text": text})
            self.BestelHoeveelheid.setText(text)
            logger.debug("<<< Exiting hoevChanged(text=%s)", text, extra={"event.action": "hoevChanged", "logrite.text": text})
            
        def prijsChanged(self,text):
            logger.warning(">>> Entering prijsChanged(text=%s)", text, extra={"event.action": "prijsChanged", "logrite.text": text})
            self.Inkoopeenheidsprijs.setText(text)
            logger.debug("<<< Exiting prijsChanged(text=%s)", text, extra={"event.action": "prijsChanged", "logrite.text": text})
        
        def startChanged(self,text):
            logger.warning(">>> Entering startChanged(text=%s)", text, extra={"event.action": "startChanged", "logrite.text": text})
            self.Levering_start.setText(text)
            logger.debug("<<< Exiting startChanged(text=%s)", text, extra={"event.action": "startChanged", "logrite.text": text})
            
        def endChanged(self, text):
            logger.warning(">>> Entering endChanged(text=%s)", text, extra={"event.action": "endChanged", "logrite.text": text})
            self.Levering_end.setText(text)
            logger.debug("<<< Exiting endChanged(text=%s)", text, extra={"event.action": "endChanged", "logrite.text": text})
          
        def returninkorder(self):
            logger.warning(">>> Entering returninkorder()", extra={"event.action": "returninkorder"})
            logger.debug("<<< Exiting returninkorder()", extra={"event.action": "returninkorder"})
            return self.Inkoopordernummer.text()
        
        def returnart(self):
            logger.warning(">>> Entering returnart()", extra={"event.action": "returnart"})
            logger.debug("<<< Exiting returnart()", extra={"event.action": "returnart"})
            return self.BestelregelArtikel.text()
        
        def returnhoev(self):
            logger.warning(">>> Entering returnhoev()", extra={"event.action": "returnhoev"})
            logger.debug("<<< Exiting returnhoev()", extra={"event.action": "returnhoev"})
            return self.BestelHoeveelheid.text()
        
        def returnprijs(self):
            logger.warning(">>> Entering returnprijs()", extra={"event.action": "returnprijs"})
            logger.debug("<<< Exiting returnprijs()", extra={"event.action": "returnprijs"})
            return self.Inkoopeenheidsprijs.text()
        
        def returnstart(self):
            logger.warning(">>> Entering returnstart()", extra={"event.action": "returnstart"})
            logger.debug("<<< Exiting returnstart()", extra={"event.action": "returnstart"})
            return self.Levering_start.text()
        
        def returnend(self):
            logger.warning(">>> Entering returnend()", extra={"event.action": "returnend"})
            logger.debug("<<< Exiting returnend()", extra={"event.action": "returnend"})
            return self.Levering_end.text()
        
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            return [dialog.returnart(), dialog.returnhoev(),\
                    dialog.returnprijs(), dialog.returnstart(), dialog.returnend()]  

    window = Widget()
    data = window.getData() 
    if mregel == 1 and data[0]:
        datum = str(datetime.datetime.now())
        mbestdatum = (datum[0:4]+'-'+datum[8:10]+'-'+datum[5:7])
        metadata = MetaData()
        orders_inkoop = Table('orders_inkoop', metadata,
            Column('orderinkoopID', Integer(), primary_key=True),
            Column('leverancierID', None, ForeignKey('leveranciers.c.leverancierID')),
            Column('besteldatum', String))
        engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
        conn = engine.connect()
        mbestdatum = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))[0:10]
        ins = insert(orders_inkoop).values(orderinkoopID = minkordnr, leverancierID =\
                    mlevnr, besteldatum = mbestdatum)
        conn.execute(ins)
        conn.close
    elif mregel == 0:
        mregel = 1
    if data[0]: 
        martikelnr = int(data[0])
    else:
        martikelnr = 0
    metadata = MetaData()
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('bestelstatus', Boolean))
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    s = select([artikelen]).where(artikelen.c.artikelID == martikelnr)
    rpart=conn.execute(s).first()
    if rpart and rpart[1] == False:
        reedsBesteld()
        inkoopRegels(m_email, rplev, mregel)
    if rpart and data[1] and data[2] and data[3]:
        martikelnr = int(data[0])
        mhoev = float(data[1])
        mprijs = float(data[2])
        mleverstart = data[3]
        if data[4]:
            mlevereind = data[4]
        else:
            mlevereind = data[3]
    else:
        foutArtikel()
        inkoopRegels(m_email, rplev, mregel)
    
    metadata = MetaData()
    orders_inkoop_artikelen = Table('orders_inkoop_artikelen', metadata,
        Column('ordartlevID', Integer(), primary_key=True),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('orderinkoopID', None, ForeignKey('orders_inkoop.order_inkoopID')),
        Column('bestelaantal', Float),
        Column('inkoopprijs', Float),
        Column('levering_start', String),
        Column('levering_eind', String),
        Column('regel', Integer))
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer, primary_key=True),
        Column('bestelsaldo', Float),
        Column('bestelstatus', Boolean),
        Column('art_voorraad', Float),
        Column('reserveringsaldo', Float))
    materiaallijsten = Table('materiaallijsten', metadata,
        Column('matlijstID', Integer, primary_key=True),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('orderinkoopID', Integer),
        Column('hoeveelheid', Float),
        Column('reserverings_datum', String),
        Column('levertijd_begin', String),
        Column('levertijd_end', String))

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    try:
        mordlevnr=(conn.execute(select([func.max(orders_inkoop_artikelen.c.ordartlevID,\
            type_=Integer)])).scalar())
        mordlevnr += 1
    except:
        mordlevnr = 1
    mlevnr = minkgeg[1]
          
    insrgl = insert(orders_inkoop_artikelen).values(ordartlevID = mordlevnr,\
                 orderinkoopID = minkordnr, artikelID = martikelnr,\
                 bestelaantal = mhoev, inkoopprijs = mprijs, levering_start = mleverstart,\
                 levering_eind = mlevereind, regel = mregel)
    conn.execute(insrgl)
    selart1 = select([artikelen]).where(artikelen.c.artikelID == martikelnr)
    rpart1 = conn.execute(selart1).first()
    mressaldo = rpart1[4]
    martvrd = rpart1[3]
    mbestsaldo = rpart1[1]
     
    selmat = select([materiaallijsten]).where(and_(materiaallijsten.c.artikelID == martikelnr,\
            materiaallijsten.c.orderinkoopID == 0))
    rpmat = conn.execute(selmat)
    mbehoefte = martvrd + mbestsaldo +mhoev - mressaldo
    if mbehoefte >= 0:
        if rpart1:
            updart = update(artikelen).where(and_(orders_inkoop_artikelen.c.artikelID == \
                  artikelen.c.artikelID, artikelen.c.artikelID == martikelnr))\
                  .values(bestelsaldo = artikelen.c.bestelsaldo + mhoev, bestelstatus = False)
            conn.execute(updart)
            mregel += 1
        else:
            foutInvoer()
            inkoopRegels(m_email, rplev, mregel)
    for row in rpmat:
        if mbehoefte >= 0:
            updmat = update(materiaallijsten).where(materiaallijsten.c.artikelID\
              == martikelnr).values(orderinkoopID = minkordnr, levertijd_begin\
              = mleverstart, levertijd_end = mlevereind) 
            conn.execute(updmat)
        else:
            if mregel == 1:
                mregel = 0
            onvBesteld(-mbehoefte)
            inkoopRegels(m_email, rplev, mregel)
            
    invoerOk(mregel-1)
    conn.close
    inkoopRegels(m_email, rplev, mregel)