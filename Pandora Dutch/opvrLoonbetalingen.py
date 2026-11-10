from login import hoofdMenu
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
     QDialog, QMessageBox, QComboBox, QWidget, QTableView, QVBoxLayout
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QAbstractTableModel
from sqlalchemy import (Table, Column, Integer, String, Float,\
                        ForeignKey,  MetaData, create_engine)
from sqlalchemy.sql import select
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
    msg.setText('Foutieve invoer\nzoekterm opnieuw invoeren s.v.p.!')
    msg.setWindowTitle('Loonbetalingen opvragen')               
    logger.debug("<<< Exiting ongInvoer()", extra={"event.action": "ongInvoer"})
    msg.exec_() 

def geenRecord():
    logger.warning(">>> Entering geenRecord()", extra={"event.action": "geenRecord"})
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg, extra={"event.action": "geenRecord"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen record gevonden\nmaak een andere selektie s.v.p.!')
    msg.setWindowTitle('Loonbetalingen opvragen')               
    logger.debug("<<< Exiting geenRecord()", extra={"event.action": "geenRecord"})
    msg.exec_() 

def zoeken(m_email):
    logger.warning(">>> Entering zoeken(m_email=%s)", m_email, extra={"event.action": "zoeken"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Loonbetalingen")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                              
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze, extra={"event.action": "__init__"})
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit, extra={"event.action": "__init__"})
            k0Edit.setFixedWidth(250)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('     Opvragen Loonbetalingen')
            k0Edit.addItem('1. Gesorteerd op periode')
            k0Edit.addItem('2. Gefilterd op periode (jjjj-mm)\n    of (jjjjvak)')
            k0Edit.addItem('3. Gefilterd op achternaam')
            k0Edit.activated[str].connect(self.k0Changed)
    
            self.Zoekterm = QLabel()
            logger.debug("__init__(parent=%s): self.Zoekterm → %s", parent, self.Zoekterm, extra={"event.action": "__init__"})
            zktermEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): zktermEdit → %s", self, parent, zktermEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): zktermEdit → %s", parent, zktermEdit, extra={"event.action": "__init__"})
            zktermEdit.setFixedWidth(150)
            zktermEdit.setFont(QFont("Times", 10))
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
                                  
            grid.addWidget(k0Edit, 2, 0, 1, 2, Qt.AlignRight)
            lbl1 = QLabel('Zoekterm')  
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            lbl1.setAlignment(Qt.AlignRight)
            grid.addWidget(lbl1, 3, 0)
            grid.addWidget(zktermEdit, 3, 0, 1, 2, Qt.AlignRight)
            
            self.setLayout(grid)
            self.setGeometry(700, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 5, 0, 1, 2, Qt.AlignCenter)
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 1, 1, 1, Qt.AlignRight)
    
            applyBtn = QPushButton('Zoeken')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 4, 1, 1 , 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial", 10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            closeBtn = QPushButton('Sluiten')
            logger.debug("__init__(parent=%s): closeBtn → %s", parent, closeBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): closeBtn → %s", self, parent, closeBtn, extra={"event.action": "__init__"})
            closeBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(closeBtn, 4, 0, 1, 2, Qt.AlignCenter)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            closeBtn.setFont(QFont("Arial", 10))
            closeBtn.setFixedWidth(100)
            closeBtn.setStyleSheet("color: black;  background-color: gainsboro")
                   
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
    toonBetalingen(keuze, zoekterm, m_email)
    
def selectRow(index):
    logger.warning(">>> Entering selectRow(index=%s)", index, extra={"event.action": "selectRow", "logrite.index": index})
    print('Recordnummer is: ', index.row())
    logger.debug("<<< Exiting selectRow(index=%s)", index, extra={"event.action": "selectRow", "logrite.index": index})
 
