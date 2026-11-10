import datetime
from login import hoofdMenu
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor, QImage, QPainter
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QGridLayout, QDialog,\
                  QWidget,QTableView, QStyledItemDelegate, QMessageBox, QComboBox
from sqlalchemy import (Table, Column, Integer, String, Float, Boolean,\
                     MetaData, create_engine, select, update, and_)
import logging
logger = logging.getLogger(__name__)

def refresh(m_email, keuze, self):
    logger.warning(">>> Entering refresh(m_email=%s,keuze=%s)", m_email, keuze, extra={"event.action": "refresh", "logrite.keuze": keuze})
    self.close()
    jaarVerbruik(m_email, keuze)
    logger.debug("<<< Exiting refresh(m_email=%s,keuze=%s)", m_email, keuze, extra={"event.action": "refresh", "logrite.keuze": keuze})

def artVerwerkt(rpartikelen, mbestgr, minvrd):
    logger.warning(">>> Entering artVerwerkt(rpartikelen=%s,mbestgr=%s,minvrd=%s)", rpartikelen, mbestgr, minvrd, extra={"event.action": "artVerwerkt", "logrite.rpartikelen": rpartikelen, "logrite.mbestgr": mbestgr, "logrite.minvrd": minvrd})
    msg = QMessageBox()
    logger.debug("artVerwerkt(rpartikelen=%s,mbestgr=%s,minvrd=%s): msg → %s", rpartikelen, mbestgr, minvrd, msg, extra={"event.action": "artVerwerkt", "logrite.rpartikelen": rpartikelen, "logrite.mbestgr": mbestgr, "logrite.minvrd": minvrd})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setWindowTitle('Stock control')
    msg.setIcon(QMessageBox.Information)
    msg.setText('Article: '+str(rpartikelen[0])+'\nDescription: '+rpartikelen[1]+'\nMinimum stock changed to '+str(minvrd)+'\nOrder size changed to '+str(mbestgr))
    logger.debug("<<< Exiting artVerwerkt(rpartikelen=%s,mbestgr=%s,minvrd=%s)", rpartikelen, mbestgr, minvrd, extra={"event.action": "artVerwerkt", "logrite.rpartikelen": rpartikelen, "logrite.mbestgr": mbestgr, "logrite.minvrd": minvrd})
    msg.exec_()
    
