from login import hoofdMenu
from PyQt5.QtWidgets import  QDialog, QLabel, QGridLayout,\
                 QPushButton, QLineEdit, QWidget, QTableView, QVBoxLayout
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QPixmap, QIcon
from sqlalchemy import (Table, Column, Integer, String, MetaData, create_engine, ForeignKey)
from sqlalchemy.sql import select, and_
import logging
logger = logging.getLogger(__name__)

def noRecord():
    logger.debug(">>> Entering noRecord()")
    msg = QMessageBox()
    logger.debug("noRecord(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen records, breng deze eerst in!')
    msg.setWindowTitle('Inbrengen records')
    logger.debug("<<< Exiting noRecord()")
    msg.exec_()

def eigenBedrijf(m_email):
    logger.debug(">>> Entering eigenBedrijf(m_email=%s)", m_email)
    metadata = MetaData()
    logger.debug("eigenBedrijf(m_email=%s): metadata → %s", m_email, metadata)
    kopers = Table('kopers', metadata,
       Column('koperID', Integer(), primary_key=True),
       Column('bedrijfsnaam', String),
       Column('rechtsvorm', String),
       Column('afdeling', String),
       Column('btwnummer', String),
       Column('kvknummer', String),
       Column('telnr', String),
       Column('huisnummer', String),
       Column('toevoeging', String),
       Column('postcode', String))
    koper_accounts = Table('koper_accounts', metadata,
       Column('koperaccID', Integer, primary_key=True),
       Column('accountID', Integer, ForeignKey('accounts.accountID')),
       Column('koperID', Integer, ForeignKey('kopers.koperID')))
    accounts = Table('accounts', metadata,
       Column('accountID', Integer, primary_key=True),
       Column('email', String))

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("eigenBedrijf(m_email=%s): engine → %s", m_email, engine)
    conn = engine.connect()
    selkop = select([kopers, koper_accounts, accounts]).where(and_(kopers.c.koperID == koper_accounts.c.koperID,\
                         koper_accounts.c.accountID == accounts.c.accountID, accounts.c.email == m_email))
    logger.debug("eigenBedrijf(m_email=%s): conn → %s", m_email, conn)
    rpkop = conn.execute(selkop)
    class MyWindow(QDialog):
        logger.debug("eigenBedrijf(m_email=%s): selkop → %s", m_email, selkop)
        def __init__(self, data_list, header, *args):
            logger.debug("<<< Exiting eigenBedrijf(m_email=%s)", m_email)
            QWidget.__init__(self, *args,)
            logger.debug(">>> Entering __init__(data_list=%s,header=%s)", data_list, header)
            self.setGeometry(50, 50, 1500, 900)
            self.setWindowTitle('Verkoopbedrijf opvragen')
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
            table_view.clicked.connect(showBedrijf)
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
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
            logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit)
            logger.debug("__init__(parent=%s): self.Bedrijfsnaam → %s", parent, self.Bedrijfsnaam)
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit)
            logger.debug("__init__(parent=%s): q16Edit → %s", parent, q16Edit)
            logger.debug("__init__(parent=%s): self.Afdeling → %s", parent, self.Afdeling)
            logger.debug("__init__(self=%s,parent=%s): q16Edit → %s", self, parent, q16Edit)
            logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit)
            logger.debug("__init__(parent=%s): self.Rechtsvorm → %s", parent, self.Rechtsvorm)
            logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit)
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit)
            logger.debug("__init__(parent=%s): self.BTWnummer → %s", parent, self.BTWnummer)
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit)
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit)
            logger.debug("__init__(parent=%s): self.KvKnummer → %s", parent, self.KvKnummer)
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit)
            logger.debug("__init__(parent=%s): q1Edit → %s", parent, q1Edit)
            logger.debug("__init__(parent=%s): self.Straat → %s", parent, self.Straat)
            logger.debug("__init__(self=%s,parent=%s): q1Edit → %s", self, parent, q1Edit)
            logger.debug("__init__(parent=%s): q7Edit → %s", parent, q7Edit)
            logger.debug("__init__(parent=%s): self.Huisnummer → %s", parent, self.Huisnummer)
            logger.debug("__init__(self=%s,parent=%s): q7Edit → %s", self, parent, q7Edit)
            logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit)
            logger.debug("__init__(parent=%s): self.Toevoeging → %s", parent, self.Toevoeging)
            logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit)
            logger.debug("__init__(parent=%s): q6Edit → %s", parent, q6Edit)
            logger.debug("__init__(parent=%s): self.Postcode → %s", parent, self.Postcode)
            logger.debug("__init__(self=%s,parent=%s): q6Edit → %s", self, parent, q6Edit)
            logger.debug("__init__(parent=%s): q15Edit → %s", parent, q15Edit)
            logger.debug("__init__(parent=%s): self.Woonplaats → %s", parent, self.Woonplaats)
            logger.debug("__init__(self=%s,parent=%s): q15Edit → %s", self, parent, q15Edit)
            logger.debug("__init__(parent=%s): q13Edit → %s", parent, q13Edit)
            logger.debug("__init__(parent=%s): self.Telefoonnr → %s", parent, self.Telefoonnr)
            logger.debug("__init__(self=%s,parent=%s): q13Edit → %s", self, parent, q13Edit)
            logger.debug("__init__(parent=%s): q14Edit → %s", parent, q14Edit)
            logger.debug("__init__(parent=%s): self.Bedrijfverkoopnummer → %s", parent, self.Bedrijfverkoopnummer)
            logger.debug("__init__(self=%s,parent=%s): q14Edit → %s", self, parent, q14Edit)
            logger.debug("__init__(parent=%s): grid → %s", parent, grid)
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid)
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl)
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl)
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): terugBtn → %s", parent, terugBtn)
            logger.debug("__init__(self=%s,parent=%s): terugBtn → %s", self, parent, terugBtn)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
            self.header = header
        def rowCount(self, parent):
            logger.debug(">>> Entering rowCount(parent=%s)", parent)
            return len(self.mylist)
        def columnCount(self, parent):
            logger.debug(">>> Entering columnCount(parent=%s)", parent)
            try:
                logger.debug("<<< Exiting columnCount(parent=%s)", parent)
                return len(self.mylist[0])
            except:
                logger.error("Exception in columnCount(parent=%s)", parent, exc_info=True)
                noRecord()
                hoofdMenu(m_email)
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
 
    header = ['VerkoopbedrijfID','Bedrijfsnaam', 'Rechtsvorm','Afdeling', 'BTWNummer', 'KVKNummer',\
              'Telefoonnummer','Straat', 'Huisnummer', 'Toevoeging', 'Postcode', 'Woonplaats']  
      

    import postcode
    
    data_list=[]
    for row in rpkop:
        msp = postcode.checkpostcode(row[9],int(row[7]))
        mstraat = msp[0]
        mplaats = msp[1]
        
        data_list += [(row[0],row[1],row[2],row[3],row[4],row[5],\
                     row[6],mstraat,int(row[7]),row[8],row[9],mplaats)]  
                                    
    def showBedrijf(idx):
        logger.debug(">>> Entering showBedrijf(idx=%s)", idx)
        mbedrnr = idx.data()
        logger.debug("showBedrijf(idx=%s): mbedrnr → %s", idx, mbedrnr)
        if idx.column() == 0:
            selkoper = select([kopers]).where(kopers.c.koperID == mbedrnr)
            logger.debug("showBedrijf(idx=%s): selkoper → %s", idx, selkoper)
            rpkoper = conn.execute(selkoper).first()
            logger.debug("showBedrijf(idx=%s): rpkoper → %s", idx, rpkoper)
            mpostcode = rpkoper[9]
            mhuisnr = int(rpkoper[7])
            logger.debug("showBedrijf(idx=%s): mpostcode → %s", idx, mpostcode)
            logger.debug("showBedrijf(idx=%s): mhuisnr → %s", idx, mhuisnr)
            import postcode
            mstrtplts = postcode.checkpostcode(mpostcode,mhuisnr)
            mstraat = mstrtplts[0]
            logger.debug("showBedrijf(idx=%s): mstrtplts → %s", idx, mstrtplts)
            mplaats = mstrtplts[1]  
            
            logger.debug("showBedrijf(idx=%s): mstraat → %s", idx, mstraat)
            logger.debug("showBedrijf(idx=%s): mplaats → %s", idx, mplaats)
            class Widget(QDialog):
                def __init__(self, parent=None):
                    super(Widget, self).__init__(parent)
                    logger.debug("<<< Exiting showBedrijf(idx=%s)", idx)
                    self.setWindowTitle("Opvragen verkoopbedrijven")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                                          
                    self.setFont(QFont('Arial', 10))
                          
                    self.Bedrijfsnaam = QLabel()
                    q3Edit = QLineEdit(rpkoper[1])
                    q3Edit.setFixedWidth(540)
                    q3Edit.setFont(QFont("Arial",10))
                    q3Edit.setDisabled(True)
                    q3Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    
                    self.Afdeling = QLabel()
                    q16Edit = QLineEdit(rpkoper[3])
                    q16Edit.setFixedWidth(540)
                    q16Edit.setFont(QFont("Arial",10))
                    q16Edit.setDisabled(True) 
                    q16Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    
                    self.Rechtsvorm = QLabel()
                    q5Edit = QLineEdit(rpkoper[2])
                    q5Edit.setFixedWidth(100)
                    q5Edit.setFont(QFont("Arial",10))
                    q5Edit.setDisabled(True) 
                    q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
             
                    self.BTWnummer =  QLabel()
                    q2Edit = QLineEdit(rpkoper[4])
                    q2Edit.setDisabled(True)
                    q2Edit.setFixedWidth(170)
                    q2Edit.setFont(QFont("Arial",10))
                    q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                          
                    self.KvKnummer =  QLabel()
                    q4Edit = QLineEdit(rpkoper[5])
                    q4Edit.setFixedWidth(110)
                    q4Edit.setDisabled(True)
                    q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
        
                    self.Straat =  QLabel()
                    q1Edit = QLineEdit()
                    q1Edit.setText(mstraat)
                    q1Edit.setFixedWidth(540)
                    q1Edit.setDisabled(True)
                    q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            
                    self.Huisnummer = QLabel()
                    q7Edit = QLineEdit(str(mhuisnr))
                    q7Edit.setFixedWidth(60)
                    q7Edit.setAlignment(Qt.AlignRight)
                    q7Edit.setFont(QFont("Arial",10))
                    q7Edit.setDisabled(True)
                    q7Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
        
                    self.Toevoeging = QLabel()
                    q8Edit = QLineEdit(rpkoper[8])
                    q8Edit.setFixedWidth(80)
                    q8Edit.setFont(QFont("Arial",10))
                    q8Edit.setDisabled(True)
                    q8Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    
                    self.Postcode = QLabel()
                    q6Edit = QLineEdit(mpostcode)
                    q6Edit.setFixedWidth(80)
                    q6Edit.setFont(QFont("Arial",10))
                    q6Edit.setDisabled(True)
                    q6Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                       
                    self.Woonplaats =  QLabel()
                    q15Edit = QLineEdit(mplaats)
                    q15Edit.setFixedWidth(400)
                    q15Edit.setDisabled(True)
                    q15Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                       
                    self.Telefoonnr = QLabel()
                    q13Edit = QLineEdit(rpkoper[6])
                    q13Edit.setFixedWidth(120)
                    q13Edit.setFont(QFont("Arial",10))
                    q13Edit.setDisabled(True)
                    q13Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    
                    self.Bedrijfverkoopnummer =  QLabel()
                    q14Edit = QLineEdit(str(rpkoper[0]))
                    q14Edit.setFixedWidth(120)
                    q14Edit.setAlignment(Qt.AlignRight)
                    q14Edit.setDisabled(True)
                    q14Edit.setFont(QFont("Arial",10))
                    q14Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                    
                    lbl = QLabel()
                    pixmap = QPixmap('./images/logos/verbinding.jpg')
                    lbl.setPixmap(pixmap)
                    grid.addWidget(lbl , 0, 0)
                    
                    logo = QLabel()
                    pixmap = QPixmap('./images/logos/logo.jpg')
                    logo.setPixmap(pixmap)
                    grid.addWidget(logo , 0, 1, 1, 2, Qt.AlignRight)
           
                    self.setFont(QFont('Arial', 10))
                    grid.addWidget(QLabel('Verkoopbedrijven opvragen'), 0, 1)
                                                            
                    grid.addWidget(QLabel('Bedrijfsnaam'), 1, 0)
                    grid.addWidget(q3Edit, 1, 1, 1, 3) 
                    
                    grid.addWidget(QLabel('Afdelingsnaam/Kamer/\nKontaktpersoon'), 2, 0)
                    grid.addWidget(q16Edit, 2, 1, 1, 3)  
                         
                    grid.addWidget(QLabel('Rechtsvorm'), 3, 0)
                    grid.addWidget(q5Edit, 3, 1) 
                    
                    grid.addWidget(QLabel('BTWnummer'), 3, 1, 1, 1, Qt.AlignRight)
                    grid.addWidget(q2Edit, 3, 2) 
                    
                    grid.addWidget(QLabel('KvKnummer'), 4, 0)
                    grid.addWidget(q4Edit, 4, 1) 
                    
                    grid.addWidget(QLabel('Straat'), 5, 0)
                    grid.addWidget(q1Edit, 5, 1, 1, 3)
             
                    grid.addWidget(QLabel('Huisnummer'), 6, 0)
                    grid.addWidget(q7Edit, 6, 1)
            
                    grid.addWidget(QLabel('Toevoeging'), 6, 1, 1, 1, Qt.AlignRight)
                    grid.addWidget(q8Edit, 6, 2)
                    
                    grid.addWidget(QLabel('Postcode Woonplaats'), 7, 0)
                    grid.addWidget(q6Edit, 7, 1)
                    
                    grid.addWidget(q15Edit, 7, 1, 1, 2, Qt.AlignRight) 
             
                    grid.addWidget(QLabel('Telefoonnummer'), 8, 0)
                    grid.addWidget(q13Edit, 8, 1) 
                    
                    grid.addWidget(QLabel('Verkoopbedrijfnummer'), 9, 0)
                    grid.addWidget(q14Edit, 9, 1) 
                                        
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 10, 1)
                      
                    terugBtn = QPushButton('Sluiten')
                    terugBtn.clicked.connect(self.accept)           
                
                    grid.addWidget(terugBtn, 9, 2, 1, 1, Qt.AlignRight)
                    terugBtn.setFont(QFont("Arial",10))
                    terugBtn.setFixedWidth(100)
                    terugBtn.setStyleSheet("color: black;  background-color: gainsboro")
                       
                    self.setLayout(grid)
                    self.setGeometry(500, 100, 150, 150)
                
            mainWin = Widget()
            mainWin.exec_()       
       
    win = MyWindow(data_list, header)
    win.exec_()
    hoofdMenu(m_email)
 
