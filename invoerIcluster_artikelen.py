from login import hoofdMenu
from PyQt5.QtCore import Qt, QAbstractTableModel, QRegExp
from PyQt5.QtGui import QFont, QPixmap, QRegExpValidator, QIcon
from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout, QComboBox,\
    QDialog, QLabel, QGridLayout, QPushButton, QMessageBox, QLineEdit   
from sqlalchemy import (Table, Column, Integer, String, Float, MetaData,\
                         create_engine, ForeignKey)
from sqlalchemy.sql import select, insert, update, func, and_
import logging
logger = logging.getLogger(__name__)

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    
def ongInvoer():
    logger.warning(">>> Entering ongInvoer()", extra={"event.action": "ongInvoer"})
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg, extra={"event.action": "ongInvoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Please re-enter incorrect input\nsearch term!')
    msg.setWindowTitle('Enter articles per cluster')
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
    msg.setWindowTitle('Enter articles per cluster')
    logger.debug("<<< Exiting geenRecord()", extra={"event.action": "geenRecord"})
    msg.exec_() 

def invoerOK():
    logger.warning(">>> Entering invoerOK()", extra={"event.action": "invoerOK"})
    msg = QMessageBox()
    logger.debug("invoerOK(): msg → %s", msg, extra={"event.action": "invoerOK"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Insert successful!')
    msg.setWindowTitle('Enter articles per cluster')
    logger.debug("<<< Exiting invoerOK()", extra={"event.action": "invoerOK"})
    msg.exec_()

def calcBestaat():
    logger.warning(">>> Entering calcBestaat()", extra={"event.action": "calcBestaat"})
    msg = QMessageBox()
    logger.debug("calcBestaat(): msg → %s", msg, extra={"event.action": "calcBestaat"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Cluster item line exists\nexisting quantity has been replaced\nby changed quantity!')

    msg.setWindowTitle('Enter articles per cluster')
    msg.exec_()
    logger.debug("<<< Exiting calcBestaat()", extra={"event.action": "calcBestaat"})
    
def foutCluster():
    logger.warning(">>> Entering foutCluster()", extra={"event.action": "foutCluster"})
    msg = QMessageBox()
    logger.debug("foutCluster(): msg → %s", msg, extra={"event.action": "foutCluster"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Nonexistent cluster number\nCorrect!')
    msg.setWindowTitle('Enter articles per cluster')
    logger.debug("<<< Exiting foutCluster()", extra={"event.action": "foutCluster"})
    msg.exec_() 

def zoeken(m_email):
    logger.warning(">>> Entering zoeken(m_email=%s)", m_email, extra={"event.action": "zoeken"})
    import validZt
    class Widget(QDialog):
        logger.debug("<<< Exiting zoeken(m_email=%s)", m_email, extra={"event.action": "zoeken"})
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Cluster -> Articles range")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
            
            self.Clusternummer = QLabel()
            logger.debug("__init__(parent=%s): self.Clusternummer → %s", parent, self.Clusternummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): font → %s", parent, font, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): font → %s", self, parent, font, extra={"event.action": "__init__"})
            clEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): clEdit → %s", self, parent, clEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): clEdit → %s", parent, clEdit, extra={"event.action": "__init__"})
            clEdit.setFixedWidth(210)
            font = QFont("Arial",10)
            font.setCapitalization(QFont.AllUppercase)
            clEdit.setFont(font)
            reg_ex = QRegExp('^[L-Tl-t]{1}[A-Za-z]{1}[0-9]{5}')
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            input_validator = QRegExpValidator(reg_ex, clEdit)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            clEdit.setValidator(input_validator)
            clEdit.textChanged.connect(self.clChanged)
                                
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze, extra={"event.action": "__init__"})
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit, extra={"event.action": "__init__"})
            k0Edit.setFixedWidth(320)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('                  Search articles')
            k0Edit.addItem('1. All aticles')
            k0Edit.addItem('2. Filtered bu articles numbers')
            k0Edit.addItem('3. Filtered by articles description')
            k0Edit.activated[str].connect(self.k0Changed)
    
            self.Zoekterm = QLabel()
            logger.debug("__init__(parent=%s): self.Zoekterm → %s", parent, self.Zoekterm, extra={"event.action": "__init__"})
            zktermEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): zktermEdit → %s", self, parent, zktermEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): zktermEdit → %s", parent, zktermEdit, extra={"event.action": "__init__"})
            zktermEdit.setFixedWidth(210)
            zktermEdit.setFont(QFont("Arial",10))
            reg_ex = QRegExp('^.{0,20}$')
            input_validator = QRegExpValidator(reg_ex, zktermEdit)
            zktermEdit.setValidator(input_validator)
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
            grid.addWidget(lbl , 1, 0, 1, 2)
            
            lbl2 = QLabel('Cluster number')
            logger.debug("__init__(parent=%s): lbl2 → %s", parent, lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl2 → %s", self, parent, lbl2, extra={"event.action": "__init__"})
            lbl2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl2, 2, 0)
            grid.addWidget(clEdit, 2, 1)
            
            grid.addWidget(k0Edit, 3, 0, 1, 2, Qt.AlignRight)
            lbl1 = QLabel('Search term')
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 4, 0)
            grid.addWidget(zktermEdit, 4, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 6, 0, 1, 3)
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 1, 1, 1, Qt.AlignRight)
   
            applyBtn = QPushButton('Search')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 5, 1 , 1 ,1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 5, 1, 1, 2)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")

        def clChanged(self, text):
            logger.warning(">>> Entering clChanged(text=%s)", text, extra={"event.action": "clChanged", "logrite.text": text})
            self.Clusternummer.setText(text)
            logger.debug("<<< Exiting clChanged(text=%s)", text, extra={"event.action": "clChanged", "logrite.text": text})
              
        def k0Changed(self, text):
            logger.warning(">>> Entering k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            self.Keuze.setText(text)
            logger.debug("<<< Exiting k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            
        def zktermChanged(self, text):
            logger.warning(">>> Entering zktermChanged(text=%s)", text, extra={"event.action": "zktermChanged", "logrite.text": text})
            self.Zoekterm.setText(text)
            logger.debug("<<< Exiting zktermChanged(text=%s)", text, extra={"event.action": "zktermChanged", "logrite.text": text})
        
        def returnClusternummer(self):
            logger.warning(">>> Entering returnClusternummer()", extra={"event.action": "returnClusternummer"})
            logger.debug("<<< Exiting returnClusternummer()", extra={"event.action": "returnClusternummer"})
            return self.Clusternummer.text()
         
        def returnKeuze(self):
            logger.warning(">>> Entering returnKeuze()", extra={"event.action": "returnKeuze"})
            logger.debug("<<< Exiting returnKeuze()", extra={"event.action": "returnKeuze"})
            return self.Keuze.text()
        
        def returnZoekterm(self):
            logger.warning(">>> Entering returnZoekterm()", extra={"event.action": "returnZoekterm"})
            logger.debug("<<< Exiting returnZoekterm()", extra={"event.action": "returnZoekterm"})
            return self.Zoekterm.text()
        
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnClusternummer(), dialog.returnKeuze(),\
                    dialog.returnZoekterm()]       

    window = Widget()
    data = window.getData()
    zoekterm = ''
    keuze = ''
    metadata = MetaData()
    iclusters = Table('iclusters', metadata,
        Column('iclusterID', Integer, primary_key=True),
        Column('omschrijving', String))
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    selcl = select([iclusters]).where(iclusters.c.iclusterID == str(data[0]).upper())
    rpcl = con.execute(selcl).first()
    if rpcl:
        momschr = rpcl[1]
    else:
        foutCluster()
        zoeken(m_email)
    if data[0]:
        clusternr = str(data[0]).upper()
    if not data[1] or data[1][0] == ' ':
        ongInvoer()
        zoeken(m_email)
    if not data[1] or data[1][0] == ' ':
        ongInvoer()
        zoeken(m_email)
    elif data[1][0] == '1':
        keuze = '1'
    elif data[1][0] == '2' and validZt.zt(data[2], 2):
        keuze = '2'
        zoekterm = data[2]
    elif data[1][0] == '3' and data[1]:
        keuze = '3'
        zoekterm = data[2]
    else:
        ongInvoer()
        zoeken(m_email)
    toonArtikelen(keuze, zoekterm, m_email, momschr, clusternr)   
 
def toonArtikelen(keuze,zoekterm, m_email, momschr, clusternr):             
    logger.warning(">>> Entering toonArtikelen(keuze=%s,zoekterm=%s,m_email=%s,momschr=%s,clusternr=%s)", keuze, zoekterm, m_email, momschr, clusternr, extra={"event.action": "toonArtikelen", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm, "logrite.momschr": momschr, "logrite.clusternr": clusternr})
    class MyWindow(QDialog):
        logger.error("Exception in toonArtikelen(keuze=%s,zoekterm=%s,m_email=%s,momschr=%s,clusternr=%s)", keuze, zoekterm, m_email, momschr, clusternr, exc_info=True, extra={"event.action": "toonArtikelen", "event.category": "process", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm, "logrite.momschr": momschr, "logrite.clusternr": clusternr})
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setGeometry(100, 50, 1350, 900)
            self.setWindowTitle('Cluster Articles')
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
            table_view.clicked.connect(showSelection)
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
            logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
            logger.debug("__init__(): grid → %s", grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): grid → %s", self, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.lbl → %s", self.lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.pixmap → %s", self.pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl → %s", self, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.logo → %s", self.logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): logo → %s", self, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Hoeveelheid → %s", self.Hoeveelheid, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.hoev → %s", self.hoev, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): hoev → %s", self, hoev, extra={"event.action": "__init__"})
            logger.debug("__init__(): reg_ex → %s", reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): reg_ex → %s", self, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(): input_validator → %s", input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): input_validator → %s", self, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.applyBtn → %s", self.applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): applyBtn → %s", self, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.cancelBtn → %s", self.cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): cancelBtn → %s", self, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})
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
     
    header = ['Article number', 'Description', 'Price', 'Stock', 'Unit',\
          'Minimum\nstock', 'Order size', 'Location', 'Group', 'Category', 'Size']

    metadata = MetaData()

    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('artikelomschrijving', String),
        Column('artikelprijs', Float),
        Column('art_voorraad', Float),
        Column('art_eenheid', String(20)),
        Column('art_min_voorraad', Float),
        Column('art_bestelgrootte', Float),
        Column('locatie_magazijn', String(10)),
        Column('artikelgroep', String),
        Column('categorie', String(10)),
        Column('afmeting', String))     
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    if keuze == '1':
        sel = select([artikelen]).order_by(artikelen.c.artikelID)
    elif keuze == '2':
        zoekterm = zoekterm+''
        aanv = '200000000'
        suppl = '299999999'
        zoekbegin = (zoekterm+aanv)[0:9]
        zoekeind = (zoekterm+suppl)[0:9]
        sel = select([artikelen]).where(and_(artikelen.c.artikelID >= int(zoekbegin),\
                     artikelen.c.artikelID <= int(zoekeind)))\
                    .order_by(artikelen.c.artikelID)
    elif keuze == '3':
        sel = select([artikelen]).where(artikelen.c.artikelomschrijving.ilike('%'+zoekterm+'%'))\
                              .order_by(artikelen.c.artikelID)
    else:
        ongInvoer()
        zoeken(m_email)
    
    if con.execute(sel).fetchone():
        rp = con.execute(sel)
    else:
        geenRecord()
        zoeken(m_email)
    
    data_list=[]
    for row in rp:
        data_list += [(row)] 
    
    def showSelection(idx):
        logger.warning(">>> Entering showSelection(idx=%s)", idx, extra={"event.action": "showSelection", "logrite.idx": idx})
        artikelnr = idx.data()
        logger.debug("showSelection(idx=%s): artikelnr → %s", idx, artikelnr, extra={"event.action": "showSelection", "logrite.idx": idx})
        if idx.column() == 0:
            class MainWindow(QDialog):
                logger.debug("<<< Exiting showSelection(idx=%s)", idx, extra={"event.action": "showSelection", "logrite.idx": idx})
                def __init__(self):
                    QDialog.__init__(self)
                       
                    grid = QGridLayout()
                    grid.setSpacing(20)
                                
                    self.lbl = QLabel()
                    self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                    self.lbl.setPixmap(self.pixmap)
                    grid.addWidget(self.lbl , 0, 1, 1, 2)
            
                    self.logo = QLabel()
                    self.pixmap = QPixmap('./images/logos/logo.jpg')
                    self.logo.setPixmap(self.pixmap)
                    grid.addWidget(self.logo , 0, 2, 1, 1, Qt.AlignRight)
                                  
                    grid.addWidget(QLabel('Cluster number              '+clusternr+\
                                        '\n'+momschr[:35]), 1, 1, 1, 3)
                        
                    self.setFont(QFont('Arial', 10))
                    grid.addWidget(QLabel('Article number              '+str(artikelnr)), 3, 1, 1, 3)
                                  
                    self.setWindowTitle("Building clusters")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                    self.setFont(QFont('Arial', 10))
               
                    self.Hoeveelheid = QLabel(self)
                    self.Hoeveelheid.setText('Amount ')
                    self.hoev = QLineEdit(self)
                    self.hoev.setFixedWidth(210)
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, self.hoev)
                    self.hoev.setValidator(input_validator)
                    
                    grid.addWidget(self.Hoeveelheid, 4, 1)
                    grid.addWidget(self.hoev, 4, 2)
                    
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved\n     dj.jansen@casema.nl'), 6, 0, 1, 3, Qt.AlignCenter)
                    
                    self.applyBtn = QPushButton('Insert', self)
                    self.applyBtn.clicked.connect(self.clickMethod)
                    grid.addWidget(self.applyBtn, 5, 2, 1, 1, Qt.AlignRight)
                    self.applyBtn.setFont(QFont("Arial",10))
                    self.applyBtn.setFixedWidth(100)
                    self.applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    
                    self.cancelBtn = QPushButton('Close')
                    self.cancelBtn.clicked.connect(self.close)
                    grid.addWidget(self.cancelBtn, 5, 2, 1, 2)
                    self.cancelBtn.setFont(QFont("Arial",10))
                    self.cancelBtn.setFixedWidth(100)
                    self.cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                        
                    self.setLayout(grid)
                    self.setGeometry(500, 100, 150, 150)
                                   
                def clickMethod(self):
                    logger.warning(">>> Entering clickMethod()", extra={"event.action": "clickMethod"})
                    mhoev = self.hoev.text()
                    logger.debug("clickMethod(): mhoev → %s", mhoev, extra={"event.action": "clickMethod"})
                    if mhoev == '' or mhoev == '0':
                        logger.debug("<<< Exiting clickMethod()", extra={"event.action": "clickMethod"})
                        return
                    mhoev = float(str(mhoev))
                    
                    metadata = MetaData()
                    logger.debug("clickMethod(self=%s): metadata → %s", self, metadata, extra={"event.action": "clickMethod"})
                    
                    icluster_artikelen = Table('icluster_artikelen', metadata,
                        Column('icluster_artID', Integer, primary_key=True),
                        Column('iclusterID', None, ForeignKey('iclusters.iclusterID')),
                        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
                        Column('hoeveelheid', Float))
                    artikelen = Table('artikelen', metadata,
                        Column('artikelID', Integer(), primary_key=True),
                        Column('artikelprijs', Float))
                    iclusters = Table('iclusters', metadata,
                        Column('iclusterID', Integer(), primary_key=True),
                        Column('materialen', Float))
                    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
                    con = engine.connect()
                    selclart = select([icluster_artikelen]).where(and_(icluster_artikelen\
                      .c.iclusterID == clusternr, icluster_artikelen.c.artikelID == artikelnr))
                    rpclart = con.execute(selclart).first()
                    logger.debug("clickMethod(self=%s): rpclart → %s", self, rpclart, extra={"event.action": "clickMethod"})
                    selart = select([artikelen]).where(artikelen.c.artikelID == artikelnr)
                    rpart = con.execute(selart).first()
                    logger.debug("clickMethod(self=%s): rpart → %s", self, rpart, extra={"event.action": "clickMethod"})
                    martprijs = rpart[1]
                    logger.debug("clickMethod(self=%s): martprijs → %s", self, martprijs, extra={"event.action": "clickMethod"})
                    updcl = update(iclusters).where(iclusters.c.iclusterID == clusternr).\
                      values(materialen = iclusters.c.materialen + martprijs*mhoev)
                    con.execute(updcl)
                    if rpclart:
                        updclart = update(icluster_artikelen).where(and_(icluster_artikelen.c.\
                         iclusterID == clusternr, icluster_artikelen.c.artikelID == artikelnr))\
                         .values(hoeveelheid = mhoev)
                        con.execute(updclart)
                        calcBestaat()
                    else:
                        try:
                            mclartnr = (con.execute(select([func.max(icluster_artikelen.c.\
                             icluster_artID, type_=Integer)])).scalar())
                            mclartnr += 1
                        except:
                            mclartnr = 1
                            logger.debug("clickMethod(self=%s): mclartnr → %s", self, mclartnr, extra={"event.action": "clickMethod"})
                        insclart = insert(icluster_artikelen).values(icluster_artID = mclartnr,\
                        iclusterID = clusternr, artikelID = artikelnr, hoeveelheid = mhoev)
                        logger.error("Exception in clickMethod()", exc_info=True, extra={"event.action": "clickMethod", "event.category": "process"})
                        con.execute(insclart)
                        invoerOK()
                    self.accept()
                    
            mainWin = MainWindow()
            mainWin.exec_()
 
    win = MyWindow(data_list, header)
    win.exec_()
 