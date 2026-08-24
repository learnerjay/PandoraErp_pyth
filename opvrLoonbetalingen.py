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
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)

def ongInvoer():
    logger.debug(">>> Entering ongInvoer()")
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Invalid input\nsearch term re-enter please!')
    msg.setWindowTitle('Request wage payments')
    logger.debug("<<< Exiting ongInvoer()")
    msg.exec_() 

def geenRecord():
    logger.debug(">>> Entering geenRecord()")
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No record found\nmake another selection please!')
    msg.setWindowTitle('Request wage payments')
    logger.debug("<<< Exiting geenRecord()")
    msg.exec_() 

def zoeken(m_email):
    logger.debug(">>> Entering zoeken(m_email=%s)", m_email)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            self.setWindowTitle("Payments")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                              
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze)
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit)
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit)
            k0Edit.setFixedWidth(250)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('     Request wage payments')
            k0Edit.addItem('1. Sorted by period')
            k0Edit.addItem('2. Filtered by period (yyyy-mm)\n    or (yyyyvak)')
            k0Edit.addItem('3. Filtered by surname')
            k0Edit.activated[str].connect(self.k0Changed)
    
            self.Zoekterm = QLabel()
            logger.debug("__init__(parent=%s): self.Zoekterm → %s", parent, self.Zoekterm)
            zktermEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): zktermEdit → %s", self, parent, zktermEdit)
            logger.debug("__init__(parent=%s): zktermEdit → %s", parent, zktermEdit)
            zktermEdit.setFixedWidth(150)
            zktermEdit.setFont(QFont("Times", 10))
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
            grid.addWidget(lbl , 1, 0, 1, 2)
                                  
            grid.addWidget(k0Edit, 2, 0, 1, 2, Qt.AlignRight)
            lbl1 = QLabel('Search term')
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1)
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1)
            lbl1.setAlignment(Qt.AlignRight)
            grid.addWidget(lbl1, 3, 0)
            grid.addWidget(zktermEdit, 3, 0, 1, 2, Qt.AlignRight)
            
            self.setLayout(grid)
            self.setGeometry(700, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 5, 0, 1, 2, Qt.AlignCenter)
            
            logo = QLabel()
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 1, 1, 1, Qt.AlignRight)
    
            applyBtn = QPushButton('Search')
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 4, 1, 1 , 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial", 10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            closeBtn = QPushButton('Close')
            logger.debug("__init__(self=%s,parent=%s): closeBtn → %s", self, parent, closeBtn)
            logger.debug("__init__(parent=%s): closeBtn → %s", parent, closeBtn)
            closeBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(closeBtn, 4, 0, 1, 2, Qt.AlignCenter)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
            closeBtn.setFont(QFont("Arial", 10))
            closeBtn.setFixedWidth(100)
            closeBtn.setStyleSheet("color: black;  background-color: gainsboro")
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
    toonBetalingen(keuze, zoekterm, m_email)
    
def selectRow(index):
    logger.debug(">>> Entering selectRow(index=%s)", index)
    print('Recordnummer is: ', index.row())
    logger.debug("<<< Exiting selectRow(index=%s)", index)
 
