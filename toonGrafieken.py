from login import hoofdMenu
import datetime
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog, QPrintDialog
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis, QCategoryAxis
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QIcon, QFont, QPixmap, QRegExpValidator, QBrush, QColor,\
      QPen, QPainter, QPageLayout
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QGridLayout,\
        QPushButton, QMessageBox, QComboBox
from sqlalchemy import (Table, Column, Integer, String, MetaData,\
                        create_engine, Float, select, and_)
import logging
logger = logging.getLogger(__name__)

# colorpicker hex for graph line colors https://colors-picker.com/hex-color-picker/

def jaarweek():
    logger.warning(">>> Entering jaarweek()", extra={"event.action": "jaarweek"})
    dt = datetime.datetime.now()
    logger.debug("jaarweek(): dt → %s", dt, extra={"event.action": "jaarweek"})
    week = str('0'+str(dt.isocalendar()[1]))[-2:]
    logger.debug("jaarweek(): week → %s", week, extra={"event.action": "jaarweek"})
    jaar = str(dt.isocalendar()[0])
    jrwk = jaar+week
    logger.debug("jaarweek(): jrwk → %s", jrwk, extra={"event.action": "jaarweek"})
    logger.debug("jaarweek(): jaar → %s", jaar, extra={"event.action": "jaarweek"})
    logger.debug("<<< Exiting jaarweek()", extra={"event.action": "jaarweek"})
    return(jrwk)
    
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
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Please re-enter incorrect input\nsearch term!')
    msg.setWindowTitle('Progress charts')
    logger.debug("<<< Exiting ongInvoer()", extra={"event.action": "ongInvoer"})
    msg.exec_()
 
