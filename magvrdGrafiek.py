from datetime import date
from login import hoofdMenu
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog, QPrintDialog
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QIcon, QPainter, QPageLayout
from PyQt5.QtWidgets import QDialog, QGridLayout, QPushButton,QVBoxLayout,\
    QTableView, QWidget, QMessageBox
from sqlalchemy import (Table, Column, String, MetaData,\
                       create_engine, Float, select)
import logging
logger = logging.getLogger(__name__)

def sluiten(self, m_email):
    logger.warning(">>> Entering sluiten(m_email=%s)", m_email, extra={"event.action": "sluiten"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting sluiten(m_email=%s)", m_email, extra={"event.action": "sluiten"})
    
def alertText(m_email):
    logger.warning(">>> Entering alertText(m_email=%s)", m_email, extra={"event.action": "alertText"})
    msg = QMessageBox()
    logger.debug("alertText(m_email=%s): msg → %s", m_email, msg, extra={"event.action": "alertText"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./logos/logo.jpg'))
    msg.setFont(QFont("Arial", 10))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Data for chart not complete!')
    msg.setWindowTitle('Warning message')
    msg.exec_() 
    hoofdMenu(m_email)
    logger.debug("<<< Exiting alertText(m_email=%s)", m_email, extra={"event.action": "alertText"})
   
def toonGrafiek(m_email):
    logger.warning(">>> Entering toonGrafiek(m_email=%s)", m_email, extra={"event.action": "toonGrafiek"})
    mjrmnd = str(date.today())[0:7]
    logger.debug("toonGrafiek(m_email=%s): mjrmnd → %s", m_email, mjrmnd, extra={"event.action": "toonGrafiek"})
    mjrmndvj = str(int(str(date.today())[0:4])-1)+'-'+('0'+str(int(str(date.today())[5:7])))[-2:]
    metadata = MetaData()
    logger.debug("toonGrafiek(m_email=%s): mjrmndvj → %s", m_email, mjrmndvj, extra={"event.action": "toonGrafiek"})
    magazijnvoorraad = Table('magazijnvoorraad', metadata,
        Column('jaarmaand', String, primary_key=True),
        Column('totaal', Float),
        Column('courant', Float),                     
        Column('incourant', Float))
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("toonGrafiek(m_email=%s): metadata → %s", m_email, metadata, extra={"event.action": "toonGrafiek"})
    con = engine.connect()
    selvrd = select([magazijnvoorraad]).where(magazijnvoorraad.c.jaarmaand.between(mjrmndvj, mjrmnd)).order_by(magazijnvoorraad.c.jaarmaand)
    logger.debug("toonGrafiek(m_email=%s): engine → %s", m_email, engine, extra={"event.action": "toonGrafiek"})
    rpvrd = con.execute(selvrd).fetchall()
    if len(rpvrd) < 12:
        logger.debug("toonGrafiek(m_email=%s): con → %s", m_email, con, extra={"event.action": "toonGrafiek"})
        alertText(m_email)
    
        logger.debug("toonGrafiek(m_email=%s): selvrd → %s", m_email, selvrd, extra={"event.action": "toonGrafiek"})
    class Window(QDialog):
        logger.debug("<<< Exiting toonGrafiek(m_email=%s)", m_email, extra={"event.action": "toonGrafiek"})
        def __init__(self):          
            logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
            QDialog.__init__(self)
            self.setWindowTitle("Printing chart warehouse stock amounts")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                                                  Qt.WindowMinMaxButtonsHint)
            self.chart = QChart()
            logger.debug("__init__(): self.chart → %s", self.chart, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): chart_view → %s", self, chart_view, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.buttonPreview → %s", self.buttonPreview, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): buttonPreview → %s", self, buttonPreview, extra={"event.action": "__init__"})
            self.chart_view = QChartView(self.chart)
            logger.debug("__init__(): self.chart_view → %s", self.chart_view, extra={"event.action": "__init__"})
            self.chart_view.setRenderHint(QPainter.Antialiasing)
            self.buttonPreview = QPushButton('Printing preview', self)
            self.buttonPreview.setStyleSheet("color: black;  background-color: gainsboro")
            self.buttonPreview.clicked.connect(self.handle_preview)
            self.buttonPrint = QPushButton('Printing', self)
            logger.debug("__init__(): self.buttonPrint → %s", self.buttonPrint, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): buttonPrint → %s", self, buttonPrint, extra={"event.action": "__init__"})
            self.buttonPrint.setStyleSheet("color: black;  background-color: gainsboro")
            self.buttonPrint.clicked.connect(self.handle_print) 
            self.sluiten = QPushButton('Close', self)
            logger.debug("__init__(): self.sluiten → %s", self.sluiten, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): sluiten → %s", self, sluiten, extra={"event.action": "__init__"})
            self.sluiten.setStyleSheet("color: black;  background-color: gainsboro")
            self.sluiten.clicked.connect(lambda: sluiten(self, m_email))
            layout = QGridLayout(self)
            logger.debug("__init__(): layout → %s", layout, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): layout → %s", self, layout, extra={"event.action": "__init__"})
            layout.addWidget(self.buttonPrint, 1, 1)
            layout.addWidget(self.sluiten, 1, 0)
            layout.addWidget(self.chart_view, 0, 0, 1, 3)
            layout.addWidget(self.buttonPreview, 1, 2)        
            self.create_chart()
            logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})
  
        def create_chart(self):
            logger.warning(">>> Entering create_chart()", extra={"event.action": "create_chart"})
            logger.debug("create_chart(self=%s): chart → %s", self, chart, extra={"event.action": "create_chart"})
            logger.debug("create_chart(self=%s): font → %s", self, font, extra={"event.action": "create_chart"})
            logger.debug("create_chart(): font → %s", font, extra={"event.action": "create_chart"})
            self.chart.setTitle('Chart finances warehouse inventory')
            font = QFont("Sans Serif", 10)
            font.setWeight(QFont.Bold)
            self.chart.setTitleFont(font)
           
            set0 = QBarSet('Total')
            logger.debug("create_chart(self=%s): set0 → %s", self, set0, extra={"event.action": "create_chart"})
            logger.debug("create_chart(): set0 → %s", set0, extra={"event.action": "create_chart"})
            set1 = QBarSet('Current')
            logger.debug("create_chart(): set1 → %s", set1, extra={"event.action": "create_chart"})
            logger.debug("create_chart(self=%s): set1 → %s", self, set1, extra={"event.action": "create_chart"})
            set2 = QBarSet('Obsolete')
            logger.debug("create_chart(): set2 → %s", set2, extra={"event.action": "create_chart"})
            logger.debug("create_chart(self=%s): set2 → %s", self, set2, extra={"event.action": "create_chart"})
            
            set0 << rpvrd[0][1] << rpvrd[1][1] << rpvrd[2][1] << rpvrd[3][1] << rpvrd[4][1] << rpvrd[5][1] << rpvrd[6][1] << rpvrd[7][1] << rpvrd[8][1] << rpvrd[9][1] << rpvrd[10][1] << rpvrd[11][1] 
            set1 << rpvrd[0][2] << rpvrd[1][2] << rpvrd[2][2] << rpvrd[3][2] << rpvrd[4][2] << rpvrd[5][2] << rpvrd[6][2] << rpvrd[7][2] << rpvrd[8][2] << rpvrd[9][2] << rpvrd[10][2] << rpvrd[11][2] 
            set2 << rpvrd[0][3] << rpvrd[1][3] << rpvrd[2][3] << rpvrd[3][3] << rpvrd[4][3] << rpvrd[5][3] << rpvrd[6][3] << rpvrd[7][3] << rpvrd[8][3] << rpvrd[9][3] << rpvrd[10][3] << rpvrd[11][3] 

            barseries = QBarSeries()
            logger.debug("create_chart(): barseries → %s", barseries, extra={"event.action": "create_chart"})
            logger.debug("create_chart(self=%s): barseries → %s", self, barseries, extra={"event.action": "create_chart"})
            barseries.append(set0)
            barseries.append(set1)
            barseries.append(set2)
                                                  
            categories = [rpvrd[0][0],rpvrd[1][0],rpvrd[2][0],rpvrd[3][0],rpvrd[4][0],\
                          rpvrd[5][0],rpvrd[6][0],rpvrd[7][0],rpvrd[8][0],rpvrd[9][0],\
                          rpvrd[10][0],rpvrd[11][0]]
                                               
            self.chart.addSeries(barseries)                                                         
            self.chart.axisX() 
            self.chart.createDefaultAxes()  
            axisX = QBarCategoryAxis()
            logger.debug("create_chart(): axisX → %s", axisX, extra={"event.action": "create_chart"})
            logger.debug("create_chart(self=%s): axisX → %s", self, axisX, extra={"event.action": "create_chart"})
            axisX.append(categories)
            axisX.setTitleText('12-month rolling period')
            logger.debug("<<< Exiting create_chart()", extra={"event.action": "create_chart"})
            self.chart.setAxisX(axisX, barseries)
            axisX.setRange(rpvrd[0][0], rpvrd[11][0])
            axisX.setLabelsAngle(-90)
                         
        def handle_print(self):
            logger.warning(">>> Entering handle_print()", extra={"event.action": "handle_print"})
            printer = QPrinter(QPrinter.HighResolution)
            logger.debug("handle_print(): printer → %s", printer, extra={"event.action": "handle_print"})
            logger.debug("handle_print(self=%s): printer → %s", self, printer, extra={"event.action": "handle_print"})
            printer.setOrientation(QPrinter.Landscape) 
            dialog = QPrintDialog(printer, self)
            dialog.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                                                  Qt.WindowMinMaxButtonsHint)
            logger.debug("handle_print(self=%s): dialog → %s", self, dialog, extra={"event.action": "handle_print"})
            logger.debug("handle_print(): dialog → %s", dialog, extra={"event.action": "handle_print"})
            if dialog.exec_() == QPrintDialog.Accepted:
                self.handle_paint_request(printer)
                logger.debug("<<< Exiting handle_print()", extra={"event.action": "handle_print"})
    
        def handle_preview(self):
            logger.warning(">>> Entering handle_preview()", extra={"event.action": "handle_preview"})
            dialog = QPrintPreviewDialog()
            logger.debug("handle_preview(self=%s): dialog → %s", self, dialog, extra={"event.action": "handle_preview"})
            dialog.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                                                  Qt.WindowMinMaxButtonsHint)
            logger.debug("handle_preview(): dialog → %s", dialog, extra={"event.action": "handle_preview"})
            dialog.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            dialog.resize(1200,800)
            #dialog.setMinimumSize(1200, 800)
            dialog.paintRequested.connect(self.handle_paint_request)
            dialog.exec_()
            logger.debug("<<< Exiting handle_preview()", extra={"event.action": "handle_preview"})
    
        def handle_paint_request(self, printer):
            logger.warning(">>> Entering handle_paint_request(printer=%s)", printer, extra={"event.action": "handle_paint_request", "logrite.printer": printer})
            logger.debug("handle_paint_request(self=%s,printer=%s): printer → %s", self, printer, printer, extra={"event.action": "handle_paint_request", "logrite.printer": printer})
            logger.debug("handle_paint_request(self=%s,printer=%s): painter → %s", self, printer, painter, extra={"event.action": "handle_paint_request", "logrite.printer": printer})
            logger.debug("handle_paint_request(printer=%s): painter → %s", printer, painter, extra={"event.action": "handle_paint_request", "logrite.printer": printer})
            printer.setPageOrientation(QPageLayout.Landscape)
            painter = QPainter(printer)
            painter.setViewport(self.chart_view.rect())
            painter.setWindow(self.chart_view.rect())                        
            self.chart_view.render(painter)
            painter.end()
            logger.debug("<<< Exiting handle_paint_request(printer=%s)", printer, extra={"event.action": "handle_paint_request", "logrite.printer": printer})

    window = Window()
    window.resize(1350, 900)
    window.exec_()
    hoofdMenu(m_email)
    
