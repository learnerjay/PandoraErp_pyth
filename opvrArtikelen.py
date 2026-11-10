from login import hoofdMenu
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor, QImage
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QGridLayout, QStyledItemDelegate,\
      QComboBox, QDialog, QLineEdit, QMessageBox , QVBoxLayout, QTableView
from sqlalchemy import (Table, Column, Integer, String, MetaData,\
                         create_engine, Float)
from sqlalchemy.sql import select, and_
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
    msg.setWindowTitle('Request articles')               
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
    msg.setWindowTitle('Request articles')               
    logger.debug("<<< Exiting geenRecord()", extra={"event.action": "geenRecord"})
    msg.exec_() 

def artKeuze(m_email):
    logger.warning(">>> Entering artKeuze(m_email=%s)", m_email, extra={"event.action": "artKeuze"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Request articles")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze, extra={"event.action": "__init__"})
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit, extra={"event.action": "__init__"})
            k0Edit.setFixedWidth(340)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('                    Search sort key')
            k0Edit.addItem('1. Sorted by article number')
            k0Edit.addItem('2. Sorted by stock')
            k0Edit.addItem('3. Filtered by description')
            k0Edit.addItem('4. Filtered by article group.')
            k0Edit.addItem('5. Filtered by storage location.')
            k0Edit.addItem('6. Obsolete after yyyy-mm-dd')
            k0Edit.addItem('7. To order by reservations')
            k0Edit.addItem('8. To order by stock controlled')
            k0Edit.addItem('9. Minimum stock + order size < reservation')
            k0Edit.activated[str].connect(self.k0Changed)
              
            self.Zoekterm = QLabel()
            logger.debug("__init__(parent=%s): self.Zoekterm → %s", parent, self.Zoekterm, extra={"event.action": "__init__"})
            zktermEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): zktermEdit → %s", self, parent, zktermEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): zktermEdit → %s", parent, zktermEdit, extra={"event.action": "__init__"})
            
            zktermEdit.setFixedWidth(210)
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
                                  
            grid.addWidget(k0Edit, 1, 0 ,1, 2, Qt.AlignRight)
            lbl1 = QLabel('Search term')
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            grid.addWidget(lbl1, 2, 0 , 1, 1, Qt.AlignRight)
            grid.addWidget(zktermEdit, 2, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1 , 2, Qt.AlignCenter)
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1 ,1, Qt.AlignRight)
    
            applyBtn = QPushButton('Search')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 3, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
              
            cancelBtn = QPushButton('Close')
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            cancelBtn.clicked.connect(lambda: windowSluit(self,m_email))
    
            grid.addWidget(cancelBtn, 3, 1)
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
    toonArtikelen(keuze,zoekterm, m_email)
    
