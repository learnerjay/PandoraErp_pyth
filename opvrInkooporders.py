from login import hoofdMenu
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor, QImage
from PyQt5.QtWidgets import  QLabel, QPushButton, QWidget, QGridLayout, QStyledItemDelegate,\
      QComboBox, QDialog, QLineEdit, QMessageBox, QTableView, QVBoxLayout
from sqlalchemy import (Table, Column, ForeignKey,  Integer, String, MetaData,\
                       create_engine, Float)
from sqlalchemy.sql import select, and_ 
import logging
logger = logging.getLogger(__name__)

def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.setAttribute(Qt.WA_DeleteOnClose)
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
    msg.setText('Please re-enter incorrect input\nsearch term!')
    msg.setWindowTitle('Request purchase orders')
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
    msg.setWindowTitle('Request purchase orders')               
    logger.debug("<<< Exiting geenRecord()")
    msg.exec_() 

def inkooporderKeuze(m_email):
    logger.debug(">>> Entering inkooporderKeuze(m_email=%s)", m_email)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Request purchase orders materials")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Keuze = QLabel()
            k0Edit = QComboBox()
            k0Edit.setFixedWidth(330)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('                  Search sort key')
            k0Edit.addItem('1. All purchase orders sorted by item number')
            k0Edit.addItem('2. All purchase orders sorted by order number')
            k0Edit.addItem('3. Filtered by company name')
            k0Edit.addItem('4. Filtered by item description')
            k0Edit.addItem('5. Filtered by order number')
            k0Edit.addItem('6. Filtered by delivery start yyyy(-mm(-dd))')
            k0Edit.addItem('7. Filtered by delivery end yyyy(-mm(-dd))')
            k0Edit.activated[str].connect(self.k0Changed)
                            
            self.Zoekterm = QLabel()
            zktermEdit = QLineEdit()
            zktermEdit.setFixedWidth(220)
            zktermEdit.setFont(QFont("Arial",10))
            zktermEdit.textChanged.connect(self.zktermChanged)
     
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
                                  
            grid.addWidget(k0Edit, 1, 0, 1, 3, Qt.AlignRight)
            lbl1 = QLabel('Search term')
            lbl1.setAlignment(Qt.AlignRight)
            grid.addWidget(lbl1, 2, 0, 1, 1, Qt. AlignRight)
            grid.addWidget(zktermEdit, 2, 1, 1, 2, Qt.AlignRight)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1, 3, Qt.AlignCenter)            
            self.setLayout(grid)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 2, Qt.AlignRight)
            
            self.setGeometry(500, 300, 150, 150)
    
            applyBtn = QPushButton('Search')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 3, 1, 1, 2, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 3, 1)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            logger.debug(">>> Entering __init__(data_list=%s,header=%s)", data_list, header)
            logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font)
            logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view)
            logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_model → %s", self, data_list, header, table_model)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_view → %s", self, data_list, header, table_view)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): font → %s", self, data_list, header, font)
            logger.debug("__init__(data_list=%s,header=%s): layout → %s", data_list, header, layout)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): layout → %s", self, data_list, header, layout)
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header)
                    
        def k0Changed(self, text):
            logger.debug(">>> Entering k0Changed(text=%s)", text)
            logger.debug("k0Changed(self=%s,text=%s): Keuze → %s", self, text, Keuze)
            self.Keuze.setText(text)
            logger.debug("<<< Exiting k0Changed(text=%s)", text)
            
        def zktermChanged(self, text):
            logger.debug(">>> Entering zktermChanged(text=%s)", text)
            logger.debug("zktermChanged(self=%s,text=%s): Zoekterm → %s", self, text, Zoekterm)
            self.Zoekterm.setText(text)
            logger.debug("<<< Exiting zktermChanged(text=%s)", text)
 
        def returnk0(self):
            logger.debug(">>> Entering returnk0()")
            logger.debug("<<< Exiting returnk0()")
            return self.Keuze.text()
        
        def returnzkterm(self):
            logger.debug(">>> Entering returnzkterm()")
            logger.debug("<<< Exiting returnzkterm()")
            return self.Zoekterm.text()
        
        @staticmethod
        def getData(parent=None):
            logger.debug(">>> Entering getData(parent=%s)", parent)
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent)
            return [dialog.returnk0(), dialog.returnzkterm()]       

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
    del window
    opvrOrder(keuze,zoekterm,m_email)
    
