from login import hoofdMenu
from postcode import checkpostcode
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QDialog, QTableView, QVBoxLayout
from sqlalchemy import (Table, Column, Integer, String, MetaData, ForeignKey,\
                        create_engine, and_ , select)
import logging
logger = logging.getLogger(__name__)

def noRecord():
    logger.warning(">>> Entering noRecord()", extra={"event.action": "noRecord"})
    msg = QMessageBox()
    logger.debug("noRecord(): msg → %s", msg, extra={"event.action": "noRecord"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No record present, first insert record(s)!')
    msg.setWindowTitle('Insert parameters')
    logger.debug("<<< Exiting noRecord()", extra={"event.action": "noRecord"})
    msg.exec_()

def eigenLeverancier(m_email):
    logger.warning(">>> Entering eigenLeverancier(m_email=%s)", m_email, extra={"event.action": "eigenLeverancier"})
    metadata = MetaData()
    logger.debug("eigenLeverancier(m_email=%s): metadata → %s", m_email, metadata, extra={"event.action": "eigenLeverancier"})
    accounts = Table('accounts', metadata,
        Column('accountID', Integer, primary_key=True),
        Column('email', String))
    lev_accounts = Table('lev_accounts', metadata,
        Column('levaccID', Integer(), primary_key=True), 
        Column('accountID', None, ForeignKey('accounts.accountID')),
        Column('leverancierID', None, ForeignKey('leveranciers.leverancierID')))    
    logger.debug("eigenLeverancier(m_email=%s): sel → %s", m_email, sel, extra={"event.action": "eigenLeverancier"})
    leveranciers = Table('leveranciers', metadata,
        Column('leverancierID', Integer(), primary_key=True),
        Column('bedrijfsnaam', String),
        Column('rechtsvorm', String),
        Column('btwnummer', String),
        Column('kvknummer', String),
        Column('telnr', String),
        Column('postcode', String),  
        Column('huisnummer', String),
        Column('toevoeging', String))
     
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("eigenLeverancier(m_email=%s): engine → %s", m_email, engine, extra={"event.action": "eigenLeverancier"})
    con = engine.connect()
    logger.debug("eigenLeverancier(m_email=%s): con → %s", m_email, con, extra={"event.action": "eigenLeverancier"})
    sel = select([leveranciers]).where(and_(leveranciers.c.leverancierID == lev_accounts.c.leverancierID,\
                    lev_accounts.c.accountID == accounts.c.accountID, accounts.c.email == m_email))
    rplev = con.execute(sel)
    logger.debug("eigenLeverancier(m_email=%s): rplev → %s", m_email, rplev, extra={"event.action": "eigenLeverancier"})
    class MyWindow(QDialog):
        logger.debug("<<< Exiting eigenLeverancier(m_email=%s)", m_email, extra={"event.action": "eigenLeverancier"})
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setGeometry(50, 50, 1500, 900)
            self.setWindowTitle('Leveranciers opvragen')
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
            #table_view.clicked.connect(showLeverancier)
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
            self.header = header
        def rowCount(self, parent):
            logger.warning(">>> Entering rowCount(parent=%s)", parent, extra={"event.action": "rowCount"})
            return len(self.mylist)
        def columnCount(self, parent):
            logger.warning(">>> Entering columnCount(parent=%s)", parent, extra={"event.action": "columnCount"})
            try:
                return len(self.mylist[0])
            except:
                logger.error("Exception in columnCount(parent=%s)", parent, exc_info=True, extra={"event.action": "columnCount", "event.category": "process"})
                noRecord()
                logger.debug("<<< Exiting columnCount(parent=%s)", parent, extra={"event.action": "columnCount"})
                hoofdMenu(m_email)
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
  
    header = ['Leveranciernummer','Bedrijfsnaam', 'Rechtsvorm','BTWnummer',\
              'KvKnummer','Telefoonnummer','Straat', 'Huisnummer','Toevoeging',\
              'Postcode','Woonplaats']  
  
    data_list=[]
    for row in rplev:
        mstrtplts = checkpostcode(row[6], int(row[7]))
        data_list += [(row[0],row[1],row[2],row[3],row[4],row[5],mstrtplts[0],int(row[7]),\
                      row[8],row[6], mstrtplts[1])] 
        
    win = MyWindow(data_list, header)
    win.exec_()
    hoofdMenu(m_email)  
