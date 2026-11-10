from login import hoofdMenu
from datetime import date
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor, QImage, QPainter
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QGridLayout, QStyledItemDelegate,\
      QDialog, QLineEdit, QVBoxLayout, QTableView, QMessageBox
from sqlalchemy import (Table, Column, Integer, String, Float, Boolean,\
                     MetaData, create_engine, select, update, and_, or_)
import logging
logger = logging.getLogger(__name__)

def ongKeuze():
    logger.warning(">>> Entering ongKeuze()", extra={"event.action": "ongKeuze"})
    msg = QMessageBox()
    logger.debug("ongKeuze(): msg → %s", msg, extra={"event.action": "ongKeuze"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Invalid choice')
    msg.setWindowTitle('Order Article')
    logger.debug("<<< Exiting ongKeuze()", extra={"event.action": "ongKeuze"})
    msg.exec_()

def bestelStatus():
    logger.warning(">>> Entering bestelStatus()", extra={"event.action": "bestelStatus"})
    msg = QMessageBox()
    logger.debug("bestelStatus(): msg → %s", msg, extra={"event.action": "bestelStatus"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setWindowTitle('Printing order letter')
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

def printBrief(rpartikel):
    logger.warning(">>> Entering printBrief(rpartikel=%s)", rpartikel, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel})
    from sys import platform
    vandaag = str(date.today())[0:10]
    logger.debug("printBrief(rpartikel=%s): vandaag → %s", rpartikel, vandaag, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel})
    metadata =  MetaData()
    logger.debug("printBrief(rpartikel=%s): metadata → %s", rpartikel, metadata, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel})
    params_system = Table('params_system', metadata,
        Column('systemID', Integer, primary_key=True),
        Column('system_value', Integer))
         
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("printBrief(rpartikel=%s): engine → %s", rpartikel, engine, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel})
    con = engine.connect()
    logger.debug("printBrief(rpartikel=%s): con → %s", rpartikel, con, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel})
    selpar = select([params_system]).where(params_system.c.systemID == 1)
    rppar = con.execute(selpar).first()
    logger.debug("printBrief(rpartikel=%s): selpar → %s", rpartikel, selpar, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel})
    logger.debug("printBrief(rpartikel=%s): rppar → %s", rpartikel, rppar, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel})
    bestnr = int(rppar[1])
    updpar = update(params_system).where(params_system.c.systemID == 1).values(system_value = int(bestnr+1))
    con.execute(updpar)
    logger.debug("printBrief(rpartikel=%s): bestnr → %s", rpartikel, bestnr, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel})
    if rpartikel[9] == 1:
        besteltekst = 'Order size stock controlled: '+str(round(rpartikel[11],2))+'\n\n'
        logger.debug("printBrief(rpartikel=%s): updpar → %s", rpartikel, updpar, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel})
        termijn = ' 3 weeks'
    elif rpartikel[9] == 2:
        besteltekst = 'Order size stock controlled: '+str(round(rpartikel[11],2))+'\n\n'
        logger.debug("printBrief(rpartikel=%s): besteltekst → %s", rpartikel, besteltekst, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel})
        termijn = ' 8 weeks'
        logger.debug("printBrief(rpartikel=%s): termijn → %s", rpartikel, termijn, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel})
    elif rpartikel[9] == 3:
        besteltekst = 'Order size stock controlled: '+str(round(rpartikel[11],2))+'\n\n'
        termijn = ' 26 weeks'
    elif rpartikel[9] == 4:
        besteltekst = 'Order size stock controlled: '+str(round(rpartikel[11],2))+'\n\n'
        termijn = ' 1 year'
    elif rpartikel[9] == 5:
        besteltekst = 'Minimum order size reservation controlled: '+str(round(rpartikel[8]-rpartikel[3]-rpartikel[6],2))+'\n\n'
        termijn = ' 3 weeks'
    elif rpartikel[9] == 6:
        besteltekst = 'Minimum order size reservation controlled: '+str(round(rpartikel[8]-rpartikel[3]-rpartikel[6],2))+'\n\n'
        termijn = ' 6 weeks'
    elif rpartikel[9] == 7:
        besteltekst = 'Minimum order size reservation controlled: '+str(round(rpartikel[8]-rpartikel[3]-rpartikel[6],2))+'\n\n'
        termijn = ' 12 weeks'
    elif rpartikel[9] == 8:
        besteltekst = 'Minimum order size reservation controlled: '+str(round(rpartikel[8]-rpartikel[3]-rpartikel[6],2))+'\n\n'
        termijn = ' 24 weeks'
    elif rpartikel[9] == 9:
        besteltekst = 'Minimum order size reservation controlled: '+str(round(rpartikel[8]-rpartikel[3]-rpartikel[6],2))+'\n\n'
        termijn = ' 1 year'
    if platform == 'win32':
        filename = '.\\forms\\Internal_Order_letters\\Order_letter_number_'+str(bestnr)+'.txt'
    else:
        filename = './forms/Internal_Order_letters\\Order_letter_number_'+str(bestnr)+'.txt'
    open(filename,"w").write('\n\n\nDate: '+str(vandaag)+'\n')
    gegevens = ('\n\n'+\
    'Internal order slip serial number: '+str(bestnr)+'\n\n\n\n'+\
    'Order letter for warehouse item: '+str(rpartikel[0])+'\n\n'+\
    'Article description: '+str(rpartikel[1])+'\n\n'+\
    'Article price including surcharge: '+str(round(rpartikel[2],2))+'\n\n'+\
    'Article stock: '+str(round(rpartikel[3],2))+'\n\n'+\
    'Article unit: '+str(rpartikel[4])+'\n\n'+\
    'Article minimum stock:  '+str(round(rpartikel[5],2))+'\n\n'+\
    'Order balance: '+str(round(rpartikel[6],2))+'\n\n'+\
    'Order status: '+str(rpartikel[7])+'\n\n'+\
    'Reservation balance: '+str(round(rpartikel[8],2))+'\n\n'+\
    'Category: '+str(rpartikel[9])+'\n\n'+\
    str(besteltekst)+'Delivery period : '+str(termijn)+'\n\n')
    open(filename,"a").write(gegevens+'\n')

    class Window(QDialog):
        logger.debug("<<< Exiting printBrief(rpartikel=%s)", rpartikel, extra={"event.action": "printBrief", "logrite.rpartikel": rpartikel})
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
        'Internal order letter serail number: '+str(bestnr)+'\n\n\n\n'+\
        'Order letter for warehouse article: '+str(rpartikel[0])+'\n\n'+\
        'Article description: '+rpartikel[1]+'\n\n'+\
        'Article price including surcharges: '+str(round(rpartikel[2],2))+'\n\n'+\
        'Article stock : '+str(round(rpartikel[3],2))+'\n\n'+\
        'Article unit: '+rpartikel[4]+'\n\n'+
        'Article miminimum stock:  '+str(round(rpartikel[5],2))+'\n\n'+\
        'Order balance: '+str(round(rpartikel[6],2))+'\n\n'+\
        'Order status: '+str(rpartikel[7])+'\n\n'+\
        'Reservation balance: '+str(round(rpartikel[8],2))+'\n\n'+\
        'Category: '+str(rpartikel[9])+'\n\n'+\
        besteltekst+\
        'Delivery period : ' + termijn)
            
            if platform == 'win32':
                lblinfo.setStyleSheet("font: 72pt 'Comic Sans MS'")
            else:
                lblinfo.setStyleSheet("font: 144pt 'Comic Sans MS'")
            return(lblinfo)
                    
    Window()
            
