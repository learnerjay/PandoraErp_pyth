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
    logger.debug(">>> Entering foutInvoer()")
    msg = QMessageBox()
    logger.debug("foutInvoer(): msg → %s", msg)
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Verplichte Invoer!')
    msg.setWindowTitle('Invoer werkorders')
    logger.debug("<<< Exiting foutInvoer()")
    msg.exec_()
    
def foutLeverancier():
    logger.debug(">>> Entering foutLeverancier()")
    msg = QMessageBox()
    logger.debug("foutLeverancier(): msg → %s", msg)
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))        
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Leverancier niet gevonden!')
    msg.setWindowTitle('INKOOPORDER')
    logger.debug("<<< Exiting foutLeverancier()")
    msg.exec_()

def geenArtnr():
    logger.debug(">>> Entering geenArtnr()")
    msg = QMessageBox()
    logger.debug("geenArtnr(): msg → %s", msg)
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen bestaand artikel gevonden\nNieuw artikelnummer wordt aangemaakt!')
    msg.setWindowTitle('Invoer Artikelnummer')               
    logger.debug("<<< Exiting geenArtnr()")
    msg.exec_() 

def invoerOk(mregel):
    logger.debug(">>> Entering invoerOk(mregel=%s)", mregel)
    msg = QMessageBox()
    logger.debug("invoerOk(mregel=%s): msg → %s", mregel, msg)
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Bestelregel '+str(mregel)+' ingevoerd')
    msg.setWindowTitle('Bestelling regelinkooporder')
    logger.debug("<<< Exiting invoerOk(mregel=%s)", mregel)
    msg.exec_()
    
def reedsBesteld():
    logger.debug(">>> Entering reedsBesteld()")
    msg = QMessageBox()
    logger.debug("reedsBesteld(): msg → %s", msg)
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Dit produkt is in de bestelprocedure\nBestellen is weer mogelijk na uitlevering!')
    msg.setWindowTitle('Bestelling regelinkooporder')
    logger.debug("<<< Exiting reedsBesteld()")
    msg.exec_()
    
def foutArtikel():
    logger.debug(">>> Entering foutArtikel()")
    msg = QMessageBox()
    logger.debug("foutArtikel(): msg → %s", msg)
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Onjuist artikelnummer, of niet alle vereiste gegevens ingevoerd!')
    msg.setWindowTitle('Bestelling regel inkooporder')
    logger.debug("<<< Exiting foutArtikel()")
    msg.exec_()
        
def onvBesteld(aantal):
    logger.debug(">>> Entering onvBesteld(aantal=%s)", aantal)
    msg = QMessageBox()
    logger.debug("onvBesteld(aantal=%s): msg → %s", aantal, msg)
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Er zijn '+str(aantal)+' artikelen minder opgegeven'+
     '\nom in reserveringen minus voorraad te voorzien!'+\
     '\nZie "Voorraadmanagement-Reserveringen"'+\
     '\nVoer de bestelregel opnieuw in met vergrote hoeveelheid!')
    msg.setWindowTitle('Bestelling regel inkooporder')
    logger.debug("<<< Exiting onvBesteld(aantal=%s)", aantal)
    msg.exec_()
  
def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)
    
def sluitRegels(m_email, mlevnr, mregel, self):
    logger.debug(">>> Entering sluitRegels(m_email=%s,mlevnr=%s,mregel=%s)", m_email, mlevnr, mregel)
    self.close()
    zoekLeverancier(m_email, mlevnr, mregel)
    logger.debug("<<< Exiting sluitRegels(m_email=%s,mlevnr=%s,mregel=%s)", m_email, mlevnr, mregel)

def foutLeveranciernr():
    logger.debug(">>> Entering foutLeveranciernr()")
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            msg = QMessageBox()
            msg.setStyleSheet("color: black;  background-color: gainsboro")
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Leverancier niet gevonden!')
            msg.setWindowTitle('Bestelling inkooporder')
            msg.exec_()
            
    window = Widget()
    window.show() 
                
