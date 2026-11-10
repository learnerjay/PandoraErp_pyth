from login import hoofdMenu
import datetime
from PyQt5.QtGui import  QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QComboBox, QMessageBox,\
          QGridLayout, QDialog, QPushButton, QLabel, QLineEdit,QCheckBox
from sqlalchemy import (Table, Column, Integer, Float, String, MetaData,\
                                create_engine)
from sqlalchemy.sql import select, update
import logging
logger = logging.getLogger(__name__)

def refresh(m_email, keuze, self):
    logger.warning(">>> Entering refresh(m_email=%s,keuze=%s)", m_email, keuze, extra={"event.action": "refresh", "logrite.keuze": keuze})
    self.close()
    toonRetouren(m_email, keuze) 
    logger.debug("<<< Exiting refresh(m_email=%s,keuze=%s)", m_email, keuze, extra={"event.action": "refresh", "logrite.keuze": keuze})

def windowSluit(m_email, self):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})

def betalingGeboekt():
    logger.warning(">>> Entering betalingGeboekt()", extra={"event.action": "betalingGeboekt"})
    msg = QMessageBox()
    logger.debug("betalingGeboekt(): msg → %s", msg, extra={"event.action": "betalingGeboekt"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Betaling is geboekt!')
    msg.setWindowTitle('RETOURBETALING')               
    logger.debug("<<< Exiting betalingGeboekt()", extra={"event.action": "betalingGeboekt"})
    msg.exec_() 

def retKeuze(m_email):
    logger.warning(">>> Entering retKeuze(m_email=%s)", m_email, extra={"event.action": "retKeuze"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Opvragen Webretouren")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze, extra={"event.action": "__init__"})
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit, extra={"event.action": "__init__"})
            k0Edit.setFixedWidth(230)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem(' Sorteersleutel voor zoeken')
            k0Edit.addItem('1. Gesorteerd op e-mailadres')
            k0Edit.addItem('2. Gefilterd niet betaald')
            k0Edit.addItem('3. Gefilterd betaald')
            k0Edit.activated[str].connect(self.k0Changed)
                   
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
            grid.addWidget(lbl , 1, 0, 1 ,2)
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 1, 1, 2, Qt.AlignRight)
                                  
            grid.addWidget(k0Edit, 2, 1, 1, 2)
                       
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 6, 0, 1, 3)
        
            applyBtn = QPushButton('Zoeken')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 5, 2, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            closeBtn = QPushButton('Sluiten')
            logger.debug("__init__(parent=%s): closeBtn → %s", parent, closeBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): closeBtn → %s", self, parent, closeBtn, extra={"event.action": "__init__"})
            closeBtn.clicked.connect(lambda: windowSluit(m_email, self))
    
            grid.addWidget(closeBtn, 5, 1, 1, 1)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            closeBtn.setFont(QFont("Arial",10))
            closeBtn.setFixedWidth(100)
            closeBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
        def k0Changed(self, text):
            logger.warning(">>> Entering k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            self.Keuze.setText(text)
            logger.debug("<<< Exiting k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            
        def returnk0(self):
            logger.warning(">>> Entering returnk0()", extra={"event.action": "returnk0"})
            logger.debug("<<< Exiting returnk0()", extra={"event.action": "returnk0"})
            return self.Keuze.text()
        
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnk0()] 
        
    window = Widget()
    data = window.getData()
    if not data[0] or data[0][0] == ' ':
        keuze = 0
    elif data[0]:
        keuze = int(data[0][0])
    else:
        retKeuze(m_email)
    toonRetouren(m_email, keuze)
                    
def toonRetouren(m_email, keuze):
    logger.warning(">>> Entering toonRetouren(m_email=%s,keuze=%s)", m_email, keuze, extra={"event.action": "toonRetouren", "logrite.keuze": keuze})
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setWindowTitle('Webretouren betalen/ opvragen')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                    Qt.WindowMinMaxButtonsHint)
            self.setFont(QFont('Arial', 10))
            grid = QGridLayout()
            logger.debug("__init__(data_list=%s,header=%s): grid → %s", data_list, header, grid, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): grid → %s", self, data_list, header, grid, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_model → %s", self, data_list, header, table_model, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_view → %s", self, data_list, header, table_view, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): font → %s", self, data_list, header, font, extra={"event.action": "__init__", "logrite.data_list": data_list})
            grid.setSpacing(20)
            table_model = MyTableModel(self, data_list, header)
            table_view = QTableView()
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            #table_view.clicked.connect(selectRow)
            table_view.clicked.connect(showSelection)
            grid.addWidget(table_view, 0, 0, 1, 8)
            
            lbl = QLabel()
            logger.debug("__init__(data_list=%s,header=%s): lbl → %s", data_list, header, lbl, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): lbl → %s", self, data_list, header, lbl, extra={"event.action": "__init__", "logrite.data_list": data_list})
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(self=%s,data_list=%s,header=%s): pixmap → %s", self, data_list, header, pixmap, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): pixmap → %s", data_list, header, pixmap, extra={"event.action": "__init__", "logrite.data_list": data_list})
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 1, 0, 1, 2)
       
            logo = QLabel()
            logger.debug("__init__(data_list=%s,header=%s): logo → %s", data_list, header, logo, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): logo → %s", self, data_list, header, logo, extra={"event.action": "__init__", "logrite.data_list": data_list})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 7, 1, 1, Qt.AlignRight)
            
            freshBtn = QPushButton('Verversen')
            logger.debug("__init__(data_list=%s,header=%s): freshBtn → %s", data_list, header, freshBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): freshBtn → %s", self, data_list, header, freshBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            freshBtn.clicked.connect(lambda: refresh(m_email, keuze, self))

            freshBtn.setFont(QFont("Arial",10))
            freshBtn.setFixedWidth(100) 
            freshBtn.setStyleSheet("color: black;  background-color: gainsboro")
   
            grid.addWidget(freshBtn, 1, 6, 1, 1, Qt.AlignRight)
            
            sluitBtn = QPushButton('Sluiten')
            logger.debug("__init__(data_list=%s,header=%s): sluitBtn → %s", data_list, header, sluitBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): sluitBtn → %s", self, data_list, header, sluitBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            sluitBtn.clicked.connect(self.close)

            sluitBtn.setFont(QFont("Arial",10))
            sluitBtn.setFixedWidth(100) 
            sluitBtn.setStyleSheet("color: black;  background-color: gainsboro") 
            
            grid.addWidget(sluitBtn, 1, 5)
          
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 1, 1, 1, 5, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(50, 50, 1050, 900)
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
            logger.debug("__init__(): q1Edit → %s", q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): cBox → %s", cBox, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): cBox → %s", self, cBox, extra={"event.action": "__init__"})
            logger.debug("__init__(): retourBtn → %s", retourBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): retourBtn → %s", self, retourBtn, extra={"event.action": "__init__"})
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
  
    header = ['Retournummer','E-mailadres', 'Bedrag','Rekeningnummer', 'Artikelnummer',\
              'Aantal','Ordernummer','Betaald', 'Boeking']
    
    metadata = MetaData()              
    webretouren = Table('webretouren', metadata,
        Column('retourID', Integer(), primary_key=True),
        Column('e_mail', String),
        Column('bedrag', Float),
        Column('rekening', String),
        Column('artikelID', Integer),
        Column('aantal', Float),
        Column('ordernummer', Integer),
        Column('betaald', String),
        Column('boeking', String))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    
    if keuze == 1:
        sel = select([webretouren]).order_by(webretouren.c.e_mail)
    elif keuze == 2:
        sel = select([webretouren]).where(webretouren.c.betaald == '')\
         .order_by(webretouren.c.e_mail.asc()) 
    elif keuze == 3:
        sel = select([webretouren]).where(webretouren.c.betaald != '').\
         order_by(webretouren.c.betaald)
    else:
        sel = select([webretouren]).order_by(webretouren.c.e_mail)
        
    rp = con.execute(sel)
     
    data_list=[]
    for row in rp:
        data_list += [(row)]
        
    def showSelection(idx):
        logger.warning(">>> Entering showSelection(idx=%s)", idx, extra={"event.action": "showSelection", "logrite.idx": idx})
        mretnr = idx.data()
        logger.debug("showSelection(idx=%s): mretnr → %s", idx, mretnr, extra={"event.action": "showSelection", "logrite.idx": idx})
        if idx.column() == 0:
            
            header = ['Retournummer','E-mailadres', 'Bedrag','Rekeningnummer', 'Artikelnummer',\
                  'Aantal','Ordernummer','Betaald', 'Boeking']
            
            metadata = MetaData()              
            logger.debug("showSelection(idx=%s): metadata → %s", idx, metadata, extra={"event.action": "showSelection", "logrite.idx": idx})
            webretouren = Table('webretouren', metadata,
                Column('retourID', Integer(), primary_key=True),
                Column('e_mail', String),
                Column('bedrag', Float),
                Column('rekening', String),
                Column('artikelID', Integer),
                Column('aantal', Float),
                Column('ordernummer', Integer),
                Column('betaald', String),
                Column('boeking', String))
            
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showSelection(idx=%s): engine → %s", idx, engine, extra={"event.action": "showSelection", "logrite.idx": idx})
            con = engine.connect()
            logger.debug("showSelection(idx=%s): con → %s", idx, con, extra={"event.action": "showSelection", "logrite.idx": idx})
              
            sel = select([webretouren]).where(webretouren.c.retourID == mretnr)
            logger.debug("showSelection(idx=%s): sel → %s", idx, sel, extra={"event.action": "showSelection", "logrite.idx": idx})
            rpret = con.execute(sel).first()
            logger.debug("showSelection(idx=%s): rpret → %s", idx, rpret, extra={"event.action": "showSelection", "logrite.idx": idx})
            mbet = rpret[7]
            logger.debug("showSelection(idx=%s): mbet → %s", idx, mbet, extra={"event.action": "showSelection", "logrite.idx": idx})
               
            class MainWindow(QDialog):
                logger.debug("<<< Exiting showSelection(idx=%s)", idx, extra={"event.action": "showSelection", "logrite.idx": idx})
                def __init__(self):
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                     
                    self.setWindowTitle("Retouren Webartikelen")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                    
                    self.setFont(QFont('Arial', 10))   
                                                      
                    self.lbl = QLabel()
                    self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                    self.lbl.setPixmap(self.pixmap)
                    grid.addWidget(self.lbl , 0, 0)
                    
                    grid.addWidget(QLabel('Retouren Webartikelen'),0, 1, 1, 2)
            
                    self.logo = QLabel()
                    self.pixmap = QPixmap('./images/logos/logo.jpg')
                    self.logo.setPixmap(self.pixmap)
                    grid.addWidget(self.logo , 0, 2, 1, 1, Qt.AlignRight)    
                    
                    index = 1
                    for item in header:
                        self.lbl = QLabel(header[index-1])
                        if type(rpret[index-1]) == float:
                            q1Edit = QLineEdit('{:12.2f}'.format(rpret[index-1]))
                            q1Edit.setAlignment(Qt.AlignRight)
                        elif type(rpret[index-1]) == int:
                            q1Edit = QLineEdit(str(rpret[index-1]))
                            q1Edit.setAlignment(Qt.AlignRight)
                        else:
                            q1Edit = QLineEdit(str(rpret[index-1]))
                        q1Edit.setFixedWidth(200)
                        q1Edit.setDisabled(True)
                        q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                        grid.addWidget(self.lbl, index, 0)
                        grid.addWidget(q1Edit, index, 1)
                        index +=1
                        
                    cBox = QCheckBox('Betalen')
                    if mbet:
                        cBox.setDisabled(True)
                    cBox.stateChanged.connect(self.cBoxChanged)
                    grid.addWidget(cBox, index -1, 2)
                         
                    retourBtn = QPushButton('OK')
                    retourBtn.clicked.connect(self.accept)
                    
                    grid.addWidget(retourBtn, index+1, 2)
                    retourBtn.setFont(QFont("Arial",10))
                    retourBtn.setFixedWidth(100)  
                    retourBtn.setStyleSheet("color: black;  background-color: gainsboro")
                   
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), index+2, 0, 1, 3, Qt.AlignCenter)
                    
                    self.setLayout(grid)
                    self.setGeometry(100, 150, 150, 150)
       
                state = False
                def cBoxChanged(self, state):
                    logger.warning(">>> Entering cBoxChanged(state=%s)", state, extra={"event.action": "cBoxChanged", "logrite.state": state})
                    logger.debug("cBoxChanged(state=%s): self.state → %s", state, self.state, extra={"event.action": "cBoxChanged", "logrite.state": state})
                    logger.debug("cBoxChanged(self=%s,state=%s): self.state → %s", self, state, self.state, extra={"event.action": "cBoxChanged", "logrite.state": state})
                    if state == Qt.Checked:
                        self.state = True                    
                        logger.debug("<<< Exiting cBoxChanged(state=%s)", state, extra={"event.action": "cBoxChanged", "logrite.state": state})
                    
                def returncBox(self):
                      logger.warning(">>> Entering returncBox()", extra={"event.action": "returncBox"})
                      logger.debug("<<< Exiting returncBox()", extra={"event.action": "returncBox"})
                      return self.state
                       
                @staticmethod
                def getData(parent=None):
                    dialog = MainWindow()
                    dialog.exec_()
                    return [dialog.returncBox()] 
                
            mainWin = MainWindow()
            data = mainWin.getData()
                 
            if data[0] and not mbet:
                upd = update(webretouren).where(webretouren.c.retourID == mretnr).\
                 values(betaald = str(datetime.datetime.now())[0:10])
                con.execute(upd) 
                betalingGeboekt()
           
    win = MyWindow(data_list, header)
    win.exec_()
    retKeuze(m_email)