def bestelStatus():
    logger.warning(">>> Entering bestelStatus()", extra={"event.action": "bestelStatus"})
    msg = QMessageBox()
    logger.debug("bestelStatus(): msg → %s", msg, extra={"event.action": "bestelStatus"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setWindowTitle('Order letter printing')
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Order letter is already processed!')
    logger.debug("<<< Exiting bestelStatus()", extra={"event.action": "bestelStatus"})
    msg.exec_()
    
def handle_paint_request(self, printer):
    logger.warning(">>> Entering handle_paint_request(printer=%s)", printer, extra={"event.action": "handle_paint_request", "logrite.printer": printer})
    painter = QPainter(printer)
    logger.debug("handle_paint_request(printer=%s): painter → %s", printer, painter, extra={"event.action": "handle_paint_request", "logrite.printer": printer})
    logger.debug("handle_paint_request(self=%s,printer=%s): painter → %s", self, printer, painter, extra={"event.action": "handle_paint_request", "logrite.printer": printer})
    painter.setViewport(self.view.rect())
    painter.setWindow(self.view.rect())                        
    self.view.render(painter)
    painter.end()
    logger.debug("<<< Exiting handle_paint_request(printer=%s)", printer, extra={"event.action": "handle_paint_request", "logrite.printer": printer})

def printBrief(rpartikel, bestelhoeveelheid, bestelBtn):
    logger.warning(">>> Entering printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s)", rpartikel, bestelhoeveelheid, bestelBtn, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
    from sys import platform
    vandaag = str(datetime.date.today())[0:10]
    logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): vandaag → %s", rpartikel, bestelhoeveelheid, bestelBtn, vandaag, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
    metadata =  MetaData()
    logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): metadata → %s", rpartikel, bestelhoeveelheid, bestelBtn, metadata, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
    params_system = Table('params_system', metadata,
        Column('systemID', Integer, primary_key=True),
        Column('system_value', Float))
         
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): engine → %s", rpartikel, bestelhoeveelheid, bestelBtn, engine, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
    con = engine.connect()
    logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): con → %s", rpartikel, bestelhoeveelheid, bestelBtn, con, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
    selpar = select([params_system]).where(params_system.c.systemID == 1)
    rppar = con.execute(selpar).first()
    logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): selpar → %s", rpartikel, bestelhoeveelheid, bestelBtn, selpar, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
    logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): rppar → %s", rpartikel, bestelhoeveelheid, bestelBtn, rppar, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
    bestnr = int(rppar[1])
    updpar = update(params_system).where(params_system.c.systemID == 1).values(system_value = int(bestnr+1))
    con.execute(updpar)
    logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): bestnr → %s", rpartikel, bestelhoeveelheid, bestelBtn, bestnr, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
    if rpartikel[9] == 1:
        besteltekst = 'Order size stock controlled: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n'
        logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): updpar → %s", rpartikel, bestelhoeveelheid, bestelBtn, updpar, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
        termijn = ' 3 weeks'
    elif rpartikel[9] == 2:
        besteltekst = 'Order size stock controlled: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n'
        logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): besteltekst → %s", rpartikel, bestelhoeveelheid, bestelBtn, besteltekst, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
        termijn = ' 12 weeks'
        logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): termijn → %s", rpartikel, bestelhoeveelheid, bestelBtn, termijn, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
    elif rpartikel[9] == 3:
        besteltekst = 'Order size stock controlled: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n'
        termijn = ' 26 weeks'
    elif rpartikel[9] == 4:
        besteltekst = 'Order size stock controlled: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n'
        termijn = ' 52 weeks'
    elif rpartikel[9] == 5:
        besteltekst = 'Minimum order size reservation controlled: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n'
        termijn = ' 3 weeks'
    elif rpartikel[9] == 6:
        besteltekst = 'Minimum order size reservation controlled: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n'
        termijn = ' 6 weeks'
    elif rpartikel[9] == 7:
        besteltekst = 'Minimum order size reservation controlled: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n'
        termijn = ' 12 weeks'
    elif rpartikel[9] == 8:
        besteltekst = 'Minimum order size reservation controlled: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n'
        termijn = ' 24 weeks'
    elif rpartikel[9] == 9:
        besteltekst = 'Minimum order size reservation controlled: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n'
        termijn = ' 52 weeks'
    if platform == 'win32':
        filename = '.\\forms\\Intern_Orderbrieven\\Order_letter_number_'+str(bestnr)+'.txt'
    else:
        filename = './forms/Intern_Orderbrieven/Order_letter_number_'+str(bestnr)+'.txt'
    open(filename,"w").write('\n\n\nDate: '+str(vandaag)+'\n')
    gegevens = ('\n\n'+\
    'Internal order slip serial number: '+str(bestnr)+'\n\n\n\n'+\
    'Order letter for warehouse item: '+str(rpartikel[0])+'\n\n'+\
    'Article description: '+str(rpartikel[1])+'\n\n'+\
    'Article price including surcharges: '+'{:12.2f}'.format(rpartikel[2])+'\n\n'+\
    'Article stock : '+'{:12.2f}'.format(rpartikel[3])+'\n\n'+\
    'Article unit: '+str(rpartikel[4])+'\n\n'+\
    'Article miminimum stock:  '+'{:12.2f}'.format(rpartikel[5])+'\n\n'+\
    'Order balance: '+'{:12.2f}'.format(rpartikel[6])+'\n\n'+\
    'Order status: '+str(rpartikel[7])+'\n\n'+\
    'Reservation balance: '+'{:12.2f}'.format(rpartikel[8])+'\n\n'+\
    'Category: '+str(rpartikel[9])+'\n\n'+\
    str(besteltekst)+'Delivery term : '+str(termijn)+'\n\n')
    open(filename,"a").write(gegevens+'\n')

    class Window(QDialog):
        logger.debug("<<< Exiting printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s)", rpartikel, bestelhoeveelheid, bestelBtn, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
        def __init__(self):
            logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
            QDialog.__init__(self)
            self.setWindowTitle("Printing internal order letter")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                                                  Qt.WindowMinMaxButtonsHint)
            self.setFont(QFont('Arial', 10))
            self.view = QLabel(self)
            self.view = self.create_view()
            logger.debug("__init__(): self.view → %s", self.view, extra={"event.action": "__init__"})
            layout = QGridLayout(self)
            logger.debug("__init__(): layout → %s", layout, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): layout → %s", self, layout, extra={"event.action": "__init__"})
            logger.debug("__init__(): printer → %s", printer, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): printer → %s", self, printer, extra={"event.action": "__init__"})
            logger.debug("__init__(): dialog → %s", dialog, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): dialog → %s", self, dialog, extra={"event.action": "__init__"})
            layout.addWidget(self.view, 0, 0, 1, 2)
            printer = QPrinter(QPrinter.HighResolution)
            #printer.setPageMargins(12, 16, 12, 20, QPrinter.Millimeter)
            dialog = QPrintDialog(printer, self)
            if dialog.exec_() == QPrintDialog.Accepted:
                handle_paint_request(self, printer)
                logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})
       
        def create_view(self):
            logger.warning(">>> Entering create_view()", extra={"event.action": "create_view"})
            lblinfo = QLabel(
        '\n\n\n'+\
        'Date: '+str(vandaag)+'\n\n\n'+\
        'Internal order letter serial number: '+str(bestnr)+'\n\n\n\n'+\
        'Order letter for warehouse article: '+str(rpartikel[0])+'\n\n'+\
        'Article description: '+rpartikel[1]+'\n\n'+\
        'Article price including surcharges: '+'{:12.2f}'.format(rpartikel[2])+'\n\n'+\
        'Article stock : '+'{:12.2f}'.format(rpartikel[3])+'\n\n'+\
        'Article unit: '+rpartikel[4]+'\n\n'+
        'Article miminimum stock:  '+'{:12.2f}'.format(rpartikel[5])+'\n\n'+\
        'Order balance: '+'{:12.2f}'.format(rpartikel[6])+'\n\n'+\
        'Order status: '+str(rpartikel[7])+'\n\n'+\
        'Reservation balance: '+'{:12.2f}'.format(rpartikel[8])+'\n\n'+\
        'Category: '+str(rpartikel[9])+'\n\n'+\
        besteltekst+\
        'Delivery term: ' + termijn)
            
            if platform == 'win32':
                lblinfo.setStyleSheet("font: 72pt 'Comic Sans MS'")
            else:
                lblinfo.setStyleSheet("font: 144pt 'Comic Sans MS'")
            return(lblinfo)
         
    Window()
            
