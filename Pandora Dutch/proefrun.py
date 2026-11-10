from login import hoofdMenu
import os, csv
from sys import platform
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
            QDialog, QMessageBox, QTableView, QVBoxLayout, QWidget
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QRegExp, QAbstractTableModel
from sqlalchemy import (Table, Column, Integer, String, Float, Boolean,\
                        ForeignKey,  MetaData, create_engine)
from sqlalchemy.sql import select, and_
import logging
logger = logging.getLogger(__name__)

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    
def winSluit(self, m_email):
    logger.warning(">>> Entering winSluit(m_email=%s)", m_email, extra={"event.action": "winSluit"})
    self.close()
    maandPeriode(m_email)
    logger.debug("<<< Exiting winSluit(m_email=%s)", m_email, extra={"event.action": "winSluit"})

def ongPeriode():
    logger.warning(">>> Entering ongPeriode()", extra={"event.action": "ongPeriode"})
    msg = QMessageBox()
    logger.debug("ongPeriode(): msg → %s", msg, extra={"event.action": "ongPeriode"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen geldige betaalperiode opgegeven!')
    msg.setWindowTitle('Controle werkuren')
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    logger.debug("<<< Exiting ongPeriode()", extra={"event.action": "ongPeriode"})
    msg.exec_()
       
def printGeg(mjrmnd):
    logger.warning(">>> Entering printGeg(mjrmnd=%s)", mjrmnd, extra={"event.action": "printGeg", "logrite.mjrmnd": mjrmnd})
    if platform == 'win32':
        filename = '.\\forms\\Uren\\'+str(mjrmnd)+'.txt'
        logger.debug("printGeg(mjrmnd=%s): filename → %s", mjrmnd, filename, extra={"event.action": "printGeg", "logrite.mjrmnd": mjrmnd})
        os.startfile(filename, "print")
    else:
        filename = './forms/Uren/'+str(mjrmnd)+'.txt'
        os.system('lpr '+filename)
        logger.debug("<<< Exiting printGeg(mjrmnd=%s)", mjrmnd, extra={"event.action": "printGeg", "logrite.mjrmnd": mjrmnd})
        
def selectRow(index):
    logger.warning(">>> Entering selectRow(index=%s)", index, extra={"event.action": "selectRow", "logrite.index": index})
    #print('Recordnummer is: ', index.row())
    pass
    logger.debug("<<< Exiting selectRow(index=%s)", index, extra={"event.action": "selectRow", "logrite.index": index})
               
def toonGeg(mjrmnd):
    logger.warning(">>> Entering toonGeg(mjrmnd=%s)", mjrmnd, extra={"event.action": "toonGeg", "logrite.mjrmnd": mjrmnd})
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setGeometry(100, 50, 800, 600)
            self.setWindowTitle('Cluster Calculatie')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            table_model = MyTableModel(self, data_list, header)
            logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_model → %s", self, data_list, header, table_model, extra={"event.action": "__init__", "logrite.data_list": data_list})
            table_view = QTableView()
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_view → %s", self, data_list, header, table_view, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view, extra={"event.action": "__init__", "logrite.data_list": data_list})
            font = QFont("Arial", 10)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): font → %s", self, data_list, header, font, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font, extra={"event.action": "__init__", "logrite.data_list": data_list})
            table_view.setFont(font)
            table_view.setModel(table_model)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.clicked.connect(selectRow)
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
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Betaalperiode → %s", parent, self.Betaalperiode, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): betEdit → %s", parent, betEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): betEdit → %s", self, parent, betEdit, extra={"event.action": "__init__"})
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
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
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
            self.font = QFont('Arial', 10)
            logger.debug("headerData(col=%s,orientation=%s,role=%s): self.font → %s", col, orientation, role, self.font, extra={"event.action": "headerData", "logrite.col": col, "logrite.orientation": orientation, "logrite.role": role})
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self.header[col]
            logger.debug("<<< Exiting headerData(col=%s,orientation=%s,role=%s)", col, orientation, role, extra={"event.action": "headerData", "logrite.col": col, "logrite.orientation": orientation, "logrite.role": role})
            return None
                 
    header = ['Accountnr', 'Voornaam', 'Tussenvoegsel', 'Achternaam', 'Uren', 'Geboekt']
    if platform == 'win32':
        with open('.\\forms\\Uren\\'+str(mjrmnd)+'.csv', newline='') as f:
            fname = csv.reader(f, delimiter='|', quotechar='@')
            
            data_list = []
            for row in fname:
                data_list += [(row)]
    else:
        with open('./forms/Uren/'+str(mjrmnd)+'.csv', newline='') as f:
            fname = csv.reader(f, delimiter='|', quotechar='@')
            
            data_list = []
            for row in fname:
                data_list += [(row)]
     
    win = MyWindow(data_list, header)
    win.exec_()
  