def toonBetalingen(keuze,zoekterm, m_email):
    logger.warning(">>> Entering toonBetalingen(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "toonBetalingen", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    import validZt      
    class MyWindow(QDialog):
        logger.debug("<<< Exiting toonBetalingen(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "toonBetalingen", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setGeometry(10, 50, 1900, 900)
            self.setWindowTitle('Loonbetalingen opvragen')
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
            table_view.hideColumn(3)
            table_view.hideColumn(36)
            table_view.hideColumn(37)
            #table_view.clicked.connect(selectRow)
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
            logger.debug("__init__(self=%s): index → %s", self, index, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): horpos → %s", self, horpos, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): verpos → %s", self, verpos, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Gegevens → %s", self.Gegevens, extra={"event.action": "__init__"})
            logger.debug("__init__(): q1Edit → %s", q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): terugBtn → %s", terugBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): terugBtn → %s", self, terugBtn, extra={"event.action": "__init__"})
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
              
    header = ['Betalingnr', 'Maandperiode', 'Accountnummer', 'Werknemer', 'Voornaam',\
      'Tussenvoegsel','Achternaam', 'Straat', 'Huisnummer', 'Toevoeging',\
      'Postcode', 'Woonplaats', 'Geboortedatum', 'Indienstdatum','Brutoloon',\
      'Bruto variabel', 'Pensioenpremie', 'Bijtelling auto','Loonheffing',\
      'Inhouding overig','Periodieke uitkering','Vergoeding overig',\
      'Vergoeding reiskosten','Res. vakantietoeslag','Werkuren',\
      'Bijzonder tarief', 'Bedrag_byz_tarief','Reisuren', 'Overuren 125%',\
      'Overuren 150%', 'Overuren 200%', 'Nettoloon','Uurloon', 'Reisuurloon',\
      'Uren verlof', 'Uren extra verlof', 'Uren feestdag', 'Uren ziekte',\
      'Uren dokter', 'Uren geoorl. verzuim', 'Uren ongeoorl. verzuim',\
      'Loonschaal', 'Loontrede', 'Verlofsaldo', 'Alg. Heffingskorting',\
      'Arbeidskorting', 'Werkgever pensioenpremie','Werkgever WAO-IVA-WGA premie',\
      'Werkgever AWF premie', 'Werkgever ZVW kosten','Boekdatum', 'Cumulatief verschil uren',\
      'Uren in deze maand', 'Geboekt deze maand']
  
    metadata = MetaData()   
    loonbetalingen = Table('loonbetalingen', metadata,
        Column('betalingID', Integer(), primary_key=True),
        Column('periode', String),
        Column('accountID', None, ForeignKey('accounts.accountID')),
        Column('werknemerID', None, ForeignKey('werknemers.werknemerID')),
        Column('voornaam', String),
        Column('tussenvoegsel', String),
        Column('achternaam', String),
        Column('straat', String),
        Column('huisnummer', Integer),
        Column('toevoeging', String),
        Column('postcode', String),
        Column('woonplaats', String),
        Column('geboortedatum', String),
        Column('indienst', String),
        Column('brutoloon', Float),
        Column('bruto_variabel', Float),
        Column('pensioenpremie', Float),
        Column('bijtelling_auto', Float),
        Column('loonheffing', Float),
        Column('inhouding_overig', Float),
        Column('periodieke_uitkering', Float),
        Column('vergoeding_overig', Float),
        Column('vergoeding_reiskosten',Float),
        Column('res_vakantietoeslag', Float),
        Column('werkuren', Float),
        Column('byz_tarief', Float),
        Column('bedrag_byz_tarief', Float),
        Column('reisuren', Float),
        Column('overuren_125', Float),
        Column('overuren_150', Float),
        Column('overuren_200', Float),
        Column('nettoloon', Float),
        Column('uurloon', Float),
        Column('reisuurloon', Float),
        Column('uren_verlof', Float),
        Column('uren_extra_verlof', Float),
        Column('uren_feestdag', Float),
        Column('uren_ziek', Float),
        Column('uren_dokter', Float),
        Column('uren_geoorloofd_verzuim', Float),
        Column('uren_ongeoorloofd_verzuim', Float),
        Column('loonschaal', Integer),
        Column('loontrede', Integer),
        Column('verlofsaldo', Float),
        Column('alg_heffingskorting', Float),
        Column('arbeidskorting', Float),
        Column('wg_pensioenpremie', Float),
        Column('wg_WAO_IVA_WGA', Float),
        Column('wg_AWF', Float),
        Column('wg_ZVW', Float),
        Column('boekdatum', String),
        Column('saldo_uren_geboekt', Float),
        Column('maandwerkuren', Float),
        Column('uren_geboekt', Float))
     
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    if keuze == 1:
       selbet = select([loonbetalingen]).order_by(loonbetalingen.c.periode,\
                            loonbetalingen.c.accountID)
    elif keuze == 2 and validZt.zt(zoekterm, 20):
        selbet = select([loonbetalingen]).where(loonbetalingen.c.periode.like(zoekterm+'%'))
    elif keuze == 2 and zoekterm[4:7]=='vak':
        selbet = select([loonbetalingen]).where(loonbetalingen.c.periode.like(zoekterm+'%'))
    elif keuze == 3:
        selbet = select([loonbetalingen]).where(loonbetalingen.c.achternaam.ilike('%'+zoekterm+'%'))
    else:
        ongInvoer()
        zoeken(m_email)
    
    if con.execute(selbet).fetchone():
        rpbet = con.execute(selbet)
    else:
        geenRecord()
        zoeken(m_email)
        
    data_list=[]
    for row in rpbet:
        data_list += [(row)]

    def showSelection(idx):
        logger.warning(">>> Entering showSelection(idx=%s)", idx, extra={"event.action": "showSelection", "logrite.idx": idx})
        mbetaalnr = idx.data()
        logger.debug("showSelection(idx=%s): mbetaalnr → %s", idx, mbetaalnr, extra={"event.action": "showSelection", "logrite.idx": idx})
        if  idx.column() == 0:
 
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showSelection(idx=%s): engine → %s", idx, engine, extra={"event.action": "showSelection", "logrite.idx": idx})
            con = engine.connect()
            logger.debug("showSelection(idx=%s): con → %s", idx, con, extra={"event.action": "showSelection", "logrite.idx": idx})
            selbet = select([loonbetalingen]).where(loonbetalingen.c.betalingID == mbetaalnr)
            rpbet = con.execute(selbet).first()
            logger.debug("showSelection(idx=%s): selbet → %s", idx, selbet, extra={"event.action": "showSelection", "logrite.idx": idx})
            logger.debug("showSelection(idx=%s): rpbet → %s", idx, rpbet, extra={"event.action": "showSelection", "logrite.idx": idx})
            
            header = ['Betalingnr', 'Maandperiode', 'Accountnummer', 'Werknemer', 'Voornaam',\
              'Tussenvoegsel','Achternaam', 'Straat', 'Huisnummer', 'Toevoeging',\
              'Postcode', 'Woonplaats', 'Geboortedatum', 'Indienstdatum','Brutoloon',\
              'Bruto variabel', 'Pensioenpremie', 'Bijtelling auto','Loonheffing',\
              'Inhouding overig','Periodieke uitkering','Vergoeding overig',\
              'Vergoeding reiskosten','Res. vakantietoeslag','Werkuren',\
              'Bijzonder tarief', 'Bedrag_byz_tarief','Reisuren', 'Overuren 125%',\
              'Overuren 150%', 'Overuren 200%', 'Nettoloon','Uurloon', 'Reisuurloon',\
              'Uren verlof', 'Uren extra verlof', 'Uren feestdag', 'Uren ziekte',\
              'Uren dokter', 'Uren geoorl. verzuim', 'Uren ongeoorl. verzuim',\
              'Loonschaal', 'Loontrede', 'Verlofsaldo', 'Alg. Heffingskorting',\
              'Arbeidskorting', 'Werkgever pensioenpremie','Werkgever WAO-IVA-WGA premie',\
              'Werkgever AWF premie', 'Werkgever ZVW kosten','Boekdatum', 'Cumulatief verschil uren',\
              'Uren in deze maand', 'Geboekt deze maand']
            
            logger.debug("showSelection(idx=%s): header → %s", idx, header, extra={"event.action": "showSelection", "logrite.idx": idx})
            class MainWindow(QDialog):
                logger.debug("<<< Exiting showSelection(idx=%s)", idx, extra={"event.action": "showSelection", "logrite.idx": idx})
                def __init__(self):
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                    
                    self.setWindowTitle("Opvragen loonbetaling")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                    
                    self.setFont(QFont('Arial', 10))   
                                                      
                    self.lbl = QLabel()
                    self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                    self.lbl.setPixmap(self.pixmap)
                    grid.addWidget(self.lbl , 0, 0)
                    
                    grid.addWidget(QLabel('Opvragen Loonbetalingen per werknemer en periode'),0, 2, 1, 3)
            
                    self.logo = QLabel()
                    self.pixmap = QPixmap('./images/logos/logo.jpg')
                    self.logo.setPixmap(self.pixmap)
                    grid.addWidget(self.logo , 0, 5, 1, 1, Qt.AlignRight)                
                    index = 3
                    for item in header:
                        horpos = index%3
                        verpos = index
                        if index%3 == 1:
                            verpos = index - 1
                        elif index%3 == 2:
                            verpos = index -2
                        self.lbl = QLabel(header[index-3])
                        
                        self.Gegevens = QLabel()
                        if type(rpbet[index-3]) == float:
                            q1Edit = QLineEdit('{:12.2f}'.format(rpbet[index-3]))
                            q1Edit.setAlignment(Qt.AlignRight)
                        elif type(rpbet[index-3]) == int:
                            q1Edit = QLineEdit(str(rpbet[index-3]))
                            q1Edit.setAlignment(Qt.AlignRight)
                        else:
                            q1Edit = QLineEdit(str(rpbet[index-3]))
                        q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                        q1Edit.setFixedWidth(200)
                        q1Edit.setDisabled(True)
                        grid.addWidget(self.lbl, verpos, horpos+horpos%3)
                        grid.addWidget(q1Edit, verpos, horpos+horpos%3+1)
                        
                        index +=1
                        
                    terugBtn = QPushButton('Sluiten')
                    terugBtn.clicked.connect(self.accept)
            
                    grid.addWidget(terugBtn, verpos+1, 5, 1 , 1, Qt.AlignRight)
                    terugBtn.setFont(QFont("Arial",10))
                    terugBtn.setFixedWidth(100) 
                    terugBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), verpos+1, 2, 1, 2)
                                                                            
                    self.setLayout(grid)
                    self.setGeometry(100, 50, 150, 150)
            
            mainWin = MainWindow()
            mainWin.exec_()
        
    win = MyWindow(data_list, header)
    win.exec_()
    zoeken(m_email)