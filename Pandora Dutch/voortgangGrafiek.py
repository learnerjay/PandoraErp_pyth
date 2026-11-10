from login import hoofdMenu
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog, QPrintDialog
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries,\
                          QBarCategoryAxis, QPieSeries, QPieSlice     
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QIcon, QFont, QPixmap, QPainter, QRegExpValidator, QPen, QPageLayout
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QGridLayout,\
        QPushButton, QMessageBox, QComboBox
from sqlalchemy import (Table, Column, Integer, String, MetaData,\
                        create_engine, Float)
from sqlalchemy.sql import select
import datetime
import logging
logger = logging.getLogger(__name__)

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    
def sluit(self, m_email):
    logger.warning(">>> Entering sluit(m_email=%s)", m_email, extra={"event.action": "sluit"})
    self.close()
    zoekwk(m_email)   
    logger.debug("<<< Exiting sluit(m_email=%s)", m_email, extra={"event.action": "sluit"})
    
def ongInvoer():
    logger.warning(">>> Entering ongInvoer()", extra={"event.action": "ongInvoer"})
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg, extra={"event.action": "ongInvoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Foutieve invoer\nzoekterm opnieuw invoeren s.v.p.!')
    msg.setWindowTitle('Voortgangsgrafieken')               
    logger.debug("<<< Exiting ongInvoer()", extra={"event.action": "ongInvoer"})
    msg.exec_()

def jaarweek():
    logger.warning(">>> Entering jaarweek()", extra={"event.action": "jaarweek"})
    dt = datetime.datetime.now()
    logger.debug("jaarweek(): dt → %s", dt, extra={"event.action": "jaarweek"})
    week = str('0'+str(dt.isocalendar()[1]))[-2:]
    logger.debug("jaarweek(): week → %s", week, extra={"event.action": "jaarweek"})
    jaar = str(dt.isocalendar()[0])
    jrwk = jaar+week
    logger.debug("jaarweek(): jaar → %s", jaar, extra={"event.action": "jaarweek"})
    logger.debug("jaarweek(): jrwk → %s", jrwk, extra={"event.action": "jaarweek"})
    logger.debug("<<< Exiting jaarweek()", extra={"event.action": "jaarweek"})
    return(jrwk)
    
def geenWeek():
    logger.warning(">>> Entering geenWeek()", extra={"event.action": "geenWeek"})
    msg = QMessageBox()
    logger.debug("geenWeek(): msg → %s", msg, extra={"event.action": "geenWeek"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Weeknummer is niet aanwezig!')
    msg.setWindowTitle('Voortgangsgrafieken')               
    logger.debug("<<< Exiting geenWeek()", extra={"event.action": "geenWeek"})
    msg.exec_() 
    
def info(self):
    logger.warning(">>> Entering info()", extra={"event.action": "info"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Informatie status van externe werken")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
            grid = QGridLayout()
            grid.setSpacing(20)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 0, 1, 1, Qt.AlignRight)
        
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 0, 0)
            
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): kEdit → %s", parent, kEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): kEdit → %s", self, parent, kEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Zoekterm → %s", parent, self.Zoekterm, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): zktermEdit → %s", parent, zktermEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): zktermEdit → %s", self, parent, zktermEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): sluitBtn → %s", parent, sluitBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): sluitBtn → %s", self, parent, sluitBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            infolbl = QLabel(
    '''
    
    Informatie over Voortgangstatus
    
    
    A. Voorbereiding / Opdracht verwerven, materialen reserveren.
    
    B. Werk is gestart / 1e gedeelte materialen geleverd.           
    
    C. Werk is 33% gereed. (Factuur indienen van  1e termijn van 33%)
    
    D. Werk is 50% gereed.
    
    E. Werk is 75% gereed. (Factuur indienen van 2e termijn van 33%)
    
    F. Werk is 90 % gereed. (Factuur indienen van 3e termijn van 20%)\t\t       
    
    G. Werk is technisch gereed incl meerminderwerk.
       (Factuur indienen van 14% +/- meerminderwerk)
       
    H. Werk is financieel afgerond en afgemeld.
    
    
    ''')
            grid.addWidget(infolbl, 1, 0)
            infolbl.setStyleSheet("font: 10pt Comic Sans MS; color: black ; background-color: #D9E1DF")  
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 2, 0, 1, 1, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(500, 200, 150, 100)
            
    window = Widget()
    window.exec_()
                
