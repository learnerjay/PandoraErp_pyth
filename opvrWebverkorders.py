from login import hoofdMenu
from postcode import checkpostcode
import os, datetime
from PyQt5.QtCore import Qt, QAbstractTableModel, QRegExp
from PyQt5.QtGui import QFont, QPixmap, QIcon, QRegExpValidator
from PyQt5.QtWidgets import  QDialog, QLabel, QGridLayout,\
                             QPushButton, QLineEdit, QWidget, QMessageBox,\
                             QTableView, QComboBox, QCheckBox
from sqlalchemy import (Table, Column, Integer, String, MetaData,\
                         create_engine, Float, ForeignKey)
from sqlalchemy.sql import select, update, and_
import logging
logger = logging.getLogger(__name__)

def refresh(m_email, keuze, zoekterm, afd, self):
    logger.debug(">>> Entering refresh(m_email=%s,keuze=%s,zoekterm=%s,afd=%s)", m_email, keuze, zoekterm, afd)
    self.close()
    bestelOrder(m_email, keuze, zoekterm, afd)
    logger.debug("<<< Exiting refresh(m_email=%s,keuze=%s,zoekterm=%s,afd=%s)", m_email, keuze, zoekterm, afd)

def ongInvoer():
    logger.debug(">>> Entering ongInvoer()")
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Please re-enter incorrect input\nsearch term!')
    msg.setWindowTitle('Request web sales orders')               
    logger.debug("<<< Exiting ongInvoer()")
    msg.exec_() 
    
def geenRecord():
    logger.debug(">>> Entering geenRecord()")
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No record found\ncreate another selection please!')
    msg.setWindowTitle('Request web sales orders')               
    logger.debug("<<< Exiting geenRecord()")
    msg.exec_() 
    
def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)

def geenOrder():
    logger.debug(">>> Entering geenOrder()")
    msg = QMessageBox()
    logger.debug("geenOrder(): msg → %s", msg)
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Web sales order not found!')
    msg.setWindowTitle('Request web sales orders')               
    logger.debug("<<< Exiting geenOrder()")
    msg.exec_()
     
def printing():
    logger.debug(">>> Entering printing()")
    msg = QMessageBox()
    logger.debug("printing(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Information)
    msg.setText('Just a moment, printing starts!')
    msg.setWindowTitle('Request web sales orders')
    logger.debug("<<< Exiting printing()")
    msg.exec_()
    
def printFactuur(rpord,mstraat,mplaats,movbestnr):
    logger.debug(">>> Entering printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s)", rpord, mstraat, mplaats, movbestnr)
    from sys import platform
    metadata = MetaData()
    logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): metadata → %s", rpord, mstraat, mplaats, movbestnr, metadata)
    orders_verkoop_artikelen = Table('orders_verkoop_artikelen', metadata,
        Column('ovaID', Integer, primary_key=True),
        Column('ovbestelID', None, ForeignKey('orders_verkoop.ovbestelID')),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('ovaantal', Integer),
        Column('ovleverdatum', String),
        Column('verkoopprijs', Float),
        Column('regel', Integer),
        Column('retour', Float),
        Column('betaaldatum', String),
        Column('leveringsdatum', String))
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('artikelomschrijving', String),
        Column('artikelprijs', Float),
        Column('art_voorraad', Float),
        Column('art_eenheid', String),
        Column('locatie_magazijn', String))
        
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): engine → %s", rpord, mstraat, mplaats, movbestnr, engine)
    con = engine.connect()
    logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): con → %s", rpord, mstraat, mplaats, movbestnr, con)
    selova = select([orders_verkoop_artikelen,artikelen]).where(and_(\
      orders_verkoop_artikelen.c.ovbestelID == movbestnr, orders_verkoop_artikelen\
      .c.artikelID == artikelen.c.artikelID)).order_by(orders_verkoop_artikelen.c.ovaID)
    rpova = con.execute(selova)
    logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): selova → %s", rpord, mstraat, mplaats, movbestnr, selova)
        
    mblad = 1
    logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): rpova → %s", rpord, mstraat, mplaats, movbestnr, rpova)
    rgl = 0
    if platform == 'win32':
        logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): mblad → %s", rpord, mstraat, mplaats, movbestnr, mblad)
        filename = '.\\forms\\Weborders_Facturen\\Web_order-bill_'+str(rpord[0])+'.txt'
    else:
        filename = './forms/Weborders_Facturen/Web-order_bill_'+str(rpord[0])+'.txt'
        logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): filename → %s", rpord, mstraat, mplaats, movbestnr, filename)
    adreskop=\
    ('\n\n\n\n\n\n\nBill\n\n'+rpord[10]+' '+rpord[11]+' '+rpord[12]+' '+rpord[13]+',\n'+\
     mstraat+' '+rpord[15]+rpord[16]+',\n'+\
     rpord[14]+' '+mplaats+'.\n\n\n\n\n')
    logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): adreskop → %s", rpord, mstraat, mplaats, movbestnr, adreskop)
    kop=\
    ('Order number: '+ str(rpord[0])+'          Date : '+str(datetime.datetime.now())[0:10]+'  Page : '+str(mblad)+'\n'+
    '==============================================================================================\n'+
    'Articlenr  Description                            Unit  Quantity  Price   Subtotal        BTW \n'+
    '==============================================================================================\n')
    logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): kop → %s", rpord, mstraat, mplaats, movbestnr, kop)
    mtotaal = 0
    logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): mtotaal → %s", rpord, mstraat, mplaats, movbestnr, mtotaal)
    
    for row in rpova:
        if rgl == 0 and mblad == 1:
            open(filename, 'w').write(adreskop)
            open(filename, 'a').write(kop)
            rgl = 16
        elif rgl%57 == 0:
            open(filename, 'a').write(kop)
            mblad += 1
        msub = row[3]*row[5]
        logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): msub → %s", rpord, mstraat, mplaats, movbestnr, msub)
        open(filename,'a').write('{:<11d}'.format(row[2])+'{:<37.35s}'.format(row[11])+\
         '{:>6s}'.format(row[14])+' '+'{:>6.2f}'.format(row[3])+'{:>10.2f}'.format(row[5])+\
         ' '+'{:>10.2f}'.format(msub)+' '+'{:>10.2f}'.format(msub*21/121)+'\n')
        mtotaal = mtotaal+msub
        rgl += 1
   
    tail =(\
           
    '----------------------------------------------------------------------------------------------\n'+
    'Total  invoiceamount inclusive 21% VAT                                  '+'{:10.2f}'.format(mtotaal)+' \n'+
    '==============================================================================================\n')    
    open(filename,'a').write(tail)
    if platform == 'win32':
        os.startfile(filename, "print")
    else:
        os.system("lpr "+filename)
    printing()
    logger.debug("<<< Exiting printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s)", rpord, mstraat, mplaats, movbestnr)
    