def magVoorraad(m_email):
    logger.warning(">>> Entering magVoorraad(m_email=%s)", m_email, extra={"event.action": "magVoorraad"})
    metadata = MetaData()
    metadata = MetaData()
    logger.debug("magVoorraad(m_email=%s): metadata → %s", m_email, metadata, extra={"event.action": "magVoorraad"})
    magazijnvoorraad = Table('magazijnvoorraad', metadata,
        Column('jaarmaand', String, primary_key=True),
        Column('totaal', Float),
        Column('courant', Float),                     
        Column('incourant', Float))
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    logger.debug("magVoorraad(m_email=%s): engine → %s", m_email, engine, extra={"event.action": "magVoorraad"})
    selvrd = select([magazijnvoorraad]).order_by(magazijnvoorraad.c.jaarmaand)
    rpvrd = con.execute(selvrd)
    logger.debug("magVoorraad(m_email=%s): con → %s", m_email, con, extra={"event.action": "magVoorraad"})
          
    class MyWindow(QDialog):
        logger.debug("magVoorraad(m_email=%s): selvrd → %s", m_email, selvrd, extra={"event.action": "magVoorraad"})
        def __init__(self, data_list, header, *args):
            logger.debug("<<< Exiting magVoorraad(m_email=%s)", m_email, extra={"event.action": "magVoorraad"})
            QWidget.__init__(self, *args,)
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            self.setGeometry(100, 50, 600, 900)
            self.setWindowTitle('Annual consumption last year')
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
                                        
    header = ['Year-Month', 'Total stock', 'Current stock', 'Obsolete stock']
        
    data_list=[]
    for row in rpvrd:
        data_list += [(row)] 
  
    win = MyWindow(data_list, header)
    win.exec_()
    hoofdMenu(m_email)
