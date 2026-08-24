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
    logger.debug(">>> Entering sluiten(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting sluiten(m_email=%s)", m_email)
    
def alertText(m_email):
    logger.debug(">>> Entering alertText(m_email=%s)", m_email)
    msg = QMessageBox()
    logger.debug("alertText(m_email=%s): msg → %s", m_email, msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./logos/logo.jpg'))
    msg.setFont(QFont("Arial", 10))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Data for chart not complete!')
    msg.setWindowTitle('Warning message')
    msg.exec_() 
    hoofdMenu(m_email)
    logger.debug("<<< Exiting alertText(m_email=%s)", m_email)
   
def toonGrafiek(m_email):
    logger.debug(">>> Entering toonGrafiek(m_email=%s)", m_email)
    mjrmnd = str(date.today())[0:7]
    logger.debug("toonGrafiek(m_email=%s): mjrmnd → %s", m_email, mjrmnd)
    mjrmndvj = str(int(str(date.today())[0:4])-1)+'-'+('0'+str(int(str(date.today())[5:7])))[-2:]
    metadata = MetaData()
    logger.debug("toonGrafiek(m_email=%s): mjrmndvj → %s", m_email, mjrmndvj)
    magazijnvoorraad = Table('magazijnvoorraad', metadata,
        Column('jaarmaand', String, primary_key=True),
        Column('totaal', Float),
        Column('courant', Float),                     
        Column('incourant', Float))
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("toonGrafiek(m_email=%s): metadata → %s", m_email, metadata)
    con = engine.connect()
    selvrd = select([magazijnvoorraad]).where(magazijnvoorraad.c.jaarmaand.between(mjrmndvj, mjrmnd)).order_by(magazijnvoorraad.c.jaarmaand)
    logger.debug("toonGrafiek(m_email=%s): magazijnvoorraad → %s", m_email, magazijnvoorraad)
    logger.debug("toonGrafiek(m_email=%s): engine → %s", m_email, engine)
    rpvrd = con.execute(selvrd).fetchall()
    if len(rpvrd) < 12:
        alertText(m_email)
        logger.debug("toonGrafiek(m_email=%s): con → %s", m_email, con)
    
    class Window(QDialog):
        logger.debug("toonGrafiek(m_email=%s): selvrd → %s", m_email, selvrd)
        def __init__(self):          
            logger.debug("<<< Exiting toonGrafiek(m_email=%s)", m_email)
            QDialog.__init__(self)
            logger.debug(">>> Entering __init__()")
            self.setWindowTitle("Printing chart warehouse stock amounts")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                                                  Qt.WindowMinMaxButtonsHint)
            self.chart = QChart()
            logger.debug("__init__(): self.chart → %s", self.chart)
            logger.debug("__init__(self=%s): chart_view → %s", self, chart_view)
            logger.debug("__init__(): self.buttonPreview → %s", self.buttonPreview)
            logger.debug("__init__(self=%s): buttonPreview → %s", self, buttonPreview)
            self.chart_view = QChartView(self.chart)
            logger.debug("__init__(): self.chart_view → %s", self.chart_view)
            self.chart_view.setRenderHint(QPainter.Antialiasing)
            self.buttonPreview = QPushButton('Printing preview', self)
            self.buttonPreview.setStyleSheet("color: black;  background-color: gainsboro")
            self.buttonPreview.clicked.connect(self.handle_preview)
            self.buttonPrint = QPushButton('Printing', self)
            logger.debug("__init__(): self.buttonPrint → %s", self.buttonPrint)
            logger.debug("__init__(self=%s): buttonPrint → %s", self, buttonPrint)
            self.buttonPrint.setStyleSheet("color: black;  background-color: gainsboro")
            self.buttonPrint.clicked.connect(self.handle_print) 
            self.sluiten = QPushButton('Close', self)
            logger.debug("__init__(): self.sluiten → %s", self.sluiten)
            logger.debug("__init__(self=%s): sluiten → %s", self, sluiten)
            logger.debug("__init__(): layout → %s", layout)
            logger.debug("__init__(self=%s): layout → %s", self, layout)
            self.sluiten.setStyleSheet("color: black;  background-color: gainsboro")
            self.sluiten.clicked.connect(lambda: sluiten(self, m_email))
            layout = QGridLayout(self)
            layout.addWidget(self.buttonPrint, 1, 1)
            layout.addWidget(self.sluiten, 1, 0)
            layout.addWidget(self.chart_view, 0, 0, 1, 3)
            layout.addWidget(self.buttonPreview, 1, 2)        
            self.create_chart()
            logger.debug("<<< Exiting __init__()")
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
  
        def create_chart(self):
            logger.debug(">>> Entering create_chart()")
            logger.debug("create_chart(self=%s): chart → %s", self, chart)
            logger.debug("create_chart(self=%s): font → %s", self, font)
            logger.debug("create_chart(): font → %s", font)
            self.chart.setTitle('Chart finances warehouse inventory')
            font = QFont("Sans Serif", 10)
            font.setWeight(QFont.Bold)
            self.chart.setTitleFont(font)
           
            set0 = QBarSet('Total')
            logger.debug("create_chart(self=%s): set0 → %s", self, set0)
            logger.debug("create_chart(): set0 → %s", set0)
            set1 = QBarSet('Current')
            logger.debug("create_chart(): set1 → %s", set1)
            logger.debug("create_chart(self=%s): set1 → %s", self, set1)
            set2 = QBarSet('Obsolete')
            logger.debug("create_chart(): set2 → %s", set2)
            logger.debug("create_chart(self=%s): set2 → %s", self, set2)
            
            set0 << rpvrd[0][1] << rpvrd[1][1] << rpvrd[2][1] << rpvrd[3][1] << rpvrd[4][1] << rpvrd[5][1] << rpvrd[6][1] << rpvrd[7][1] << rpvrd[8][1] << rpvrd[9][1] << rpvrd[10][1] << rpvrd[11][1] 
            set1 << rpvrd[0][2] << rpvrd[1][2] << rpvrd[2][2] << rpvrd[3][2] << rpvrd[4][2] << rpvrd[5][2] << rpvrd[6][2] << rpvrd[7][2] << rpvrd[8][2] << rpvrd[9][2] << rpvrd[10][2] << rpvrd[11][2] 
            set2 << rpvrd[0][3] << rpvrd[1][3] << rpvrd[2][3] << rpvrd[3][3] << rpvrd[4][3] << rpvrd[5][3] << rpvrd[6][3] << rpvrd[7][3] << rpvrd[8][3] << rpvrd[9][3] << rpvrd[10][3] << rpvrd[11][3] 

            barseries = QBarSeries()
            logger.debug("create_chart(self=%s): barseries → %s", self, barseries)
            logger.debug("create_chart(): barseries → %s", barseries)
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
            logger.debug("create_chart(self=%s): axisX → %s", self, axisX)
            logger.debug("create_chart(): axisX → %s", axisX)
            axisX.append(categories)
            logger.debug("<<< Exiting create_chart()")
            axisX.setTitleText('12-month rolling period')
            self.chart.setAxisX(axisX, barseries)
            axisX.setRange(rpvrd[0][0], rpvrd[11][0])
            axisX.setLabelsAngle(-90)
                         
        def handle_print(self):
            logger.debug(">>> Entering handle_print()")
            printer = QPrinter(QPrinter.HighResolution)
            logger.debug("handle_print(): printer → %s", printer)
            logger.debug("handle_print(self=%s): printer → %s", self, printer)
            printer.setOrientation(QPrinter.Landscape) 
            dialog = QPrintDialog(printer, self)
            dialog.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                                                  Qt.WindowMinMaxButtonsHint)
            logger.debug("handle_print(self=%s): dialog → %s", self, dialog)
            logger.debug("handle_print(): dialog → %s", dialog)
            if dialog.exec_() == QPrintDialog.Accepted:
                self.handle_paint_request(printer)
                logger.debug("<<< Exiting handle_print()")
    
        def handle_preview(self):
            logger.debug(">>> Entering handle_preview()")
            dialog = QPrintPreviewDialog()
            logger.debug("handle_preview(self=%s): dialog → %s", self, dialog)
            dialog.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                                                  Qt.WindowMinMaxButtonsHint)
            logger.debug("handle_preview(): dialog → %s", dialog)
            dialog.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            dialog.resize(1200,800)
            #dialog.setMinimumSize(1200, 800)
            dialog.paintRequested.connect(self.handle_paint_request)
            dialog.exec_()
            logger.debug("<<< Exiting handle_preview()")
    
        def handle_paint_request(self, printer):
            logger.debug(">>> Entering handle_paint_request(printer=%s)", printer)
            logger.debug("handle_paint_request(self=%s,printer=%s): printer → %s", self, printer, printer)
            logger.debug("handle_paint_request(self=%s,printer=%s): painter → %s", self, printer, painter)
            logger.debug("handle_paint_request(printer=%s): painter → %s", printer, painter)
            printer.setPageOrientation(QPageLayout.Landscape)
            painter = QPainter(printer)
            painter.setViewport(self.chart_view.rect())
            painter.setWindow(self.chart_view.rect())                        
            self.chart_view.render(painter)
            painter.end()
            logger.debug("<<< Exiting handle_paint_request(printer=%s)", printer)

    window = Window()
    window.resize(1350, 900)
    window.exec_()
    hoofdMenu(m_email)
    
