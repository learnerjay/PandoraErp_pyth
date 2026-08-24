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
    logger.debug(">>> Entering refresh(m_email=%s,keuze=%s)", m_email, keuze)
    self.close()
    jaarVerbruik(m_email, keuze)
    logger.debug("<<< Exiting refresh(m_email=%s,keuze=%s)", m_email, keuze)

def artVerwerkt(rpartikelen, mbestgr, minvrd):
    logger.debug(">>> Entering artVerwerkt(rpartikelen=%s,mbestgr=%s,minvrd=%s)", rpartikelen, mbestgr, minvrd)
    msg = QMessageBox()
    logger.debug("artVerwerkt(rpartikelen=%s,mbestgr=%s,minvrd=%s): msg → %s", rpartikelen, mbestgr, minvrd, msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setWindowTitle('Voorraadbeheersing')
    msg.setIcon(QMessageBox.Information)
    msg.setText('Artikel: '+str(rpartikelen[0])+'\nOmschrijving: '+rpartikelen[1]+'\nMinimumvoorraad gewijzigd in '+str(minvrd)+'\nBestelgrootte gewijzigd in '+str(mbestgr))
    logger.debug("<<< Exiting artVerwerkt(rpartikelen=%s,mbestgr=%s,minvrd=%s)", rpartikelen, mbestgr, minvrd)
    msg.exec_()
    
def bestelStatus():
    logger.debug(">>> Entering bestelStatus()")
    msg = QMessageBox()
    logger.debug("bestelStatus(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setWindowTitle('Bestelbrief printen')
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Bestelbrief is reeds aangemaakt!')
    logger.debug("<<< Exiting bestelStatus()")
    msg.exec_()
    
def handle_paint_request(self, printer):
    logger.debug(">>> Entering handle_paint_request(printer=%s)", printer)
    painter = QPainter(printer)
    logger.debug("handle_paint_request(printer=%s): painter → %s", printer, painter)
    logger.debug("handle_paint_request(self=%s,printer=%s): painter → %s", self, printer, painter)
    painter.setViewport(self.view.rect())
    painter.setWindow(self.view.rect())                        
    self.view.render(painter)
    painter.end()
    logger.debug("<<< Exiting handle_paint_request(printer=%s)", printer)

def printBrief(rpartikel, bestelhoeveelheid, bestelBtn):
    logger.debug(">>> Entering printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s)", rpartikel, bestelhoeveelheid, bestelBtn)
    from sys import platform
    vandaag = str(datetime.date.today())[0:10]
    logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): vandaag → %s", rpartikel, bestelhoeveelheid, bestelBtn, vandaag)
    metadata =  MetaData()
    logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): metadata → %s", rpartikel, bestelhoeveelheid, bestelBtn, metadata)
    params_system = Table('params_system', metadata,
          Column('systemID', Integer, primary_key=True),
          Column('system_value', Float))

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): engine → %s", rpartikel, bestelhoeveelheid, bestelBtn, engine)
    con = engine.connect()
    selpar = select([params_system]).where(params_system.c.systemID == 1)
    logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): con → %s", rpartikel, bestelhoeveelheid, bestelBtn, con)
    rppar = con.execute(selpar).first()
    bestnr = int(rppar[1])
    logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): selpar → %s", rpartikel, bestelhoeveelheid, bestelBtn, selpar)
    logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): rppar → %s", rpartikel, bestelhoeveelheid, bestelBtn, rppar)
    updpar = update(params_system).where(params_system.c.systemID == 1).values(system_value=int(bestnr + 1))
    con.execute(updpar)
    if rpartikel[9] == 1:
        logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): bestnr → %s", rpartikel, bestelhoeveelheid, bestelBtn, bestnr)
        besteltekst = 'Bestelgrootte voorraadgestuurd: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n' 
        termijn = ' 3 weken'
        logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): updpar → %s", rpartikel, bestelhoeveelheid, bestelBtn, updpar)
        logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): besteltekst → %s", rpartikel, bestelhoeveelheid, bestelBtn, besteltekst)
    elif rpartikel[9] == 2:
        besteltekst = 'Bestelgrootte voorraadgestuurd: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n' 
        termijn = ' 12 weken'
        logger.debug("printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): termijn → %s", rpartikel, bestelhoeveelheid, bestelBtn, termijn)
    elif rpartikel[9] == 3:
        besteltekst = 'Bestelgrootte voorraadgestuurd: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n'
        termijn = ' 26 weken'
    elif rpartikel[9] == 4:
        besteltekst = 'Bestelgrootte voorraadgestuurd: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n' 
        termijn = ' 52 weken'
    elif rpartikel[9] == 5:
        besteltekst = 'Minimale bestelgrootte reserveringgestuurd: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n'
        termijn = ' 3 weken'
    elif rpartikel[9] == 6:
        besteltekst = 'Minimale bestelgrootte reserveringgestuurd: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n'
        termijn = ' 6 weken'
    elif rpartikel[9] == 7:
        besteltekst = 'Minimale bestelgrootte reserveringgestuurd: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n'
        termijn = ' 12 weken'
    elif rpartikel[9] == 8:
        besteltekst = 'Minimale bestelgrootte reserveringgestuurd: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n'
        termijn = ' 24 weken'
    elif rpartikel[9] == 9:
        besteltekst = 'Minimale bestelgrootte reserveringgestuurd: '+'{:12.2f}'.format(bestelhoeveelheid)+'\n\n'
        termijn = ' 52 weken'
    if platform == 'win32':
        filename = '.\\forms\\Intern_Orderbrieven\\Orderbriefnr_'+str(bestnr)+'.txt'
    else:
        filename = './forms/Intern_Orderbrieven/Orderbriefnr_'+str(bestnr)+'.txt'
    open(filename,"w").write('\n\n\nDatum: '+str(vandaag)+'\n')
    gegevens = ('\n\n'+\
    'Interne orderbrief volgnummer: '+str(bestnr)+'\n\n\n\n'+\
    'Bestelbrief voor magazijnartikel: '+str(rpartikel[0])+'\n\n'+\
    'Artikelomschrijving: '+str(rpartikel[1])+'\n\n'+\
    'Artikelprijs inclusief opslagen: '+'{:12.2f}'.format(rpartikel[2])+'\n\n'+\
    'Artikelvoorraad : '+'{:12.2f}'.format(rpartikel[3])+'\n\n'+\
    'Artikel eenheid: '+str(rpartikel[4])+'\n\n'+\
    'Artikel miminimum voorraad:  '+'{:12.2f}'.format(rpartikel[5])+'\n\n'+\
    'Bestelsaldo: '+'{:12.2f}'.format(rpartikel[6])+'\n\n'+\
    'Bestelstatus: '+str(rpartikel[7])+'\n\n'+\
    'Reserveringssaldo: '+'{:12.2f}'.format(rpartikel[8])+'\n\n'+\
    'Categorie: '+str(rpartikel[9])+'\n\n'+\
    str(besteltekst)+'Levertermijn : '+str(termijn)+'\n\n')
    open(filename,"a").write(gegevens+'\n')

    class Window(QDialog):
        logger.debug("<<< Exiting printBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s)", rpartikel, bestelhoeveelheid, bestelBtn)
        def __init__(self):
            logger.debug(">>> Entering __init__()")
            QDialog.__init__(self)
            self.setWindowTitle("Printen interne orderbrief") 
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                                                  Qt.WindowMinMaxButtonsHint)
            logger.debug("__init__(): dialog → %s", dialog)
            logger.debug("__init__(): layout → %s", layout)
            logger.debug("__init__(): self.view → %s", self.view)
            self.setFont(QFont('Arial', 10))
            self.view = QLabel(self)
            self.view = self.create_view()
            layout = QGridLayout(self)
            logger.debug("__init__(self=%s): layout → %s", self, layout)
            logger.debug("__init__(): printer → %s", printer)
            logger.debug("__init__(self=%s): printer → %s", self, printer)
            layout.addWidget(self.view, 0, 0, 1, 2)
            printer = QPrinter(QPrinter.HighResolution)
            #printer.setPageMargins(12, 16, 12, 20, QPrinter.Millimeter)
            dialog = QPrintDialog(printer, self)
            logger.debug("__init__(self=%s): dialog → %s", self, dialog)
            if dialog.exec_() == QPrintDialog.Accepted:
                handle_paint_request(self, printer)
                logger.debug("<<< Exiting __init__()")
       
        def create_view(self):
            logger.debug(">>> Entering create_view()")
            lblinfo = QLabel(
        '\n\n\n'+\
        'Datum: '+str(vandaag)+'\n\n\n'+\
        'Interne orderbrief volgnummer: '+str(bestnr)+'\n\n\n\n'+\
        'Bestelbrief voor magazijnartikel: '+str(rpartikel[0])+'\n\n'+\
        'Artikelomschrijving: '+rpartikel[1]+'\n\n'+\
        'Artikelprijs inclusief opslagen: '+'{:12.2f}'.format(rpartikel[2])+'\n\n'+\
        'Artikelvoorraad : '+'{:12.2f}'.format(rpartikel[3])+'\n\n'+\
        'Artikel eenheid: '+rpartikel[4]+'\n\n'+
        'Artikel miminimum voorraad:  '+'{:12.2f}'.format(rpartikel[5])+'\n\n'+\
        'Bestelsaldo: '+'{:12.2f}'.format(rpartikel[6])+'\n\n'+\
        'Bestelstatus: '+str(rpartikel[7])+'\n\n'+\
        'Reserveringssaldo: '+'{:12.2f}'.format(rpartikel[8])+'\n\n'+\
        'Categorie: '+str(rpartikel[9])+'\n\n'+\
        besteltekst+\
        'Levertermijn : ' + termijn)
            
            if platform == 'win32':
                lblinfo.setStyleSheet("font: 72pt 'Comic Sans MS'")
            else:
                lblinfo.setStyleSheet("font: 144pt 'Comic Sans MS'")
            return(lblinfo)
         
    Window()
            