def _11check(mlevnr):
    logger.debug(">>> Entering _11check(mlevnr=%s)", mlevnr)
    number = str(mlevnr)
    logger.debug("_11check(mlevnr=%s): number → %s", mlevnr, number)
    total = 0       
    fullnumber = number                       
    logger.debug("_11check(mlevnr=%s): total → %s", mlevnr, total)
    for i in range(8):
        total += int(fullnumber[i])*(9-i)
        logger.debug("_11check(mlevnr=%s): fullnumber → %s", mlevnr, fullnumber)
        checkdigit = total % 11
    if checkdigit == 10:
        checkdigit = 0
    if checkdigit == int(fullnumber[8]):
        return True
    else:
        logger.debug("<<< Exiting _11check(mlevnr=%s)", mlevnr)
        return False
 
def maak11proef(basisnr):
   logger.debug(">>> Entering maak11proef(basisnr=%s)", basisnr)
   basisnr = str(basisnr)
   basisnr = str((int(basisnr[0:8]))+int(1))
   logger.debug("maak11proef(basisnr=%s): basisnr → %s", basisnr, basisnr)
   total = 0                       
   logger.debug("maak11proef(basisnr=%s): total → %s", basisnr, total)
   for i in range(int(8)):
       total += int(basisnr[i])*(int(9)-i)
   checkdigit = total % 11
   if checkdigit == 10:
            checkdigit = 0
   basisuitnr = basisnr+str(checkdigit)
   logger.debug("maak11proef(basisnr=%s): basisuitnr → %s", basisnr, basisuitnr)
   logger.debug("<<< Exiting maak11proef(basisnr=%s)", basisnr)
   logger.debug("zoekLeverancier(m_email=%s,mlevnr=%s,mregel=%s): leveranciers → %s", m_email, mlevnr, mregel, leveranciers)
   logger.debug("zoekLeverancier(m_email=%s,mlevnr=%s,mregel=%s): engine → %s", m_email, mlevnr, mregel, engine)
   return basisuitnr