def bestelBrief(rpartikel, bestelBtn):
    logger.warning(">>> Entering bestelBrief(rpartikel=%s,bestelBtn=%s)", rpartikel, bestelBtn, extra={"event.action": "bestelBrief", "logrite.rpartikel": rpartikel, "logrite.bestelBtn": bestelBtn})
    metadata = MetaData()
    logger.debug("bestelBrief(rpartikel=%s,bestelBtn=%s): metadata → %s", rpartikel, bestelBtn, metadata, extra={"event.action": "bestelBrief", "logrite.rpartikel": rpartikel, "logrite.bestelBtn": bestelBtn})
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('bestelstatus', Boolean))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("bestelBrief(rpartikel=%s,bestelBtn=%s): engine → %s", rpartikel, bestelBtn, engine, extra={"event.action": "bestelBrief", "logrite.rpartikel": rpartikel, "logrite.bestelBtn": bestelBtn})
    con = engine.connect()
    logger.debug("bestelBrief(rpartikel=%s,bestelBtn=%s): con → %s", rpartikel, bestelBtn, con, extra={"event.action": "bestelBrief", "logrite.rpartikel": rpartikel, "logrite.bestelBtn": bestelBtn})
    if rpartikel[7] == False:
        bestelStatus()
    else:
        updart = update(artikelen).where(artikelen.c.artikelID == rpartikel[0])\
        .values(bestelstatus = False)
        logger.debug("bestelBrief(rpartikel=%s,bestelBtn=%s): updart → %s", rpartikel, bestelBtn, updart, extra={"event.action": "bestelBrief", "logrite.rpartikel": rpartikel, "logrite.bestelBtn": bestelBtn})
        con.execute(updart)
        
        printBrief(rpartikel)
        logger.debug("<<< Exiting bestelBrief(rpartikel=%s,bestelBtn=%s)", rpartikel, bestelBtn, extra={"event.action": "bestelBrief", "logrite.rpartikel": rpartikel, "logrite.bestelBtn": bestelBtn})
        logger.debug("bestelBrief(rpartikel=%s,bestelBtn=%s): bestelBtn → %s", rpartikel, bestelBtn, bestelBtn, extra={"event.action": "bestelBrief", "logrite.rpartikel": rpartikel, "logrite.bestelBtn": bestelBtn})
        bestelBtn.setEnabled(False)