def toonBetalingen(keuze,zoekterm, m_email):
    logger.debug(">>> Entering toonBetalingen(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email)
    import validZt      
    class MyWindow(QDialog):
        logger.debug("<<< Exiting toonBetalingen(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email)
        def __init__(self, data_list, header, *args):
            QWidget.__init__(self, *args,)
            self.setGeometry(10, 50, 1900, 900)
            self.setWindowTitle('Request wage payments')
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
            table_view.hideColumn(3)
            table_view.hideColumn(36)
            table_view.hideColumn(37)
            #table_view.clicked.connect(selectRow)
            table_view.clicked.connect(showSelection)
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
            logger.debug(">>> Entering __init__()")
            logger.debug("__init__(): grid → %s", grid)
            logger.debug("__init__(self=%s): grid → %s", self, grid)
            logger.debug("__init__(): self.lbl → %s", self.lbl)
            logger.debug("__init__(): self.pixmap → %s", self.pixmap)
            logger.debug("__init__(self=%s): lbl → %s", self, lbl)
            logger.debug("__init__(): self.logo → %s", self.logo)
            logger.debug("__init__(self=%s): logo → %s", self, logo)
            logger.debug("__init__(self=%s): index → %s", self, index)
            logger.debug("__init__(self=%s): horpos → %s", self, horpos)
            logger.debug("__init__(self=%s): verpos → %s", self, verpos)
            logger.debug("__init__(): self.Gegevens → %s", self.Gegevens)
            logger.debug("__init__(): q1Edit → %s", q1Edit)
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit)
            logger.debug("__init__(): terugBtn → %s", terugBtn)
            logger.debug("__init__(self=%s): terugBtn → %s", self, terugBtn)
            logger.debug("<<< Exiting __init__()")
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

    header = ['Payment no.', 'Monthly period', 'Account number', 'Employee', 'Thirst name', \
              'Infix', 'Surname', 'Street', 'House number', 'Suffix', \
              'Zipcode', 'Residence', 'Birth date', 'Into service date', 'Gross salary', \
              'Gross variable', 'Pension contribution', 'Addition car', 'Payroll tax', \
              'Withholding other', 'Periodic payment', 'Other compensation', \
              'Travel compensation', 'Res. holiday allowance cum.', 'Working hours', \
              'Special rate hours', 'Amount special rate', 'Travel hours', 'Overtime 125%', \
              'Overtime 150%', 'Overtime 200%', 'Net salary', 'Hourly wage', 'Travel hourly wage', \
              'Leave hours', 'Extra leave hours', 'Holiday hours', 'Illness hours', \
              'Doctor hours', 'Permitted leave hours', 'Illegal leave hours', \
              'Wage scale', 'Wage step', 'Leave balance', 'General tax credit', \
              'Employment tax credit', 'Employer pension contrib.', 'Employer WAO-IVA-WGA contrib.', \
              'Employer AWF contrib.', 'Employer ZVW costs', 'Booking date', \
              'Cumulative difference hours', 'Hours in this month', 'Booked this month']

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
        logger.debug(">>> Entering showSelection(idx=%s)", idx)
        mbetaalnr = idx.data()
        logger.debug("showSelection(idx=%s): mbetaalnr → %s", idx, mbetaalnr)
        if  idx.column() == 0:
 
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showSelection(idx=%s): engine → %s", idx, engine)
            con = engine.connect()
            logger.debug("showSelection(idx=%s): con → %s", idx, con)
            selbet = select([loonbetalingen]).where(loonbetalingen.c.betalingID == mbetaalnr)
            rpbet = con.execute(selbet).first()
            logger.debug("showSelection(idx=%s): selbet → %s", idx, selbet)
            logger.debug("showSelection(idx=%s): rpbet → %s", idx, rpbet)

            header = ['Payment no.', 'Monthly period', 'Account number', 'Employee', 'Thirst name', \
                      'Infix', 'Surname', 'Street', 'House number', 'Suffix', \
                      'Zipcode', 'Residence', 'Birth date', 'Into service date', 'Gross salary', \
                      'Gross variable', 'Pension contribution', 'Addition car', 'Payroll tax', \
                      'Withholding other', 'Periodic payment', 'Other compensation', \
                      'Travel compensation', 'Res. holiday allowance cum.', 'Working hours', \
                      'Special rate hours', 'Amount special rate', 'Travel hours', 'Overtime 125%', \
                      'Overtime 150%', 'Overtime 200%', 'Net salary', 'Hourly wage', 'Travel hourly wage', \
                      'Leave hours', 'Extra leave hours', 'Holiday hours', 'Illness hours', \
                      'Doctor hours', 'Permitted leave hours', 'Illegal leave hours', \
                      'Wage scale', 'Wage step', 'Leave balance', 'General tax credit', \
                      'Employment tax credit', 'Employer pension contrib.', 'Employer WAO-IVA-WGA contrib.', \
                      'Employer AWF contrib.', 'Employer ZVW costs', 'Booking date', \
                      'Cumulative difference hours', 'Hours in this month', 'Booked this month']
            
            logger.debug("showSelection(idx=%s): header → %s", idx, header)
            class MainWindow(QDialog):
                logger.debug("<<< Exiting showSelection(idx=%s)", idx)
                def __init__(self):
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                    
                    self.setWindowTitle("Request wage payments")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                    
                    self.setFont(QFont('Arial', 10))   
                                                      
                    self.lbl = QLabel()
                    self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                    self.lbl.setPixmap(self.pixmap)
                    grid.addWidget(self.lbl , 0, 0)
                    
                    grid.addWidget(QLabel('Request wage payments per employee and period'),0, 2, 1, 3)
            
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
                        
                    terugBtn = QPushButton('Close')
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