def zoekLeverancier(m_email, mlevnr, mregel):
    logger.debug(">>> Entering zoekLeverancier(m_email=%s,mlevnr=%s,mregel=%s)", m_email, mlevnr, mregel)
    metadata = MetaData()
    logger.debug("zoekLeverancier(m_email=%s,mlevnr=%s,mregel=%s): metadata → %s", m_email, mlevnr, mregel, metadata)
    leveranciers = Table('leveranciers', metadata,
        Column('leverancierID', Integer(), primary_key=True),
        Column('bedrijfsnaam', String),
        Column('rechtsvorm', String),
        Column('postcode', String),
        Column('huisnummer', String),
        Column('toevoeging', String))
            
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()

    logger.debug("zoekLeverancier(m_email=%s,mlevnr=%s,mregel=%s): conn → %s", m_email, mlevnr, mregel, conn)
    class Widget(QDialog):
        logger.debug("<<< Exiting zoekLeverancier(m_email=%s,mlevnr=%s,mregel=%s)", m_email, mlevnr, mregel)
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Leverancier zoeken materialen.")
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
     
            grid.addWidget(QLabel('Leverancier'), 2, 1)
            grid.addWidget(levEdit, 2, 2)
       
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
         
            applyBtn = QPushButton('Zoeken')
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
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator)
            logger.debug("__init__(parent=%s): inkorderEdit → %s", parent, inkorderEdit)
            logger.debug("__init__(parent=%s): self.Inkoopordernummer → %s", parent, self.Inkoopordernummer)
            logger.debug("__init__(self=%s,parent=%s): inkorderEdit → %s", self, parent, inkorderEdit)
            logger.debug("__init__(parent=%s): artEdit → %s", parent, artEdit)
            logger.debug("__init__(parent=%s): self.BestelregelArtikel → %s", parent, self.BestelregelArtikel)
            logger.debug("__init__(self=%s,parent=%s): artEdit → %s", self, parent, artEdit)
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex)
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator)
            logger.debug("__init__(parent=%s): hoevEdit → %s", parent, hoevEdit)
            logger.debug("__init__(parent=%s): self.BestelHoeveelheid → %s", parent, self.BestelHoeveelheid)
            logger.debug("__init__(self=%s,parent=%s): hoevEdit → %s", self, parent, hoevEdit)
            logger.debug("__init__(parent=%s): prijsEdit → %s", parent, prijsEdit)
            logger.debug("__init__(parent=%s): self.Inkoopeenheidsprijs → %s", parent, self.Inkoopeenheidsprijs)
            logger.debug("__init__(self=%s,parent=%s): prijsEdit → %s", self, parent, prijsEdit)
            logger.debug("__init__(parent=%s): self.Levering_start → %s", parent, self.Levering_start)
            logger.debug("__init__(parent=%s): startEdit → %s", parent, startEdit)
            logger.debug("__init__(self=%s,parent=%s): startEdit → %s", self, parent, startEdit)
            logger.debug("__init__(parent=%s): self.Levering_end → %s", parent, self.Levering_end)
            logger.debug("__init__(parent=%s): endEdit → %s", parent, endEdit)
            logger.debug("__init__(self=%s,parent=%s): endEdit → %s", self, parent, endEdit)
            logger.debug("__init__(parent=%s): grid → %s", parent, grid)
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid)
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl)
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl)
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1)
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1)
            logger.debug("__init__(parent=%s): lbl2 → %s", parent, lbl2)
            logger.debug("__init__(self=%s,parent=%s): lbl2 → %s", self, parent, lbl2)
            logger.debug("__init__(parent=%s): lbl3 → %s", parent, lbl3)
            logger.debug("__init__(self=%s,parent=%s): lbl3 → %s", self, parent, lbl3)
            logger.debug("__init__(parent=%s): lbl4 → %s", parent, lbl4)
            logger.debug("__init__(self=%s,parent=%s): lbl4 → %s", self, parent, lbl4)
            logger.debug("__init__(parent=%s): lbl5 → %s", parent, lbl5)
            logger.debug("__init__(self=%s,parent=%s): lbl5 → %s", self, parent, lbl5)
            logger.debug("__init__(parent=%s): lbl6 → %s", parent, lbl6)
            logger.debug("__init__(self=%s,parent=%s): lbl6 → %s", self, parent, lbl6)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("__init__(parent=%s): sluitBtn → %s", parent, sluitBtn)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
            logger.debug("__init__(self=%s,parent=%s): sluitBtn → %s", self, parent, sluitBtn)
    
        def levChanged(self, text):
            logger.debug(">>> Entering levChanged(text=%s)", text)
            logger.debug("levChanged(self=%s,text=%s): Leveranciernummer → %s", self, text, Leveranciernummer)
            self.Leveranciernummer.setText(text)
            logger.debug("<<< Exiting levChanged(text=%s)", text)
    
        def returnLeveranciernummer(self):
            logger.debug(">>> Entering returnLeveranciernummer()")
            logger.debug("<<< Exiting returnLeveranciernummer()")
            return self.Leveranciernummer.text()
    
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            logger.debug(">>> Entering getData(parent=%s)", parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            logger.debug("<<< Exiting getData(parent=%s)", parent)
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
    logger.debug(">>> Entering bepaalInkoopOrdernr(mregel=%s)", mregel)
    metadata = MetaData()
    logger.debug("bepaalInkoopOrdernr(mregel=%s): metadata → %s", mregel, metadata)
    orders_inkoop = Table('orders_inkoop', metadata,
        Column('orderinkoopID', Integer, primary_key=True),
        Column('leverancierID', None, ForeignKey('leveranciers.c.leverancierID')))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("bepaalInkoopOrdernr(mregel=%s): engine → %s", mregel, engine)
    conn = engine.connect()
    
    logger.debug("bepaalInkoopOrdernr(mregel=%s): conn → %s", mregel, conn)
    try:
        morderinkoopnr=(conn.execute(select([func.max(orders_inkoop.c.orderinkoopID,\
            type_=Integer)])).scalar())
        logger.debug("bepaalInkoopOrdernr(mregel=%s): morderinkoopnr → %s", mregel, morderinkoopnr)
        logger.debug("bepaalInkoopOrdernr(mregel=%s): type_ → %s", mregel, type_)
        if mregel == 1:
            morderinkoopnr=int(maak11proef(morderinkoopnr))
        conn.close
    except:
        logger.error("Exception in bepaalInkoopOrdernr(mregel=%s)", mregel, exc_info=True)
        if mregel == 1:
            morderinkoopnr = 400000003
    logger.debug("<<< Exiting bepaalInkoopOrdernr(mregel=%s)", mregel)
    return(morderinkoopnr)
   
def Inkooporder(m_email, rplev, mregel):
    logger.debug(">>> Entering Inkooporder(m_email=%s,rplev=%s,mregel=%s)", m_email, rplev, mregel)
    mlevnr = int(rplev[0])
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mlevnr → %s", m_email, rplev, mregel, mlevnr)
    mbedrnaam = rplev[1]
    mrechtsvorm = rplev[2]
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mbedrnaam → %s", m_email, rplev, mregel, mbedrnaam)
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mrechtsvorm → %s", m_email, rplev, mregel, mrechtsvorm)
    mpostcode = rplev[3]
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mpostcode → %s", m_email, rplev, mregel, mpostcode)
    mhuisnr = int(rplev[4])
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mhuisnr → %s", m_email, rplev, mregel, mhuisnr)
    if rplev[5]:
        mtoev = rplev[5]
    else:
        mtoev=''
        logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mtoev → %s", m_email, rplev, mregel, mtoev)
    import postcode
    mstrplts = postcode.checkpostcode(mpostcode, mhuisnr)
    mstraat = mstrplts[0]
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mstrplts → %s", m_email, rplev, mregel, mstrplts)
    mplaats = mstrplts[1]
    minkordnr = bepaalInkoopOrdernr(mregel)
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mstraat → %s", m_email, rplev, mregel, mstraat)
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): minkordnr → %s", m_email, rplev, mregel, minkordnr)
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mplaats → %s", m_email, rplev, mregel, mplaats)
    logger.debug("<<< Exiting Inkooporder(m_email=%s,rplev=%s,mregel=%s)", m_email, rplev, mregel)
    return(minkordnr, mlevnr, mbedrnaam, mrechtsvorm, mstraat, mhuisnr,\
               mtoev, mpostcode, mplaats)
    