def toonArtikellijst(m_email):
    logger.warning(">>> Entering toonArtikellijst(m_email=%s)", m_email, extra={"event.action": "toonArtikellijst"})
    metadata = MetaData()
    logger.debug("toonArtikellijst(m_email=%s): metadata → %s", m_email, metadata, extra={"event.action": "toonArtikellijst"})
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
        Column('art_bestelgrootte', Float))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("toonArtikellijst(m_email=%s): engine → %s", m_email, engine, extra={"event.action": "toonArtikellijst"})
    conn = engine.connect()
    logger.debug("toonArtikellijst(m_email=%s): conn → %s", m_email, conn, extra={"event.action": "toonArtikellijst"})
    sel = select([artikelen]).where(or_(and_(artikelen.c.art_voorraad+artikelen.c.bestelsaldo\
         -artikelen.c.reserveringsaldo < artikelen.c.art_min_voorraad, artikelen.c.categorie < 5),\
         and_(artikelen.c.art_voorraad+artikelen.c.bestelsaldo < artikelen.c.reserveringsaldo,\
         artikelen.c.categorie > 4))).order_by(artikelen.c.artikelID)
    rpartikelen = conn.execute(sel)
    logger.debug("toonArtikellijst(m_email=%s): sel → %s", m_email, sel, extra={"event.action": "toonArtikellijst"})
    updart = update(artikelen).where(and_(artikelen.c.art_voorraad+artikelen.c.bestelsaldo\
         < artikelen.c.reserveringsaldo, artikelen.c.categorie > 4))\
          .values(art_bestelgrootte = artikelen.c.reserveringsaldo \
          - artikelen.c.art_voorraad - artikelen.c.bestelsaldo)
    logger.debug("toonArtikellijst(m_email=%s): rpartikelen → %s", m_email, rpartikelen, extra={"event.action": "toonArtikellijst"})
    conn.execute(updart)
    class MyWindow(QDialog):
        logger.debug("toonArtikellijst(m_email=%s): updart → %s", m_email, updart, extra={"event.action": "toonArtikellijst"})
        def __init__(self, data_list, header, *args):
            logger.debug("<<< Exiting toonArtikellijst(m_email=%s)", m_email, extra={"event.action": "toonArtikellijst"})
            QWidget.__init__(self, *args,)
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            self.setGeometry(100, 50, 1800, 900)
            self.setWindowTitle('Articles order list')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
            table_model = MyTableModel(self, data_list, header)
            logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_model → %s", self, data_list, header, table_model, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): font → %s", self, data_list, header, font, extra={"event.action": "__init__", "logrite.data_list": data_list})
            table_view = QTableView()
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_view → %s", self, data_list, header, table_view, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view, extra={"event.action": "__init__", "logrite.data_list": data_list})
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.setItemDelegateForColumn(10, showImage(self))
            table_view.setColumnWidth(10, 100)
            table_view.verticalHeader().setDefaultSectionSize(75)
            table_view.clicked.connect(showArtikel)
            layout = QVBoxLayout(self)
            logger.debug("__init__(data_list=%s,header=%s): layout → %s", data_list, header, layout, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): layout → %s", self, data_list, header, layout, extra={"event.action": "__init__", "logrite.data_list": data_list})
            layout.addWidget(table_view)
            self.setLayout(layout)
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
            if not index.isValid():
                return None
            #elif index.column() == 9 and role == Qt.DecorationRole: # alternative picture however
            #    return QPixmap(index.data())                        # with text right from path
            elif role != Qt.DisplayRole:
                return None
            return str(self.mylist[index.row()][index.column()])
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
               logger.debug("__init__(parent=%s): self.Bestelhoeveelheid → %s", parent, self.Bestelhoeveelheid, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): q9Edit → %s", parent, q9Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): q9Edit → %s", self, parent, q9Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): lbl2 → %s", parent, lbl2, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): lbl2 → %s", self, parent, lbl2, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
               logger.debug("__init__(parent=%s): bestelBtn → %s", parent, bestelBtn, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s,parent=%s): bestelBtn → %s", self, parent, bestelBtn, extra={"event.action": "__init__"})
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
                                       
    header = ['Article number', 'Description', 'Price', 'Stock', 'Unit','Minimum Stock',\
              'Order balance', 'Order status', 'Reservation balance', 'Category', 'Image',\
              'To order']
        
    data_list=[]
    for row in rpartikelen:
        data_list += [(row)] 
        
    def showArtikel(idx):
        logger.warning(">>> Entering showArtikel(idx=%s)", idx, extra={"event.action": "showArtikel", "logrite.idx": idx})
        martikelnr = idx.data()
        logger.debug("showArtikel(idx=%s): martikelnr → %s", idx, martikelnr, extra={"event.action": "showArtikel", "logrite.idx": idx})
        if idx.column() == 0:
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showArtikel(idx=%s): engine → %s", idx, engine, extra={"event.action": "showArtikel", "logrite.idx": idx})
            con = engine.connect()
            sel = select([artikelen]).where(artikelen.c.artikelID == martikelnr)
            logger.debug("showArtikel(idx=%s): con → %s", idx, con, extra={"event.action": "showArtikel", "logrite.idx": idx})
            rpartikel = con.execute(sel).first()
              
            logger.debug("showArtikel(idx=%s): sel → %s", idx, sel, extra={"event.action": "showArtikel", "logrite.idx": idx})
            logger.debug("showArtikel(idx=%s): rpartikel → %s", idx, rpartikel, extra={"event.action": "showArtikel", "logrite.idx": idx})
            class Widget(QDialog):
                def __init__(self, parent=None):
                    super(Widget, self).__init__(parent)
                    logger.debug("<<< Exiting showArtikel(idx=%s)", idx, extra={"event.action": "showArtikel", "logrite.idx": idx})
                
                    self.setWindowTitle("Artikelen Bestellijst")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                                
                    self.setFont(QFont('Arial', 10))
                               
                    self.Artikelnummer = QLabel()
                    q1Edit = QLineEdit(str(rpartikel[0]))
                    q1Edit.setFixedWidth(100)
                    q1Edit.setDisabled(True)
                    q1Edit.setFont(QFont("Arial",10))
                
                    self.Artikelomschrijving = QLabel()
                    q2Edit = QLineEdit(str(rpartikel[1]))
                    q2Edit.setFixedWidth(400)
                    q2Edit.setFont(QFont("Arial",10))
                    q2Edit.setDisabled(True)
                    
                    self.Artikelprijs = QLabel()
                    q3Edit = QLineEdit(str(rpartikel[2]))
                    q3Edit.setFixedWidth(100)
                    q3Edit.setFont(QFont("Arial",10))
                    q3Edit.setDisabled(True)
                                    
                    self.Artikelvoorraad = QLabel()
                    q4Edit = QLineEdit(str(rpartikel[3]))
                    q4Edit.setFixedWidth(100)
                    q4Edit.setFont(QFont("Arial",10))
                    q4Edit.setDisabled(True)
                    
                    self.Artikeleenheid = QLabel()
                    q5Edit = QLineEdit(rpartikel[4])
                    q5Edit.setFixedWidth(100)
                    q5Edit.setFont(QFont("Arial",10))
                    q5Edit.setDisabled(True)
                    
                    self.Minimumvoorraad = QLabel()
                    q6Edit = QLineEdit(str(rpartikel[5]))
                    q6Edit.setFixedWidth(100)
                    q6Edit.setFont(QFont("Arial",10))
                    q6Edit.setDisabled(True)
                     
                    self.Bestelsaldo = QLabel()
                    q16Edit = QLineEdit(str(rpartikel[6]))
                    q16Edit.setFixedWidth(100)
                    q16Edit.setFont(QFont("Arial",10))
                    q16Edit.setDisabled(True)
    
                    self.Bestelstatus = QLabel()
                    q7Edit = QLineEdit(str(rpartikel[7]))
                    q7Edit.setFixedWidth(100)
                    q7Edit.setFont(QFont("Arial",10))
                    q7Edit.setDisabled(True)
                    
                    self.Reserveringsaldo = QLabel()
                    q12Edit = QLineEdit(str(rpartikel[8]))
                    q12Edit.setFixedWidth(100)
                    q12Edit.setFont(QFont("Arial",10))
                    q12Edit.setDisabled(True)
                                   
                    self.Categorie = QLabel()
                    q8Edit = QLineEdit(str(rpartikel[9]))
                    q8Edit.setFixedWidth(100)
                    q8Edit.setFont(QFont("Arial",10))
                    q8Edit.setDisabled(True)
                    
                    self.Bestelhoeveelheid = QLabel()
                    if rpartikel[9] > 4:
                        q9Edit = QLineEdit(str(rpartikel[8]-rpartikel[6]-rpartikel[3]))
                    elif rpartikel[9] < 5:
                        q9Edit = QLineEdit(str(rpartikel[11]))
                    q9Edit.setFixedWidth(100)
                    q9Edit.setFont(QFont("Arial",10))
                    q9Edit.setDisabled(True)
                    
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
                                  
                    grid.addWidget(QLabel('Minimum stock'), 6, 2)
                    grid.addWidget(q6Edit, 6, 3)
                    
                    grid.addWidget(QLabel('Order balance'), 7, 0)
                    grid.addWidget(q16Edit, 7, 1)
                    
                    grid.addWidget(QLabel('Reservation balance '), 8, 0)
                    grid.addWidget(q12Edit, 8, 1)
                                       
                    grid.addWidget(QLabel('Order status'),7 ,2)
                    grid.addWidget(q7Edit, 7, 3)
                    
                    grid.addWidget(QLabel('Category'),8 ,2)
                    grid.addWidget(q8Edit, 8,3)
                    
                    grid.addWidget(QLabel('To order'),9 ,0)
                    grid.addWidget(q9Edit, 9,1)
                    
                    pixmap = QPixmap(rpartikel[10])
                    lbl2 = QLabel(self)
                    lbl2.setPixmap(pixmap)
                    grid.addWidget(lbl2 , 1, 2, 2, 2, Qt.AlignRight)
                
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 11, 0, 1, 4, Qt.AlignCenter)
                    
                    cancelBtn = QPushButton('Close')
                    cancelBtn.clicked.connect(self.close)
                
                    grid.addWidget(cancelBtn, 10, 2, 1, 1, Qt.AlignRight)
                    cancelBtn.setFont(QFont("Arial",10))
                    cancelBtn.setFixedWidth(100)
                    cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    
                    bestelBtn = QPushButton('Order letter')
                    bestelBtn.clicked.connect(lambda: bestelBrief(rpartikel, bestelBtn))
                                
                    grid.addWidget(bestelBtn, 10, 3, 1, 1, Qt.AlignRight)
                    bestelBtn.setFont(QFont("Arial",10))
                    bestelBtn.setFixedWidth(100) 
                    bestelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    
                    self.setLayout(grid)
                    self.setGeometry(500, 100, 350, 300)
                    logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
                
            window = Widget()
            window.exec_()
                                            
    win = MyWindow(data_list, header)
    win.exec_()
    hoofdMenu(m_email)