def printPakbon(rpord,mstraat,mplaats,movbestnr): 
    logger.debug(">>> Entering printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s)", rpord, mstraat, mplaats, movbestnr)
    from sys import platform
    metadata = MetaData()
    logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): metadata → %s", rpord, mstraat, mplaats, movbestnr, metadata)
    orders_verkoop_artikelen = Table('orders_verkoop_artikelen', metadata,
        Column('ovaID', Integer, primary_key=True),
        Column('ovbestelID', None, ForeignKey('orders_verkoop.ovbestelID')),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('ovaantal', Integer),
        Column('ovleverdatum', String),
        Column('verkoopprijs', Float),
        Column('regel', Integer),
        Column('retour', Float),
        Column('betaaldatum', String),
        Column('leveringsdatum', String))
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('artikelomschrijving', String),
        Column('artikelprijs', Float),
        Column('art_voorraad', Float),
        Column('art_eenheid', String),
        Column('locatie_magazijn', String))
        
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): engine → %s", rpord, mstraat, mplaats, movbestnr, engine)
    con = engine.connect()
    logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): con → %s", rpord, mstraat, mplaats, movbestnr, con)
    selova = select([orders_verkoop_artikelen,artikelen]).where(and_(\
      orders_verkoop_artikelen.c.ovbestelID == movbestnr, orders_verkoop_artikelen\
      .c.artikelID == artikelen.c.artikelID)).order_by(orders_verkoop_artikelen.c.ovaID)
    rpova = con.execute(selova)
    logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): selova → %s", rpord, mstraat, mplaats, movbestnr, selova)

    mblad = 1
    logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): rpova → %s", rpord, mstraat, mplaats, movbestnr, rpova)
    rgl = 0
    if platform == 'win32':
        logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): mblad → %s", rpord, mstraat, mplaats, movbestnr, mblad)
        filename = '.\\forms\\Weborders_Pakbonnen\\Web_order_packing_slip_'+str(rpord[0])+'.txt'
    else:
        filename = './forms/Weborders_Pakbonnen/Web_order-packing_slip_'+str(rpord[0])+'.txt'
        logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): filename → %s", rpord, mstraat, mplaats, movbestnr, filename)
    adreskop=\
    ('\n\n\n\n\n\n\nPacking slip\n\n'+rpord[10]+' '+rpord[11]+' '+rpord[12]+' '+rpord[13]+',\n'+\
     mstraat+' '+rpord[15]+rpord[16]+',\n'+\
     rpord[14]+' '+mplaats+'.\n\n\n\n\n')
    logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): adreskop → %s", rpord, mstraat, mplaats, movbestnr, adreskop)
    open(filename,'w').write(adreskop)
    kop=\
    ('Order number '+ str(rpord[0])+'          Date : '+str(datetime.datetime.now())[0:10]+'  Page : '+str(mblad)+'\n'+
    '==============================================================================================\n'+
    'Articlenr  Description                         Unit    Amount  Location   Delivered           \n'+
    '==============================================================================================\n')
    logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): kop → %s", rpord, mstraat, mplaats, movbestnr, kop)
    
    for row in rpova:
        if rgl == 0 and mblad == 1:
            open(filename, 'w').write(adreskop)
            open(filename, 'a').write(kop)
            rgl = 16
        elif rgl%57 == 0:
            open(filename, 'a').write(kop)
            mblad += 1
        open(filename,'a').write('{:<11d}'.format(row[2])+'{:<37.35s}'.format(row[11])+\
           '{:>6s}'.format(row[14])+' '+'{:>6.2f}'.format(row[3])+' '\
           +'{:>8s}'.format(row[15])+'{:>12s}'.format(row[9])+'  ________ \n')
        rgl += 1
    if platform == 'win32':
        os.startfile(filename, "print")
    else:
        os.system("lpr "+filename)
    printing()
    logger.debug("<<< Exiting printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s)", rpord, mstraat, mplaats, movbestnr)
    