def toonArtikelen(keuze,zoekterm, m_email):
    logger.warning(">>> Entering toonArtikelen(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "toonArtikelen", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    import validZt  
    metadata = MetaData()
    logger.debug("toonArtikelen(keuze=%s,zoekterm=%s,m_email=%s): metadata → %s", keuze, zoekterm, m_email, metadata, extra={"event.action": "toonArtikelen", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('barcode', String),
        Column('artikelomschrijving', String),
        Column('thumb_artikel', String(70)),
        Column('artikelprijs', Float),
        Column('art_voorraad', Float),
        Column('art_eenheid', String(20)),
        Column('art_min_voorraad', Float),
        Column('art_bestelgrootte', Float),
        Column('locatie_magazijn', String(10)),
        Column('artikelgroep', String),
        Column('categorie', Integer),
        Column('afmeting', String),
        Column('mutatiedatum', String),
        Column('bestelsaldo', Float),
        Column('reserveringsaldo', Float),
        Column('jaarverbruik_1', Float),
        Column('jaarverbruik_2', Float))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("toonArtikelen(keuze=%s,zoekterm=%s,m_email=%s): engine → %s", keuze, zoekterm, m_email, engine, extra={"event.action": "toonArtikelen", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    con = engine.connect()
    logger.debug("toonArtikelen(keuze=%s,zoekterm=%s,m_email=%s): con → %s", keuze, zoekterm, m_email, con, extra={"event.action": "toonArtikelen", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
     
    if keuze == 1:
        sel = select([artikelen]).order_by(artikelen.c.artikelID)
    elif keuze == 2:
        sel = select([artikelen]).order_by(artikelen.c.art_voorraad.desc())
        logger.debug("toonArtikelen(keuze=%s,zoekterm=%s,m_email=%s): sel → %s", keuze, zoekterm, m_email, sel, extra={"event.action": "toonArtikelen", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    elif keuze == 3:
        sel = select([artikelen]).where(artikelen.c.artikelomschrijving.ilike('%'+zoekterm+'%'))
    elif keuze == 4:
        sel = select([artikelen]).where(artikelen.c.artikelgroep.ilike('%'+zoekterm+'%'))
    elif keuze == 5:
        sel = select([artikelen]).where(artikelen.c.locatie_magazijn.ilike('%'+zoekterm+'%'))
    elif keuze == 6 and validZt.zt(zoekterm, 10):
        sel = select([artikelen]).where(artikelen.c.mutatiedatum >= (zoekterm+'%')).\
          order_by(artikelen.c.artikelID)
    elif keuze == 7:
        sel = select([artikelen]).where(and_(artikelen.c.reserveringsaldo > 0,\
                     artikelen.c.art_voorraad+artikelen.c.bestelsaldo < \
                     artikelen.c.reserveringsaldo,artikelen.c.categorie > 4))
    elif keuze == 8:
        sel = select([artikelen]).where(and_(artikelen.c.art_voorraad < artikelen.c.art_min_voorraad,\
                    artikelen.c.categorie < 5))
    elif keuze == 9:
        sel = select([artikelen]).where(and_(artikelen.c.art_min_voorraad+artikelen.c.\
            art_bestelgrootte < artikelen.c.reserveringsaldo,artikelen.c.categorie > 4)) 
    else:
        ongInvoer()
        artKeuze(m_email)
    
    if con.execute(sel).fetchone():    
        rpartikelen = con.execute(sel)
    else:
        logger.debug("toonArtikelen(keuze=%s,zoekterm=%s,m_email=%s): rpartikelen → %s", keuze, zoekterm, m_email, rpartikelen, extra={"event.action": "toonArtikelen", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
        geenRecord()
        artKeuze(m_email)

    class MyWindow(QDialog):
        logger.debug("<<< Exiting toonArtikelen(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "toonArtikelen", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setGeometry(100, 50, 1800, 900)
            self.setWindowTitle('Request articles')
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
            table_view.setItemDelegateForColumn(3, showImage(self))
            table_view.setColumnWidth(3, 100)
            table_view.verticalHeader().setDefaultSectionSize(75)
            table_view.clicked.connect(showArtikel)
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
            #elif index.column() == 9 and role == Qt.DecorationRole: # alternative picture however
                                                                     # with text right to path
            #    return QPixmap(index.data())
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
               logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
               logger.debug("__init__(): self.Artikelnummer → %s", self.Artikelnummer, extra={"event.action": "__init__"})
               logger.debug("__init__(): q1Edit → %s", q1Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(): self.Barcode → %s", self.Barcode, extra={"event.action": "__init__"})
               logger.debug("__init__(): q1aEdit → %s", q1aEdit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): q1aEdit → %s", self, q1aEdit, extra={"event.action": "__init__"})
               logger.debug("__init__(): self.Artikelomschrijving → %s", self.Artikelomschrijving, extra={"event.action": "__init__"})
               logger.debug("__init__(): q2Edit → %s", q2Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): q2Edit → %s", self, q2Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(): self.Artikelprijs → %s", self.Artikelprijs, extra={"event.action": "__init__"})
               logger.debug("__init__(): q3Edit → %s", q3Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): q3Edit → %s", self, q3Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(): self.Artikelvoorraad → %s", self.Artikelvoorraad, extra={"event.action": "__init__"})
               logger.debug("__init__(): q4Edit → %s", q4Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): q4Edit → %s", self, q4Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(): self.Bestelsaldo → %s", self.Bestelsaldo, extra={"event.action": "__init__"})
               logger.debug("__init__(): q16Edit → %s", q16Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): q16Edit → %s", self, q16Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(): self.Artikeleenheid → %s", self.Artikeleenheid, extra={"event.action": "__init__"})
               logger.debug("__init__(): q5Edit → %s", q5Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): q5Edit → %s", self, q5Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(): self.Minimumvoorraad → %s", self.Minimumvoorraad, extra={"event.action": "__init__"})
               logger.debug("__init__(): q6Edit → %s", q6Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): q6Edit → %s", self, q6Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(): self.Bestelgrootte → %s", self.Bestelgrootte, extra={"event.action": "__init__"})
               logger.debug("__init__(): q7Edit → %s", q7Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): q7Edit → %s", self, q7Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(): self.Reserveringsaldo → %s", self.Reserveringsaldo, extra={"event.action": "__init__"})
               logger.debug("__init__(): q12Edit → %s", q12Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): q12Edit → %s", self, q12Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(): self.Magazijnlocatie → %s", self.Magazijnlocatie, extra={"event.action": "__init__"})
               logger.debug("__init__(): q8Edit → %s", q8Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): q8Edit → %s", self, q8Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(): self.Artikelgroep → %s", self.Artikelgroep, extra={"event.action": "__init__"})
               logger.debug("__init__(): q9Edit → %s", q9Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): q9Edit → %s", self, q9Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(): self.Artikelthumbnail → %s", self.Artikelthumbnail, extra={"event.action": "__init__"})
               logger.debug("__init__(): q11Edit → %s", q11Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): q11Edit → %s", self, q11Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(): self.Categorie → %s", self.Categorie, extra={"event.action": "__init__"})
               logger.debug("__init__(): q13Edit → %s", q13Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): q13Edit → %s", self, q13Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(): self.Afmeting → %s", self.Afmeting, extra={"event.action": "__init__"})
               logger.debug("__init__(): q14Edit → %s", q14Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): q14Edit → %s", self, q14Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(): self.Mutatiedatum → %s", self.Mutatiedatum, extra={"event.action": "__init__"})
               logger.debug("__init__(): q15Edit → %s", q15Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): q15Edit → %s", self, q15Edit, extra={"event.action": "__init__"})
               logger.debug("__init__(): grid → %s", grid, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): grid → %s", self, grid, extra={"event.action": "__init__"})
               logger.debug("__init__(): lbl → %s", lbl, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): lbl → %s", self, lbl, extra={"event.action": "__init__"})
               logger.debug("__init__(): pixmap → %s", pixmap, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): pixmap → %s", self, pixmap, extra={"event.action": "__init__"})
               logger.debug("__init__(): logo → %s", logo, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): logo → %s", self, logo, extra={"event.action": "__init__"})
               logger.debug("__init__(): lbl2 → %s", lbl2, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): lbl2 → %s", self, lbl2, extra={"event.action": "__init__"})
               logger.debug("__init__(): cancelBtn → %s", cancelBtn, extra={"event.action": "__init__"})
               logger.debug("__init__(self=%s): cancelBtn → %s", self, cancelBtn, extra={"event.action": "__init__"})
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
                                       
    header = ['Article number', 'Barcodenumber','Description', 'Image', 'Price', 'Stock', 'Unit',\
          'Minimum stock', 'Order size', 'Location', 'Group', 'Category',\
          'Size', 'Mutation\ndate', 'Order balance' ,'Reservation\nbalance', \
          'Annual consumption\neven years','Annual consumption\nodd years']    
        
    data_list=[]
    for row in rpartikelen:
        data_list += [(row)] 
        
    def showArtikel(idx):
        logger.warning(">>> Entering showArtikel(idx=%s)", idx, extra={"event.action": "showArtikel", "logrite.idx": idx})
        martikelnr = idx.data()
        logger.debug("showArtikel(idx=%s): martikelnr → %s", idx, martikelnr, extra={"event.action": "showArtikel", "logrite.idx": idx})
        if idx.column() == 0:
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showArtikel(idx=%s): engine → %s", idx, engine, extra={"event.action": "showArtikel", "logrite.idx": idx})
            con = engine.connect()
            sel = select([artikelen]).where(artikelen.c.artikelID == martikelnr)
            logger.debug("showArtikel(idx=%s): con → %s", idx, con, extra={"event.action": "showArtikel", "logrite.idx": idx})
            rpartikel = con.execute(sel).first()
 
            logger.debug("showArtikel(idx=%s): sel → %s", idx, sel, extra={"event.action": "showArtikel", "logrite.idx": idx})
            logger.debug("showArtikel(idx=%s): rpartikel → %s", idx, rpartikel, extra={"event.action": "showArtikel", "logrite.idx": idx})
            class Widget(QDialog):
                def __init__(self):
                    super(Widget, self).__init__()
                    logger.debug("<<< Exiting showArtikel(idx=%s)", idx, extra={"event.action": "showArtikel", "logrite.idx": idx})
                
                    self.setWindowTitle("Request articles")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                                
                    self.setFont(QFont('Arial', 10))
                               
                    self.Artikelnummer = QLabel()
                    q1Edit = QLineEdit(str(rpartikel[0]))
                    q1Edit.setFixedWidth(100)
                    q1Edit.setAlignment(Qt.AlignRight)
                    q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q1Edit.setDisabled(True)
                    
                    self.Barcode = QLabel()
                    q1aEdit = QLineEdit(str(rpartikel[1]))
                    q1aEdit.setFixedWidth(130)
                    q1aEdit.setAlignment(Qt.AlignRight)
                    q1aEdit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q1aEdit.setDisabled(True)
    
                    self.Artikelomschrijving = QLabel()
                    q2Edit = QLineEdit(str(rpartikel[2]))
                    q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q2Edit.setFixedWidth(400)
                    q2Edit.setDisabled(True)
                    
                    self.Artikelprijs = QLabel()
                    q3Edit = QLineEdit('{:12.2f}'.format(rpartikel[4]))
                    q3Edit.setAlignment(Qt.AlignRight)
                    q3Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q3Edit.setAlignment(Qt.AlignRight)
                    q3Edit.setFixedWidth(100)
                    q3Edit.setDisabled(True)
                                    
                    self.Artikelvoorraad = QLabel()
                    q4Edit = QLineEdit('{:12.2f}'.format(rpartikel[5]))
                    q4Edit.setAlignment(Qt.AlignRight)
                    q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q4Edit.setFixedWidth(100)
                    q4Edit.setDisabled(True)
                     
                    self.Bestelsaldo = QLabel()
                    q16Edit = QLineEdit('{:12.2f}'.format(rpartikel[14]))
                    q16Edit.setAlignment(Qt.AlignRight)
                    q16Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q16Edit.setFixedWidth(100)
                    q16Edit.setDisabled(True)
                    
                    self.Artikeleenheid = QLabel()
                    q5Edit = QLineEdit(rpartikel[6])
                    q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q5Edit.setFixedWidth(100)
                    q5Edit.setDisabled(True)
          
                    self.Minimumvoorraad = QLabel()
                    q6Edit = QLineEdit('{:12.2f}'.format(rpartikel[7]))
                    q6Edit.setAlignment(Qt.AlignRight)
                    q6Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q6Edit.setFixedWidth(100)
                    q6Edit.setDisabled(True)
         
                    self.Bestelgrootte = QLabel()
                    q7Edit = QLineEdit('{:12.2f}'.format(rpartikel[8]))
                    q7Edit.setAlignment(Qt.AlignRight)
                    q7Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q7Edit.setFixedWidth(100)
                    q7Edit.setDisabled(True)
                    
                    self.Reserveringsaldo = QLabel()
                    q12Edit = QLineEdit('{:12.2f}'.format(rpartikel[15]))
                    q12Edit.setAlignment(Qt.AlignRight)
                    q12Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q12Edit.setFixedWidth(100)
                    q12Edit.setDisabled(True)
                                   
                    self.Magazijnlocatie = QLabel()
                    q8Edit = QLineEdit(str(rpartikel[9]))
                    q8Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q8Edit.setFixedWidth(100)
                    q8Edit.setDisabled(True)
                    
                    self.Artikelgroep = QLabel()
                    q9Edit = QLineEdit(str(rpartikel[10]))
                    q9Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q9Edit.setFixedWidth(200)
                    q9Edit.setDisabled(True)
             
                    self.Artikelthumbnail = QLabel()
                    q11Edit = QLineEdit(str(rpartikel[3]))
                    q11Edit.setFixedWidth(400)
                    q11Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q11Edit.setDisabled(True)
                           
                    self.Categorie = QLabel()
                    q13Edit = QLineEdit(str(rpartikel[11]))
                    q13Edit.setFixedWidth(100)
                    q13Edit.setAlignment(Qt.AlignRight)
                    q13Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q13Edit.setDisabled(True)
                    
                    self.Afmeting = QLabel()
                    q14Edit = QLineEdit(str(rpartikel[12]))
                    q14Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q14Edit.setFixedWidth(100)
                    q14Edit.setDisabled(True)
                    
                    self.Mutatiedatum = QLabel()
                    q15Edit = QLineEdit(str(rpartikel[13]))
                    q15Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q15Edit.setFixedWidth(100)
                    q15Edit.setDisabled(True)
                            
                    grid = QGridLayout()
                    grid.setSpacing(20)
                
                    lbl = QLabel()
                    pixmap = QPixmap('./images/logos/verbinding.jpg')
                    lbl.setPixmap(pixmap)
                    grid.addWidget(lbl , 0, 0, 1, 2)
                
                    logo = QLabel()
                    pixmap = QPixmap('./images/logos/logo.jpg')
                    logo.setPixmap(pixmap)
                    grid.addWidget(logo , 0, 2, 1, 3, Qt.AlignRight) 
                  
                    grid.addWidget(QLabel('Article number'), 1, 0, 2, 1)
                    grid.addWidget(q1Edit, 1, 1, 2, 1)
                    
                    grid.addWidget(QLabel('Barcodenumber'), 1, 2, 2, 1)
                    grid.addWidget(q1aEdit, 1, 3, 2, 1)
                
                    grid.addWidget(QLabel('Article description'), 3, 0)
                    grid.addWidget(q2Edit, 3, 1, 1 ,3)
                    
                    grid.addWidget(QLabel('Article group'), 4, 0)
                    grid.addWidget(q9Edit, 4, 1, 1, 3) 
                    
                    grid.addWidget(QLabel('Size'),5, 0)
                    grid.addWidget(q14Edit, 5, 1)
                    
                    grid.addWidget(QLabel('Unit'), 5, 2)
                    grid.addWidget(q5Edit, 5, 3)
                    
                    grid.addWidget(QLabel('Warehouse location'), 6, 0)
                    grid.addWidget(q8Edit, 6, 1)
         
                    grid.addWidget(QLabel('Article price'), 6, 2)
                    grid.addWidget(q3Edit, 6 , 3) 
                
                    grid.addWidget(QLabel('Article stock'), 7, 0)
                    grid.addWidget(q4Edit, 7, 1)
                    
                    grid.addWidget(QLabel('Minimum stock'), 7, 2)
                    grid.addWidget(q6Edit, 7, 3)
                    
                    grid.addWidget(QLabel('Order balance'), 8, 0)
                    grid.addWidget(q16Edit, 8, 1)
                    
                    grid.addWidget(QLabel('Reservation balance'), 8, 2)
                    grid.addWidget(q12Edit, 8, 3)
                    
                    grid.addWidget(QLabel('Order size'), 9, 0)
                    grid.addWidget(q7Edit, 9, 1)
                    
                    grid.addWidget(QLabel('Category'),9 ,2)
                    grid.addWidget(q13Edit, 9, 3)
        
                    grid.addWidget(QLabel('Mutation date'),10, 0)
                    grid.addWidget(q15Edit, 10, 1)
          
                    pixmap = QPixmap(rpartikel[9])
                    lbl2 = QLabel(self)
                    lbl2.setPixmap(pixmap)
                    grid.addWidget(lbl2 , 1, 2, 2, 2, Qt.AlignRight)
                
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 12, 0, 1, 4, Qt.AlignCenter)
                        
                    cancelBtn = QPushButton('Close')
                    cancelBtn.clicked.connect(self.close)
                
                    grid.addWidget(cancelBtn, 11, 3, 1, 1, Qt.AlignRight)
                    cancelBtn.setFont(QFont("Arial",10))
                    cancelBtn.setFixedWidth(100)
                    cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                                  
                    self.setLayout(grid)
                    logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})
                    self.setGeometry(500, 100, 350, 300)
            win = Widget()
            win.exec_()      
                                   
    win = MyWindow(data_list, header)
    win.exec_()
    artKeuze(m_email)