def opvrOrder(keuze,zoekterm, m_email):
    logger.debug(">>> Entering opvrOrder(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email)
    import validZt
    metadata = MetaData()
    logger.debug("opvrOrder(keuze=%s,zoekterm=%s,m_email=%s): metadata → %s", keuze, zoekterm, m_email, metadata)
    orders_inkoop_artikelen = Table('orders_inkoop_artikelen', metadata,
        Column('ordartlevID', Integer(), primary_key=True),
        Column('orderinkoopID', None, ForeignKey('orders_inkoop.orderinkoopID')),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('bestelaantal', Float),
        Column('inkoopprijs', Float),
        Column('levering_start', String),
        Column('levering_eind', String),
        Column('reclamatie', String),
        Column('aantal_reclamaties', Integer),
        Column('ontvangstdatum', String),
        Column('ontvangen_hoeveelheid', Float),
        Column('acceptatie_datum', String),
        Column('hoeveelheid_acceptatie', Float),
        Column('betaald', Float),
        Column('regel', Integer))
    orders_inkoop = Table('orders_inkoop', metadata,
        Column('orderinkoopID', Integer(), primary_key=True),
        Column('leverancierID', None, ForeignKey('leveranciers.leverancierID')),
        Column('besteldatum', String),
        Column('goedgekeurd', String),
        Column('betaald', String),
        Column('afgemeld', String))
    leveranciers = Table('leveranciers', metadata,
        Column('leverancierID', Integer(), primary_key=True),
        Column('bedrijfsnaam', String),
        Column('rechtsvorm', String))
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('artikelomschrijving', String),
        Column('art_voorraad', Float),
        Column('art_eenheid', String(20)),
        Column('thumb_artikel', String(70)))
      
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("opvrOrder(keuze=%s,zoekterm=%s,m_email=%s): engine → %s", keuze, zoekterm, m_email, engine)
    con = engine.connect()
    logger.debug("opvrOrder(keuze=%s,zoekterm=%s,m_email=%s): con → %s", keuze, zoekterm, m_email, con)
    
    if keuze == 1:
        sel = select([orders_inkoop_artikelen,orders_inkoop, leveranciers,artikelen]).\
         where(and_(orders_inkoop.c.leverancierID == leveranciers.c.\
           leverancierID, orders_inkoop_artikelen.c.artikelID == artikelen.c.\
           artikelID, orders_inkoop_artikelen.c.orderinkoopID == orders_inkoop.c.\
           orderinkoopID)).order_by(orders_inkoop_artikelen.c.artikelID)
        logger.debug("opvrOrder(keuze=%s,zoekterm=%s,m_email=%s): sel → %s", keuze, zoekterm, m_email, sel)
    elif keuze == 2:
        sel = select([orders_inkoop_artikelen,orders_inkoop, leveranciers,artikelen]).\
         where(and_(orders_inkoop.c.leverancierID == leveranciers.c.\
           leverancierID, orders_inkoop_artikelen.c.artikelID == artikelen.c.\
           artikelID, orders_inkoop_artikelen.c.orderinkoopID == orders_inkoop.c.\
           orderinkoopID)).order_by(orders_inkoop_artikelen.c.orderinkoopID,\
            orders_inkoop_artikelen.c.regel)
    elif keuze == 3:
       sel = select([orders_inkoop_artikelen,orders_inkoop, leveranciers,artikelen])\
        .where(and_(orders_inkoop_artikelen.c.orderinkoopID==orders_inkoop.c.orderinkoopID,\
          orders_inkoop.c.leverancierID == leveranciers.c.leverancierID,\
          orders_inkoop_artikelen.c.artikelID == artikelen.c.artikelID,\
          orders_inkoop_artikelen.c.orderinkoopID == orders_inkoop.c.orderinkoopID,\
          leveranciers.c.bedrijfsnaam.ilike('%'+zoekterm+'%')))
    elif keuze == 4:
       sel = select([orders_inkoop_artikelen,orders_inkoop, leveranciers,artikelen])\
         .where(and_(orders_inkoop.c.leverancierID == leveranciers.c.leverancierID,\
         orders_inkoop_artikelen.c.orderinkoopID == orders_inkoop.c.orderinkoopID,\
         orders_inkoop_artikelen.c.artikelID == artikelen.c.artikelID,\
          artikelen.c.artikelomschrijving.ilike('%'+zoekterm+'%')))
    elif keuze == 5 and validZt.zt(zoekterm, 4):
        sel = select([orders_inkoop_artikelen,orders_inkoop, leveranciers,artikelen])\
         .where(and_(orders_inkoop.c.leverancierID == leveranciers.c.leverancierID,\
            orders_inkoop_artikelen.c.artikelID == artikelen.c.artikelID,\
         orders_inkoop_artikelen.c.orderinkoopID == orders_inkoop.c.orderinkoopID,
         orders_inkoop_artikelen.c.orderinkoopID == int(zoekterm))).order_by(\
             orders_inkoop_artikelen.c.orderinkoopID, orders_inkoop_artikelen.c.regel)
    elif keuze == 6 and validZt.zt(zoekterm, 10):
        sel = select([orders_inkoop_artikelen,orders_inkoop, leveranciers,artikelen])\
         .where(and_(orders_inkoop.c.leverancierID == leveranciers.c.leverancierID,\
         orders_inkoop_artikelen.c.artikelID == artikelen.c.artikelID,\
         orders_inkoop_artikelen.c.orderinkoopID == orders_inkoop.c.orderinkoopID,
         orders_inkoop_artikelen.c.levering_start.like(zoekterm+'%')))
    elif keuze == 7 and validZt.zt(zoekterm, 10):
        sel = select([orders_inkoop_artikelen,orders_inkoop, leveranciers,artikelen])\
         .where(and_(orders_inkoop.c.leverancierID == leveranciers.c.leverancierID,\
         orders_inkoop_artikelen.c.artikelID == artikelen.c.artikelID,\
         orders_inkoop_artikelen.c.orderinkoopID == orders_inkoop.c.orderinkoopID,
         orders_inkoop_artikelen.c.levering_eind.like(zoekterm+'%')))
    else:
        ongInvoer()
        inkooporderKeuze(m_email)
        
    if con.execute(sel).fetchone():
        rpinkorders = con.execute(sel)
        logger.debug("opvrOrder(keuze=%s,zoekterm=%s,m_email=%s): rpinkorders → %s", keuze, zoekterm, m_email, rpinkorders)
    else:
        geenRecord()
        inkooporderKeuze(m_email)
 
    class Window(QDialog):
       logger.debug("<<< Exiting opvrOrder(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email)
       def __init__(self, data_list, header, *args):
            QWidget.__init__(self, *args,)
            self.setGeometry(100, 50, 1600, 900)
            self.setWindowTitle('Request purchase orders')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
            table_model = MyTableModel(self, data_list, header)
            table_view = QTableView()
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.resizeColumnsToContents()
            table_view.setColumnHidden(1,True)
            table_view.setColumnHidden(2,True)
            table_view.setColumnHidden(16,True)
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.setColumnWidth(28, 100)
            table_view.verticalHeader().setDefaultSectionSize(75)
            table_view.setItemDelegateForColumn(28, showImage(self))
            table_view.clicked.connect(showOrder)
            layout = QVBoxLayout(self)
            layout.addWidget(table_view)
            self.setLayout(layout)
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
           logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
           logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit)
           logger.debug("__init__(parent=%s): self.Orderinkoopnummer → %s", parent, self.Orderinkoopnummer)
           logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit)
           logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit)
           logger.debug("__init__(parent=%s): self.Leveranciernummer → %s", parent, self.Leveranciernummer)
           logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit)
           logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit)
           logger.debug("__init__(parent=%s): self.Besteldatum → %s", parent, self.Besteldatum)
           logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit)
           logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit)
           logger.debug("__init__(parent=%s): self.Goedgekeurd → %s", parent, self.Goedgekeurd)
           logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit)
           logger.debug("__init__(parent=%s): q11Edit → %s", parent, q11Edit)
           logger.debug("__init__(parent=%s): self.Betaald → %s", parent, self.Betaald)
           logger.debug("__init__(self=%s,parent=%s): q11Edit → %s", self, parent, q11Edit)
           logger.debug("__init__(parent=%s): q12Edit → %s", parent, q12Edit)
           logger.debug("__init__(parent=%s): self.Afgemeld → %s", parent, self.Afgemeld)
           logger.debug("__init__(self=%s,parent=%s): q12Edit → %s", self, parent, q12Edit)
           logger.debug("__init__(parent=%s): q13Edit → %s", parent, q13Edit)
           logger.debug("__init__(self=%s,parent=%s): q13Edit → %s", self, parent, q13Edit)
           logger.debug("__init__(parent=%s): q19Edit → %s", parent, q19Edit)
           logger.debug("__init__(parent=%s): self.Bedrijfsnaam → %s", parent, self.Bedrijfsnaam)
           logger.debug("__init__(self=%s,parent=%s): q19Edit → %s", self, parent, q19Edit)
           logger.debug("__init__(parent=%s): q14Edit → %s", parent, q14Edit)
           logger.debug("__init__(parent=%s): self.Rechtsvorm → %s", parent, self.Rechtsvorm)
           logger.debug("__init__(self=%s,parent=%s): q14Edit → %s", self, parent, q14Edit)
           logger.debug("__init__(parent=%s): q15Edit → %s", parent, q15Edit)
           logger.debug("__init__(parent=%s): self.Artikelnummer → %s", parent, self.Artikelnummer)
           logger.debug("__init__(self=%s,parent=%s): q15Edit → %s", self, parent, q15Edit)
           logger.debug("__init__(parent=%s): q16Edit → %s", parent, q16Edit)
           logger.debug("__init__(parent=%s): self.Artikelomschrijving → %s", parent, self.Artikelomschrijving)
           logger.debug("__init__(self=%s,parent=%s): q16Edit → %s", self, parent, q16Edit)
           logger.debug("__init__(parent=%s): q18Edit → %s", parent, q18Edit)
           logger.debug("__init__(parent=%s): self.Bestelaantal → %s", parent, self.Bestelaantal)
           logger.debug("__init__(self=%s,parent=%s): q18Edit → %s", self, parent, q18Edit)
           logger.debug("__init__(parent=%s): q17Edit → %s", parent, q17Edit)
           logger.debug("__init__(parent=%s): self.Inkoopprijs → %s", parent, self.Inkoopprijs)
           logger.debug("__init__(self=%s,parent=%s): q17Edit → %s", self, parent, q17Edit)
           logger.debug("__init__(parent=%s): q20Edit → %s", parent, q20Edit)
           logger.debug("__init__(parent=%s): self.Levering_start → %s", parent, self.Levering_start)
           logger.debug("__init__(self=%s,parent=%s): q20Edit → %s", self, parent, q20Edit)
           logger.debug("__init__(parent=%s): q28Edit → %s", parent, q28Edit)
           logger.debug("__init__(parent=%s): self.Levering_eind → %s", parent, self.Levering_eind)
           logger.debug("__init__(self=%s,parent=%s): q28Edit → %s", self, parent, q28Edit)
           logger.debug("__init__(parent=%s): q21Edit → %s", parent, q21Edit)
           logger.debug("__init__(parent=%s): self.Reclamatiedatum → %s", parent, self.Reclamatiedatum)
           logger.debug("__init__(self=%s,parent=%s): q21Edit → %s", self, parent, q21Edit)
           logger.debug("__init__(parent=%s): q22Edit → %s", parent, q22Edit)
           logger.debug("__init__(parent=%s): self.Reclamatieaantal → %s", parent, self.Reclamatieaantal)
           logger.debug("__init__(self=%s,parent=%s): q22Edit → %s", self, parent, q22Edit)
           logger.debug("__init__(parent=%s): q23Edit → %s", parent, q23Edit)
           logger.debug("__init__(parent=%s): self.Ontvangdatum → %s", parent, self.Ontvangdatum)
           logger.debug("__init__(self=%s,parent=%s): q23Edit → %s", self, parent, q23Edit)
           logger.debug("__init__(parent=%s): q24Edit → %s", parent, q24Edit)
           logger.debug("__init__(parent=%s): self.Ontvangstaantal → %s", parent, self.Ontvangstaantal)
           logger.debug("__init__(self=%s,parent=%s): q24Edit → %s", self, parent, q24Edit)
           logger.debug("__init__(parent=%s): q25Edit → %s", parent, q25Edit)
           logger.debug("__init__(parent=%s): self.Acceptatiedatum → %s", parent, self.Acceptatiedatum)
           logger.debug("__init__(self=%s,parent=%s): q25Edit → %s", self, parent, q25Edit)
           logger.debug("__init__(parent=%s): q26Edit → %s", parent, q26Edit)
           logger.debug("__init__(parent=%s): self.Aantalgeaccepteerd → %s", parent, self.Aantalgeaccepteerd)
           logger.debug("__init__(self=%s,parent=%s): q26Edit → %s", self, parent, q26Edit)
           logger.debug("__init__(parent=%s): q27Edit → %s", parent, q27Edit)
           logger.debug("__init__(parent=%s): self.Betaaldaantal → %s", parent, self.Betaaldaantal)
           logger.debug("__init__(self=%s,parent=%s): q27Edit → %s", self, parent, q27Edit)
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
   
    header = ['Order articleID','Order purchase number','Article number', 'Order quantity',\
              'Purchase price','Delivery start','Delivery end', 'Complaint date', 'Complaint number', \
              'Receive date', 'Receive number', 'Acceptance date','Acceptance number',\
              'Payed', 'Line number','Order purchase number', 'Supplier number',\
              'Order date', 'Approved','Payed', 'Unsubscribed','Supplier number',\
              'Company name', 'Legal status', 'Article number','Article description',\
              'Article stock', 'Article unit', 'Image']
        
    data_list=[]
    for row in rpinkorders:
        data_list += [(row)]  
        
    def showOrder(idx):
        logger.debug(">>> Entering showOrder(idx=%s)", idx)
        mordartlevnr = idx.data()
        logger.debug("showOrder(idx=%s): mordartlevnr → %s", idx, mordartlevnr)
        engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
        con = engine.connect()
        engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
        logger.debug("showOrder(idx=%s): engine → %s", idx, engine)
        con = engine.connect()
        logger.debug("showOrder(idx=%s): con → %s", idx, con)
        if idx.column() == 0:
            seloal = select([orders_inkoop_artikelen, orders_inkoop, leveranciers, artikelen]).\
               where(and_(orders_inkoop.c.leverancierID == leveranciers.c.\
               leverancierID, orders_inkoop_artikelen.c.artikelID == artikelen.c.\
               artikelID, orders_inkoop_artikelen.c.orderinkoopID == orders_inkoop.c.\
               orderinkoopID, orders_inkoop_artikelen.c.ordartlevID == mordartlevnr))
            rpordartlev = con.execute(seloal).first()
            
            class Widget(QDialog):
                 logger.debug("showOrder(idx=%s): seloal → %s", idx, seloal)
                 def __init__(self, parent=None):
                    super(Widget, self).__init__(parent)
                    logger.debug("<<< Exiting showOrder(idx=%s)", idx)
                    self.setWindowTitle("Request purchase orders for materials")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                                          
                    self.setFont(QFont('Arial', 10))
                        
                    self.Orderinkoopnummer = QLabel()
                    q2Edit = QLineEdit(str(rpordartlev[15]))
                    q2Edit.setAlignment(Qt.AlignRight)
                    q2Edit.setFixedWidth(90)
                    q2Edit.setDisabled(True)
                    q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
        
                    self.Leveranciernummer = QLabel()
                    q4Edit = QLineEdit(str(rpordartlev[16]))
                    q4Edit.setFixedWidth(90)
                    q4Edit.setAlignment(Qt.AlignRight)
                    q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q4Edit.setDisabled(True)
         
                    self.Besteldatum = QLabel()
                    q5Edit = QLineEdit(str(rpordartlev[17]))
                    q5Edit.setFixedWidth(90)
                    q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q5Edit.setDisabled(True)                              
                    
                    self.Goedgekeurd = QLabel()
                    q8Edit = QLineEdit(str(rpordartlev[18]))
                    q8Edit.setFixedWidth(90)
                    q8Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q8Edit.setDisabled(True)
                                                         
                    self.Betaald = QLabel()
                    q11Edit = QLineEdit(str(rpordartlev[19]))
                    q11Edit.setFixedWidth(90)
                    q11Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q11Edit.setDisabled(True)
                      
                    self.Afgemeld = QLabel()
                    q12Edit = QLineEdit(str(rpordartlev[20]))
                    q12Edit.setFixedWidth(90)
                    q12Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q12Edit.setDisabled(True)
                     
                    self.Leveranciernummer = QLabel()
                    q13Edit = QLineEdit(str(rpordartlev[21]))
                    q13Edit.setFixedWidth(100)
                    q13Edit.setAlignment(Qt.AlignRight)
                    q13Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q13Edit.setDisabled(True)
             
                    self.Bedrijfsnaam = QLabel()
                    q19Edit = QLineEdit(str(rpordartlev[22]))
                    q19Edit.setFixedWidth(380)
                    q19Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q19Edit.setDisabled(True)
             
                    self.Rechtsvorm = QLabel()
                    q14Edit = QLineEdit(str(rpordartlev[23]))
                    q14Edit.setFixedWidth(100)
                    q14Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q14Edit.setDisabled(True)
                                    
                    self.Artikelnummer= QLabel()
                    q15Edit = QLineEdit(str(rpordartlev[24]))
                    q15Edit.setDisabled(True)
                    q15Edit.setFixedWidth(100)
                    q15Edit.setAlignment(Qt.AlignRight)
                    q15Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q15Edit.setDisabled(True)
          
                    self.Artikelomschrijving = QLabel()
                    q16Edit = QLineEdit(str(rpordartlev[25]))
                    q16Edit.setFixedWidth(370)
                    q16Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q16Edit.setDisabled(True)
                        
                    self.Bestelaantal = QLabel()
                    q18Edit = QLineEdit('{:12.2f}'.format(rpordartlev[3]))
                    q18Edit.setFixedWidth(90)
                    q18Edit.setAlignment(Qt.AlignRight)
                    q18Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q18Edit.setDisabled(True)
                    
                    self.Inkoopprijs = QLabel()
                    q17Edit = QLineEdit('{:12.2f}'.format(rpordartlev[4]))
                    q17Edit.setFixedWidth(100)
                    q17Edit.setAlignment(Qt.AlignRight)
                    q17Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q17Edit.setDisabled(True)
                    
                    self.Levering_start = QLabel()
                    q20Edit = QLineEdit(str(rpordartlev[5]))
                    q20Edit.setFixedWidth(100)
                    q20Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q20Edit.setDisabled(True)
                                   
                    self.Levering_eind = QLabel()
                    q28Edit = QLineEdit(str(rpordartlev[6]))
                    q28Edit.setFixedWidth(100)
                    q28Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q28Edit.setDisabled(True)
                    
                    self.Reclamatiedatum = QLabel()
                    q21Edit = QLineEdit(str(rpordartlev[7]))
                    q21Edit.setFixedWidth(100)
                    q21Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q21Edit.setDisabled(True)
        
                    self.Reclamatieaantal = QLabel()
                    q22Edit = QLineEdit('{:12.2f}'.format(rpordartlev[8]))
                    q22Edit.setFixedWidth(100)
                    q22Edit.setAlignment(Qt.AlignRight)
                    q22Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q22Edit.setDisabled(True)
        
                    self.Ontvangdatum = QLabel()
                    q23Edit = QLineEdit(str(rpordartlev[9]))
                    q23Edit.setFixedWidth(100)
                    q23Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q23Edit.setDisabled(True)
                    
                    self.Ontvangstaantal = QLabel()
                    q24Edit = QLineEdit('{:12.2f}'.format(rpordartlev[10]))
                    q24Edit.setFixedWidth(100)
                    q24Edit.setAlignment(Qt.AlignRight)
                    q24Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q24Edit.setDisabled(True)
                    
                    self.Acceptatiedatum = QLabel()
                    q25Edit = QLineEdit(str(rpordartlev[11]))
                    q25Edit.setFixedWidth(100)
                    q25Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q25Edit.setDisabled(True)
                    
                    self.Aantalgeaccepteerd = QLabel()
                    q26Edit = QLineEdit('{:12.2f}'.format(rpordartlev[12]))
                    q26Edit.setFixedWidth(100)
                    q26Edit.setAlignment(Qt.AlignRight)
                    q26Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q26Edit.setDisabled(True)
                    
                    self.Betaaldaantal = QLabel()
                    q27Edit = QLineEdit('{:12.2f}'.format(rpordartlev[13]))
                    q27Edit.setFixedWidth(100)
                    q27Edit.setAlignment(Qt.AlignRight)
                    q27Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q27Edit.setDisabled(True) 
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                    
                    lbl = QLabel()
                    pixmap = QPixmap('./images/logos/verbinding.jpg')
                    lbl.setPixmap(pixmap)
                    grid.addWidget(lbl ,0 , 0)
                    
                    logo = QLabel()
                    pixmap = QPixmap('./images/logos/logo.jpg')
                    logo.setPixmap(pixmap)
                    grid.addWidget(logo , 0, 5, 1, 1, Qt.AlignRight)
            
                    self.setFont(QFont('Arial', 10))
                    
                    lbl1 = QLabel('Order details')
                    lbl1.setStyleSheet("font: 12pt Comic Sans MS")
                    grid.addWidget(lbl1, 1, 0)
                    grid.addWidget(QLabel('Order purchase number'), 2, 0)
                    grid.addWidget(q2Edit, 2, 1) 
                                                        
                    grid.addWidget(QLabel('Supplier number'), 2, 2)
                    grid.addWidget(q4Edit, 2, 3)
                    
                    grid.addWidget(QLabel('Order date'), 2, 4)
                    grid.addWidget(q5Edit, 2 , 5) 
                     
                    grid.addWidget(QLabel('Approved'), 3, 0)
                    grid.addWidget(q8Edit, 3, 1)
                                                              
                    grid.addWidget(QLabel('Pay date'), 3, 2)
                    grid.addWidget(q11Edit, 3, 3)
                                              
                    grid.addWidget(QLabel('Unsubscribed'), 3, 4)
                    grid.addWidget(q12Edit, 3, 5)
         
                    lbl2 = QLabel('Order line data'+' - line number: '+str(rpordartlev[14]))
                    lbl2.setStyleSheet("font: 12pt Comic Sans MS")               
                    grid.addWidget(lbl2, 5, 0, 1, 4)
                    grid.addWidget(QLabel('Suppler number'), 6, 0)
                    grid.addWidget(q13Edit, 6, 1) 
                    
                    grid.addWidget(QLabel('Company name'), 7, 0)
                    grid.addWidget(q19Edit, 7, 1, 1, 4) 
                                   
                    grid.addWidget(q14Edit, 7, 4) 
               
                    grid.addWidget(QLabel('Articl enumber'), 8, 0)
                    grid.addWidget(q15Edit, 8, 1) 
                     
                    pixmap = QPixmap(rpordartlev[28])
                    lbl3 = QLabel()
                    lbl3.setPixmap(pixmap)
                    grid.addWidget(lbl3 , 8, 3, 2, 3, Qt.AlignTop)
                            
                    grid.addWidget(QLabel('Article description'), 10, 0)
                    grid.addWidget(q16Edit, 10, 1, 1, 4)
                    
                    grid.addWidget(QLabel('Order quantity'), 11, 0)
                    grid.addWidget(q18Edit, 11, 1)
                    
                    grid.addWidget(QLabel('Purchase price'), 11, 2)
                    grid.addWidget(q17Edit, 11, 3)
                    
                    grid.addWidget(QLabel('Delivery start'), 11, 4)
                    grid.addWidget(q20Edit, 11, 5)
                    
                    grid.addWidget(QLabel('Delivery end'), 12, 0)
                    grid.addWidget(q28Edit, 12, 1)
                                   
                    grid.addWidget(QLabel('Complaint date'), 12, 2)
                    grid.addWidget(q21Edit, 12, 3)
                    
                    grid.addWidget(QLabel('Complaints number'), 12, 4)
                    grid.addWidget(q22Edit, 12, 5)
                    
                    grid.addWidget(QLabel('Received date'), 13, 0)
                    grid.addWidget(q23Edit, 13, 1)
                    
                    grid.addWidget(QLabel('Received number'), 13, 2)
                    grid.addWidget(q24Edit, 13, 3)
                    
                    grid.addWidget(QLabel('Approval date'), 13,  4)
                    grid.addWidget(q25Edit, 13, 5)
                    
                    grid.addWidget(QLabel('Approval number'), 14, 0)
                    grid.addWidget(q26Edit, 14, 1)
                    
                    grid.addWidget(QLabel('Payed number'), 14, 2)
                    grid.addWidget(q27Edit, 14, 3)
                                                              
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 16, 0, 1, 6, Qt.AlignCenter)
                    self.setLayout(grid)
                    self.setGeometry(500, 200, 350, 300)
                                               
                    cancelBtn = QPushButton('Close')
                    cancelBtn.clicked.connect(self.close)
                
                    grid.addWidget(cancelBtn, 15, 5, 1, 1, Qt.AlignRight)
                    logger.debug("<<< Exiting __init__(parent=%s)", parent)
                    cancelBtn.setFont(QFont("Arial",10))
                    cancelBtn.setFixedWidth(100)
                    cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            window = Widget()
            window.exec_()
                                   
    win = Window(data_list, header)
    win.exec_()
    inkooporderKeuze(m_email)