def zoekwk(m_email):
    logger.warning(">>> Entering zoekwk(m_email=%s)", m_email, extra={"event.action": "zoekwk"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Choice charts external works")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
            
            self.Keuze = QLabel()
            kEdit = QComboBox()
            kEdit.setFixedWidth(300)
            kEdit.setFont(QFont("Arial", 10))
            kEdit.setStyleSheet("color: black;  background-color: #F8F7EE")
            kEdit.addItem('                  Choice charts')
            kEdit.addItem('1. Costs total / budgeted costs')
            kEdit.addItem('2. Wages budgeted / realised')
            kEdit.addItem('3. Materials budgeted / realised')
            kEdit.addItem('4. Equipment budgeted / realised')
            kEdit.addItem('5. Hiring budgeted / realised')
            kEdit.addItem('6. Services budgeted / realised')
            kEdit.addItem('7. Project costs budgeted / realised')
            kEdit.addItem('8. Gross profit - prognosis / actual')
            kEdit.addItem('9. Work in progress - Payed amount')
            kEdit.addItem('A. Revenue - prognosis / actual')
            kEdit.addItem('B. Gross profit realised\n     More/less work')
    
            kEdit.activated[str].connect(self.kChanged)
               
            self.Zoekterm = QLabel()
            zktermEdit = QLineEdit()
            zktermEdit.setFixedWidth(65)
            zktermEdit.setFont(QFont("Arial", 10))
            zktermEdit.textChanged.connect(self.zktermChanged)
            reg_ex = QRegExp("^[2]{1}[0-9]{3}[0-5]{1}[0-9]{1}$")
            input_validator = QRegExpValidator(reg_ex, zktermEdit)
            zktermEdit.setValidator(input_validator)
     
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
             
            grid.addWidget(kEdit, 1, 0, 1, 2, Qt.AlignRight)                     
            lbl1 = QLabel('Year week-report (yyyyww)')
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
    
            applyBtn = QPushButton('Search')
            applyBtn.clicked.connect(self.accept)
 
            sluitBtn = QPushButton('Close')
            sluitBtn.clicked.connect(lambda: windowSluit(self, m_email))
                     
            grid.addWidget(applyBtn, 3, 1, 1 , 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial", 10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            grid.addWidget(sluitBtn, 3, 0, 1, 2, Qt.AlignCenter)
            sluitBtn.setFont(QFont("Arial", 10))
            sluitBtn.setFixedWidth(100)
            sluitBtn.setStyleSheet("color: black;  background-color: gainsboro")
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): selres → %s", parent, selres, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): resultaten → %s", parent, resultaten, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): metadata → %s", parent, metadata, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): metadata → %s", self, parent, metadata, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): engine → %s", parent, engine, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): engine → %s", self, parent, engine, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): con → %s", parent, con, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): con → %s", self, parent, con, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): selpar → %s", parent, selpar, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): selpar → %s", self, parent, selpar, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): rppar → %s", parent, rppar, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): rppar → %s", self, parent, rppar, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): bo_incr → %s", self, parent, bo_incr, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): bw_incr → %s", self, parent, bw_incr, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): jaar → %s", self, parent, jaar, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): rpres → %s", parent, rpres, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): rpres → %s", self, parent, rpres, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): t1 → %s", parent, t1, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): t2 → %s", parent, t2, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): t3 → %s", parent, t3, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): ysch → %s", self, parent, ysch, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): y3 → %s", parent, y3, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): y3val → %s", self, parent, y3val, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): x1 → %s", parent, x1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): xval1 → %s", self, parent, xval1, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): y4 → %s", parent, y4, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): y4val → %s", self, parent, y4val, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): x2 → %s", parent, x2, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): xval2 → %s", self, parent, xval2, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): x → %s", parent, x, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): y1 → %s", parent, y1, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): y2 → %s", parent, y2, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): idx → %s", self, parent, idx, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): yval1 → %s", self, parent, yval1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): yval2 → %s", self, parent, yval2, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): series1 → %s", parent, series1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): series1 → %s", self, parent, series1, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): series2 → %s", parent, series2, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): series2 → %s", self, parent, series2, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): chart → %s", parent, chart, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): chart → %s", self, parent, chart, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): font → %s", parent, font, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): font → %s", self, parent, font, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): axisX → %s", parent, axisX, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): axisX → %s", self, parent, axisX, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): axisY → %s", parent, axisY, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): axisY → %s", self, parent, axisY, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): axisPen → %s", parent, axisPen, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): axisPen → %s", self, parent, axisPen, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): axisBrush → %s", parent, axisBrush, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): axisBrush → %s", self, parent, axisBrush, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): Lfont → %s", parent, Lfont, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): Lfont → %s", self, parent, Lfont, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): Dfont → %s", parent, Dfont, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): Dfont → %s", self, parent, Dfont, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.chartView → %s", parent, self.chartView, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): chartView → %s", self, parent, chartView, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): buttonPreview → %s", parent, buttonPreview, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): buttonPreview → %s", self, parent, buttonPreview, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): buttonPrint → %s", parent, buttonPrint, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): buttonPrint → %s", self, parent, buttonPrint, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): buttonSluit → %s", parent, buttonSluit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): buttonSluit → %s", self, parent, buttonSluit, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
          
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
        ongInvoer()
        zoekwk(m_email)
    elif data[0]:
        keuze = data[0][0]
    else:
        ongInvoer()
        zoekwk(m_email)
    if data[1] and len(data[1]) == 6:
        jrwk = data[1]
        printGrafiek(keuze, jrwk, m_email)
    else:
        ongInvoer()
        zoekwk(m_email)
        