def zoekWeborder(m_email, afd):
    logger.debug(">>> Entering zoekWeborder(m_email=%s,afd=%s)", m_email, afd)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            self.setWindowTitle("Request web sales order")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
            
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze)
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit)
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit)
            k0Edit.setFixedWidth(230)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem(' Search sort key')
            k0Edit.addItem('1. All Orders')
            k0Edit.addItem('2. Filtered by Zipcode')
            k0Edit.addItem('3. Filtered by surname')
            k0Edit.addItem('4. Filtered by order number')
            k0Edit.addItem('5. Filtered by order date')
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator)
            logger.debug("__init__(parent=%s): zktrmEdit → %s", parent, zktrmEdit)
            logger.debug("__init__(parent=%s): self.Zoekterm → %s", parent, self.Zoekterm)
            logger.debug("__init__(self=%s,parent=%s): zktrmEdit → %s", self, parent, zktrmEdit)
            k0Edit.activated[str].connect(self.k0Changed)
               
            self.Zoekterm = QLabel()
            zktrmEdit = QLineEdit()
            zktrmEdit.setFixedWidth(220)
            zktrmEdit.setFont(QFont("Arial",10))
            zktrmEdit.textChanged.connect(self.zktrmChanged)
            reg_ex = QRegExp('.*$')
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex)
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex)
            input_validator = QRegExpValidator(reg_ex, zktrmEdit)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator)
            zktrmEdit.setValidator(input_validator)
     
            grid = QGridLayout()
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid)
            logger.debug("__init__(parent=%s): grid → %s", parent, grid)
            grid.setSpacing(20)
                          
            lbl = QLabel()
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl)
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl)
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap)
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 1, 0, 1 ,2)
            
            logo = QLabel()
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 1, 1, 2, Qt.AlignRight)
                                  
            lbl1 = QLabel('Search term')
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1)
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1)
            grid.addWidget(lbl1, 3, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(zktrmEdit, 3, 1, 1, 2)
            grid.addWidget(k0Edit, 2, 1, 1 , 2, Qt.AlignRight)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 5, 0, 1, 3, Qt.AlignCenter)
        
            applyBtn = QPushButton('Search')
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            applyBtn.clicked.connect(self.accept)
                
            grid.addWidget(applyBtn, 4, 2, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            closeBtn = QPushButton('Close')
            logger.debug("__init__(self=%s,parent=%s): closeBtn → %s", self, parent, closeBtn)
            logger.debug("__init__(parent=%s): closeBtn → %s", parent, closeBtn)
            closeBtn.clicked.connect(lambda: windowSluit(self,m_email))
    
            grid.addWidget(closeBtn, 4, 1, 1, 1, Qt.AlignRight)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
            closeBtn.setFont(QFont("Arial",10))
            closeBtn.setFixedWidth(100)
            closeBtn.setStyleSheet("color: black;  background-color: gainsboro")

        def k0Changed(self, text):
            logger.debug(">>> Entering k0Changed(text=%s)", text)
            logger.debug("k0Changed(self=%s,text=%s): Keuze → %s", self, text, Keuze)
            self.Keuze.setText(text)
            logger.debug("<<< Exiting k0Changed(text=%s)", text)
            
        def zktrmChanged(self, text):
            logger.debug(">>> Entering zktrmChanged(text=%s)", text)
            logger.debug("zktrmChanged(self=%s,text=%s): Zoekterm → %s", self, text, Zoekterm)
            self.Zoekterm.setText(text)
            logger.debug("<<< Exiting zktrmChanged(text=%s)", text)
            
        def returnk0(self):
            logger.debug(">>> Entering returnk0()")
            logger.debug("<<< Exiting returnk0()")
            return self.Keuze.text()
        
        def returnzktrmEdit(self):
            logger.debug(">>> Entering returnzktrmEdit()")
            logger.debug("<<< Exiting returnzktrmEdit()")
            return self.Zoekterm.text()
        
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            logger.debug(">>> Entering getData(parent=%s)", parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            logger.debug("<<< Exiting getData(parent=%s)", parent)
            return [dialog.returnk0(), dialog.returnzktrmEdit()] 
        
    window = Widget()
    data = window.getData()
    if not data[0] or data[0][0] == ' ':
        keuze = 0
    elif data[0]:
        keuze = int(data[0][0])
    else:
        keuze = 0
    if data[1]:
        zoekterm = data[1]
    else:
        zoekterm = ''
    bestelOrder(m_email, keuze, zoekterm, afd)
     
def regelsOrder(rpova, afd):
    logger.debug(">>> Entering regelsOrder(rpova=%s,afd=%s)", rpova, afd)
    for rij in rpova:
        class RegelWindow(QDialog):
            logger.debug("<<< Exiting regelsOrder(rpova=%s,afd=%s)", rpova, afd)
            def __init__(self):
                QDialog.__init__(self)
                
                grid = QGridLayout()
                grid.setSpacing(20)
                            
                self.setWindowTitle("Ordering article line")
                self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                
                self.setFont(QFont('Arial', 10))   
                                                  
                self.lbl = QLabel()
                self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                self.lbl.setPixmap(self.pixmap)
                grid.addWidget(self.lbl , 0, 0)
                
                grid.addWidget(QLabel('Ordering article line: ' +str(rij[6])),0, 1, 1, 2)
        
                self.logo = QLabel()
                self.pixmap = QPixmap('./images/logos/logo.jpg')
                self.logo.setPixmap(self.pixmap)
                grid.addWidget(self.logo , 0, 5, 1, 1, Qt.AlignRight) 
                
                lbl1 = QLabel('Order lineID')
                q1Edit = QLineEdit(str(rij[0]))
                q1Edit.setAlignment(Qt.AlignRight)
                q1Edit.setFixedWidth(90)
                q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q1Edit.setDisabled(True)
                
                grid.addWidget(lbl1, 1, 0)
                grid.addWidget(q1Edit, 1,1)
                
                lbl2 = QLabel('Order number')
                q2Edit = QLineEdit(str(rij[1]))
                q2Edit.setFixedWidth(100)
                q2Edit.setAlignment(Qt.AlignRight)
                q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q2Edit.setDisabled(True)
                
                grid.addWidget(lbl2, 1, 2)
                grid.addWidget(q2Edit, 1,3)
                
                lbl3 = QLabel('Article number')
                q3Edit = QLineEdit(str(rij[10]))
                q3Edit.setFixedWidth(100)
                q2Edit.setAlignment(Qt.AlignRight)
                q3Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q3Edit.setDisabled(True)
                
                grid.addWidget(lbl3, 2, 0)
                grid.addWidget(q3Edit, 2,1)
                
                lbl9 = QLabel('Description')
                q9Edit = QLineEdit(str(rij[11]))
                q9Edit.setFixedWidth(350)
                q9Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q9Edit.setDisabled(True)
                
                grid.addWidget(lbl9, 2, 2)
                grid.addWidget(q9Edit, 2, 3, 1 ,3)
                                     
                lbl4 = QLabel('Quantity')
                q4Edit = QLineEdit('{:12.2f}'.format(rij[3]))
                q4Edit.setFixedWidth(100)
                q4Edit.setAlignment(Qt.AlignRight)
                q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q4Edit.setDisabled(True)
                
                grid.addWidget(lbl4, 3, 0)
                grid.addWidget(q4Edit, 3, 1)
                
                lbl5 = QLabel('Selling price')
                q5Edit = QLineEdit('{:12.2f}'.format(rij[5]))
                q5Edit.setFixedWidth(100)
                q5Edit.setAlignment(Qt.AlignRight)
                q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q5Edit.setDisabled(True)
             
                grid.addWidget(lbl5, 3, 2)
                grid.addWidget(q5Edit, 3, 3)
                
                lbl6 = QLabel('Delivery date')
                q6Edit = QLineEdit(str(rij[4]))
                q6Edit.setFixedWidth(100)
                q6Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q6Edit.setDisabled(True)
                
                grid.addWidget(lbl6, 4, 0)
                grid.addWidget(q6Edit, 4, 1)
                
                lbl7 = QLabel('Return delivery')
                q7Edit = QLineEdit('{:12.2f}'.format(rij[7]))
                q7Edit.setFixedWidth(100)
                q7Edit.setAlignment(Qt.AlignRight)
                q7Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q7Edit.setDisabled(True)
                                            
                grid.addWidget(lbl7, 4, 2)
                grid.addWidget(q7Edit, 4, 3)
                          
                lbl8 = QLabel('Payed date')
                q8Edit = QLineEdit(str(rij[8]))
                q8Edit.setFixedWidth(100)
                q8Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q8Edit.setDisabled(True)
                                            
                grid.addWidget(lbl8, 5, 0)
                grid.addWidget(q8Edit, 5, 1)
                
                cBox = QCheckBox('Payment received')
                cBox.stateChanged.connect(self.cBoxChanged)
                if not afd or afd == 2 or rij[8]:
                    cBox.setDisabled(True)
                grid.addWidget(cBox, 5, 2)
                
                lbl9 = QLabel('Delivered date')
                q9Edit = QLineEdit(str(rij[9]))
                q9Edit.setFixedWidth(100)
                q9Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q9Edit.setDisabled(True)
                                            
                grid.addWidget(lbl9, 5, 3)
                grid.addWidget(q9Edit, 5, 4)
                
                cBox1 = QCheckBox('Delivered')
                cBox1.stateChanged.connect(self.cBox1Changed)
                if afd or rij[9] :
                    cBox1.setDisabled(True)
                grid.addWidget(cBox1,5, 5)
                
                regelBtn = QPushButton('Line')
                regelBtn.clicked.connect(self.accept)
        
                grid.addWidget(regelBtn, 6, 5)
                regelBtn.setFont(QFont("Arial",10))
                regelBtn.setFixedWidth(100)
                regelBtn.setStyleSheet("color: black;  background-color: gainsboro")
              
                grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 7, 1, 1, 3, Qt.AlignCenter)
                                                                                                       
                self.setLayout(grid)
                self.setGeometry(250, 300, 150, 150)
                logger.debug(">>> Entering __init__(data_list=%s,header=%s)", data_list, header)
                logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font)
                logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view)
                logger.debug("__init__(data_list=%s,header=%s): grid → %s", data_list, header, grid)
                logger.debug("__init__(self=%s,data_list=%s,header=%s): grid → %s", self, data_list, header, grid)
                logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model)
                logger.debug("__init__(self=%s,data_list=%s,header=%s): table_model → %s", self, data_list, header, table_model)
                logger.debug("__init__(self=%s,data_list=%s,header=%s): table_view → %s", self, data_list, header, table_view)
                logger.debug("__init__(self=%s,data_list=%s,header=%s): font → %s", self, data_list, header, font)
                logger.debug("__init__(data_list=%s,header=%s): pixmap → %s", data_list, header, pixmap)
                logger.debug("__init__(data_list=%s,header=%s): lbl → %s", data_list, header, lbl)
                logger.debug("__init__(self=%s,data_list=%s,header=%s): lbl → %s", self, data_list, header, lbl)
                logger.debug("__init__(self=%s,data_list=%s,header=%s): pixmap → %s", self, data_list, header, pixmap)
                logger.debug("__init__(data_list=%s,header=%s): logo → %s", data_list, header, logo)
                logger.debug("__init__(self=%s,data_list=%s,header=%s): logo → %s", self, data_list, header, logo)
                logger.debug("__init__(data_list=%s,header=%s): freshBtn → %s", data_list, header, freshBtn)
                logger.debug("__init__(self=%s,data_list=%s,header=%s): freshBtn → %s", self, data_list, header, freshBtn)
                logger.debug("__init__(data_list=%s,header=%s): sluitBtn → %s", data_list, header, sluitBtn)
                logger.debug("__init__(self=%s,data_list=%s,header=%s): sluitBtn → %s", self, data_list, header, sluitBtn)
                logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header)
           
            state = False   
            def cBoxChanged(self, state):
                logger.debug(">>> Entering cBoxChanged(state=%s)", state)
                logger.debug("cBoxChanged(state=%s): self.state → %s", state, self.state)
                logger.debug("cBoxChanged(self=%s,state=%s): self.state → %s", self, state, self.state)
                if state == Qt.Checked:
                    self.state = True
                    logger.debug("<<< Exiting cBoxChanged(state=%s)", state)
                    
            def returncBox(self):
                logger.debug(">>> Entering returncBox()")
                logger.debug("<<< Exiting returncBox()")
                return self.state
            
            state1 = False   
            def cBox1Changed(self, state1):
                logger.debug(">>> Entering cBox1Changed(state1=%s)", state1)
                logger.debug("cBox1Changed(self=%s,state1=%s): self.state1 → %s", self, state1, self.state1)
                if state1 == Qt.Checked:
                    logger.debug("<<< Exiting cBox1Changed(state1=%s)", state1)
                    self.state1 = True
                    
            def returncBox1(self):
                logger.debug(">>> Entering returncBox1()")
                logger.debug("<<< Exiting returncBox1()")
                return self.state1
        
            @staticmethod
            def getData(parent=None):
                logger.debug(">>> Entering getData(parent=%s)", parent)
                dialog = RegelWindow()
                dialog.exec_()
                return [dialog.returncBox(), dialog.returncBox1()]
                   
        regelWin = RegelWindow()
        data = regelWin.getData()
        
        metadata = MetaData()
        orders_verkoop_artikelen = Table('orders_verkoop_artikelen', metadata,
            Column('ovaID', Integer, primary_key=True),
            Column('ovbestelID', None, ForeignKey('orders_verkoop.ovbestelID')),
            Column('regel', Integer),
            Column('betaaldatum', String),
            Column('leveringsdatum', String))
          
        engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
        con = engine.connect()
        selb = select([orders_verkoop_artikelen]).where(and_(orders_verkoop_artikelen.\
            c.ovbestelID == rij[1], orders_verkoop_artikelen.c.regel == rij[6]))
        rpb = con.execute(selb).first()
        if data[0] and not rpb[3]:
            up = update(orders_verkoop_artikelen).where(and_(orders_verkoop_artikelen\
             .c.regel == rij[6], orders_verkoop_artikelen.c.ovbestelID == rij[1]))\
             .values(betaaldatum = str(datetime.datetime.now())[0:10]) 
            con.execute(up)
        if data[1] and not rpb[4]:
                upl = update(orders_verkoop_artikelen).where(and_(orders_verkoop_artikelen\
                 .c.regel == rij[6], orders_verkoop_artikelen.c.ovbestelID == rij[1]))\
                 .values(leveringsdatum = str(datetime.datetime.now())[0:10]) 
                con.execute(upl)
        metadata = MetaData()
        orders_verkoop = Table('orders_verkoop', metadata,
            Column('ovbestelID', Integer, primary_key=True),
            Column('datum_betaald', String),
            Column('datum_geleverd', String))
        orders_verkoop_artikelen = Table('orders_verkoop_artikelen', metadata,
            Column('ovaID', Integer, primary_key=True),
            Column('ovbestelID', None, ForeignKey('orders_verkoop.ovbestelID')),
            Column('regel', Integer),
            Column('betaaldatum', String),
            Column('leveringsdatum', String))
        engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
        con = engine.connect()
        selb = select([orders_verkoop, orders_verkoop_artikelen]).where(and_\
            (orders_verkoop_artikelen.c.ovbestelID==rij[1], orders_verkoop_artikelen.\
             c.ovbestelID == orders_verkoop.c.ovbestelID)).order_by\
            (orders_verkoop_artikelen.c.regel.desc())
        rpbal = con.execute(selb)
        rpbmax = con.execute(selb).first()
        mrgl = rpbmax[5]
        mregel = 0
        if not rpbmax[1]:
            for item in rpbal:
                mbet=item[6]
                if mbet:
                    mregel += 1
                    if mrgl == mregel:
                        updbet = update(orders_verkoop).where(orders_verkoop.c.ovbestelID ==\
                         rij[1]).values(datum_betaald = str(datetime.datetime.now())[0:10])
                        con.execute(updbet)
                        rpbal = con.execute(selb)
        mregel1 = 0
        if not rpbmax[2]:
            for item1 in rpbal:
                mlev=item1[7]
                if mlev:
                    mregel1 += 1
                    if mrgl == mregel1:
                        updlev =  update(orders_verkoop).where(orders_verkoop.c.ovbestelID ==\
                         rij[1]).values(datum_geleverd = str(datetime.datetime.now())[0:10])
                        con.execute(updlev)
                                                   
