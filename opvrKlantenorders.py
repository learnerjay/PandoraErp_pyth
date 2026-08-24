from login import hoofdMenu
from datetime import datetime 
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor, QImage
from PyQt5.QtWidgets import QWidget, QMessageBox, QDialog, QStyledItemDelegate,\
      QTableView, QVBoxLayout
from sqlalchemy import (Table, Column, Integer, String, Float, MetaData, \
                            ForeignKey, create_engine, DateTime, select)
import logging
logger = logging.getLogger(__name__)
                    
def geenOrders():
    logger.debug(">>> Entering geenOrders()")
    msg = QMessageBox()
    logger.debug("geenOrders(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No orders present!')
    msg.setWindowTitle('Request order overview')               
    logger.debug("<<< Exiting geenOrders()")
    msg.exec_()
    
def bestellingen(m_email):
    logger.debug(">>> Entering bestellingen(m_email=%s)", m_email)
    metadata = MetaData()
    logger.debug("bestellingen(m_email=%s): metadata → %s", m_email, metadata)
    accounts = Table('accounts', metadata,
        Column('accountID', Integer(), primary_key=True),
        Column('email', String, nullable=False))
    klanten = Table('klanten', metadata,
        Column('klantID', Integer(), primary_key=True),
        Column('accountID', None, ForeignKey('accounts.accountID')))
    orders_verkoop = Table('orders_verkoop', metadata,
        Column('ovbestelID', Integer, primary_key=True),
        Column('klantID', None, ForeignKey('klanten.klantID')),
        Column('ovbesteldatum', DateTime(), default=datetime.now),
        Column('datum_betaald', String))
    orders_verkoop_artikelen = Table('orders_verkoop_artikelen', metadata,
        Column('ovaID', Integer, primary_key=True),
        Column('ovbestelID', None, ForeignKey('orders_verkoop.ovbestelID')),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('ovaantal', Integer),
        Column('ovleverdatum', DateTime()),
        Column('verkoopprijs', Float),
        Column('retour',Float))
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer, primary_key=True),
        Column('artikelomschrijving', String(50)),
        Column('thumb_artikel', String(70)))
          
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("bestellingen(m_email=%s): engine → %s", m_email, engine)
    con = engine.connect()
    sel = select([accounts.c.accountID, accounts.c.email]).\
            where(accounts.c.email == m_email)
    logger.debug("bestellingen(m_email=%s): sel → %s", m_email, sel)
    rpaccount = con.execute(sel).first()
    maccountnr = rpaccount[0]
    maccountnr = int(maccountnr)
    logger.debug("bestellingen(m_email=%s): rpaccount → %s", m_email, rpaccount)
    m_email = rpaccount[1]
    con = engine.connect()
    logger.debug("bestellingen(m_email=%s): con → %s", m_email, con)
    logger.debug("bestellingen(m_email=%s): maccountnr → %s", m_email, maccountnr)
    columns = [orders_verkoop.c.ovbestelID,\
        orders_verkoop.c.ovbesteldatum, orders_verkoop.c.datum_betaald,\
        orders_verkoop_artikelen.c.ovleverdatum,\
        orders_verkoop_artikelen.c.ovaantal, artikelen.c.artikelID,\
        artikelen.c.artikelomschrijving, orders_verkoop_artikelen.c.verkoopprijs,\
        artikelen.c.thumb_artikel, orders_verkoop_artikelen.c.retour]
    bestellingen = select(columns).where(accounts.c.email == m_email)
    bestellingen = bestellingen.select_from(accounts.join(klanten)\
               .join(orders_verkoop).join(orders_verkoop_artikelen)\
               .join(artikelen)).order_by(orders_verkoop_artikelen.c.ovbestelID, orders_verkoop_artikelen.c.artikelID)
    
    if con.execute(bestellingen).fetchone():
        rp_bestellingen = con.execute(bestellingen)
        logger.debug("bestellingen(m_email=%s): columns → %s", m_email, columns)
    else:
        geenOrders()
        logger.debug("bestellingen(m_email=%s): bestellingen → %s", m_email, bestellingen)
        hoofdMenu(m_email)
    toonBest(rp_bestellingen, m_email)
    logger.debug("bestellingen(m_email=%s): rp_bestellingen → %s", m_email, rp_bestellingen)
    logger.debug("<<< Exiting bestellingen(m_email=%s)", m_email)
        
def toonBest(rp_bestellingen, m_email):
    logger.debug(">>> Entering toonBest(rp_bestellingen=%s,m_email=%s)", rp_bestellingen, m_email)
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            logger.debug(">>> Entering __init__(data_list=%s,header=%s)", data_list, header)
            QWidget.__init__(self, *args,)
            self.setGeometry(50, 50, 1500, 900)
            self.setWindowTitle('Order overview')
            logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font)
            logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view)
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
            table_model = MyTableModel(self, data_list, header)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_model → %s", self, data_list, header, table_model)
            logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model)
            table_view = QTableView()
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_view → %s", self, data_list, header, table_view)
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): font → %s", self, data_list, header, font)
            table_view.setFont(font)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.setColumnWidth(8, 100)
            table_view.verticalHeader().setDefaultSectionSize(75)
            table_view.setItemDelegateForColumn(8, showImage(self))
            #table_view.clicked.connect(showBestelling)
            layout = QVBoxLayout(self)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): layout → %s", self, data_list, header, layout)
            logger.debug("__init__(data_list=%s,header=%s): layout → %s", data_list, header, layout)
            layout.addWidget(table_view)
            self.setLayout(layout)
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header)
            logger.debug(">>> Entering __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header)
            logger.debug("<<< Exiting __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header)
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.mylist → %s", self, parent, mylist, header, self.mylist)

    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.header → %s", self, parent, mylist, header, self.header)
            QAbstractTableModel.__init__(self, parent, *args)
            self.mylist = mylist
            logger.debug(">>> Entering __init__(parent=%s)", parent)
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
   
    header = ['Order','Order date', 'Pay date','Delivery date', 'Quantity',\
              'Article number','Description','Selling price', 'Image', 'Return']
    
    data_list=[]
    for row in rp_bestellingen:
        data_list += [(row)]
               
    win = MyWindow(data_list, header)
    win.exec_()
    hoofdMenu(m_email)