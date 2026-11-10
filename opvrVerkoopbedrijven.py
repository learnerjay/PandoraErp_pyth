from login import hoofdMenu
from PyQt5.QtWidgets import QDialog, QLabel, QGridLayout,\
                             QPushButton, QLineEdit, QWidget, QComboBox,\
                             QTableView, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QPixmap, QIcon
from sqlalchemy import (Table, Column, Integer, String, MetaData, create_engine)
from sqlalchemy.sql import select
import logging
logger = logging.getLogger(__name__)

def ongInvoer():
    logger.warning(">>> Entering ongInvoer()", extra={"event.action": "ongInvoer"})
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg, extra={"event.action": "ongInvoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Please re-enter incorrect input\nsearch term!')
    msg.setWindowTitle('Request sales companies')               
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
    msg.setWindowTitle('Request sales companies')               
    logger.debug("<<< Exiting geenRecord()", extra={"event.action": "geenRecord"})
    msg.exec_() 
     
def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})

def koperKeuze(m_email):
    logger.warning(">>> Entering koperKeuze(m_email=%s)", m_email, extra={"event.action": "koperKeuze"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Sales companies overview")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Keuze4 = QLabel()
            k4Edit = QComboBox()
            k4Edit.setFixedWidth(230)
            k4Edit.setFont(QFont("Arial", 10))
            k4Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k4Edit.addItem(' Search sort key')
            k4Edit.addItem('1. All Sales companies')
            k4Edit.addItem('2. Company name')
            k4Edit.addItem('3. Sales company number')
            k4Edit.addItem('4. Zip code number')
            k4Edit.activated[str].connect(self.k4Changed)
            
            self.Zoekterm = QLabel()
            zktermEdit = QLineEdit()
            zktermEdit.setFixedWidth(220)
            zktermEdit.setFont(QFont("Arial", 10))
            zktermEdit.textChanged.connect(self.zktermChanged)
     
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 1, 0, 1, 2)
                                  
            grid.addWidget(k4Edit, 2, 1)
            lbl1 = QLabel('Search term')
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 3, 0)
            grid.addWidget(zktermEdit, 3, 1)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 5, 0, 1, 2, Qt.AlignCenter)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 1, 1, 1, Qt.AlignRight)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
    
            applyBtn = QPushButton('Search')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 4, 1, 1 , 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial", 10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 4, 1)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
                   
        def k4Changed(self, text):
            logger.warning(">>> Entering k4Changed(text=%s)", text, extra={"event.action": "k4Changed", "logrite.text": text})
            self.Keuze4.setText(text)
            logger.debug("<<< Exiting k4Changed(text=%s)", text, extra={"event.action": "k4Changed", "logrite.text": text})
            
        def zktermChanged(self, text):
            logger.warning(">>> Entering zktermChanged(text=%s)", text, extra={"event.action": "zktermChanged", "logrite.text": text})
            self.Zoekterm.setText(text)
            logger.debug("<<< Exiting zktermChanged(text=%s)", text, extra={"event.action": "zktermChanged", "logrite.text": text})
 
        def returnk4(self):
            logger.warning(">>> Entering returnk4()", extra={"event.action": "returnk4"})
            logger.debug("<<< Exiting returnk4()", extra={"event.action": "returnk4"})
            return self.Keuze4.text()
        
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
            return [dialog.returnk4(), dialog.returnzkterm()]       

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
    toonBedrijfverkoop(keuze,zoekterm,m_email)
   
