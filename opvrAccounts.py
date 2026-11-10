from login import hoofdMenu
from postcode import checkpostcode
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QDialog, QComboBox,\
      QLineEdit, QGridLayout, QMessageBox, QTableView, QVBoxLayout
from sqlalchemy import (Table, Column, Integer, String, ForeignKey, MetaData,\
                        create_engine)
from sqlalchemy.sql import select, and_
import logging
logger = logging.getLogger(__name__)

def ongInvoer():
    logger.warning(">>> Entering ongInvoer()", extra={"event.action": "ongInvoer"})
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg, extra={"event.action": "ongInvoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Please re-enter incorrect input\nsearch term!')
    msg.setWindowTitle('Requesting Accounts')               
    logger.debug("<<< Exiting ongInvoer()", extra={"event.action": "ongInvoer"})
    msg.exec_() 

def geenRecord():
    logger.warning(">>> Entering geenRecord()", extra={"event.action": "geenRecord"})
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg, extra={"event.action": "geenRecord"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No record found\ncreate another selection please!')
    msg.setWindowTitle('Requesting Accounts')               
    logger.debug("<<< Exiting geenRecord()", extra={"event.action": "geenRecord"})
    msg.exec_() 

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})

def accKeuze(m_email):
    logger.warning(">>> Entering accKeuze(m_email=%s)", m_email, extra={"event.action": "accKeuze"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Requesting Accounts")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze, extra={"event.action": "__init__"})
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit, extra={"event.action": "__init__"})
            k0Edit.setFixedWidth(230)
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.addItem(' Search sort key')
            k0Edit.addItem('1. All accounts')
            k0Edit.addItem('2. Zip code')
            k0Edit.addItem('3. email address.')
            k0Edit.addItem('4. Surname.')
            k0Edit.addItem('5. Accounts suppliers.')
            k0Edit.addItem('6. Accounts employees.')
            k0Edit.activated[str].connect(self.k0Changed)
            
            self.Zoekterm = QLabel()
            logger.debug("__init__(parent=%s): self.Zoekterm → %s", parent, self.Zoekterm, extra={"event.action": "__init__"})
            zktermEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): zktermEdit → %s", self, parent, zktermEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): zktermEdit → %s", parent, zktermEdit, extra={"event.action": "__init__"})
            zktermEdit.setFixedWidth(220)
            zktermEdit.setFont(QFont("Arial",10))
            zktermEdit.textChanged.connect(self.zktermChanged)
     
            grid = QGridLayout()
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            grid.setSpacing(20)
                          
            lbl = QLabel()
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
                                  
            grid.addWidget(k0Edit, 1, 1)
            lbl1 = QLabel('Search key')
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 2, 0)
            grid.addWidget(zktermEdit, 2, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1, 3, Qt.AlignCenter)
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1 , 1, Qt.AlignRight)
    
            applyBtn = QPushButton('Search')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
                
            grid.addWidget(applyBtn, 3, 1, 1 , 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 3, 1, 1 , 1)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                   
        def k0Changed(self, text):
            logger.warning(">>> Entering k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            self.Keuze.setText(text)
            logger.debug("<<< Exiting k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            
        def zktermChanged(self, text):
            logger.warning(">>> Entering zktermChanged(text=%s)", text, extra={"event.action": "zktermChanged", "logrite.text": text})
            self.Zoekterm.setText(text)
            logger.debug("<<< Exiting zktermChanged(text=%s)", text, extra={"event.action": "zktermChanged", "logrite.text": text})
 
        def returnk0(self):
            logger.warning(">>> Entering returnk0()", extra={"event.action": "returnk0"})
            logger.debug("<<< Exiting returnk0()", extra={"event.action": "returnk0"})
            return self.Keuze.text()
        
        def returnzkterm(self):
            logger.warning(">>> Entering returnzkterm()", extra={"event.action": "returnzkterm"})
            logger.debug("<<< Exiting returnzkterm()", extra={"event.action": "returnzkterm"})
            return self.Zoekterm.text()
        
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
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
    toonAccounts(keuze,zoekterm, m_email)
    
def toonAccounts(keuze, zoekterm, m_email):
    logger.warning(">>> Entering toonAccounts(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "toonAccounts", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    import validZt
    metadata = MetaData()
    logger.debug("toonAccounts(keuze=%s,zoekterm=%s,m_email=%s): metadata → %s", keuze, zoekterm, m_email, metadata, extra={"event.action": "toonAccounts", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    accounts = Table('accounts', metadata,
        Column('accountID', Integer(), primary_key=True),
        Column('aanhef', String(8)),
        Column('voornaam', String(30), nullable=False), 
        Column('tussenvoegsel', String(10)),
        Column('achternaam', String(50), nullable=False),
        Column('postcode', String(6), nullable=False),       
        Column('huisnummer', String(5), nullable=False),
        Column('toevoeging', String),
        Column('email', String, nullable=False),
        Column('telnr', String(10)), 
        Column('account_count', Integer(), nullable=False),
        Column('geboortedatum', String))
    leveranciers = Table('leveranciers', metadata,
        Column('leverancierID', Integer(), primary_key=True),
        Column('bedrijfsnaam', String),
        Column('rechtsvorm', String))
    lev_accounts = Table('lev_accounts', metadata,
        Column('levaccID', Integer, primary_key=True),
        Column('accountID', None, ForeignKey('accounts.accountID')),     
        Column('leverancierID', None, ForeignKey('leveranciers.leverancierID')))
    werknemers = Table('werknemers', metadata,
        Column('werknemerID', Integer, primary_key=True),
        Column('accountID', None, ForeignKey('accounts.accountID')),
        Column('loonID', Integer))
     
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("toonAccounts(keuze=%s,zoekterm=%s,m_email=%s): engine → %s", keuze, zoekterm, m_email, engine, extra={"event.action": "toonAccounts", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    conn = engine.connect()
    logger.debug("toonAccounts(keuze=%s,zoekterm=%s,m_email=%s): conn → %s", keuze, zoekterm, m_email, conn, extra={"event.action": "toonAccounts", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    
    if keuze == 1:
        sel = select([accounts]).order_by(accounts.c.accountID)
    elif keuze == 2 and validZt.zt(zoekterm, 9):
        sel = select([accounts]).where(accounts.c.postcode.ilike(zoekterm))
        logger.debug("toonAccounts(keuze=%s,zoekterm=%s,m_email=%s): sel → %s", keuze, zoekterm, m_email, sel, extra={"event.action": "toonAccounts", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    elif keuze == 3 and validZt.zt(zoekterm, 12):
        sel = select([accounts]).where(accounts.c.email.ilike('%'+zoekterm+'%'))
    elif keuze == 4:
        sel = select([accounts]).where(accounts.c.achternaam.ilike('%'+zoekterm+'%'))
    elif keuze == 5:
        sel = select([accounts, leveranciers.c.leverancierID, leveranciers.c.bedrijfsnaam,\
         leveranciers.c.rechtsvorm]).where(and_(lev_accounts.c.accountID ==\
         accounts.c.accountID, leveranciers.c.leverancierID == lev_accounts.c.leverancierID))
    elif keuze == 6:
        sel = select([accounts, werknemers.c.werknemerID, werknemers.c.loonID]).where(werknemers.c.accountID ==\
            accounts.c.accountID)
    else:
        ongInvoer()
        accKeuze(m_email)
     
    if conn.execute(sel).fetchone():
        rpaccount = conn.execute(sel)
    else:
        logger.debug("toonAccounts(keuze=%s,zoekterm=%s,m_email=%s): rpaccount → %s", keuze, zoekterm, m_email, rpaccount, extra={"event.action": "toonAccounts", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
        geenRecord()
        accKeuze(m_email)
     
    class MyWindow(QDialog):
        logger.debug("<<< Exiting toonAccounts(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "toonAccounts", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setGeometry(50, 50, 1700, 900)
            self.setWindowTitle('Request account information')
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
  
    header = ['Account number','Prefix', 'Firstname','Infix', 'Surname', 'Zipcode',\
              'House number','Suffix', 'E-mail', 'Telephone number', 'Account count', 'Date of birth']
    
    if keuze == 5:
        header1 = ['Supplier number', 'Company name', 'Legal form']
        header.extend(header1)
    elif keuze == 6:
        header2 = ['Employee number', 'Payscale']
        header.extend(header2)
   
    data_list=[]
    for row in rpaccount:
        data_list += [(row)] 

    win = MyWindow(data_list, header)
    win.exec_()
    accKeuze(m_email)