def bestelBrief(rpartikel, bestelhoeveelheid, bestelBtn):
    logger.debug(">>> Entering bestelBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s)", rpartikel, bestelhoeveelheid, bestelBtn)
    metadata = MetaData()
    logger.debug("bestelBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): metadata → %s", rpartikel, bestelhoeveelheid, bestelBtn, metadata)
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('bestelstatus', Boolean),
        Column('bestelsaldo', Float))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    if rpartikel[7]:
        logger.debug("bestelBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): con → %s", rpartikel, bestelhoeveelheid, bestelBtn, con)
        updart = update(artikelen).where(artikelen.c.artikelID == rpartikel[0])\
        .values(bestelstatus = False, bestelsaldo = artikelen.c.bestelsaldo+bestelhoeveelheid)
        logger.debug("bestelBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): updart → %s", rpartikel, bestelhoeveelheid, bestelBtn, updart)
        con.execute(updart)
        bestelBtn.setDisabled(True)
        logger.debug("bestelBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s): bestelBtn → %s", rpartikel, bestelhoeveelheid, bestelBtn, bestelBtn)
        printBrief(rpartikel, bestelhoeveelheid, bestelBtn)
    else:
        bestelStatus()
        logger.debug("<<< Exiting bestelBrief(rpartikel=%s,bestelhoeveelheid=%s,bestelBtn=%s)", rpartikel, bestelhoeveelheid, bestelBtn)