def printGrafiek(keuze, jrwk, m_email):
    logger.warning(">>> Entering printGrafiek(keuze=%s,jrwk=%s,m_email=%s)", keuze, jrwk, m_email, extra={"event.action": "printGrafiek", "logrite.keuze": keuze, "logrite.jrwk": jrwk})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle('Financial graphs external works')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
  
            grid = QGridLayout()
            grid.setSpacing(20)
            
            metadata = MetaData()
            resultaten = Table('resultaten', metadata,
                Column('resID', Integer(), primary_key=True),
                Column('statusweek', String),
                Column('btotaal', Float),
                Column('wtotaal', Float),
                Column('betaald_bedrag', Float),
                Column('meerminderwerk', Float),
                Column('onderhandenwerk', Float),
                Column('aanneemsom', Float),
                Column('blonen', Float),
                Column('wlonen', Float),
                Column('bmaterialen', Float),
                Column('wmaterialen', Float),
                Column('bmaterieel', Float),
                Column('wmaterieel', Float),
                Column('bprojectkosten', Float),
                Column('wprojectkosten', Float),
                Column('binhuur', Float),
                Column('winhuur', Float),
                Column('bdiensten', Float),
                Column('wdiensten', Float),
                Column('bruto_winst', Float),
                Column('boekweek', String))
            params_graphs = Table('params_graphs', metadata,
                Column('parID', Integer(), primary_key=True),
                Column('item', String),
                Column('y_scale', Integer),
                Column('prognosis', Integer),
                Column('color_1',String),
                Column('color_2', String))

            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            con = engine.connect()
            
            selpar = select([params_graphs]).order_by(params_graphs.c.parID)
            rppar = con.execute(selpar).fetchall()
            bo_incr = rppar[9][3]/52   # budgeted turnover per week
            bw_incr = rppar[7][3]/52   # budgeted profit per week
                                          
            jaar = jrwk[0:4]
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            con = engine.connect()
            selres = select([resultaten]).where(and_(resultaten.c.boekweek == jrwk,\
              resultaten.c.statusweek.like(jaar+'%'))).order_by(resultaten.c.statusweek)
            rpres = con.execute(selres)
            if keuze == '1':
                s1 = 2
                s2 = 3
                t1 = 'Costs total budgeted'
                t2 = 'Costs total realised'
                t3 = 'Costs total '
                c1 = rppar[0][4]
                c2 = rppar[0][5]
                ysch =  rppar[0][2]    # 160000000
            elif keuze == '2':
                s1 = 8
                s2 = 9
                t1 = 'Wages budgeted'
                t2 = 'Wages realised'
                t3 = 'Wages '
                c1 = rppar[1][4]
                c2 = rppar[1][5]
                ysch = rppar[1][2]    # 100000000
            elif keuze == '3':
                s1 = 10
                s2 = 11
                t1 = 'Materials budgeted'
                t2 = 'Materials realised'
                t3 = 'Materials '
                c1 = rppar[2][4]
                c2 = rppar[2][5]
                ysch =  rppar[2][2]   # 60000000
            elif keuze == '4':
                s1 = 12
                s2 = 13
                t1 = 'Equipment budgeted'
                t2 = 'Equipment realised'
                t3 = 'Equipment '
                c1 = rppar[3][4]
                c2 = rppar[3][5]
                ysch =  rppar[3][2]   # 20000000
            elif keuze == '5':
                s1 = 16
                s2 = 17
                t1 = 'Hiring budgeted'
                t2 = 'Hiring realised'
                t3 = 'Hiring '
                c1 = rppar[4][4]
                c2 = rppar[4][5]
                ysch = rppar[4][2]      # 30000000
            elif keuze == '6':
                s1 = 18
                s2 = 19
                t1 = 'Services budgeted'
                t2 = 'Services realised'
                t3 = 'Services '
                c1 = rppar[5][4]
                c2 = rppar[5][5]
                ysch = rppar[5][2]    # 30000000
            elif keuze == '7':
                s1 = 14
                s2 = 15
                t1 = 'Project costs budgeted'
                t2 = 'Project costs realised'
                t3 = 'Project costs '
                c1 = rppar[6][4]
                c2 = rppar[6][5]
                ysch = rppar[6][2]    # 10000000
            elif keuze == '8':
                y3 = [0,]
                y3val = 0
                x1 = [0,]
                xval1 = 0
                # prognose winst
                for teller in range(0,53):
                    y3val = y3val+bw_incr
                    y3 = y3 +[(y3val)]
                    xval1 = xval1+1
                    x1 = x1 + [(xval1)]
                s1 = 20
                s2 = 20 
                t1 = 'Gross profit prognosis'
                t2 = 'Gross profit actual'
                t3 = 'Gross profit - prognosis / actual '
                c1 = rppar[7][4]
                c2 = rppar[7][5]
                ysch =  rppar[7][2]   #20000000
            elif keuze == '9':
                s1 = 6
                s2 = 4
                t1 = 'Work in progress'
                t2 = 'Payed amount'
                t3 = 'Work in progress - Payed amount '
                c1 = rppar[8][4]
                c2 = rppar[8][5]
                ysch =  rppar[8][2]   #160000000
            elif keuze == 'A':
                y4 = [0,]
                y4val = 0
                x2 =[0,]
                xval2 = 0
                #prognose omzet
                for teller in range(0,53):
                    y4val = y4val+bo_incr
                    y4 = y4 +[(y4val)]
                    xval2 = xval2+1
                    x2 = x2 + [(xval2)]
                s1 = 7
                s2 = 7
                t1 = 'Turnover prognosis'
                t2 = 'Turnover actual'
                t3 = 'Turnover '
                c1 = rppar[9][4]
                c2 = rppar[9][5]
                ysch =  rppar[9][2]   #160000000
            elif keuze == 'B':
                s1 = 20
                s2 = 5
                t1 = 'Gross profit realised'
                t2 = 'More/less work'
                t3 = 'Gross profit realised / More/less work '
                c1 = rppar[10][4]
                c2 = rppar[10][5]
                ysch =  rppar[10][2]    #30000000
      
            x = [0,]
            y1 = [0,]
            y2 = [0,]
            idx = 0
            yval1 = 0
            yval2 = 0
            for row in rpres:
                yval1 = y1[idx]+row[s1]
                y1 = y1 +[(yval1)]
                yval2 = y2[idx]+row[s2]
                y2 = y2 +[(yval2)]
                x = x +[(int(row[1][4:]))]
                idx += 1
  
            series1 = QLineSeries()
            if keuze == '8':
                for t, val in zip(x1, y3):
                    series1.append(int(t), val)
            elif keuze == 'A':
                for t, val in zip(x2, y4):
                    series1.append(int(t), val)
            else:
                for t, val in zip(x, y1):
                    series1.append(int(t), val)
            series2 = QLineSeries()
            for t, val in zip(x, y2):
                series2.append(int(t), val)
               
            chart = QChart()
            chart.addSeries(series1)
            chart.addSeries(series2)
             
            series1.setColor(QColor(c1))
            series2.setColor(QColor(c2))
            series1.setName(t1)
            series2.setName(t2)
            chart.legend().setVisible(True)
         
            font = QFont()
            font.setPixelSize(22)
            chart.setTitleFont(font)
            chart.setTitle(t3+jaar)
            chart.setTitleBrush(QBrush(Qt.black))
            chart.legend().setLabelBrush(QColor(Qt.black))
  
            axisX = QCategoryAxis()
            axisY = QCategoryAxis()
        
            axisX.setTitleText('Year '+jaar+' - Week number')
            axisX.setTitleBrush(QBrush(Qt.black))
            font = QFont("Sans Serif")
            axisX.setTitleFont(font)
           
            axisPen = QPen(QColor(100,100,100))    # 100,100,100
            axisPen.setWidth(3)
            axisX.setLinePen(axisPen)
            axisY.setLinePen(axisPen)
        
            axisBrush = QBrush(Qt.black)
            axisX.setLabelsBrush(axisBrush)
            axisY.setLabelsBrush(axisBrush)
      
            axisX.setGridLineVisible(False)
            axisY.setGridLineVisible(True)
            axisX.setShadesBrush(QBrush(QColor(245, 245 , 245)))
            axisX.setShadesVisible(True)
            for x in range(1,54):
                axisX.append(jaar+"-"+("0"+str(x))[-2:], x)
            axisX.setRange(0, 53)
            axisX.setLabelsAngle(-90)
                 
            axisY = QValueAxis()
            axisY.setTickCount(33)
            axisY.setTitleText("Amounts in Euros")
            axisY.setTitleFont(font)
            axisY.setLabelFormat('%d')
            axisY.setTitleBrush(QBrush(Qt.black))
            axisY.setRange(0,ysch)    #disable for automatic Y scale 
            #axisY.applyNiceNumbers() #enable by automatic Y scale
        
            Lfont = QFont("Sans Serif")         
            Dfont = QFont("Sans Serif")
            Lfont.setPixelSize(10)
            Dfont.setPixelSize(10)
            axisX.setLabelsFont(Dfont)
            axisY.setLabelsFont(Lfont)
            
            axisPen = QPen(QColor('black'))
            axisPen = QPen()
            axisPen.setWidth(2)
            axisX.setLinePen(axisPen)
            axisX.setLabelsColor(QColor('black'))
            axisY.setLinePen(axisPen)
            axisY.setLabelsColor(QColor('black'))
           
            chart.addAxis(axisX, Qt.AlignBottom)
            series1.attachAxis(axisX)
            axisX.setLabelsAngle(-90)
                      
            chart.addAxis(axisY, Qt.AlignLeft)
            series1.attachAxis(axisY)
            series2.attachAxis(axisY)
 
            self.chartView = QChartView(chart)
            self.chartView.setRenderHint(QPainter.Antialiasing)
                     
            buttonPreview = QPushButton('Print preview')
            buttonPreview.clicked.connect(self.handle_preview)
            buttonPreview.setStyleSheet("color: black;  background-color: gainsboro")
            buttonPrint = QPushButton('Printing')
            buttonPrint.clicked.connect(self.handle_print)
            buttonPrint.setStyleSheet("color: black;  background-color: gainsboro")
            buttonSluit = QPushButton('Close')
            buttonSluit.clicked.connect(lambda: sluit(self, m_email))
            buttonSluit.setStyleSheet("color: black;  background-color: gainsboro")
            grid.addWidget(self.chartView, 0, 0, 0, 3)
            grid.addWidget(buttonSluit, 1, 0)
            grid.addWidget(buttonPrint, 1, 1)
            grid.addWidget(buttonPreview, 1, 2) 
                       
            self.setLayout(grid)
            self.setGeometry(200, 40, 1395, 930)
            
        def handle_print(self):
            logger.warning(">>> Entering handle_print()", extra={"event.action": "handle_print"})
            printer = QPrinter(QPrinter.HighResolution)
            logger.debug("handle_print(): printer → %s", printer, extra={"event.action": "handle_print"})
            logger.debug("handle_print(self=%s): printer → %s", self, printer, extra={"event.action": "handle_print"})
            printer.setOrientation(QPrinter.Landscape)                      
            dialog = QPrintDialog(printer, self)
            if dialog.exec_() == QPrintDialog.Accepted:
                logger.debug("handle_print(self=%s): dialog → %s", self, dialog, extra={"event.action": "handle_print"})
                logger.debug("handle_print(): dialog → %s", dialog, extra={"event.action": "handle_print"})
                self.handle_paint_request(printer)
                logger.debug("<<< Exiting handle_print()", extra={"event.action": "handle_print"})
    
        def handle_preview(self):
            logger.warning(">>> Entering handle_preview()", extra={"event.action": "handle_preview"})
            dialog = QPrintPreviewDialog()
            logger.debug("handle_preview(): dialog → %s", dialog, extra={"event.action": "handle_preview"})
            logger.debug("handle_preview(self=%s): dialog → %s", self, dialog, extra={"event.action": "handle_preview"})
            dialog.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            dialog.setWindowFlags(dialog.windowFlags()| Qt.WindowSystemMenuHint |
                                                      Qt.WindowMinMaxButtonsHint)
            dialog.paintRequested.connect(self.handle_paint_request)
            dialog.resize(1470, 980)
            #dialog.setMinimumSize(1470, 980)
            dialog.exec_()
            logger.debug("<<< Exiting handle_preview()", extra={"event.action": "handle_preview"})
    
        def handle_paint_request(self, printer):
            logger.warning(">>> Entering handle_paint_request(printer=%s)", printer, extra={"event.action": "handle_paint_request", "logrite.printer": printer})
            logger.debug("handle_paint_request(self=%s,printer=%s): printer → %s", self, printer, printer, extra={"event.action": "handle_paint_request", "logrite.printer": printer})
            logger.debug("handle_paint_request(self=%s,printer=%s): painter → %s", self, printer, painter, extra={"event.action": "handle_paint_request", "logrite.printer": printer})
            logger.debug("handle_paint_request(printer=%s): painter → %s", printer, painter, extra={"event.action": "handle_paint_request", "logrite.printer": printer})
            printer.setPageOrientation(QPageLayout.Landscape)
            painter = QPainter(printer)            
            painter.setViewport(self.chartView.rect())
            painter.setWindow(self.chartView.rect()) 
            self.chartView.render(painter)
            painter.end()
            logger.debug("<<< Exiting handle_paint_request(printer=%s)", printer, extra={"event.action": "handle_paint_request", "logrite.printer": printer})

    win = Widget()
    win.exec_()
    zoekwk(m_email)