def maandPeriode(m_email):
    logger.warning(">>> Entering maandPeriode(m_email=%s)", m_email, extra={"event.action": "maandPeriode"})
    import validZt
    class Widget(QDialog):
        logger.debug("<<< Exiting maandPeriode(m_email=%s)", m_email, extra={"event.action": "maandPeriode"})
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Periode opgeven tbv loonspecificaties")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    
            self.setFont(QFont('Arial', 10))
               
            self.Betaalperiode = QLabel()
            betEdit = QLineEdit()
            betEdit.setFixedWidth(100)
            betEdit.setFont(QFont("Arial",10))
            betEdit.textChanged.connect(self.betChanged)
            reg_ex = QRegExp('^[2]{1}[01]{1}[0-9]{2}[-][0-1]{1}[0-9]{1}$')
            input_validator = QRegExpValidator(reg_ex, betEdit)
            betEdit.setValidator(input_validator)
                            
            grid = QGridLayout()
            grid.setSpacing(20)
    
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
                           
            grid.addWidget(QLabel('Betaalperiode jjjj-mm'), 1, 0)
            grid.addWidget(betEdit, 1, 1)
              
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
         
            applyBtn = QPushButton('Uitvoeren')
            applyBtn.clicked.connect(self.accept)
                  
            grid.addWidget(applyBtn, 2, 1, 1 ,1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
        
            grid.addWidget(cancelBtn, 2, 0, 1 ,1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
        
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 2, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(400, 300, 150, 150)
                 
        def betChanged(self, text):
            logger.warning(">>> Entering betChanged(text=%s)", text, extra={"event.action": "betChanged", "logrite.text": text})
            self.Betaalperiode.setText(text)
            logger.debug("<<< Exiting betChanged(text=%s)", text, extra={"event.action": "betChanged", "logrite.text": text})
    
        def returnBetaalperiode(self):
            logger.warning(">>> Entering returnBetaalperiode()", extra={"event.action": "returnBetaalperiode"})
            logger.debug("<<< Exiting returnBetaalperiode()", extra={"event.action": "returnBetaalperiode"})
            return self.Betaalperiode.text()
    
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnBetaalperiode()]
     
    window = Widget()
    data = window.getData()
    if data[0] and validZt.zt(data[0], 20):
        mjrmnd = data[0]
        controleUren(mjrmnd, m_email)
    else:
        ongPeriode()
        maandPeriode(m_email)
  
def controleUren(mjrmnd, m_email):
    logger.warning(">>> Entering controleUren(mjrmnd=%s,m_email=%s)", mjrmnd, m_email, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
    mblad = 1
    logger.debug("controleUren(mjrmnd=%s,m_email=%s): mblad → %s", mjrmnd, m_email, mblad, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
    rgl = 0
    metadata = MetaData()   
    logger.debug("controleUren(mjrmnd=%s,m_email=%s): metadata → %s", mjrmnd, m_email, metadata, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
    werknemers = Table('werknemers', metadata,
        Column('werknemerID', Integer(), primary_key=True),
        Column('accountID', None, ForeignKey('accounts.accountID')))
    accounts = Table('accounts', metadata,
        Column('accountID', Integer, primary_key=True),
        Column('voornaam', String),
        Column('achternaam', String),
        Column('tussenvoegsel', String))
    wrkwnrln = Table('wrkwnrln', metadata,
        Column('wrkwnrurenID', Integer, primary_key=True),
        Column('werknemerID', None, ForeignKey('werknemers.werknemerID')),
        Column('loonID', None, ForeignKey('lonen.loonID')),
        Column('boekdatum', String),
        Column('aantaluren', Float),
        Column('soort', String))
    logger.debug("controleUren(mjrmnd=%s,m_email=%s): selwerkn → %s", mjrmnd, m_email, selwerkn, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
    params = Table('params', metadata,
        Column('paramID', Integer, primary_key=True),
        Column('tarief', Float),
        Column('item', String),
        Column('lock', Boolean))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("controleUren(mjrmnd=%s,m_email=%s): engine → %s", mjrmnd, m_email, engine, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
    conn = engine.connect()
    logger.debug("controleUren(mjrmnd=%s,m_email=%s): conn → %s", mjrmnd, m_email, conn, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
    selwerkn = select([werknemers, accounts]).where(werknemers.c\
        .accountID == accounts.c.accountID).order_by(werknemers.c.werknemerID)
    rpwerkn = conn.execute(selwerkn)
    logger.debug("controleUren(mjrmnd=%s,m_email=%s): rpwerkn → %s", mjrmnd, m_email, rpwerkn, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
    selpar = select([params]).where(params.c.item == mjrmnd)
    logger.debug("controleUren(mjrmnd=%s,m_email=%s): selpar → %s", mjrmnd, m_email, selpar, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
    rppar = conn.execute(selpar).first()
    logger.debug("controleUren(mjrmnd=%s,m_email=%s): rppar → %s", mjrmnd, m_email, rppar, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
    if not rppar:
          ongPeriode()
          maandPeriode(m_email)
    for record in rpwerkn:
        if rgl == 0 or rgl%57 == 0: 
            if platform == 'win32':
                filename = '.\\forms\\Uren\\'+str(mjrmnd)+'.txt'
                logger.debug("controleUren(mjrmnd=%s,m_email=%s): filename → %s", mjrmnd, m_email, filename, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
                csvfilename = './/forms//Uren//'+str(mjrmnd)+'.csv'
            else:
                filename = './forms/Uren/'+str(mjrmnd)+'.txt'
                csvfilename = './forms/Uren/'+str(mjrmnd)+'.csv' 
                logger.debug("controleUren(mjrmnd=%s,m_email=%s): csvfilename → %s", mjrmnd, m_email, csvfilename, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
            open (csvfilename, "w").write("")
            kop = \
    ("Controle uren tbv loonbetalingen van periode "+str(mjrmnd)+" Pagina "+str(mblad)+"\n"+
     "============================================================\n"
     "Account   Werknemer                        Uren     Gewerkt \n"
     "============================================================\n")
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): kop → %s", mjrmnd, m_email, kop, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
            open(filename, "w").write(kop)
        elif rgl%57 == 0:
            open(filename, 'a').write(kop)
            mblad += 1
        
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): selwrkwnrln → %s", mjrmnd, m_email, selwrkwnrln, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): verlof → %s", mjrmnd, m_email, verlof, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): feestdag → %s", mjrmnd, m_email, feestdag, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): dokter → %s", mjrmnd, m_email, dokter, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): ziek → %s", mjrmnd, m_email, ziek, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): geoorlverz → %s", mjrmnd, m_email, geoorlverz, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): extraverl → %s", mjrmnd, m_email, extraverl, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
        uren100 = 0
        logger.debug("controleUren(mjrmnd=%s,m_email=%s): uren100 → %s", mjrmnd, m_email, uren100, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
        verlof = 0
        feestdag = 0
        dokter = 0
        ziek = 0
        geoorlverz = 0
        extraverl = 0
        selwrkwnrln = select([wrkwnrln]).where(and_(record[0]==wrkwnrln.c.werknemerID,\
                wrkwnrln.c.boekdatum.like(mjrmnd+'%')))\
            .order_by(wrkwnrln.c.werknemerID)
        rpwrkwnrln = conn.execute(selwrkwnrln)  
        logger.debug("controleUren(mjrmnd=%s,m_email=%s): rpwrkwnrln → %s", mjrmnd, m_email, rpwrkwnrln, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
        for rec in rpwrkwnrln:
            if rec[5] == '100%':
                uren100 = uren100+rec[4]
            elif rec[5] == 'Verlof':
                verlof = verlof+rec[4]
            elif rec[5] == 'Extra Verlof':
                extraverl = extraverl+rec[4]
            elif rec[5] == 'Feestdag':
                feestdag = feestdag+rec[4]
            elif rec[5] == 'Geoorl. Verzuim':
                geoorlverz = geoorlverz+rec[4]
            elif rec[5] == 'Ziek':
                ziek = ziek+rec[4]
            elif rec[5] == 'Dokter':
                dokter= dokter+rec[4]
                                                 
        if uren100+verlof+extraverl+feestdag+geoorlverz+ziek+dokter < int(rppar[1]):
            urengemaakt = uren100+verlof+extraverl+feestdag+geoorlverz+ziek+dokter
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): urengemaakt → %s", mjrmnd, m_email, urengemaakt, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
            gegevens = str(record[2])+' '+"{:8.8}".format(record[3])+' '+"{:16.16}"\
                          .format(record[4])+"{:>12.0f}".format(rppar[1])+\
                          "{:>12.2f}".format(urengemaakt)+'\n'
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): gegevens → %s", mjrmnd, m_email, gegevens, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
            open (filename,'a').write(gegevens)
            csvgegevens = str(record[2])+'|'+record[3]+'|'+record[5]\
               +'|'+record[4]+'|'+"{:>12.0f}".format(rppar[1])+'|'+\
               "{:>12.2f}".format(urengemaakt)
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): csvgegevens → %s", mjrmnd, m_email, csvgegevens, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
            open (csvfilename,'a').write(str(csvgegevens))
            open (csvfilename,'a').write('\n')
            rgl += 1
                            
    class Widget(QDialog):
        logger.debug("<<< Exiting controleUren(mjrmnd=%s,m_email=%s)", mjrmnd, m_email, extra={"event.action": "controleUren", "logrite.mjrmnd": mjrmnd})
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Controle uren per periode")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid = QGridLayout()
            grid.setSpacing(20)
            grid.addWidget(lbl , 0, 0, 1, 2)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 2, 1, 1, Qt.AlignRight)
            self.setFont(QFont('Arial', 10))
            
            self.setLayout(grid)
            self.setGeometry(400, 300, 500, 150)
            
            grid.addWidget(QLabel('''
            Deze module dient om het aantal geboekte uren 
            per periode en per werknemer te controleren, 
            voor de definitieve uitdraai wordt gemaakt.
            '''), 1, 0, 1, 3)
             
            toonBtn = QPushButton('Tonen')
            toonBtn.clicked.connect(lambda: toonGeg(mjrmnd))
          
            printBtn = QPushButton('Printen')
            printBtn.clicked.connect(lambda: printGeg(mjrmnd))
            
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: winSluit(self, m_email))
            
            grid.addWidget(toonBtn, 3, 2)
            toonBtn.setFont(QFont("Arial",10))
            toonBtn.setFixedWidth(120)
            toonBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            grid.addWidget(printBtn, 3, 1)
            printBtn.setFont(QFont("Arial",10))
            printBtn.setFixedWidth(120)
            printBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            grid.addWidget(cancelBtn, 3, 0)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(120)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
          
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1, 3, Qt.AlignCenter)
            
    window = Widget()
    window.exec_()