def zoekwk(m_email):
    logger.warning(">>> Entering zoekwk(m_email=%s)", m_email, extra={"event.action": "zoekwk"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Printen status grafieken")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
            
            self.Keuze = QLabel()
            kEdit = QComboBox()
            kEdit.setFixedWidth(300)
            kEdit.setFont(QFont("Arial", 10))
            kEdit.setStyleSheet("color: black;  background-color: #F8F7EE")
            kEdit.addItem('                  Keuze grafieken')
            kEdit.addItem('1. Grafiek status externe Werken')
            kEdit.addItem('2. Grafiek werken status-aantal\n    Taartgrafiek')
            kEdit.addItem('3. Grafiek werken status-aantal\n    Staafgrafiek')
            kEdit.activated[str].connect(self.kChanged)
               
            self.Zoekterm = QLabel()
            zktermEdit = QLineEdit()
            zktermEdit.setFixedWidth(65)
            zktermEdit.setFont(QFont("Arial", 10))
            zktermEdit.textChanged.connect(self.zktermChanged)
            reg_ex = QRegExp("^[2]{1}[0-9]{1}[0-9]{2}[0-5]{1}[0-9]{1}$")
            input_validator = QRegExpValidator(reg_ex, zktermEdit)
            zktermEdit.setValidator(input_validator)
     
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
             
            grid.addWidget(kEdit, 1, 0, 1, 2, Qt.AlignRight)                     
            lbl1 = QLabel('Jaarweek-uitdraai (jjjjww)')  
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 2, 0, 1, 2, Qt.AlignCenter)
            grid.addWidget(zktermEdit, 2, 1, 1, 1, Qt.AlignRight)
            
            self.setLayout(grid)
            self.setGeometry(500, 200, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1, 2, Qt.AlignRight)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
    
            applyBtn = QPushButton('Zoeken')
            applyBtn.clicked.connect(self.accept)
            
            sluitBtn = QPushButton('Sluiten')
            sluitBtn.clicked.connect(lambda: windowSluit(self, m_email))            
          
            grid.addWidget(applyBtn, 3, 1, 1 , 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial", 10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            grid.addWidget(sluitBtn, 3, 0, 1, 2, Qt.AlignCenter)
            sluitBtn.setFont(QFont("Arial", 10))
            sluitBtn.setFixedWidth(100)
            sluitBtn.setStyleSheet("color: black;  background-color: gainsboro")
                   
        def kChanged(self, text):
            logger.warning(">>> Entering kChanged(text=%s)", text, extra={"event.action": "kChanged", "logrite.text": text})
            self.Keuze.setText(text)
            logger.debug("<<< Exiting kChanged(text=%s)", text, extra={"event.action": "kChanged", "logrite.text": text})
            
        def zktermChanged(self, text):
            logger.warning(">>> Entering zktermChanged(text=%s)", text, extra={"event.action": "zktermChanged", "logrite.text": text})
            self.Zoekterm.setText(text)
            logger.debug("<<< Exiting zktermChanged(text=%s)", text, extra={"event.action": "zktermChanged", "logrite.text": text})
 
        def returnk(self):
            logger.warning(">>> Entering returnk()", extra={"event.action": "returnk"})
            logger.debug("<<< Exiting returnk()", extra={"event.action": "returnk"})
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
            return [dialog.returnk(),dialog.returnzkterm()]       

    window = Widget()
    data = window.getData()
    if not data[0] or data[0][0] == ' ':
        keuze = 0
    elif data[0]:
        keuze = int(data[0][0])
    else:
        ongInvoer()
        zoekwk(m_email)
    if data[1] and len(data[1]) == 6:
        jrwk = data[1]
    else:
        ongInvoer()
        zoekwk(m_email)
    if keuze == 1:
        barGrafiek(keuze, jrwk, m_email)
    elif keuze == 2:
        statusPie(keuze, jrwk, m_email)
    elif keuze == 3:
        statusGrafiek(keuze, jrwk, m_email)
    zoekwk(m_email)
       
def barGrafiek(keuze, jrwk, m_email):
    logger.warning(">>> Entering barGrafiek(keuze=%s,jrwk=%s,m_email=%s)", keuze, jrwk, m_email, extra={"event.action": "barGrafiek", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    metadata = MetaData()      
    logger.debug("barGrafiek(keuze=%s,jrwk=%s,m_email=%s): metadata → %s", keuze, jrwk, m_email, metadata, extra={"event.action": "barGrafiek", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    resultaten_status = Table('resultaten_status', metadata,
        Column('rID', Integer, primary_key=True),
        Column('status', String),
        Column('aanneemsom', Float),
        Column('kosten', Float),
        Column('aantal', Integer),
        Column('boekweek', String),
        Column('betaald', Float),
        Column('meerminderwerk', Float))
    
    logger.debug("barGrafiek(keuze=%s,jrwk=%s,m_email=%s): resultaten_status → %s", keuze, jrwk, m_email, resultaten_status, extra={"event.action": "barGrafiek", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("barGrafiek(keuze=%s,jrwk=%s,m_email=%s): engine → %s", keuze, jrwk, m_email, engine, extra={"event.action": "barGrafiek", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    con = engine.connect()
    
    logger.debug("barGrafiek(keuze=%s,jrwk=%s,m_email=%s): con → %s", keuze, jrwk, m_email, con, extra={"event.action": "barGrafiek", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    selsr = select([resultaten_status]).where(resultaten_status.c.boekweek == jrwk).order_by\
         (resultaten_status.c.status)
    logger.debug("barGrafiek(keuze=%s,jrwk=%s,m_email=%s): selsr → %s", keuze, jrwk, m_email, selsr, extra={"event.action": "barGrafiek", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    rpsr = con.execute(selsr).fetchall()
    logger.debug("barGrafiek(keuze=%s,jrwk=%s,m_email=%s): rpsr → %s", keuze, jrwk, m_email, rpsr, extra={"event.action": "barGrafiek", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    if not rpsr:
        geenWeek()
        logger.debug("<<< Exiting barGrafiek(keuze=%s,jrwk=%s,m_email=%s)", keuze, jrwk, m_email, extra={"event.action": "barGrafiek", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
        return
    
    class Window(QDialog):
        def __init__(self):          
            QDialog.__init__(self)
            self.setWindowTitle("Printen grafiek status van externe werken over jaar "+jrwk[0:4]) 
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                                                  Qt.WindowMinMaxButtonsHint)
            self.chart = QChart()
            self.chart_view = QChartView(self.chart)
            self.chart_view.setRenderHint(QPainter.Antialiasing)
            self.buttonPreview = QPushButton('Afdrukvoorbeeld', self)
            self.buttonPreview.clicked.connect(self.handle_preview)
            self.buttonPreview.setStyleSheet("color: black;  background-color: gainsboro")
            self.buttonPrint = QPushButton('Printen', self)
            self.buttonPrint.clicked.connect(self.handle_print) 
            self.buttonPrint.setStyleSheet("color: black;  background-color: gainsboro")
            self.buttonSluit = QPushButton('Sluiten', self)
            self.buttonSluit.clicked.connect(lambda: sluit(self, m_email)) 
            self.buttonSluit.setStyleSheet("color: black;  background-color: gainsboro")
            self.buttonInfo = QPushButton('Info', self)
            self.buttonInfo.clicked.connect(lambda: info(self))
            self.buttonInfo.setStyleSheet("color: black;  background-color: gainsboro")
            layout = QGridLayout(self)
            layout.addWidget(self.chart_view, 0, 0, 1, 4)
            layout.addWidget(self.buttonInfo, 1, 0)
            layout.addWidget(self.buttonSluit, 1, 1)
            layout.addWidget(self.buttonPrint, 1, 2)
            layout.addWidget(self.buttonPreview, 1,3) 
 
            self.create_chart()
    
        def create_chart(self):
            self.chart.setTitle('Grafiek kosten / baten van externe werken per status - opnameweek '+jrwk)
            font = QFont("Sans Serif", 10)
            font.setWeight(QFont.Bold)
            self.chart.setTitleFont(font)
            set0 = QBarSet('Aanneemsom +/- Meerminderwerk')
            set1 = QBarSet('Kosten')
            set2 = QBarSet('Betaald Bedrag')
    
            set0 << rpsr[0][2]+rpsr[0][7] << rpsr[1][2]+rpsr[1][7] << rpsr[2][2]+rpsr[2][7]<< rpsr[3][2]+rpsr[3][7] << rpsr[4][2]+rpsr[4][7] << rpsr[5][2]+rpsr[5][7] << rpsr[6][2]+rpsr[6][7] << rpsr[7][2]+rpsr[7][7] 
            set1 << rpsr[0][3] << rpsr[1][3] << rpsr[2][3] << rpsr[3][3] << rpsr[4][3] << rpsr[5][3] << rpsr[6][3] << rpsr[7][3]
            set2 << rpsr[0][6] << rpsr[1][6] << rpsr[2][6] << rpsr[3][6] << rpsr[4][6] << rpsr[5][6] << rpsr[6][6] << rpsr[7][6] 
            
            barseries = QBarSeries()
            barseries.append(set0)
            barseries.append(set1)
            barseries.append(set2)
            barseries.append
                                      
            categories = ["Status A","Status B","Status C","Status D","Status E","Status F","Status G","Status H"]
                                               
            self.chart.addSeries(barseries)                                                         
            self.chart.axisX() 
            self.chart.createDefaultAxes()  
            axisX = QBarCategoryAxis()
            axisX.append(categories)
            self.chart.setAxisX(axisX, barseries)
            axisX.setRange(str("Status A"), str("Status H"))
                         
        def handle_print(self):
            printer = QPrinter(QPrinter.HighResolution)
            dialog = QPrintDialog(printer, self)
            printer.setOrientation(QPrinter.Landscape)
            if dialog.exec_() == QPrintDialog.Accepted:
                self.handle_paint_request(printer)
                logger.warning(">>> Entering handle_print()", extra={"event.action": "handle_print"})
                logger.debug("handle_print(self=%s): printer → %s", self, printer, extra={"event.action": "handle_print"})
                logger.debug("handle_print(): printer → %s", printer, extra={"event.action": "handle_print"})
                logger.debug("handle_print(self=%s): dialog → %s", self, dialog, extra={"event.action": "handle_print"})
                logger.debug("<<< Exiting handle_print()", extra={"event.action": "handle_print"})
    
        def handle_preview(self):
            dialog = QPrintPreviewDialog()
            dialog.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            dialog.setWindowFlags(dialog.windowFlags()| Qt.WindowSystemMenuHint |
                                                    Qt.WindowMinMaxButtonsHint)
            dialog.resize(1485, 990)
            #dialog.setMinimumSize(1485, 990)
            dialog.paintRequested.connect(self.handle_paint_request)
            dialog.exec_()
            logger.warning(">>> Entering handle_preview()", extra={"event.action": "handle_preview"})
            logger.debug("handle_preview(self=%s): dialog → %s", self, dialog, extra={"event.action": "handle_preview"})
            logger.debug("handle_preview(): dialog → %s", dialog, extra={"event.action": "handle_preview"})
            logger.debug("<<< Exiting handle_preview()", extra={"event.action": "handle_preview"})
    
        def handle_paint_request(self, printer):
            logger.warning(">>> Entering handle_paint_request(printer=%s)", printer, extra={"event.action": "handle_paint_request", "logrite.printer": printer})
            painter = QPainter(printer)
            logger.debug("handle_paint_request(printer=%s): painter → %s", printer, painter, extra={"event.action": "handle_paint_request", "logrite.printer": printer})
            logger.debug("handle_paint_request(self=%s,printer=%s): painter → %s", self, printer, painter, extra={"event.action": "handle_paint_request", "logrite.printer": printer})
            painter.setViewport(self.chart_view.rect())
            painter.setWindow(self.chart_view.rect()) 
            printer.setPageOrientation(QPageLayout.Landscape)                       
            self.chart_view.render(painter)
            logger.debug("handle_paint_request(self=%s,printer=%s): printer → %s", self, printer, printer, extra={"event.action": "handle_paint_request", "logrite.printer": printer})
            painter.end()
            logger.debug("<<< Exiting handle_paint_request(printer=%s)", printer, extra={"event.action": "handle_paint_request", "logrite.printer": printer})
         
    window = Window()
    window.resize(1350, 900)
    window.exec_()
    
def statusGrafiek(keuze, jrwk, m_email):
    logger.warning(">>> Entering statusGrafiek(keuze=%s,jrwk=%s,m_email=%s)", keuze, jrwk, m_email, extra={"event.action": "statusGrafiek", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    metadata = MetaData()      
    logger.debug("statusGrafiek(keuze=%s,jrwk=%s,m_email=%s): metadata → %s", keuze, jrwk, m_email, metadata, extra={"event.action": "statusGrafiek", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    resultaten_status = Table('resultaten_status', metadata,
        Column('rID', Integer, primary_key=True),
        Column('status', String),
        Column('aantal', Integer),
        Column('boekweek', String))
   
    logger.debug("statusGrafiek(keuze=%s,jrwk=%s,m_email=%s): resultaten_status → %s", keuze, jrwk, m_email, resultaten_status, extra={"event.action": "statusGrafiek", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("statusGrafiek(keuze=%s,jrwk=%s,m_email=%s): engine → %s", keuze, jrwk, m_email, engine, extra={"event.action": "statusGrafiek", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    con = engine.connect()
    
    logger.debug("statusGrafiek(keuze=%s,jrwk=%s,m_email=%s): con → %s", keuze, jrwk, m_email, con, extra={"event.action": "statusGrafiek", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    selr = select([resultaten_status]).where(resultaten_status.c.boekweek == jrwk).order_by\
         (resultaten_status.c.status)
    logger.debug("statusGrafiek(keuze=%s,jrwk=%s,m_email=%s): selr → %s", keuze, jrwk, m_email, selr, extra={"event.action": "statusGrafiek", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    rpr = con.execute(selr).fetchall()
    logger.debug("statusGrafiek(keuze=%s,jrwk=%s,m_email=%s): rpr → %s", keuze, jrwk, m_email, rpr, extra={"event.action": "statusGrafiek", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    if not rpr:
        geenWeek()
        logger.debug("<<< Exiting statusGrafiek(keuze=%s,jrwk=%s,m_email=%s)", keuze, jrwk, m_email, extra={"event.action": "statusGrafiek", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
        return
    
    class Window(QDialog):
        def __init__(self):
            QDialog.__init__(self)
            self.setWindowTitle("Printen grafiek aantal externe werken per status over jaar "+jrwk[0:4]) 
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                                                  Qt.WindowMinMaxButtonsHint)
            self.chart = QChart()
            self.chart_view = QChartView(self.chart)
            self.chart_view.setRenderHint(QPainter.Antialiasing)
            self.buttonPreview = QPushButton('Afdrukvoorbeeld', self)
            self.buttonPreview.clicked.connect(self.handle_preview)
            self.buttonPreview.setStyleSheet("color: navy;  background-color: gainsboro")
            self.buttonPrint = QPushButton('Printen', self)
            self.buttonPrint.clicked.connect(self.handle_print) 
            self.buttonPrint.setStyleSheet("color: navy;  background-color: gainsboro")
            self.buttonSluit = QPushButton('Sluiten', self)
            self.buttonSluit.clicked.connect(lambda: sluit(self, m_email))
            self.buttonSluit.setStyleSheet("color: navy;  background-color: gainsboro")
            self.buttonInfo = QPushButton('Info', self)
            self.buttonInfo.clicked.connect(lambda: info(self))
            self.buttonInfo.setStyleSheet("color: navy;  background-color: gainsboro")
           
            layout = QGridLayout(self)
            layout.addWidget(self.chart_view, 0, 0, 1, 4)
            layout.addWidget(self.buttonInfo, 1, 0)
            layout.addWidget(self.buttonSluit, 1, 1)
            layout.addWidget(self.buttonPrint, 1, 2)
            layout.addWidget(self.buttonPreview, 1, 3) 
            self.create_chart()
            logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
            logger.debug("__init__(): self.chart → %s", self.chart, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.view → %s", self.view, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): view → %s", self, view, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.buttonPreview → %s", self.buttonPreview, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): buttonPreview → %s", self, buttonPreview, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.buttonPrint → %s", self.buttonPrint, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): buttonPrint → %s", self, buttonPrint, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.buttonSluit → %s", self.buttonSluit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): buttonSluit → %s", self, buttonSluit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.buttonInfo → %s", self.buttonInfo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): buttonInfo → %s", self, buttonInfo, extra={"event.action": "__init__"})
            logger.debug("__init__(): layout → %s", layout, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): layout → %s", self, layout, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})
    
        def create_chart(self):
            self.chart.setTitle('Grafiek aantal externe werken per status - opnameweek '+jrwk) 
            font = QFont("Sans Serif", 10)
            font.setWeight(QFont.Bold)
            self.chart.setTitleFont(font)
            set0 = QBarSet('Aantal externe werken per status')
      
            set0 << rpr[0][2] << rpr[1][2] << rpr[2][2] << rpr[3][2] << rpr[4][2] << rpr[5][2] << rpr[6][2] << rpr[7][2]
 
            barseries = QBarSeries()
            barseries.append(set0)
            barseries.append
               
            categories = ["Status A","Status B","Status C","Status D","Status E","Status F","Status G","Status H"]
                                               
            self.chart.addSeries(barseries)                                                         
            self.chart.axisX() 
            self.chart.createDefaultAxes()  
            axisX = QBarCategoryAxis()
            axisX.append(categories)
            self.chart.setAxisX(axisX, barseries)
            axisX.setRange(str("Status A"), str("Status H"))
            logger.warning(">>> Entering create_chart()", extra={"event.action": "create_chart"})
            logger.debug("create_chart(self=%s): chart → %s", self, chart, extra={"event.action": "create_chart"})
            logger.debug("create_chart(self=%s): font → %s", self, font, extra={"event.action": "create_chart"})
            logger.debug("create_chart(): font → %s", font, extra={"event.action": "create_chart"})
            logger.debug("create_chart(self=%s): series → %s", self, series, extra={"event.action": "create_chart"})
            logger.debug("create_chart(): series → %s", series, extra={"event.action": "create_chart"})
            logger.debug("create_chart(self=%s): slice_ → %s", self, slice_, extra={"event.action": "create_chart"})
            logger.debug("<<< Exiting create_chart()", extra={"event.action": "create_chart"})
            logger.debug("create_chart(): slice_ → %s", slice_, extra={"event.action": "create_chart"})
                           
        def handle_print(self):
            logger.warning(">>> Entering handle_print()", extra={"event.action": "handle_print"})
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOrientation(QPrinter.Landscape) 
            dialog = QPrintDialog(printer, self)
            if dialog.exec_() == QPrintDialog.Accepted:
                logger.debug("handle_print(): dialog → %s", dialog, extra={"event.action": "handle_print"})
                self.handle_paint_request(printer)
    
        def handle_preview(self):
            dialog = QPrintPreviewDialog()
            dialog.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            dialog.setWindowFlags(dialog.windowFlags()| Qt.WindowSystemMenuHint |
                                                      Qt.WindowMinMaxButtonsHint)
            dialog.resize(1485, 990)
            #dialog.setMinimumSize(1485, 990)
            dialog.paintRequested.connect(self.handle_paint_request)
            dialog.exec_()
    
        def handle_paint_request(self, printer):
            painter = QPainter(printer)
            painter.setViewport(self.chart_view.rect())
            painter.setWindow(self.chart_view.rect()) 
            printer.setPageOrientation(QPageLayout.Landscape)                       
            self.chart_view.render(painter)
            painter.end()
         
    window = Window()
    window.resize(1350, 900)
    window.exec_()
    
def statusPie(keuze, jrwk, m_email):
    logger.warning(">>> Entering statusPie(keuze=%s,jrwk=%s,m_email=%s)", keuze, jrwk, m_email, extra={"event.action": "statusPie", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    metadata = MetaData()      
    logger.debug("statusPie(keuze=%s,jrwk=%s,m_email=%s): metadata → %s", keuze, jrwk, m_email, metadata, extra={"event.action": "statusPie", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    resultaten_status = Table('resultaten_status', metadata,
        Column('rID', Integer, primary_key=True),
        Column('status', String),
        Column('aantal', Integer),
        Column('boekweek', String))
   
    logger.debug("statusPie(keuze=%s,jrwk=%s,m_email=%s): resultaten_status → %s", keuze, jrwk, m_email, resultaten_status, extra={"event.action": "statusPie", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("statusPie(keuze=%s,jrwk=%s,m_email=%s): engine → %s", keuze, jrwk, m_email, engine, extra={"event.action": "statusPie", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    con = engine.connect()
    
    logger.debug("statusPie(keuze=%s,jrwk=%s,m_email=%s): con → %s", keuze, jrwk, m_email, con, extra={"event.action": "statusPie", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    selr = select([resultaten_status]).where(resultaten_status.c.boekweek == jrwk).order_by\
         (resultaten_status.c.status)
    logger.debug("statusPie(keuze=%s,jrwk=%s,m_email=%s): selr → %s", keuze, jrwk, m_email, selr, extra={"event.action": "statusPie", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    rpr = con.execute(selr).fetchall()
    logger.debug("statusPie(keuze=%s,jrwk=%s,m_email=%s): rpr → %s", keuze, jrwk, m_email, rpr, extra={"event.action": "statusPie", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    if not rpr:
        geenWeek()
        logger.debug("<<< Exiting statusPie(keuze=%s,jrwk=%s,m_email=%s)", keuze, jrwk, m_email, extra={"event.action": "statusPie", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
        return
    
    class Window(QDialog):
        def __init__(self):          
            QDialog.__init__(self)
            self.setWindowTitle("Printen grafiek status van externe werken over jaar "+jrwk[0:4]) 
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                                                  Qt.WindowMinMaxButtonsHint)
            self.chart = QChart()
            self.chart.legend().show()
            self.chart.legend().setAlignment(Qt.AlignRight)
            self.view = QChartView(self.chart)
            self.view.setRenderHint(QPainter.Antialiasing)
            self.buttonPreview = QPushButton('Afdrukvoorbeeld', self)
            self.buttonPreview.clicked.connect(self.handle_preview)
            self.buttonPreview.setStyleSheet("color: black;  background-color: gainsboro")
            self.buttonPrint = QPushButton('Printen', self)
            self.buttonPrint.clicked.connect(self.handle_print)
            self.buttonPrint.setStyleSheet("color: black;  background-color: gainsboro")
            self.buttonSluit = QPushButton('Sluiten', self)
            self.buttonSluit.clicked.connect(lambda: sluit(self, m_email))
            self.buttonSluit.setStyleSheet("color: black;  background-color: gainsboro")
            self.buttonInfo = QPushButton('Info', self)
            self.buttonInfo.clicked.connect(lambda: info(self))
            self.buttonInfo.setStyleSheet("color: black;  background-color: gainsboro") 
            layout = QGridLayout(self)
            layout.addWidget(self.view, 0, 0, 1, 4)
            layout.addWidget(self.buttonInfo, 1, 0)
            layout.addWidget(self.buttonSluit, 1, 1)
            layout.addWidget(self.buttonPrint, 1, 2)
            layout.addWidget(self.buttonPreview, 1, 3)             
            self.create_chart()
    
        def create_chart(self):
            self.chart.setTitle('Grafiek aantal externe werken per status - opnameweek '+jrwk)
            font = QFont("Sans Serif", 10)
            font.setWeight(QFont.Bold)
            self.chart.setTitleFont(font)
            
            series = QPieSeries()
            slice_ = QPieSlice()
            series.setUseOpenGL(enable=True)
            series.append('Status A = '+str(rpr[0][2]), rpr[0][2])
            series.append('Status B = '+str(rpr[1][2]), rpr[1][2])
            series.append('Status C = '+str(rpr[2][2]), rpr[2][2])
            series.append('Status D = '+str(rpr[3][2]), rpr[3][2])
            series.append('Status E = '+str(rpr[4][2]), rpr[4][2])
            series.append('Status F = '+str(rpr[5][2]), rpr[5][2])
            series.append('Status G = '+str(rpr[6][2]), rpr[6][2])
            series.append('Status H = '+str(rpr[7][2]), rpr[7][2])
  
            for i, slice_ in enumerate(series.slices()):
                slice_.setLabelVisible()
                #slice_.setLabelPosition(3)
                if i == 0:
                    slice_.setPen(QPen(Qt.black, 2))
                    slice_.setBrush(Qt.green)
                elif i == 1:
                    slice_.setPen(QPen(Qt.black, 2))
                    slice_.setBrush(Qt.red)
                elif i == 2:
                    slice_.setExploded()
                    slice_.setPen(QPen(Qt.black, 2))
                    slice_.setBrush(Qt.yellow)
                elif i == 3:
                    slice_.setPen(QPen(Qt.black, 2))
                    slice_.setBrush(Qt.magenta)
                elif i == 4:
                    slice_.setPen(QPen(Qt.black, 2))
                    slice_.setBrush(Qt.cyan)
                elif i == 5:
                    slice_.setPen(QPen(Qt.black, 2))
                    slice_.setBrush(Qt.blue)
                elif i == 6:
                    slice_.setPen(QPen(Qt.black, 2))
                    slice_.setBrush(Qt.darkYellow)
                elif i == 7:
                    slice_.setPen(QPen(Qt.black, 2))
                    slice_.setBrush(Qt.darkRed)
                       
            self.chart.addSeries(series)
            
        def handle_print(self):
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOrientation(QPrinter.Landscape) 
            dialog = QPrintDialog(printer, self)
            if dialog.exec_() == QPrintDialog.Accepted:
                self.handle_paint_request(printer)
    
        def handle_preview(self):
            dialog = QPrintPreviewDialog()
            dialog.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            dialog.setWindowFlags(dialog.windowFlags()| Qt.WindowSystemMenuHint |
                                                      Qt.WindowMinMaxButtonsHint)
            dialog.resize(1050, 700)
            #dialog.setMinimumSize(1050, 700)
            dialog.paintRequested.connect(self.handle_paint_request)
            dialog.exec_()
    
        def handle_paint_request(self, printer):
            printer.setPageOrientation(QPageLayout.Landscape)
            painter = QPainter(printer)
            painter.setViewport(self.view.rect())
            painter.setWindow(self.view.rect()) 
            self.view.render(painter)
            painter.end()
            
    window = Window()
    window.resize(1050, 700)
    window.exec_()