def vrdKeuze(m_email):
    logger.debug(">>> Entering vrdKeuze(m_email=%s)", m_email)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Opvragen artikelen")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Keuze = QLabel()
            k0Edit = QComboBox()
            k0Edit.setFixedWidth(280)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('                  Uw Keuze ')
            k0Edit.addItem('1. Reservering te bestellen')
            k0Edit.addItem('2. Minimum Voorraad te bestellen')
            k0Edit.addItem('3. Artikelen in bestelling')
   
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
    
            applyBtn = QPushButton('Zoeken')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 3, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
              
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: windowSluit(self,m_email))
    
            grid.addWidget(cancelBtn, 3, 0, 1, 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            logger.debug(">>> Entering __init__(data_list=%s,header=%s)", data_list, header)
            logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font)
            logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view)
            logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model)
            logger.debug("__init__(data_list=%s,header=%s): grid → %s", data_list, header, grid)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): grid → %s", self, data_list, header, grid)
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
        
        def k0Changed(self, text):
            logger.debug(">>> Entering k0Changed(text=%s)", text)
            logger.debug("k0Changed(self=%s,text=%s): Keuze → %s", self, text, Keuze)
            self.Keuze.setText(text)
            logger.debug("<<< Exiting k0Changed(text=%s)", text)
            
        def returnk0(self):
            logger.debug(">>> Entering returnk0()")
            logger.debug("<<< Exiting returnk0()")
            return self.Keuze.text()
       
        @staticmethod
        def getData(parent=None):
            logger.debug(">>> Entering getData(parent=%s)", parent)
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent)
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
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)

