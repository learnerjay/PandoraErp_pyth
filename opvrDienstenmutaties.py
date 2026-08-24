from login import hoofdMenu
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import  QLabel, QPushButton, QWidget, QGridLayout, QVBoxLayout,\
     QComboBox, QDialog, QLineEdit, QMessageBox, QTableView
from sqlalchemy import (Table, Column, Integer, Float, String, MetaData, ForeignKey,\
                       create_engine)
from sqlalchemy.sql import select, and_
import logging
logger = logging.getLogger(__name__)

def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)

def geenRecord():
    logger.debug(">>> Entering geenRecord()")
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No record found\ncreate another selection please!')
    msg.setWindowTitle('Request services / Equipment')
    logger.debug("<<< Exiting geenRecord()")
    msg.exec_() 
    
def ongInvoer():
    logger.debug(">>> Entering ongInvoer()")
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Please re-enter incorrect input\nsearch term!')
    msg.setWindowTitle('Request services / Equipment')
    logger.debug("<<< Exiting ongInvoer()")
    msg.exec_()
        
def mutatieKeuze(m_email):
    logger.debug(">>> Entering mutatieKeuze(m_email=%s)", m_email)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            self.setWindowTitle("Request changes services-portal accounting")
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
            k0Edit.addItem('      Search sort key')
            k0Edit.addItem('1. All mutations')
            k0Edit.addItem('2. Work number')
            k0Edit.addItem('3. Work description')
            k0Edit.addItem('4. Supplier number')
            k0Edit.addItem('5. Company name')
            k0Edit.addItem('6. By sales order')
            k0Edit.addItem('7. Cost type (1-8)')
            k0Edit.addItem('8. Booking date yyyy(-mm(-dd))')
            k0Edit.activated[str].connect(self.k0Changed)
                            
            self.Zoekterm = QLabel()
            logger.debug("__init__(parent=%s): self.Zoekterm → %s", parent, self.Zoekterm)
            zktermEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): zktermEdit → %s", self, parent, zktermEdit)
            logger.debug("__init__(parent=%s): zktermEdit → %s", parent, zktermEdit)
            zktermEdit.setFixedWidth(230)
            zktermEdit.setFont(QFont("Arial",10))
            zktermEdit.textChanged.connect(self.zktermChanged)
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
     
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
            grid.addWidget(lbl , 0, 0, 1, 2)
            
            logo = QLabel()
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
                                  
            grid.addWidget(k0Edit, 1, 1)
            lbl1 = QLabel('Search term')
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1)
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1)
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 2, 0)
            grid.addWidget(zktermEdit, 2, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1, 3 , Qt.AlignCenter)
   
            applyBtn = QPushButton('Search')
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 3, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn)
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn)
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 3, 1)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
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
    if data[0]:
        keuze = int(data[0][0])
    else:
        ongInvoer()
        mutatieKeuze(m_email)
    if data[1]:
        zoekterm = data[1]
    else:
        zoekterm = ''
    toonMutaties(keuze, zoekterm, m_email)