def magVoorraad(m_email):
    logger.debug(">>> Entering magVoorraad(m_email=%s)", m_email)
    metadata = MetaData()
    metadata = MetaData()
    logger.debug("magVoorraad(m_email=%s): metadata → %s", m_email, metadata)
    magazijnvoorraad = Table('magazijnvoorraad', metadata,
        Column('jaarmaand', String, primary_key=True),
        Column('totaal', Float),
        Column('courant', Float),                     
        Column('incourant', Float))
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    logger.debug("magVoorraad(m_email=%s): magazijnvoorraad → %s", m_email, magazijnvoorraad)
    logger.debug("magVoorraad(m_email=%s): engine → %s", m_email, engine)
    selvrd = select([magazijnvoorraad]).order_by(magazijnvoorraad.c.jaarmaand)
    rpvrd = con.execute(selvrd)
          
    logger.debug("magVoorraad(m_email=%s): con → %s", m_email, con)
    class MyWindow(QDialog):
        logger.debug("<<< Exiting magVoorraad(m_email=%s)", m_email)
        def __init__(self, data_list, header, *args):
            QWidget.__init__(self, *args,)
            self.setGeometry(100, 50, 600, 900)
            self.setWindowTitle('Annual consumption last year')
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
                                        
    header = ['Year-Month', 'Total stock', 'Current stock', 'Obsolete stock']
        
    data_list=[]
    for row in rpvrd:
        data_list += [(row)] 
  
    win = MyWindow(data_list, header)
    win.exec_()
    hoofdMenu(m_email)