def jaarVerbruik(m_email, keuze):
    logger.debug(">>> Entering jaarVerbruik(m_email=%s,keuze=%s)", m_email, keuze)
    metadata = MetaData()
    logger.debug("jaarVerbruik(m_email=%s,keuze=%s): metadata → %s", m_email, keuze, metadata)
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
    logger.debug("jaarVerbruik(m_email=%s,keuze=%s): engine → %s", m_email, keuze, engine)
    conn = engine.connect()
            
    logger.debug("jaarVerbruik(m_email=%s,keuze=%s): conn → %s", m_email, keuze, conn)
    if keuze == 1:
        sel = select([artikelen]).where(and_(artikelen.c.art_voorraad + artikelen.c.bestelsaldo\
            < artikelen.c.reserveringsaldo, artikelen.c.categorie > 4)).order_by(artikelen.c.artikelID)
        logger.debug("jaarVerbruik(m_email=%s,keuze=%s): sel → %s", m_email, keuze, sel)
    elif keuze == 2:
        sel = select([artikelen]).where(and_(artikelen.c.art_voorraad+artikelen.c.bestelsaldo\
            < artikelen.c.art_min_voorraad, artikelen.c.categorie < 5)).order_by(artikelen.c.artikelID)
    elif keuze == 3:
        sel = select([artikelen]).where(artikelen.c.bestelstatus == False)
          
    rpartikelen = conn.execute(sel)
    logger.debug("jaarVerbruik(m_email=%s,keuze=%s): rpartikelen → %s", m_email, keuze, rpartikelen)
   
    class MyWindow(QDialog):
        logger.debug("<<< Exiting jaarVerbruik(m_email=%s,keuze=%s)", m_email, keuze)
        def __init__(self, data_list, header, *args):
            QWidget.__init__(self, *args,)
            self.setGeometry(100, 50, 1800, 900)
            self.setWindowTitle('Jaarverbruik afgelopen jaar')
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
            table_view.setItemDelegateForColumn(10, showImage(self))
            table_view.setColumnWidth(10, 100)
            table_view.verticalHeader().setDefaultSectionSize(75)
            table_view.clicked.connect(aanpMinvoorraad)
            grid.addWidget(table_view, 0, 0, 1, 16)
            
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 1, 0, 1, 2)
       
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 15, 1, 1, Qt.AlignRight)
            
            freshBtn = QPushButton('Verversen')
            freshBtn.clicked.connect(lambda: refresh(m_email, keuze, self))

            freshBtn.setFont(QFont("Arial",10))
            freshBtn.setFixedWidth(100) 
            freshBtn.setStyleSheet("color: black;  background-color: gainsboro")
   
            grid.addWidget(freshBtn, 1, 14, 1, 1, Qt.AlignRight)
        
            sluitBtn = QPushButton('Sluiten')
            sluitBtn.clicked.connect(self.close)

            sluitBtn.setFont(QFont("Arial",10))
            sluitBtn.setFixedWidth(100) 
            sluitBtn.setStyleSheet("color: black;  background-color: gainsboro") 
            
            grid.addWidget(sluitBtn, 1, 13, 1, 1, Qt.AlignRight)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 1, 0, 1, 16, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(50, 50, 1800, 900)
            self.setLayout(grid)

            logger.debug(">>> Entering __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header)
            logger.debug("<<< Exiting __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header)
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.mylist → %s", self, parent, mylist, header, self.mylist)

    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.header → %s", self, parent, mylist, header, self.header)
            QAbstractTableModel.__init__(self, parent, *args)
            self.mylist = mylist
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
            #elif index.column() == 9 and role == Qt.DecorationRole: # alternatief picture echter
            #    return QPixmap(index.data())                        # met tekst rechts van path
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
       
    class showImage(QStyledItemDelegate):  
           def __init__(self, parent):
               logger.debug(">>> Entering __init__(parent=%s)", parent)
               logger.debug("__init__(parent=%s): q1Edit → %s", parent, q1Edit)
               logger.debug("__init__(parent=%s): self.Artikelnummer → %s", parent, self.Artikelnummer)
               logger.debug("__init__(self=%s,parent=%s): q1Edit → %s", self, parent, q1Edit)
               logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit)
               logger.debug("__init__(parent=%s): self.Artikelomschrijving → %s", parent, self.Artikelomschrijving)
               logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit)
               logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit)
               logger.debug("__init__(parent=%s): self.Artikelprijs → %s", parent, self.Artikelprijs)
               logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit)
               logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit)
               logger.debug("__init__(parent=%s): self.Artikelvoorraad → %s", parent, self.Artikelvoorraad)
               logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit)
               logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit)
               logger.debug("__init__(parent=%s): self.Artikeleenheid → %s", parent, self.Artikeleenheid)
               logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit)
               logger.debug("__init__(parent=%s): q6Edit → %s", parent, q6Edit)
               logger.debug("__init__(parent=%s): self.Minimumvoorraad → %s", parent, self.Minimumvoorraad)
               logger.debug("__init__(self=%s,parent=%s): q6Edit → %s", self, parent, q6Edit)
               logger.debug("__init__(parent=%s): q16Edit → %s", parent, q16Edit)
               logger.debug("__init__(parent=%s): self.Bestelsaldo → %s", parent, self.Bestelsaldo)
               logger.debug("__init__(self=%s,parent=%s): q16Edit → %s", self, parent, q16Edit)
               logger.debug("__init__(parent=%s): q7Edit → %s", parent, q7Edit)
               logger.debug("__init__(parent=%s): self.Bestelstatus → %s", parent, self.Bestelstatus)
               logger.debug("__init__(self=%s,parent=%s): q7Edit → %s", self, parent, q7Edit)
               logger.debug("__init__(parent=%s): q12Edit → %s", parent, q12Edit)
               logger.debug("__init__(parent=%s): self.Reserveringsaldo → %s", parent, self.Reserveringsaldo)
               logger.debug("__init__(self=%s,parent=%s): q12Edit → %s", self, parent, q12Edit)
               logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit)
               logger.debug("__init__(parent=%s): self.Categorie → %s", parent, self.Categorie)
               logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit)
               logger.debug("__init__(parent=%s): q9Edit → %s", parent, q9Edit)
               logger.debug("__init__(parent=%s): self.Bestelgrootte → %s", parent, self.Bestelgrootte)
               logger.debug("__init__(self=%s,parent=%s): q9Edit → %s", self, parent, q9Edit)
               logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
               logger.debug("__init__(parent=%s): q13Edit → %s", parent, q13Edit)
               logger.debug("__init__(parent=%s): self.Jaarverbruik → %s", parent, self.Jaarverbruik)
               logger.debug("__init__(self=%s,parent=%s): q13Edit → %s", self, parent, q13Edit)
               logger.debug("__init__(parent=%s): grid → %s", parent, grid)
               logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid)
               logger.debug("__init__(parent=%s): lbl → %s", parent, lbl)
               logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl)
               logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap)
               logger.debug("__init__(parent=%s): logo → %s", parent, logo)
               logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
               logger.debug("__init__(self=%s,parent=%s): bestelhoeveelheid → %s", self, parent, bestelhoeveelheid)
               logger.debug("__init__(parent=%s): lbl2 → %s", parent, lbl2)
               logger.debug("__init__(self=%s,parent=%s): lbl2 → %s", self, parent, lbl2)
               logger.debug("__init__(parent=%s): bestelBtn → %s", parent, bestelBtn)
               logger.debug("__init__(self=%s,parent=%s): bestelBtn → %s", self, parent, bestelBtn)
               logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn)
               logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn)
               logger.debug("<<< Exiting __init__(parent=%s)", parent)
               QStyledItemDelegate.__init__(self, parent)
           def paint(self, painter, option, index):        
                logger.debug(">>> Entering paint(painter=%s,option=%s,index=%s)", painter, option, index)
                logger.debug("paint(painter=%s,option=%s,index=%s): image → %s", painter, option, index, image)
                logger.debug("paint(self=%s,painter=%s,option=%s,index=%s): image → %s", self, painter, option, index, image)
                logger.debug("paint(self=%s,painter=%s,option=%s,index=%s): pixmap → %s", self, painter, option, index, pixmap)
                logger.debug("paint(painter=%s,option=%s,index=%s): pixmap → %s", painter, option, index, pixmap)
                painter.fillRect(option.rect,QColor(255,255,255))
                image = QImage(index.data())
                pixmap = QPixmap(image)
                pixmap.scaled(256,256) 
                logger.debug("<<< Exiting paint(painter=%s,option=%s,index=%s)", painter, option, index)
                return(painter.drawPixmap(option.rect, pixmap))
                                       
    header = ['Artikelnr', 'Omschrijving', 'Prijs', 'Voorraad', 'Eenheid','MinVrd',\
              'BestelSaldo', 'Bestelstatus', 'ReserveringSaldo', 'Categorie', 'Afbeelding',\
              'Te bestellen','Jaarverbruik-1', 'Jaarverbruik-2']    
        
    data_list=[]
    for row in rpartikelen:
        data_list += [(row)] 
        
    def aanpMinvoorraad(idx):
        logger.debug(">>> Entering aanpMinvoorraad(idx=%s)", idx)
        martikelnr = idx.data()
        logger.debug("aanpMinvoorraad(idx=%s): martikelnr → %s", idx, martikelnr)
        if idx.column() == 0:
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("aanpMinvoorraad(idx=%s): engine → %s", idx, engine)
            con = engine.connect()
            sel = select([artikelen]).where(artikelen.c.artikelID == martikelnr)
            logger.debug("aanpMinvoorraad(idx=%s): con → %s", idx, con)
            rpartikel = con.execute(sel).first() 
            mjaar = int(str(datetime.datetime.now())[0:4])
            logger.debug("aanpMinvoorraad(idx=%s): sel → %s", idx, sel)
            logger.debug("aanpMinvoorraad(idx=%s): rpartikel → %s", idx, rpartikel)
                             
            class Widget(QDialog):
                logger.debug("<<< Exiting aanpMinvoorraad(idx=%s)", idx)
                def __init__(self, parent=None):
                    super(Widget, self).__init__(parent)
                    logger.debug(">>> Entering __init__(parent=%s)", parent)
                
                    self.setWindowTitle("Aanpassen minimumvoorraad / bestelgrootte")
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
                  
                    grid.addWidget(QLabel('Artikelnummer'), 1, 0, 2, 1)
                    grid.addWidget(q1Edit, 1, 1, 2, 1)
                
                    grid.addWidget(QLabel('Artikelomschrijving'), 3, 0)
                    grid.addWidget(q2Edit, 3, 1, 1 ,3)
                    
                    grid.addWidget(QLabel('Eenheid'), 5, 0)
                    grid.addWidget(q5Edit, 5, 1)
                    
                    grid.addWidget(QLabel('Artikelprijs'), 5, 2)
                    grid.addWidget(q3Edit, 5 , 3) 
                    
                    grid.addWidget(QLabel('Voorraad'), 6, 0)
                    grid.addWidget(q4Edit, 6, 1)
                    
                    grid.addWidget(QLabel('Bestelsaldo'), 7, 0)
                    grid.addWidget(q16Edit, 7, 1)
                    
                    grid.addWidget(QLabel('Reserveringsaldo '), 8, 0)
                    grid.addWidget(q12Edit, 8, 1)
                                       
                    grid.addWidget(QLabel('BestelStatus'),7 ,2)
                    grid.addWidget(q7Edit, 7, 3)
                    
                    grid.addWidget(QLabel('Categorie'),8 ,2)
                    grid.addWidget(q8Edit, 8,3)
                    
                    if rpartikel[9] > 4:
                        bestelhoeveelheid = rpartikel[8]+rpartikel[6]-rpartikel[3]
                        grid.addWidget(QLabel('Te bestellen'), 10, 0)
                        if rpartikel[7]:
                            grid.addWidget(QLabel('{:12.2f}'.format(bestelhoeveelheid, 2)), 10, 1, 1, 1, Qt.AlignRight)
                        else:
                            grid.addWidget(QLabel('In bestelling'), 10, 1) 
                        grid.addWidget(QLabel('Reserveringgestuurd'), 9, 2)
                    else:
                        grid.addWidget(QLabel('Bestelgrootte'),9 ,0)
                        grid.addWidget(q9Edit, 9,1)
                        grid.addWidget(QLabel('Minimum voorraad'), 6, 2)
                        grid.addWidget(q6Edit, 6, 3)
                        
                        bestelhoeveelheid = rpartikel[11]
                        grid.addWidget(QLabel('Te bestellen'), 10, 0)
                        if rpartikel[7]:
                            grid.addWidget(QLabel('{:12.2f}'.format(bestelhoeveelheid, 2)), 10, 1, 1, 1, Qt.AlignRight)
                        else:
                            grid.addWidget(QLabel('In bestelling'), 10, 1)
                        grid.addWidget(QLabel('Voorraadgestuurd'), 9, 2)
                    
                    grid.addWidget(QLabel('Jaarverbruik'),10, 2)
                    grid.addWidget(q13Edit, 10, 3)

                    pixmap = QPixmap(rpartikel[10])
                    lbl2 = QLabel(self)
                    lbl2.setPixmap(pixmap)
                    grid.addWidget(lbl2 , 1, 2, 2, 2, Qt.AlignRight)
                    
                    bestelBtn = QPushButton('Bestelbrief')
                    bestelBtn.clicked.connect(lambda: bestelBrief(rpartikel, bestelhoeveelheid, bestelBtn))
                    
                    grid.addWidget(bestelBtn, 12, 3, 1, 1, Qt.AlignRight)
                    bestelBtn.setFont(QFont("Arial",10))
                    bestelBtn.setFixedWidth(100) 
                    bestelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    if rpartikel[7]:
                        bestelBtn.setEnabled(True)
                    else:
                        bestelBtn.setEnabled(False)
                    
                    cancelBtn = QPushButton('Sluiten')
                    cancelBtn.clicked.connect(self.close)
                
                    grid.addWidget(cancelBtn, 12, 2, 1, 1, Qt.AlignRight)
                    cancelBtn.setFont(QFont("Arial",10))
                    cancelBtn.setFixedWidth(100)
                    cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 13, 0, 1, 4, Qt.AlignCenter)
                                   
                    self.setLayout(grid)
                    self.setGeometry(500, 100, 350, 300)
                    logger.debug("<<< Exiting __init__(parent=%s)", parent)
                
            window = Widget()
            window.exec_()
                                                        
    win = MyWindow(data_list, header)
    win.exec_()
    vrdKeuze(m_email)