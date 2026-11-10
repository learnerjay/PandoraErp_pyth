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
    logger.warning(">>> Entering geenOrders()", extra={"event.action": "geenOrders"})
    msg = QMessageBox()
    logger.debug("geenOrders(): msg → %s", msg, extra={"event.action": "geenOrders"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen bestellingen aanwezig!')
    msg.setWindowTitle('Besteloverzicht opvragen')               
    logger.debug("<<< Exiting geenOrders()", extra={"event.action": "geenOrders"})
    msg.exec_()
    
def bestellingen(m_email):
    logger.warning(">>> Entering bestellingen(m_email=%s)", m_email, extra={"event.action": "bestellingen"})
    metadata = MetaData()
    logger.debug("bestellingen(m_email=%s): metadata → %s", m_email, metadata, extra={"event.action": "bestellingen"})
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
    logger.debug("bestellingen(m_email=%s): engine → %s", m_email, engine, extra={"event.action": "bestellingen"})
    con = engine.connect()
    logger.debug("bestellingen(m_email=%s): con → %s", m_email, con, extra={"event.action": "bestellingen"})
    sel = select([accounts.c.accountID, accounts.c.email]).\
            where(accounts.c.email == m_email)
    logger.debug("bestellingen(m_email=%s): sel → %s", m_email, sel, extra={"event.action": "bestellingen"})
    rpaccount = con.execute(sel).first()
    logger.debug("bestellingen(m_email=%s): rpaccount → %s", m_email, rpaccount, extra={"event.action": "bestellingen"})
    maccountnr = rpaccount[0]
    maccountnr = int(maccountnr)
    logger.debug("bestellingen(m_email=%s): maccountnr → %s", m_email, maccountnr, extra={"event.action": "bestellingen"})
    m_email = rpaccount[1]
    con = engine.connect()
    columns = [orders_verkoop.c.ovbestelID,\
        orders_verkoop.c.ovbesteldatum, orders_verkoop.c.datum_betaald,\
        orders_verkoop_artikelen.c.ovleverdatum,\
        orders_verkoop_artikelen.c.ovaantal, artikelen.c.artikelID,\
        artikelen.c.artikelomschrijving, orders_verkoop_artikelen.c.verkoopprijs,\
        artikelen.c.thumb_artikel, orders_verkoop_artikelen.c.retour]
    logger.debug("bestellingen(m_email=%s): columns → %s", m_email, columns, extra={"event.action": "bestellingen"})
    bestellingen = select(columns).where(accounts.c.email == m_email)
    bestellingen = bestellingen.select_from(accounts.join(klanten)\
               .join(orders_verkoop).join(orders_verkoop_artikelen)\
               .join(artikelen)).order_by(orders_verkoop_artikelen.c.ovbestelID, orders_verkoop_artikelen.c.artikelID)
    logger.debug("bestellingen(m_email=%s): bestellingen → %s", m_email, bestellingen, extra={"event.action": "bestellingen"})
    
    if con.execute(bestellingen).fetchone():
        rp_bestellingen = con.execute(bestellingen)
    else:
        logger.debug("bestellingen(m_email=%s): rp_bestellingen → %s", m_email, rp_bestellingen, extra={"event.action": "bestellingen"})
        geenOrders()
        hoofdMenu(m_email)
    toonBest(rp_bestellingen, m_email)
    logger.debug("<<< Exiting bestellingen(m_email=%s)", m_email, extra={"event.action": "bestellingen"})
        
def toonBest(rp_bestellingen, m_email):
    logger.warning(">>> Entering toonBest(rp_bestellingen=%s,m_email=%s)", rp_bestellingen, m_email, extra={"event.action": "toonBest", "logrite.rp_bestellingen": rp_bestellingen})
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setGeometry(50, 50, 1500, 900)
            self.setWindowTitle('Besteloverzicht')
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
            table_view.setColumnWidth(8, 100)
            table_view.verticalHeader().setDefaultSectionSize(75)
            table_view.setItemDelegateForColumn(8, showImage(self))
            #table_view.clicked.connect(showBestelling)
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
            veld = self.mylist[index.row()][index.column()]
            logger.debug("data(index=%s,role=%s): veld → %s", index, role, veld, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
            logger.debug("data(self=%s,index=%s,role=%s): veld → %s", self, index, role, veld, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
            if not index.isValid():
                return None
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
   
    header = ['Bestelnummer','Besteldatum', 'Betaaldatum','Leverdatum', 'Hoeveelheid',\
              'Artikelnummer','Omschrijving','Verkoopprijs', 'Afbeelding', 'Retour']
    
    data_list=[]
    for row in rp_bestellingen:
        data_list += [(row)]
               
    win = MyWindow(data_list, header)
    win.exec_()
    hoofdMenu(m_email)