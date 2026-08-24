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
    logger.debug(">>> Entering ongInvoer()")
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Foutieve invoer\nzoekterm opnieuw invoeren s.v.p.!')
    msg.setWindowTitle('Accounts opvragen')               
    logger.debug("<<< Exiting ongInvoer()")
    msg.exec_() 

def geenRecord():
    logger.debug(">>> Entering geenRecord()")
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen record gevonden\nmaak een andere selektie s.v.p.!')
    msg.setWindowTitle('Accounts opvragen')               
    logger.debug("<<< Exiting geenRecord()")
    msg.exec_() 

def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)

def accKeuze(m_email):
    logger.debug(">>> Entering accKeuze(m_email=%s)", m_email)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            self.setWindowTitle("Opvragen accounts")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze)
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit)
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit)
            k0Edit.setFixedWidth(230)
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.addItem(' Sorteersleutel voor zoeken')
            k0Edit.addItem('1. Alle accounts')
            k0Edit.addItem('2. Postcode')
            k0Edit.addItem('3. emailadres.')
            k0Edit.addItem('4. Achternaam.')
            k0Edit.addItem('5. Accounts leveranciers.')
            k0Edit.addItem('6. Accounts werknemers.')
            k0Edit.activated[str].connect(self.k0Changed)
            
            self.Zoekterm = QLabel()
            logger.debug("__init__(parent=%s): self.Zoekterm → %s", parent, self.Zoekterm)
            zktermEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): zktermEdit → %s", self, parent, zktermEdit)
            logger.debug("__init__(parent=%s): zktermEdit → %s", parent, zktermEdit)
            zktermEdit.setFixedWidth(220)
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
                                  
            grid.addWidget(k0Edit, 1, 1)
            lbl1 = QLabel('Zoekterm')  
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1)
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1)
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 2, 0)
            grid.addWidget(zktermEdit, 2, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1, 3, Qt.AlignCenter)
            
            logo = QLabel()
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1 , 1, Qt.AlignRight)
    
            applyBtn = QPushButton('Zoeken')
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            applyBtn.clicked.connect(self.accept)
                
            grid.addWidget(applyBtn, 3, 1, 1 , 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn)
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn)
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 3, 1, 1 , 1)
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
    logger.debug(">>> Entering toonAccounts(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email)
    import validZt
    metadata = MetaData()
    logger.debug("toonAccounts(keuze=%s,zoekterm=%s,m_email=%s): metadata → %s", keuze, zoekterm, m_email, metadata)
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
    logger.debug("toonAccounts(keuze=%s,zoekterm=%s,m_email=%s): engine → %s", keuze, zoekterm, m_email, engine)
    conn = engine.connect()
    logger.debug("toonAccounts(keuze=%s,zoekterm=%s,m_email=%s): conn → %s", keuze, zoekterm, m_email, conn)
    
    if keuze == 1:
        sel = select([accounts]).order_by(accounts.c.accountID)
        logger.debug("toonAccounts(keuze=%s,zoekterm=%s,m_email=%s): sel → %s", keuze, zoekterm, m_email, sel)
    elif keuze == 2 and validZt.zt(zoekterm, 9):
        sel = select([accounts]).where(accounts.c.postcode.ilike(zoekterm))
    elif keuze == 3 and validZt.zt(zoekterm, 12):
        sel = select([accounts]).where(accounts.c.email.ilike('%'+zoekterm+'%'))
    elif keuze == 4:
        sel = select([accounts]).where(accounts.c.achternaam.ilike('%'+zoekterm+'%'))
    elif keuze == 5:
        sel = select([accounts, leveranciers.c.leverancierID, leveranciers.c.bedrijfsnaam,\
         leveranciers.c.rechtsvorm]).where(and_(lev_accounts.c.accountID ==\
         accounts.c.accountID, leveranciers.c.leverancierID == lev_accounts.c.leverancierID))
    elif keuze == 6:
        sel = select([accounts, werknemers.c.werknemerID, werknemers.c.loonID]).where(werknemers.c.accountID == \
        accounts.c.accountID)
    else:
        ongInvoer()
        accKeuze(m_email)
     
    if conn.execute(sel).fetchone():
        rpaccount = conn.execute(sel)
        logger.debug("toonAccounts(keuze=%s,zoekterm=%s,m_email=%s): rpaccount → %s", keuze, zoekterm, m_email, rpaccount)
    else:
        geenRecord()
        accKeuze(m_email)
     
    class MyWindow(QDialog):
        logger.debug("<<< Exiting toonAccounts(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email)
        def __init__(self, data_list, header, *args):
            QWidget.__init__(self, *args,)
            self.setGeometry(50, 50, 1800, 900)
            self.setWindowTitle('Accountgegevens opvragen')
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
  
    header = ['Accountnummer','Aanhef', 'Voornaam','Tussenvoegsel', 'Achternaam', 'Postcode',\
              'Huisnummer','Toevoeging', 'E-mail', 'Telefoonnummer', 'Accountcount', 'Geboortedatum']  
    
    if keuze == 5:
        header1 = ['Leveranciernummer', 'Bedrijfsnaam', 'Rechtsvorm'] 
        header.extend(header1)
    elif keuze == 6:
        header2 = ['Werknemernummer', 'Loonschaal']
        header.extend(header2)
   
    data_list=[]
    for row in rpaccount:
        data_list += [(row)] 
        
    win = MyWindow(data_list, header)
    win.exec_()
    accKeuze(m_email)