def bestelOrder(m_email, keuze, zoekterm, afd): 
    logger.debug(">>> Entering bestelOrder(m_email=%s,keuze=%s,zoekterm=%s,afd=%s)", m_email, keuze, zoekterm, afd)
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            logger.debug(">>> Entering __init__(data_list=%s,header=%s)", data_list, header)
            QWidget.__init__(self, *args,)
            self.setWindowTitle('Websales orders')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
            self.setFont(QFont('Arial', 10))
            grid = QGridLayout()
            grid.setSpacing(20)
            
            table_model = MyTableModel(self, data_list, header)
            table_view = QTableView()
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.setColumnHidden(1,True)
            table_view.setColumnHidden(6,True)
            table_view.setColumnHidden(9,True)
            table_view.clicked.connect(showSelorder)
            grid.addWidget(table_view, 0, 0, 1, 13)
            
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 1, 0, 1, 2)
       
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 12, 1, 1, Qt.AlignRight)
            
            freshBtn = QPushButton('Refresh')
            freshBtn.clicked.connect(lambda: refresh(m_email, keuze, zoekterm, afd, self))

            freshBtn.setFont(QFont("Arial",10))
            freshBtn.setFixedWidth(100) 
            freshBtn.setStyleSheet("color: black;  background-color: gainsboro")
   
            grid.addWidget(freshBtn, 1, 11, 1, 1, Qt.AlignRight)
            
            sluitBtn = QPushButton('Close')
            sluitBtn.clicked.connect(self.close)

            sluitBtn.setFont(QFont("Arial",10))
            sluitBtn.setFixedWidth(100) 
            sluitBtn.setStyleSheet("color: black;  background-color: gainsboro") 
            
            grid.addWidget(sluitBtn, 1, 10)
          
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 1, 0, 1, 13, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(50, 50, 1500, 900)
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header)
            logger.debug(">>> Entering __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header)
            logger.debug("<<< Exiting __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header)
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.mylist → %s", self, parent, mylist, header, self.mylist)
     
    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.header → %s", self, parent, mylist, header, self.header)
            QAbstractTableModel.__init__(self, parent, *args)
            self.mylist = mylist
            logger.debug(">>> Entering __init__()")
            logger.debug("__init__(): grid → %s", grid)
            logger.debug("__init__(self=%s): grid → %s", self, grid)
            logger.debug("__init__(): self.lbl → %s", self.lbl)
            logger.debug("__init__(): self.pixmap → %s", self.pixmap)
            logger.debug("__init__(self=%s): lbl → %s", self, lbl)
            logger.debug("__init__(): self.logo → %s", self.logo)
            logger.debug("__init__(self=%s): logo → %s", self, logo)
            logger.debug("__init__(): q1Edit → %s", q1Edit)
            logger.debug("__init__(): lbl1 → %s", lbl1)
            logger.debug("__init__(self=%s): lbl1 → %s", self, lbl1)
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit)
            logger.debug("__init__(): q17Edit → %s", q17Edit)
            logger.debug("__init__(): q2Edit → %s", q2Edit)
            logger.debug("__init__(): lbl2 → %s", lbl2)
            logger.debug("__init__(self=%s): lbl2 → %s", self, lbl2)
            logger.debug("__init__(self=%s): q2Edit → %s", self, q2Edit)
            logger.debug("__init__(self=%s): q17Edit → %s", self, q17Edit)
            logger.debug("__init__(): q3Edit → %s", q3Edit)
            logger.debug("__init__(): lbl3 → %s", lbl3)
            logger.debug("__init__(self=%s): lbl3 → %s", self, lbl3)
            logger.debug("__init__(self=%s): q3Edit → %s", self, q3Edit)
            logger.debug("__init__(): q4Edit → %s", q4Edit)
            logger.debug("__init__(): lbl4 → %s", lbl4)
            logger.debug("__init__(self=%s): lbl4 → %s", self, lbl4)
            logger.debug("__init__(self=%s): q4Edit → %s", self, q4Edit)
            logger.debug("__init__(): q5Edit → %s", q5Edit)
            logger.debug("__init__(): lbl5 → %s", lbl5)
            logger.debug("__init__(self=%s): lbl5 → %s", self, lbl5)
            logger.debug("__init__(self=%s): q5Edit → %s", self, q5Edit)
            logger.debug("__init__(): q6Edit → %s", q6Edit)
            logger.debug("__init__(): lbl6 → %s", lbl6)
            logger.debug("__init__(self=%s): lbl6 → %s", self, lbl6)
            logger.debug("__init__(self=%s): q6Edit → %s", self, q6Edit)
            logger.debug("__init__(): q7Edit → %s", q7Edit)
            logger.debug("__init__(): lbl7 → %s", lbl7)
            logger.debug("__init__(self=%s): lbl7 → %s", self, lbl7)
            logger.debug("__init__(self=%s): q7Edit → %s", self, q7Edit)
            logger.debug("__init__(): q8Edit → %s", q8Edit)
            logger.debug("__init__(): lbl8 → %s", lbl8)
            logger.debug("__init__(self=%s): lbl8 → %s", self, lbl8)
            logger.debug("__init__(self=%s): q8Edit → %s", self, q8Edit)
            logger.debug("__init__(): q9Edit → %s", q9Edit)
            logger.debug("__init__(): lbl9 → %s", lbl9)
            logger.debug("__init__(self=%s): lbl9 → %s", self, lbl9)
            logger.debug("__init__(self=%s): q9Edit → %s", self, q9Edit)
            logger.debug("__init__(): q10Edit → %s", q10Edit)
            logger.debug("__init__(): lbl10 → %s", lbl10)
            logger.debug("__init__(self=%s): lbl10 → %s", self, lbl10)
            logger.debug("__init__(self=%s): q10Edit → %s", self, q10Edit)
            logger.debug("__init__(): q11Edit → %s", q11Edit)
            logger.debug("__init__(): lbl11 → %s", lbl11)
            logger.debug("__init__(self=%s): lbl11 → %s", self, lbl11)
            logger.debug("__init__(self=%s): q11Edit → %s", self, q11Edit)
            logger.debug("__init__(): q12Edit → %s", q12Edit)
            logger.debug("__init__(): lbl12 → %s", lbl12)
            logger.debug("__init__(self=%s): lbl12 → %s", self, lbl12)
            logger.debug("__init__(self=%s): q12Edit → %s", self, q12Edit)
            logger.debug("__init__(): q13Edit → %s", q13Edit)
            logger.debug("__init__(): lbl13 → %s", lbl13)
            logger.debug("__init__(self=%s): lbl13 → %s", self, lbl13)
            logger.debug("__init__(self=%s): q13Edit → %s", self, q13Edit)
            logger.debug("__init__(): q14Edit → %s", q14Edit)
            logger.debug("__init__(): lbl14 → %s", lbl14)
            logger.debug("__init__(self=%s): lbl14 → %s", self, lbl14)
            logger.debug("__init__(self=%s): q14Edit → %s", self, q14Edit)
            logger.debug("__init__(): q15Edit → %s", q15Edit)
            logger.debug("__init__(): lbl15 → %s", lbl15)
            logger.debug("__init__(self=%s): lbl15 → %s", self, lbl15)
            logger.debug("__init__(self=%s): q15Edit → %s", self, q15Edit)
            logger.debug("__init__(): q16Edit → %s", q16Edit)
            logger.debug("__init__(): lbl16 → %s", lbl16)
            logger.debug("__init__(self=%s): lbl16 → %s", self, lbl16)
            logger.debug("__init__(self=%s): q16Edit → %s", self, q16Edit)
            logger.debug("__init__(): regelBtn → %s", regelBtn)
            logger.debug("__init__(self=%s): regelBtn → %s", self, regelBtn)
            logger.debug("__init__(): terugBtn → %s", terugBtn)
            logger.debug("__init__(self=%s): terugBtn → %s", self, terugBtn)
            logger.debug("__init__(): pakbonBtn → %s", pakbonBtn)
            logger.debug("__init__(self=%s): pakbonBtn → %s", self, pakbonBtn)
            logger.debug("__init__(): factuurBtn → %s", factuurBtn)
            logger.debug("__init__(self=%s): factuurBtn → %s", self, factuurBtn)
            logger.debug("<<< Exiting __init__()")
            self.header = header
        def rowCount(self, parent):
            logger.debug(">>> Entering rowCount(parent=%s)", parent)
            return len(self.mylist)
        def columnCount(self, parent):
            logger.debug(">>> Entering columnCount(parent=%s)", parent)
            return len(self.mylist[0])
        def data(self, index, role):
            logger.debug(">>> Entering data(index=%s,role=%s)", index, role)
            veld = self.mylist[index.row()][index.column()]
            logger.debug("data(index=%s,role=%s): veld → %s", index, role, veld)
            logger.debug("data(self=%s,index=%s,role=%s): veld → %s", self, index, role, veld)
            if not index.isValid():
                return None
            elif role == Qt.TextAlignmentRole and (type(veld) == float or type(veld) == int):
                return Qt.AlignRight | Qt.AlignVCenter
            elif role != Qt.DisplayRole:
                return None
            if type(veld) == float:
                return '{:12.2f}'.format(veld)
            else:
                logger.debug("<<< Exiting data(index=%s,role=%s)", index, role)
                return veld
        def headerData(self, col, orientation, role):
            logger.debug(">>> Entering headerData(col=%s,orientation=%s,role=%s)", col, orientation, role)
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self.header[col]
            logger.debug("<<< Exiting headerData(col=%s,orientation=%s,role=%s)", col, orientation, role)
            return None
  
    header = ['Order number','-','Order date', 'Payed','Delivered','Total amount','-', 'Account number',\
              'Billing number','-','Prefix', 'First name','Infix', 'Surname',\
              'Zipcode', 'House number', 'Suffix','e-mail address','Telephone']
    
    metadata = MetaData()
    orders_verkoop = Table('orders_verkoop', metadata,
        Column('ovbestelID', Integer, primary_key=True),
        Column('klantID', None, ForeignKey('klanten.klantID')),
        Column('ovbesteldatum', String),
        Column('datum_betaald', String),
        Column('datum_geleverd', String),
        Column('bedrag', Float))
    klanten = Table('klanten', metadata,
        Column('klantID', Integer(), primary_key=True),
        Column('accountID', None, ForeignKey('accounts.accountID')),
        Column('rekening', String))
    accounts = Table('accounts', metadata,
        Column('accountID', Integer(), primary_key=True),
        Column('aanhef', String),
        Column('voornaam', String), 
        Column('tussenvoegsel', String),
        Column('achternaam', String),
        Column('postcode', String),       
        Column('huisnummer', String),
        Column('toevoeging', String),
        Column('email', String),
        Column('telnr', String)) 

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    import validZt  
    if keuze == 1:
        selwo = select([orders_verkoop, klanten, accounts]).where(and_(orders_verkoop\
            .c.klantID == klanten.c.klantID, klanten.c.accountID == accounts\
            .c.accountID)).order_by(orders_verkoop.c.ovbestelID)
    elif keuze == 2 and validZt.zt(zoekterm, 9):
        selwo = select([orders_verkoop, klanten, accounts]).where(and_(orders_verkoop\
            .c.klantID == klanten.c.klantID, klanten.c.accountID == accounts\
            .c.accountID, accounts.c.postcode.ilike(zoekterm+'%')))\
            .order_by(orders_verkoop.c.ovbestelID)
    elif keuze == 3:
        selwo = select([orders_verkoop, klanten, accounts]).where(and_(orders_verkoop\
            .c.klantID == klanten.c.klantID, klanten.c.accountID == accounts\
            .c.accountID, accounts.c.achternaam.ilike('%'+zoekterm+'%')))\
            .order_by(orders_verkoop.c.ovbestelID)
    elif keuze == 4 and validZt.zt(zoekterm, 5):
        selwo = select([orders_verkoop, klanten, accounts]).where(and_(orders_verkoop\
            .c.klantID == klanten.c.klantID, klanten.c.accountID == accounts\
            .c.accountID, orders_verkoop.c.ovbestelID == int(zoekterm)))\
            .order_by(orders_verkoop.c.ovbestelID)
    elif keuze == 5 and validZt.zt(zoekterm, 10):
        selwo = select([orders_verkoop, klanten, accounts]).where(and_(orders_verkoop\
            .c.klantID == klanten.c.klantID, klanten.c.accountID == accounts\
            .c.accountID, orders_verkoop.c.ovbesteldatum.like(zoekterm+'%')))\
            .order_by(orders_verkoop.c.ovbestelID)
    else:
        ongInvoer()
        zoekWeborder(m_email, afd)
    
    if con.execute(selwo).fetchone():
        rpwo = con.execute(selwo)
    else:
        geenRecord()
        zoekWeborder(m_email, afd)
  
    data_list=[]
    for row in rpwo:
        data_list += [(row)]
        
    def showSelorder(idx):
        logger.debug(">>> Entering showSelorder(idx=%s)", idx)
        movbestnr = idx.data()
        logger.debug("showSelorder(idx=%s): movbestnr → %s", idx, movbestnr)
        if idx.column() == 0:
            metadata = MetaData()
            logger.debug("showSelorder(idx=%s): metadata → %s", idx, metadata)
            orders_verkoop = Table('orders_verkoop', metadata,
                Column('ovbestelID', Integer, primary_key=True),
                Column('klantID', None, ForeignKey('klanten.klantID')),
                Column('ovbesteldatum', String),
                Column('bedrag', Float),
                Column('datum_betaald', String),
                Column('datum_geleverd',String))
            klanten = Table('klanten', metadata,
                Column('klantID', Integer(), primary_key=True),
                Column('accountID', None, ForeignKey('accounts.accountID')),
                Column('rekening', String))
            accounts = Table('accounts', metadata,
                Column('accountID', Integer(), primary_key=True),
                Column('aanhef', String),
                Column('voornaam', String), 
                Column('tussenvoegsel', String),
                Column('achternaam', String),
                Column('postcode', String),       
                Column('huisnummer', String),
                Column('toevoeging', String),
                Column('email', String),
                Column('telnr', String)) 
            orders_verkoop_artikelen = Table('orders_verkoop_artikelen', metadata,
                Column('ovaID', Integer, primary_key=True),
                Column('ovbestelID', None, ForeignKey('orders_verkoop.ovbestelID')),
                Column('artikelID', None, ForeignKey('artikelen.artikelID')),
                Column('ovaantal', Integer),
                Column('ovleverdatum', String),
                Column('verkoopprijs', Float),
                Column('regel', Integer),
                Column('retour', Float),
                Column('betaaldatum', String),
                Column('leveringsdatum', String))
            artikelen = Table('artikelen', metadata,
                Column('artikelID', Integer(), primary_key=True),
                Column('artikelomschrijving', String),
                Column('artikelprijs', Float),
                Column('art_voorraad', Float),
                Column('art_eenheid', String),
                Column('locatie_magazijn', String))
            
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showSelorder(idx=%s): engine → %s", idx, engine)
            con = engine.connect()
            
            logger.debug("showSelorder(idx=%s): con → %s", idx, con)
            selord = select([orders_verkoop, klanten, accounts]).where(and_(orders_verkoop\
                .c.ovbestelID == movbestnr, orders_verkoop.c.klantID == klanten.c.klantID,\
                 klanten.c.accountID == accounts.c.accountID))
            rpord = con.execute(selord).first()
            logger.debug("showSelorder(idx=%s): selord → %s", idx, selord)
                 
            selova = select([orders_verkoop_artikelen,artikelen]).where(and_(\
              orders_verkoop_artikelen.c.ovbestelID == movbestnr, orders_verkoop_artikelen\
             .c.artikelID == artikelen.c.artikelID)).order_by(orders_verkoop_artikelen.c.ovaID)
            logger.debug("showSelorder(idx=%s): rpord → %s", idx, rpord)
            rpova = con.execute(selova)
            
            logger.debug("showSelorder(idx=%s): selova → %s", idx, selova)
            mpostcode = rpord[14]
            mhuisnr = int(rpord[15])
            logger.debug("showSelorder(idx=%s): rpova → %s", idx, rpova)
            madres = checkpostcode(mpostcode,mhuisnr)
            mstraat = madres[0]
            logger.debug("showSelorder(idx=%s): mpostcode → %s", idx, mpostcode)
            logger.debug("showSelorder(idx=%s): mhuisnr → %s", idx, mhuisnr)
            mplaats = madres[1]
                 
            class MainWindow(QDialog):
                logger.debug("showSelorder(idx=%s): madres → %s", idx, madres)
                def __init__(self):
                    logger.debug("<<< Exiting showSelorder(idx=%s)", idx)
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                                
                    self.setWindowTitle("Order web articles")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                    
                    self.setFont(QFont('Arial', 10))   
                                                      
                    self.lbl = QLabel()
                    self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                    self.lbl.setPixmap(self.pixmap)
                    grid.addWidget(self.lbl , 0, 0)
                    
                    grid.addWidget(QLabel('Order web articles'),0, 1, 1, 2)
            
                    self.logo = QLabel()
                    self.pixmap = QPixmap('./images/logos/logo.jpg')
                    self.logo.setPixmap(self.pixmap)
                    grid.addWidget(self.logo , 0, 4, 1, 1, Qt.AlignRight) 
                    
                    lbl1 = QLabel('Order number')
                    q1Edit = QLineEdit(str(rpord[0]))
                    q1Edit.setAlignment(Qt.AlignRight)
                    q1Edit.setFixedWidth(90)
                    q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q1Edit.setDisabled(True)
                    
                    grid.addWidget(lbl1, 1, 0)
                    grid.addWidget(q1Edit, 1,1)
                    
                    lbl2 = QLabel('Order / Delivery date')
                    q2Edit = QLineEdit(str(rpord[2]))
                    q2Edit.setFixedWidth(100)
                    q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q2Edit.setDisabled(True)
                    q17Edit = QLineEdit(str(rpord[5]))
                    q17Edit.setFixedWidth(90)
                    q17Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q17Edit.setDisabled(True)
                    
                    grid.addWidget(lbl2, 1, 2)
                    grid.addWidget(q2Edit, 1, 3)
                    grid.addWidget(q17Edit, 1, 4, 1, 1,Qt.AlignRight)
                    
                    lbl3 = QLabel('Total amount')
                    q3Edit = QLineEdit('{:12.2f}'.format(rpord[3]))
                    q3Edit.setFixedWidth(100)
                    q3Edit.setAlignment(Qt.AlignRight)
                    q3Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q3Edit.setDisabled(True)
                    
                    grid.addWidget(lbl3, 2, 0)
                    grid.addWidget(q3Edit, 2,1)
                                         
                    lbl4 = QLabel('Pay date')
                    q4Edit = QLineEdit(rpord[4])
                    q4Edit.setFixedWidth(100)
                    q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q4Edit.setDisabled(True)
                    
                    grid.addWidget(lbl4, 2, 2)
                    grid.addWidget(q4Edit, 2, 3, 1, 2)
                    
                    lbl5 = QLabel('Account number')
                    q5Edit = QLineEdit(str(rpord[7]))
                    q5Edit.setFixedWidth(100)
                    q5Edit.setAlignment(Qt.AlignRight)
                    q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q5Edit.setDisabled(True)
                 
                    grid.addWidget(lbl5, 3, 0)
                    grid.addWidget(q5Edit,3,1)
                    
                    lbl6 = QLabel('Billing number')
                    q6Edit = QLineEdit(str(rpord[8]))
                    q6Edit.setFixedWidth(200)
                    q6Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q6Edit.setDisabled(True)
                    
                    grid.addWidget(lbl6, 3, 2)
                    grid.addWidget(q6Edit, 3, 3, 1 ,2)
                    
                    lbl7 = QLabel('Prefix')
                    q7Edit = QLineEdit(str(rpord[10]))
                    q7Edit.setFixedWidth(100)
                    q7Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q7Edit.setDisabled(True)
                    
                    grid.addWidget(lbl7, 4, 0)
                    grid.addWidget(q7Edit, 4, 1)
                    
                    lbl8 = QLabel('First name')
                    q8Edit = QLineEdit(str(rpord[11]))
                    q8Edit.setFixedWidth(230)
                    q8Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q8Edit.setDisabled(True)
                    
                    grid.addWidget(lbl8, 4, 2)
                    grid.addWidget(q8Edit, 4, 3, 1 ,2)
                    
                    lbl9 = QLabel('Infix')
                    q9Edit = QLineEdit(str(rpord[12]))
                    q9Edit.setFixedWidth(100)
                    q9Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q9Edit.setDisabled(True)
                    
                    grid.addWidget(lbl9, 5, 0)
                    grid.addWidget(q9Edit, 5, 1)
                    
                    lbl10 = QLabel('Surname')
                    q10Edit = QLineEdit(str(rpord[13]))
                    q10Edit.setFixedWidth(230)
                    q10Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q10Edit.setDisabled(True)
                    
                    grid.addWidget(lbl10, 5, 2)
                    grid.addWidget(q10Edit, 5, 3, 1, 2)
                                  
                    lbl11= QLabel('Street name')
                    q11Edit = QLineEdit(mstraat)
                    q11Edit.setFixedWidth(260)
                    q11Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q11Edit.setDisabled(True)
                    
                    grid.addWidget(lbl11, 6, 0)
                    grid.addWidget(q11Edit, 6, 1, 1, 3)
                    
                    lbl12= QLabel('House number')
                    q12Edit = QLineEdit(str(rpord[15])+rpord[16])
                    q12Edit.setFixedWidth(100)
                    q12Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q12Edit.setDisabled(True)
                    
                    grid.addWidget(lbl12, 6, 3)
                    grid.addWidget(q12Edit, 6, 4)
                                                   
                    lbl13= QLabel('Zipcode')
                    q13Edit = QLineEdit(rpord[14])
                    q13Edit.setFixedWidth(70)
                    q13Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q13Edit.setDisabled(True)
                    
                    grid.addWidget(lbl13, 7, 0)
                    grid.addWidget(q13Edit, 7, 1)
                    
                    lbl14= QLabel('Residence')
                    q14Edit = QLineEdit(str(mplaats))
                    q14Edit.setFixedWidth(230)
                    q14Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q14Edit.setDisabled(True)
                    
                    grid.addWidget(lbl14, 7, 2)
                    grid.addWidget(q14Edit, 7, 3, 1 , 2)
                    
                    lbl15= QLabel('E-Mail address')
                    q15Edit = QLineEdit(rpord[17])
                    q15Edit.setFixedWidth(260)
                    q15Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q15Edit.setDisabled(True)
                    
                    grid.addWidget(lbl15, 8, 0)
                    grid.addWidget(q15Edit, 8, 1, 1, 3)
                    
                    lbl16= QLabel('Telephone')
                    q16Edit = QLineEdit(str(rpord[18]))
                    q16Edit.setFixedWidth(100)
                    q16Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q16Edit.setDisabled(True)
                    
                    grid.addWidget(lbl16, 8, 3)
                    grid.addWidget(q16Edit, 8, 3 , 1, 2, Qt.AlignRight)
                    
                    regelBtn = QPushButton('Order lines')
                    regelBtn.clicked.connect(lambda: regelsOrder(rpova, afd))
                            
                    grid.addWidget(regelBtn, 10, 4)
                    regelBtn.setFont(QFont("Arial",10))
                    regelBtn.setFixedWidth(110)
                    regelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    
                    terugBtn = QPushButton('Close')
                    terugBtn.clicked.connect(self.accept)
            
                    grid.addWidget(terugBtn, 10, 3, 1, 1, Qt.AlignRight)
                    terugBtn.setFont(QFont("Arial",10))
                    terugBtn.setFixedWidth(110)
                    terugBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                   
                    pakbonBtn = QPushButton('Printing\nPacking slip')
                    pakbonBtn.clicked.connect(lambda: printPakbon(rpord,mstraat,mplaats,movbestnr))
                           
                    grid.addWidget(pakbonBtn, 9, 4)
                    pakbonBtn.setFont(QFont("Arial",10))
                    pakbonBtn.setFixedWidth(110)
                               
                    factuurBtn = QPushButton('Printing Bill')
                    factuurBtn.clicked.connect(lambda: printFactuur(rpord,mstraat,mplaats,movbestnr))
    
                    grid.addWidget(factuurBtn, 9, 3, 1, 1, Qt.AlignRight)
                    factuurBtn.setFont(QFont("Arial",10))
                    factuurBtn.setFixedWidth(110)
                      
                    if afd == 1:
                        pakbonBtn.setDisabled(True)
                        factuurBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    elif afd == 0:
                        factuurBtn.setDisabled(True)
                        pakbonBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    elif afd == 2:
                        factuurBtn.setDisabled(True)
                        pakbonBtn.setDisabled(True)
                            
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 11, 1, 1, 3, Qt.AlignCenter)
                                                                                                           
                    self.setLayout(grid)
                    self.setGeometry(300, 150, 150, 150)
                         
            mainWin = MainWindow()
            mainWin.exec_()
      
    win = MyWindow(data_list, header)
    win.exec_()
    zoekWeborder(m_email, afd)