def toonMutaties(keuze,zoekterm, m_email):
    logger.debug(">>> Entering toonMutaties(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email)
    import validZt
    metadata = MetaData()
    logger.debug("toonMutaties(keuze=%s,zoekterm=%s,m_email=%s): metadata → %s", keuze, zoekterm, m_email, metadata)
    dienstenmutaties = Table('dienstenmutaties', metadata,
        Column('mutatieID', Integer, primary_key=True),
        Column('werknummerID', None, ForeignKey('werken.werknummerID')),
        Column('orderinkoopID', None, ForeignKey('orders_inkoop.orderinkoopID')),
        Column('boekbedrag', Float),
        Column('boekdatum', String),
        Column('leverancierID', None, ForeignKey('leveranciers.leverancierID')),
        Column('werkomschr', String),
        Column('btw_hoog', Float),
        Column('omschrijving', String),
        Column('regel', Integer))
    werken = Table('werken', metadata,
        Column('werknummerID', Integer(), primary_key=True),
        Column('werkomschrijving', String(50)))
    orders_inkoop = Table('orders_inkoop', metadata,
        Column('orderinkoopID', Integer, primary_key=True),
        Column('leverancierID', None, ForeignKey('leveranciers.leverancierID')))
    leveranciers = Table('leveranciers', metadata,
        Column('leverancierID', Integer, primary_key=True),
        Column('bedrijfsnaam',  String),
        Column('rechtsvorm', String))
                    
    engine = create_engine('postgresql://postgres@localhost/bisystem')
    logger.debug("toonMutaties(keuze=%s,zoekterm=%s,m_email=%s): engine → %s", keuze, zoekterm, m_email, engine)
    conn = engine.connect()
    logger.debug("toonMutaties(keuze=%s,zoekterm=%s,m_email=%s): conn → %s", keuze, zoekterm, m_email, conn)
   
    if keuze == 1:
        sel = select([dienstenmutaties, werken, orders_inkoop, leveranciers])\
           .where(and_(werken.c.werknummerID==dienstenmutaties.c.werknummerID,\
            leveranciers.c.leverancierID == dienstenmutaties.c.leverancierID,\
            orders_inkoop.c.orderinkoopID==dienstenmutaties.c.orderinkoopID))\
            .order_by(werken.c.werknummerID)
        logger.debug("toonMutaties(keuze=%s,zoekterm=%s,m_email=%s): sel → %s", keuze, zoekterm, m_email, sel)
    elif keuze == 2 and validZt.zt(zoekterm, 8):
        sel = select([dienstenmutaties, werken, orders_inkoop, leveranciers])\
            .where(and_(werken.c.werknummerID==dienstenmutaties.c.werknummerID,\
            leveranciers.c.leverancierID == dienstenmutaties.c.leverancierID,\
            orders_inkoop.c.orderinkoopID==dienstenmutaties.c.orderinkoopID,\
           werken.c.werknummerID== int(zoekterm)))
    elif keuze == 3:
        sel = select([dienstenmutaties, werken, orders_inkoop, leveranciers])\
            .where(and_(werken.c.werknummerID==dienstenmutaties.c.werknummerID,\
            leveranciers.c.leverancierID == dienstenmutaties.c.leverancierID,\
            orders_inkoop.c.orderinkoopID==dienstenmutaties.c.orderinkoopID,\
           werken.c.werkomschrijving.ilike('%'+zoekterm+'%')))\
           .order_by(werken.c.werknummerID)
    elif keuze == 4 and validZt.zt(zoekterm, 3):
        sel = select([dienstenmutaties, werken, orders_inkoop, leveranciers])\
            .where(and_(werken.c.werknummerID==dienstenmutaties.c.werknummerID,\
            leveranciers.c.leverancierID == dienstenmutaties.c.leverancierID,\
            orders_inkoop.c.orderinkoopID==dienstenmutaties.c.orderinkoopID,\
           leveranciers.c.leverancierID == int(zoekterm)))
    elif keuze == 5:
        sel = select([dienstenmutaties, werken, orders_inkoop, leveranciers])\
            .where(and_(werken.c.werknummerID==dienstenmutaties.c.werknummerID,\
            leveranciers.c.leverancierID == dienstenmutaties.c.leverancierID,\
            orders_inkoop.c.orderinkoopID==dienstenmutaties.c.orderinkoopID,\
           leveranciers.c.bedrijfsnaam.ilike('%'+zoekterm+'%')))
    elif keuze == 6 and validZt.zt(zoekterm, 5):
        sel = select([dienstenmutaties, werken, orders_inkoop, leveranciers])\
            .where(and_(werken.c.werknummerID==dienstenmutaties.c.werknummerID,\
            leveranciers.c.leverancierID == dienstenmutaties.c.leverancierID,\
            orders_inkoop.c.orderinkoopID==dienstenmutaties.c.orderinkoopID,\
            orders_inkoop.c.orderinkoopID== int(zoekterm)))
    elif keuze == 7 and validZt.zt(zoekterm, 16):
        sel = select([dienstenmutaties, werken, orders_inkoop, leveranciers])\
            .where(and_(werken.c.werknummerID==dienstenmutaties.c.werknummerID,\
            leveranciers.c.leverancierID == dienstenmutaties.c.leverancierID,\
            orders_inkoop.c.orderinkoopID==dienstenmutaties.c.orderinkoopID,\
           dienstenmutaties.c.werkomschr.like(zoekterm+'%')))\
           .order_by(dienstenmutaties.c.werkomschr)
    elif keuze == 8 and validZt.zt(zoekterm, 10):
        sel = select([dienstenmutaties, werken, orders_inkoop, leveranciers])\
            .where(and_(werken.c.werknummerID==dienstenmutaties.c.werknummerID,\
            leveranciers.c.leverancierID == dienstenmutaties.c.leverancierID,\
            orders_inkoop.c.orderinkoopID==dienstenmutaties.c.orderinkoopID,\
             dienstenmutaties.c.boekdatum.ilike(zoekterm+'%')))\
           .order_by(dienstenmutaties.c.boekdatum)
    else:
       ongInvoer()
       mutatieKeuze(m_email)
       
    if conn.execute(sel).fetchone():
        rp = conn.execute(sel)
        logger.debug("toonMutaties(keuze=%s,zoekterm=%s,m_email=%s): rp → %s", keuze, zoekterm, m_email, rp)
    else:
        geenRecord()
        mutatieKeuze(m_email)
       
    class MyWindow(QDialog):
        logger.debug("<<< Exiting toonMutaties(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email)
        def __init__(self, data_list, header, *args):
            QWidget.__init__(self, *args,)
            self.setGeometry(50, 50, 1800, 900)
            self.setWindowTitle('Request services mutations')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
            table_model = MyTableModel(self, data_list, header)
            table_view = QTableView()
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.setColumnHidden(1, True)
            table_view.setColumnHidden(2, True)
            table_view.setColumnHidden(5, True)
            table_view.setColumnHidden(12, True)
            #table_view.clicked.connect(showAccount)
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
  
    header = ['Mutation number','Work number', 'Supplier orderID','Amount booking', 'Booking date', 'SupplierID',\
              'Category work','VAT high', 'Description', 'Line number', 'Work number', 'Description',\
              'Supplier orderID', 'SupplierID', 'SupplierID','Company name', 'Legal status']
    
    data_list=[]
    for row in rp:
        data_list += [(row)] 
    
    win = MyWindow(data_list, header)
    win.exec_()
    mutatieKeuze(m_email)