def inkoopRegels(m_email, rplev, mregel):
    logger.debug(">>> Entering inkoopRegels(m_email=%s,rplev=%s,mregel=%s)", m_email, rplev, mregel)
    minkgeg = Inkooporder(m_email, rplev, mregel)
    logger.debug("inkoopRegels(m_email=%s,rplev=%s,mregel=%s): minkgeg → %s", m_email, rplev, mregel, minkgeg)
    minkordnr = minkgeg[0]
    mlevnr = minkgeg[1]
    logger.debug("inkoopRegels(m_email=%s,rplev=%s,mregel=%s): minkordnr → %s", m_email, rplev, mregel, minkordnr)
    logger.debug("inkoopRegels(m_email=%s,rplev=%s,mregel=%s): mlevnr → %s", m_email, rplev, mregel, mlevnr)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug("<<< Exiting inkoopRegels(m_email=%s,rplev=%s,mregel=%s)", m_email, rplev, mregel)
            self.setWindowTitle('Bestelregels inkooporder materialen invoeren')
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
            grid.addWidget(QLabel("Artikelen bestellen"), 0, 1)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 2, 1, 1, Qt.AlignRight)
            
            self.setFont(QFont('Arial', 10))
            grid.addWidget(QLabel('Bestelling voor\nLeverancier: '+str(minkgeg[1])+\
              ',\n'+minkgeg[2]+' '+minkgeg[3]+',\n'+minkgeg[4]+' '+str(minkgeg[5])+\
              minkgeg[6]+',\n'+minkgeg[7]+' '+minkgeg[8]+'.\nOrderregel '+str(mregel)), 1, 1, 5, 2)
            
            grid.addWidget(QLabel("* Invoer vereist"), 6 , 2)
                                             
            lbl1 = QLabel('Ordernummer')  
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 6, 0)
            grid.addWidget(inkorderEdit, 6, 1)
                                          
            lbl2 = QLabel('Artikelnummer')  
            lbl2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl2, 7, 0)
            grid.addWidget(artEdit, 7, 1)
            grid.addWidget(QLabel("*"), 7,2)
            
            lbl3 = QLabel('Bestelhoeveelheid')  
            lbl3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl3, 8, 0)
            grid.addWidget(hoevEdit,8, 1)
            grid.addWidget(QLabel("*"), 8,2)
                       
            lbl4 = QLabel('Inkoopeenheidsprijs')  
            lbl4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl4, 9, 0)
            grid.addWidget(prijsEdit,9, 1)
            grid.addWidget(QLabel("*"), 9,2)
            
            lbl5 = QLabel('Levering start jjjj-mm-dd')  
            lbl5.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl5, 10, 0)
            grid.addWidget(startEdit, 10, 1)
            grid.addWidget(QLabel("*"),10, 2)
            
            lbl6 = QLabel('Levering eind jjjj-mm-dd')  
            lbl6.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl6, 11, 0)
            grid.addWidget(endEdit, 11, 1)
                        
            self.setLayout(grid)
            self.setGeometry(600, 300, 150, 150)
    
            applyBtn = QPushButton('Invoeren')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 12, 2, 1 , 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            sluitBtn = QPushButton('Sluiten')
            sluitBtn.clicked.connect(lambda: sluitRegels(m_email, mlevnr, 0, self))
    
            grid.addWidget(sluitBtn, 12, 1, 1, 1, Qt.AlignRight)
            sluitBtn.setFont(QFont("Arial",10))
            sluitBtn.setFixedWidth(100)
            sluitBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 13, 0, 1, 3, Qt.AlignCenter)
                                                                                            
        def inkorderChanged(self, text):
            logger.debug(">>> Entering inkorderChanged(text=%s)", text)
            logger.debug("inkorderChanged(self=%s,text=%s): Inkoopordernummer → %s", self, text, Inkoopordernummer)
            self.Inkoopordernummer.setText(text)
            logger.debug("<<< Exiting inkorderChanged(text=%s)", text)
            
        def artChanged(self,text):
            logger.debug(">>> Entering artChanged(text=%s)", text)
            logger.debug("artChanged(self=%s,text=%s): BestelregelArtikel → %s", self, text, BestelregelArtikel)
            self.BestelregelArtikel.setText(text)
            logger.debug("<<< Exiting artChanged(text=%s)", text)
            
        def hoevChanged(self,text):
            logger.debug(">>> Entering hoevChanged(text=%s)", text)
            logger.debug("hoevChanged(self=%s,text=%s): BestelHoeveelheid → %s", self, text, BestelHoeveelheid)
            self.BestelHoeveelheid.setText(text)
            logger.debug("<<< Exiting hoevChanged(text=%s)", text)
            
        def prijsChanged(self,text):
            logger.debug(">>> Entering prijsChanged(text=%s)", text)
            logger.debug("prijsChanged(self=%s,text=%s): Inkoopeenheidsprijs → %s", self, text, Inkoopeenheidsprijs)
            self.Inkoopeenheidsprijs.setText(text)
            logger.debug("<<< Exiting prijsChanged(text=%s)", text)
        
        def startChanged(self,text):
            logger.debug(">>> Entering startChanged(text=%s)", text)
            logger.debug("startChanged(self=%s,text=%s): Levering_start → %s", self, text, Levering_start)
            self.Levering_start.setText(text)
            logger.debug("<<< Exiting startChanged(text=%s)", text)
            
        def endChanged(self, text):
            logger.debug(">>> Entering endChanged(text=%s)", text)
            logger.debug("endChanged(self=%s,text=%s): Levering_end → %s", self, text, Levering_end)
            self.Levering_end.setText(text)
            logger.debug("<<< Exiting endChanged(text=%s)", text)
          
        def returninkorder(self):
            logger.debug(">>> Entering returninkorder()")
            logger.debug("<<< Exiting returninkorder()")
            return self.Inkoopordernummer.text()
        
        def returnart(self):
            logger.debug(">>> Entering returnart()")
            logger.debug("<<< Exiting returnart()")
            return self.BestelregelArtikel.text()
        
        def returnhoev(self):
            logger.debug(">>> Entering returnhoev()")
            logger.debug("<<< Exiting returnhoev()")
            return self.BestelHoeveelheid.text()
        
        def returnprijs(self):
            logger.debug(">>> Entering returnprijs()")
            logger.debug("<<< Exiting returnprijs()")
            return self.Inkoopeenheidsprijs.text()
        
        def returnstart(self):
            logger.debug(">>> Entering returnstart()")
            logger.debug("<<< Exiting returnstart()")
            return self.Levering_start.text()
        
        def returnend(self):
            logger.debug(">>> Entering returnend()")
            logger.debug("<<< Exiting returnend()")
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