def bestelBrief(rpartikel, bestelhoeveelheid, bestelBtn):
    logger.warning(">>> Entering bestelBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s)", rpartikel, bestelhoeveelheid, bestelBtn, extra={"event.action": "bestelBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
    metadata = MetaData()
    logger.debug("bestelBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): metadata → %s", rpartikel, bestelhoeveelheid, bestelBtn, metadata, extra={"event.action": "bestelBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('bestelstatus', Boolean),
        Column('bestelsaldo', Float))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("bestelBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): engine → %s", rpartikel, bestelhoeveelheid, bestelBtn, engine, extra={"event.action": "bestelBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
    con = engine.connect()
    logger.debug("bestelBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): con → %s", rpartikel, bestelhoeveelheid, bestelBtn, con, extra={"event.action": "bestelBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
    if rpartikel[7]:
        updart = update(artikelen).where(artikelen.c.artikelID == rpartikel[0])\
        .values(bestelstatus = False, bestelsaldo = artikelen.c.bestelsaldo+bestelhoeveelheid)
        logger.debug("bestelBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): updart → %s", rpartikel, bestelhoeveelheid, bestelBtn, updart, extra={"event.action": "bestelBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
        con.execute(updart)
        bestelBtn.setDisabled(True)
        logger.debug("bestelBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): bestelBtn → %s", rpartikel, bestelhoeveelheid, bestelBtn, bestelBtn, extra={"event.action": "bestelBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})
        printBrief(rpartikel, bestelhoeveelheid, bestelBtn)
    else:
        bestelStatus()
        logger.debug("<<< Exiting bestelBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s)", rpartikel, bestelhoeveelheid, bestelBtn, extra={"event.action": "bestelBrief", "logrite.rpartikel": rpartikel, "logrite.bestelhoeveelheid": bestelhoeveelheid, "logrite.bestelBtn": bestelBtn})

def vrdKeuze(m_email):
    logger.warning(">>> Entering vrdKeuze(m_email=%s)", m_email, extra={"event.action": "vrdKeuze"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Requesting articles")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Keuze = QLabel()
            k0Edit = QComboBox()
            k0Edit.setFixedWidth(280)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('                  Your choice ')
            k0Edit.addItem('1. By reservation to order')
            k0Edit.addItem('2. By minimum stock to order')
            k0Edit.addItem('3. Articles on order')
   
            k0Edit.activated[str].connect(self.k0Changed)
              
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
                                  
            grid.addWidget(k0Edit, 1, 0 ,1, 2, Qt.AlignRight)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1 , 2, Qt.AlignCenter)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1 ,1, Qt.AlignRight)
    
            applyBtn = QPushButton('Search')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 3, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
              
            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: windowSluit(self,m_email))
    
            grid.addWidget(cancelBtn, 3, 0, 1, 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
        
        def k0Changed(self, text):
            logger.warning(">>> Entering k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            self.Keuze.setText(text)
            logger.debug("<<< Exiting k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            
        def returnk0(self):
            logger.warning(">>> Entering returnk0()", extra={"event.action": "returnk0"})
            logger.debug("<<< Exiting returnk0()", extra={"event.action": "returnk0"})
            return self.Keuze.text()
       
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnk0()] 
        
    window = Widget()
    data = window.getData()
    if not data[0] or data[0][0] == ' ':
        vrdKeuze(m_email)
    elif data[0]:
        keuze = int(data[0][0])
        jaarVerbruik(m_email, keuze)
    else:
        vrdKeuze(m_email)
  
def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})

def jaarVerbruik(m_email, keuze):
    logger.warning(">>> Entering jaarVerbruik(m_email=%s,keuze=%s)", m_email, keuze, extra={"event.action": "jaarVerbruik", "logrite.keuze": keuze})
    metadata = MetaData()
    logger.debug("jaarVerbruik(m_email=%s,keuze=%s): metadata → %s", m_email, keuze, metadata, extra={"event.action": "jaarVerbruik", "logrite.keuze": keuze})
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('artikelomschrijving', String),
        Column('artikelprijs', Float),
        Column('art_voorraad', Float),
        Column('art_eenheid', String),
        Column('art_min_voorraad', Float),
        Column('bestelsaldo', Float),
        Column('bestelstatus', Boolean),
        Column('reserveringsaldo', Float),
        Column('categorie', Integer),
        Column('thumb_artikel', String),
        Column('art_bestelgrootte', Float),
        Column('jaarverbruik_1', Float),
        Column('jaarverbruik_2', Float))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("jaarVerbruik(m_email=%s,keuze=%s): engine → %s", m_email, keuze, engine, extra={"event.action": "jaarVerbruik", "logrite.keuze": keuze})
    conn = engine.connect()
    logger.debug("jaarVerbruik(m_email=%s,keuze=%s): conn → %s", m_email, keuze, conn, extra={"event.action": "jaarVerbruik", "logrite.keuze": keuze})
            
    if keuze == 1:
        sel = select([artikelen]).where(and_(artikelen.c.art_voorraad + artikelen.c.bestelsaldo\
            < artikelen.c.reserveringsaldo, artikelen.c.categorie > 4)).order_by(artikelen.c.artikelID)
    elif keuze == 2:
        sel = select([artikelen]).where(and_(artikelen.c.art_voorraad+artikelen.c.bestelsaldo\
            < artikelen.c.art_min_voorraad, artikelen.c.categorie < 5)).order_by(artikelen.c.artikelID)
    elif keuze == 3:
        sel = select([artikelen]).where(artikelen.c.bestelstatus == False)
        logger.debug("jaarVerbruik(m_email=%s,keuze=%s): sel → %s", m_email, keuze, sel, extra={"event.action": "jaarVerbruik", "logrite.keuze": keuze})
          
    rpartikelen = conn.execute(sel)
    logger.debug("jaarVerbruik(m_email=%s,keuze=%s): rpartikelen → %s", m_email, keuze, rpartikelen, extra={"event.action": "jaarVerbruik", "logrite.keuze": keuze})
   
    class MyWindow(QDialog):
        logger.debug("<<< Exiting jaarVerbruik(m_email=%s,keuze=%s)", m_email, keuze, extra={"event.action": "jaarVerbruik", "logrite.keuze": keuze})
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setGeometry(100, 50, 1800, 900)
            self.setWindowTitle('Annual consumption last year')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
            self.setFont(QFont('Arial', 10))
            grid = QGridLayout()
            logger.debug("__init__(data_list=%s,header=%s): grid → %s", data_list, header, grid, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): grid → %s", self, data_list, header, grid, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_model → %s", self, data_list, header, table_model, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_view → %s", self, data_list, header, table_view, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): font → %s", self, data_list, header, font, extra={"event.action": "__init__", "logrite.data_list": data_list})
            grid.setSpacing(20)
            table_model = MyTableModel(self, data_list, header)
            table_view = QTableView()
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.setItemDelegateForColumn(10, showImage(self))
            table_view.setColumnWidth(10, 100)
            table_view.verticalHeader().setDefaultSectionSize(75)
            table_view.clicked.connect(aanpMinvoorraad)
            grid.addWidget(table_view, 0, 0, 1, 16)
            
            lbl = QLabel()
            logger.debug("__init__(data_list=%s,header=%s): lbl → %s", data_list, header, lbl, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): lbl → %s", self, data_list, header, lbl, extra={"event.action": "__init__", "logrite.data_list": data_list})
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(self=%s,data_list=%s,header=%s): pixmap → %s", self, data_list, header, pixmap, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): pixmap → %s", data_list, header, pixmap, extra={"event.action": "__init__", "logrite.data_list": data_list})
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 1, 0, 1, 2)
       
            logo = QLabel()
            logger.debug("__init__(data_list=%s,header=%s): logo → %s", data_list, header, logo, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): logo → %s", self, data_list, header, logo, extra={"event.action": "__init__", "logrite.data_list": data_list})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 15, 1, 1, Qt.AlignRight)
            
            freshBtn = QPushButton('Refresh')
            logger.debug("__init__(data_list=%s,header=%s): freshBtn → %s", data_list, header, freshBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): freshBtn → %s", self, data_list, header, freshBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            freshBtn.clicked.connect(lambda: refresh(m_email, keuze, self))

            freshBtn.setFont(QFont("Arial",10))
            freshBtn.setFixedWidth(100) 
            freshBtn.setStyleSheet("color: black;  background-color: gainsboro")
   
            grid.addWidget(freshBtn, 1, 14, 1, 1, Qt.AlignRight)
        
            sluitBtn = QPushButton('Close')
            logger.debug("__init__(data_list=%s,header=%s): sluitBtn → %s", data_list, header, sluitBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): sluitBtn → %s", self, data_list, header, sluitBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            sluitBtn.clicked.connect(self.close)

            sluitBtn.setFont(QFont("Arial",10))
            sluitBtn.setFixedWidth(100) 
            sluitBtn.setStyleSheet("color: black;  background-color: gainsboro") 
            
            grid.addWidget(sluitBtn, 1, 13, 1, 1, Qt.AlignRight)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 1, 0, 1, 16, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(50, 50, 1800, 900)
            self.setLayout(grid)
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})


    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            logger.warning(">>> Entering __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.mylist → %s", self, parent, mylist, header, self.mylist, extra={"event.action": "__init__", "logrite.mylist": mylist})
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.header → %s", self, parent, mylist, header, self.header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            QAbstractTableModel.__init__(self, parent, *args)
            logger.debug("<<< Exiting __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            self.mylist = mylist
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.header = header
        def rowCount(self, parent):
            logger.warning(">>> Entering rowCount(parent=%s)", parent, extra={"event.action": "rowCount"})
            return len(self.mylist)
        def columnCount(self, parent):
            logger.warning(">>> Entering columnCount(parent=%s)", parent, extra={"event.action": "columnCount"})
            return len(self.mylist[0])
        def data(self, index, role):
            logger.warning(">>> Entering data(index=%s,role=%s)", index, role, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
            veld = self.mylist[index.row()][index.column()]
            logger.debug("data(index=%s,role=%s): veld → %s", index, role, veld, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
            logger.debug("data(self=%s,index=%s,role=%s): veld → %s", self, index, role, veld, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
            if not index.isValid():
                return None
            #elif index.column() == 9 and role == Qt.DecorationRole: # alternatief picture echter
            #    return QPixmap(index.data())                        # met tekst rechts van path
            elif role == Qt.TextAlignmentRole and (type(veld) == float or type(veld) == int):
                return Qt.AlignRight | Qt.AlignVCenter
            elif role != Qt.DisplayRole:
                return None
            if type(veld) == float:
                return '{:12.2f}'.format(veld)
            else:
                logger.debug("<<< Exiting data(index=%s,role=%s)", index, role, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
                return veld
        def headerData(self, col, orientation, role):
            logger.warning(">>> Entering headerData(col=%s,orientation=%s,role=%s)", col, orientation, role, extra={"event.action": "headerData", "logrite.col": col, "logrite.orientation": orientation, "logrite.role": role})
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self.header[col]
            logger.debug("<<< Exiting headerData(col=%s,orientation=%s,role=%s)", col, orientation, role, extra={"event.action": "headerData", "logrite.col": col, "logrite.orientation": orientation, "logrite.role": role})
            return None
       
    class showImage(QStyledItemDelegate):  
           def __init__(self, parent):
               logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): self.Artikelnummer → %s", parent, self.Artikelnummer, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): q1Edit → %s", parent, q1Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): q1Edit → %s", self, parent, q1Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): self.Artikelomschrijving → %s", parent, self.Artikelomschrijving, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): self.Artikelprijs → %s", parent, self.Artikelprijs, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): self.Artikelvoorraad → %s", parent, self.Artikelvoorraad, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): self.Artikeleenheid → %s", parent, self.Artikeleenheid, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): self.Minimumvoorraad → %s", parent, self.Minimumvoorraad, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): q6Edit → %s", parent, q6Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): q6Edit → %s", self, parent, q6Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): self.Bestelsaldo → %s", parent, self.Bestelsaldo, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): q16Edit → %s", parent, q16Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): q16Edit → %s", self, parent, q16Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): self.Bestelstatus → %s", parent, self.Bestelstatus, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): q7Edit → %s", parent, q7Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): q7Edit → %s", self, parent, q7Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): self.Reserveringsaldo → %s", parent, self.Reserveringsaldo, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): q12Edit → %s", parent, q12Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): q12Edit → %s", self, parent, q12Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): self.Categorie → %s", parent, self.Categorie, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): self.Bestelgrootte → %s", parent, self.Bestelgrootte, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): q9Edit → %s", parent, q9Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): q9Edit → %s", self, parent, q9Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): self.Jaarverbruik → %s", parent, self.Jaarverbruik, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): q13Edit → %s", parent, q13Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): q13Edit → %s", self, parent, q13Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): bestelhoeveelheid → %s", self, parent, bestelhoeveelheid, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): lbl2 → %s", parent, lbl2, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): lbl2 → %s", self, parent, lbl2, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): bestelBtn → %s", parent, bestelBtn, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): bestelBtn → %s", self, parent, bestelBtn, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
               logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
               QStyledItemDelegate.__init__(self, parent)
           def paint(self, painter, option, index):        
                logger.warning(">>> Entering paint(painter=%s,option=%s,index=%s)", painter, option, index, extra={"event.action": "paint", "logrite.painter": painter, "logrite.option": option, "logrite.index": index})
                painter.fillRect(option.rect,QColor(255,255,255))
                image = QImage(index.data())
                logger.debug("paint(painter=%s,option=%s,index=%s): image → %s", painter, option, index, image, extra={"event.action": "paint", "logrite.painter": painter, "logrite.option": option, "logrite.index": index})
                logger.debug("paint(self=%s,painter=%s,option=%s,index=%s): image → %s", self, painter, option, index, image, extra={"event.action": "paint", "logrite.painter": painter, "logrite.option": option, "logrite.index": index})
                pixmap = QPixmap(image)
                logger.debug("paint(painter=%s,option=%s,index=%s): pixmap → %s", painter, option, index, pixmap, extra={"event.action": "paint", "logrite.painter": painter, "logrite.option": option, "logrite.index": index})
                logger.debug("paint(self=%s,painter=%s,option=%s,index=%s): pixmap → %s", self, painter, option, index, pixmap, extra={"event.action": "paint", "logrite.painter": painter, "logrite.option": option, "logrite.index": index})
                pixmap.scaled(256,256) 
                logger.debug("<<< Exiting paint(painter=%s,option=%s,index=%s)", painter, option, index, extra={"event.action": "paint", "logrite.painter": painter, "logrite.option": option, "logrite.index": index})
                return(painter.drawPixmap(option.rect, pixmap))
                                       
    header = ['Article number', 'Description', 'Price', 'Stock', 'Unit','Minimum stock',\
              'Order balance', 'Order status', 'Reservation balance', 'Category', 'Image',\
              'To order','Annual consumption-1', 'Annual consumption-2']
        
    data_list=[]
    for row in rpartikelen:
        data_list += [(row)] 
        
    def aanpMinvoorraad(idx):
        logger.warning(">>> Entering aanpMinvoorraad(idx=%s)", idx, extra={"event.action": "aanpMinvoorraad", "logrite.idx": idx})
        martikelnr = idx.data()
        logger.debug("aanpMinvoorraad(idx=%s): martikelnr → %s", idx, martikelnr, extra={"event.action": "aanpMinvoorraad", "logrite.idx": idx})
        if idx.column() == 0:
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("aanpMinvoorraad(idx=%s): engine → %s", idx, engine, extra={"event.action": "aanpMinvoorraad", "logrite.idx": idx})
            con = engine.connect()
            sel = select([artikelen]).where(artikelen.c.artikelID == martikelnr)
            logger.debug("aanpMinvoorraad(idx=%s): con → %s", idx, con, extra={"event.action": "aanpMinvoorraad", "logrite.idx": idx})
            rpartikel = con.execute(sel).first() 
            mjaar = int(str(datetime.datetime.now())[0:4])
            logger.debug("aanpMinvoorraad(idx=%s): sel → %s", idx, sel, extra={"event.action": "aanpMinvoorraad", "logrite.idx": idx})
            logger.debug("aanpMinvoorraad(idx=%s): rpartikel → %s", idx, rpartikel, extra={"event.action": "aanpMinvoorraad", "logrite.idx": idx})
                             
            class Widget(QDialog):
                logger.debug("<<< Exiting aanpMinvoorraad(idx=%s)", idx, extra={"event.action": "aanpMinvoorraad", "logrite.idx": idx})
                def __init__(self, parent=None):
                    super(Widget, self).__init__(parent)
                
                    self.setWindowTitle("Adjust minimum stock / order size")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                                
                    self.setFont(QFont('Arial', 10))
                               
                    self.Artikelnummer = QLabel()
                    q1Edit = QLineEdit(str(rpartikel[0]))
                    q1Edit.setFixedWidth(100)
                    q1Edit.setAlignment(Qt.AlignRight)
                    q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q1Edit.setDisabled(True)
                                    
                    self.Artikelomschrijving = QLabel()
                    q2Edit = QLineEdit(str(rpartikel[1]))
                    q2Edit.setFixedWidth(400)
                    q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q2Edit.setDisabled(True)
                    
                    self.Artikelprijs = QLabel()
                    q3Edit = QLineEdit('{:12.2f}'.format(rpartikel[2]))
                    q3Edit.setFixedWidth(100)
                    q3Edit.setAlignment(Qt.AlignRight)
                    q3Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q3Edit.setDisabled(True)
                                    
                    self.Artikelvoorraad = QLabel()
                    q4Edit = QLineEdit('{:12.2f}'.format(rpartikel[3]))
                    q4Edit.setFixedWidth(100)
                    q4Edit.setAlignment(Qt.AlignRight)
                    q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q4Edit.setDisabled(True)
                    
                    self.Artikeleenheid = QLabel()
                    q5Edit = QLineEdit(rpartikel[4])
                    q5Edit.setFixedWidth(100)
                    q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q5Edit.setDisabled(True)
                    
                    self.Minimumvoorraad = QLabel()
                    q6Edit = QLineEdit('{:12.2f}'.format(rpartikel[5]))
                    q6Edit.setFixedWidth(100)
                    q6Edit.setAlignment(Qt.AlignRight)
                    q6Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q6Edit.setDisabled(True)
                     
                    self.Bestelsaldo = QLabel()
                    q16Edit = QLineEdit('{:12.2f}'.format(rpartikel[6]))
                    q16Edit.setFixedWidth(100)
                    q16Edit.setAlignment(Qt.AlignRight)
                    q16Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q16Edit.setDisabled(True)
    
                    self.Bestelstatus = QLabel()
                    q7Edit = QLineEdit(str(rpartikel[7]))
                    q7Edit.setFixedWidth(100)
                    q7Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q7Edit.setDisabled(True)
                    
                    self.Reserveringsaldo = QLabel()
                    q12Edit = QLineEdit('{:12.2f}'.format(rpartikel[8]))
                    q12Edit.setFixedWidth(100)
                    q12Edit.setAlignment(Qt.AlignRight)
                    q12Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q12Edit.setDisabled(True)
                                   
                    self.Categorie = QLabel()
                    q8Edit = QLineEdit(str(rpartikel[9]))
                    q8Edit.setFixedWidth(100)
                    q8Edit.setAlignment(Qt.AlignRight)
                    q8Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q8Edit.setDisabled(True)
 
                    self.Bestelgrootte = QLabel()
                    q9Edit = QLineEdit('{:12.2f}'.format(rpartikel[11]))
                    q9Edit.setFixedWidth(100)
                    q9Edit.setAlignment(Qt.AlignRight)
                    q9Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q9Edit.setDisabled(True)
                          
                    if mjaar%2 == 1:
                        self.Jaarverbruik = QLabel()
                        q13Edit = QLineEdit('{:12.2f}'.format(rpartikel[12]))
                        q13Edit.setFixedWidth(100)
                        q13Edit.setAlignment(Qt.AlignRight)
                        q13Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                        q13Edit.setDisabled(True) 
                    else:
                        self.Jaarverbruik = QLabel()
                        q13Edit = QLineEdit('{:12.2f}'.format(rpartikel[13]))
                        q13Edit.setFixedWidth(100)
                        q13Edit.setAlignment(Qt.AlignRight)
                        q13Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                        q13Edit.setDisabled(True)  
                         
                    grid = QGridLayout()
                    grid.setSpacing(20)
                
                    lbl = QLabel()
                    pixmap = QPixmap('./images/logos/verbinding.jpg')
                    lbl.setPixmap(pixmap)
                    grid.addWidget(lbl , 0, 0, 1, 2)
                
                    logo = QLabel()
                    pixmap = QPixmap('./images/logos/logo.jpg')
                    logo.setPixmap(pixmap)
                    grid.addWidget(logo , 0, 2, 1, 3, Qt.AlignRight) 
                  
                    grid.addWidget(QLabel('Article number'), 1, 0, 2, 1)
                    grid.addWidget(q1Edit, 1, 1, 2, 1)
                
                    grid.addWidget(QLabel('Article description'), 3, 0)
                    grid.addWidget(q2Edit, 3, 1, 1 ,3)
                    
                    grid.addWidget(QLabel('Unit'), 5, 0)
                    grid.addWidget(q5Edit, 5, 1)
                    
                    grid.addWidget(QLabel('Article price'), 5, 2)
                    grid.addWidget(q3Edit, 5 , 3) 
                    
                    grid.addWidget(QLabel('Stock'), 6, 0)
                    grid.addWidget(q4Edit, 6, 1)
                    
                    grid.addWidget(QLabel('Order balance'), 7, 0)
                    grid.addWidget(q16Edit, 7, 1)
                    
                    grid.addWidget(QLabel('Reservation balance'), 8, 0)
                    grid.addWidget(q12Edit, 8, 1)
                                       
                    grid.addWidget(QLabel('Order status'),7 ,2)
                    grid.addWidget(q7Edit, 7, 3)
                    
                    grid.addWidget(QLabel('Category'),8 ,2)
                    grid.addWidget(q8Edit, 8,3)
                    
                    if rpartikel[9] > 4:
                        bestelhoeveelheid = rpartikel[8]+rpartikel[6]-rpartikel[3]
                        grid.addWidget(QLabel('To order'), 10, 0)
                        if rpartikel[7]:
                            grid.addWidget(QLabel('{:12.2f}'.format(bestelhoeveelheid, 2)), 10, 1, 1, 1, Qt.AlignRight)
                        else:
                            grid.addWidget(QLabel('On order'), 10, 1)
                        grid.addWidget(QLabel('Reservation controlled'), 9, 2)
                    else:
                        grid.addWidget(QLabel('Order size'),9 ,0)
                        grid.addWidget(q9Edit, 9,1)
                        grid.addWidget(QLabel('Minimum stock'), 6, 2)
                        grid.addWidget(q6Edit, 6, 3)
                        
                        bestelhoeveelheid = rpartikel[11]
                        grid.addWidget(QLabel('To order'), 10, 0)
                        if rpartikel[7]:
                            grid.addWidget(QLabel('{:12.2f}'.format(bestelhoeveelheid, 2)), 10, 1, 1, 1, Qt.AlignRight)
                        else:
                            grid.addWidget(QLabel('On order'), 10, 1)
                        grid.addWidget(QLabel('Stock controlled'), 9, 2)
                    
                    grid.addWidget(QLabel('Annual consumption'),10, 2)
                    grid.addWidget(q13Edit, 10, 3)

                    pixmap = QPixmap(rpartikel[10])
                    lbl2 = QLabel(self)
                    lbl2.setPixmap(pixmap)
                    grid.addWidget(lbl2 , 1, 2, 2, 2, Qt.AlignRight)
                    
                    bestelBtn = QPushButton('Order letter')
                    bestelBtn.clicked.connect(lambda: bestelBrief(rpartikel, bestelhoeveelheid, bestelBtn))
                    
                    grid.addWidget(bestelBtn, 12, 3, 1, 1, Qt.AlignRight)
                    bestelBtn.setFont(QFont("Arial",10))
                    bestelBtn.setFixedWidth(100) 
                    bestelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    if rpartikel[7]:
                        bestelBtn.setEnabled(True)
                    else:
                        bestelBtn.setEnabled(False)
                    
                    cancelBtn = QPushButton('Close')
                    cancelBtn.clicked.connect(self.close)
                
                    grid.addWidget(cancelBtn, 12, 2, 1, 1, Qt.AlignRight)
                    cancelBtn.setFont(QFont("Arial",10))
                    cancelBtn.setFixedWidth(100)
                    cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 13, 0, 1, 4, Qt.AlignCenter)
                                   
                    self.setLayout(grid)
                    self.setGeometry(500, 100, 350, 300)
                    logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
                
            window = Widget()
            window.exec_()
                                                        
    win = MyWindow(data_list, header)
    win.exec_()
    vrdKeuze(m_email)