def toonBedrijfverkoop(keuze,zoekterm, m_email):
    logger.warning(">>> Entering toonBedrijfverkoop(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "toonBedrijfverkoop", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    import validZt
    class MyWindow(QDialog):
        logger.debug("<<< Exiting toonBedrijfverkoop(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "toonBedrijfverkoop", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setGeometry(50, 50, 1500, 900)
            self.setWindowTitle('Sales companies requesting')
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
            table_view.clicked.connect(showBedrijf)
            layout = QVBoxLayout(self)
            logger.debug("__init__(data_list=%s,header=%s): layout → %s", data_list, header, layout, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): layout → %s", self, data_list, header, layout, extra={"event.action": "__init__", "logrite.data_list": data_list})
            layout.addWidget(table_view)
            self.setLayout(layout)
    
    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            logger.warning(">>> Entering __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.mylist → %s", self, parent, mylist, header, self.mylist, extra={"event.action": "__init__", "logrite.mylist": mylist})
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.header → %s", self, parent, mylist, header, self.header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            QAbstractTableModel.__init__(self, parent, *args)
            logger.debug("<<< Exiting __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            self.mylist = mylist
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Bedrijfsnaam → %s", parent, self.Bedrijfsnaam, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Afdeling → %s", parent, self.Afdeling, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q16Edit → %s", parent, q16Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q16Edit → %s", self, parent, q16Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Rechtsvorm → %s", parent, self.Rechtsvorm, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.BTWnummer → %s", parent, self.BTWnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.KvKnummer → %s", parent, self.KvKnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Straat → %s", parent, self.Straat, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q1Edit → %s", parent, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q1Edit → %s", self, parent, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Huisnummer → %s", parent, self.Huisnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q7Edit → %s", parent, q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q7Edit → %s", self, parent, q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Toevoeging → %s", parent, self.Toevoeging, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Postcode → %s", parent, self.Postcode, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q6Edit → %s", parent, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q6Edit → %s", self, parent, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Woonplaats → %s", parent, self.Woonplaats, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q15Edit → %s", parent, q15Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q15Edit → %s", self, parent, q15Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Telefoonnr → %s", parent, self.Telefoonnr, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q13Edit → %s", parent, q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q13Edit → %s", self, parent, q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Bedrijfverkoopnummer → %s", parent, self.Bedrijfverkoopnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q14Edit → %s", parent, q14Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q14Edit → %s", self, parent, q14Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): terugBtn → %s", parent, terugBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): terugBtn → %s", self, parent, terugBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
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
 
    header = ['Sales companyID','Company name', 'Legal status','Department', 'VAT number', 'KVK number',\
              'Telephone number','Street', 'House number', 'Suffix', 'Zipcode', 'Residence']
   
    metadata = MetaData()   
    kopers= Table('kopers', metadata,
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
              
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    
    if keuze == 1:
        selkop = select([kopers]).order_by(kopers.c.koperID)   
    elif keuze == 2:
        selkop = select([kopers]).where(kopers.c.bedrijfsnaam.ilike('%'+zoekterm+'%'))\
          .order_by(kopers.c.koperID)
    elif keuze == 3 and validZt.zt(zoekterm, 6):
        selkop = select([kopers]).where(kopers.c.koperID == zoekterm).\
          order_by(kopers.c.koperID)
    elif keuze == 4 and validZt.zt(zoekterm, 9):
        selkop = select([kopers]).where(kopers.c.postcode.ilike(zoekterm+'%')).\
          order_by(kopers.c.koperID)
    else:        
        ongInvoer()
        koperKeuze(m_email)
        
    if conn.execute(selkop).fetchone():
        rpkop = conn.execute(selkop)
    else:
        geenRecord()
        koperKeuze(m_email)
        
    import postcode
    
    data_list=[]
    for row in rpkop:
        msp = postcode.checkpostcode(row[9],int(row[7]))
        mstraat = msp[0]
        mplaats = msp[1]
        data_list += [(row[0],row[1],row[2],row[3],row[4],row[5],\
                     row[6],mstraat,int(row[7]),row[8],row[9],mplaats)]     
                                 
    def showBedrijf(idx):
        logger.warning(">>> Entering showBedrijf(idx=%s)", idx, extra={"event.action": "showBedrijf", "logrite.idx": idx})
        mbedrnr = idx.data()
        logger.debug("showBedrijf(idx=%s): mbedrnr → %s", idx, mbedrnr, extra={"event.action": "showBedrijf", "logrite.idx": idx})
        if idx.column() == 0:
            selkoper = select([kopers]).where(kopers.c.koperID == mbedrnr)
            logger.debug("showBedrijf(idx=%s): selkoper → %s", idx, selkoper, extra={"event.action": "showBedrijf", "logrite.idx": idx})
            rpkoper = conn.execute(selkoper).first()
            logger.debug("showBedrijf(idx=%s): rpkoper → %s", idx, rpkoper, extra={"event.action": "showBedrijf", "logrite.idx": idx})
            mpostcode = rpkoper[9]
            mhuisnr = int(rpkoper[7])
            logger.debug("showBedrijf(idx=%s): mpostcode → %s", idx, mpostcode, extra={"event.action": "showBedrijf", "logrite.idx": idx})
            logger.debug("showBedrijf(idx=%s): mhuisnr → %s", idx, mhuisnr, extra={"event.action": "showBedrijf", "logrite.idx": idx})
            import postcode
            mstrtplts = postcode.checkpostcode(mpostcode,mhuisnr)
            mstraat = mstrtplts[0]
            logger.debug("showBedrijf(idx=%s): mstrtplts → %s", idx, mstrtplts, extra={"event.action": "showBedrijf", "logrite.idx": idx})
            mplaats = mstrtplts[1]  
            
            logger.debug("showBedrijf(idx=%s): mstraat → %s", idx, mstraat, extra={"event.action": "showBedrijf", "logrite.idx": idx})
            logger.debug("showBedrijf(idx=%s): mplaats → %s", idx, mplaats, extra={"event.action": "showBedrijf", "logrite.idx": idx})
            class Widget(QDialog):
                def __init__(self, parent=None):
                    super(Widget, self).__init__(parent)
                    logger.debug("<<< Exiting showBedrijf(idx=%s)", idx, extra={"event.action": "showBedrijf", "logrite.idx": idx})
                    self.setWindowTitle("Request sales comanies")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                                          
                    self.setFont(QFont('Arial', 10))
                          
                    self.Bedrijfsnaam = QLabel()
                    q3Edit = QLineEdit(rpkoper[1])
                    q3Edit.setFixedWidth(540)
                    q3Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q3Edit.setDisabled(True)
                    
                    self.Afdeling = QLabel()
                    q16Edit = QLineEdit(rpkoper[3])
                    q16Edit.setFixedWidth(540)
                    q16Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q16Edit.setDisabled(True) 
                    
                    self.Rechtsvorm = QLabel()
                    q5Edit = QLineEdit(rpkoper[2])
                    q5Edit.setFixedWidth(100)
                    q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q5Edit.setDisabled(True) 
             
                    self.BTWnummer =  QLabel()
                    q2Edit = QLineEdit(rpkoper[4])
                    q2Edit.setDisabled(True)
                    q2Edit.setFixedWidth(170)
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
                    grid.addWidget(QLabel('Request sales companies'), 0, 1)
                                                            
                    grid.addWidget(QLabel('Company name'), 1, 0)
                    grid.addWidget(q3Edit, 1, 1, 1, 3) 
                    
                    grid.addWidget(QLabel('Department name/Room/\nContact person'), 2, 0)
                    grid.addWidget(q16Edit, 2, 1, 1, 3)  
                         
                    grid.addWidget(QLabel('Legal status'), 3, 0)
                    grid.addWidget(q5Edit, 3, 1) 
                    
                    grid.addWidget(QLabel('VAT number'), 3, 1, 1, 1, Qt.AlignRight)
                    grid.addWidget(q2Edit, 3, 2) 
                    
                    grid.addWidget(QLabel('KvK number'), 4, 0)
                    grid.addWidget(q4Edit, 4, 1) 
                    
                    grid.addWidget(QLabel('Street'), 5, 0)
                    grid.addWidget(q1Edit, 5, 1, 1, 3)
             
                    grid.addWidget(QLabel('House number'), 6, 0)
                    grid.addWidget(q7Edit, 6, 1)
            
                    grid.addWidget(QLabel('Suffix'), 6, 1, 1, 1, Qt.AlignRight)
                    grid.addWidget(q8Edit, 6, 2)
                    
                    grid.addWidget(QLabel('Zipcode Residence'), 7, 0)
                    grid.addWidget(q6Edit, 7, 1)
                    
                    grid.addWidget(q15Edit, 7, 1, 1, 2, Qt.AlignRight) 
             
                    grid.addWidget(QLabel('Telephone number'), 8, 0)
                    grid.addWidget(q13Edit, 8, 1) 
                    
                    grid.addWidget(QLabel('Sales company number'), 9, 0)
                    grid.addWidget(q14Edit, 9, 1) 
                                        
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 10, 1)
                      
                    terugBtn = QPushButton('Close')
                    terugBtn.clicked.connect(self.close)           
                
                    grid.addWidget(terugBtn, 9, 2, 1, 1, Qt.AlignRight)
                    terugBtn.setFont(QFont("Arial",10))
                    terugBtn.setFixedWidth(100)
                    terugBtn.setStyleSheet("color: black;  background-color: gainsboro")
                       
                    self.setLayout(grid)
                    self.setGeometry(500, 100, 150, 150)
                    logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
                
            mainWin = Widget()
            mainWin.exec_()  
         
    win = MyWindow(data_list, header)
    win.exec_()
    koperKeuze(m_email)  