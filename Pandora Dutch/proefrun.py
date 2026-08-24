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
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)
    
def winSluit(self, m_email):
    logger.debug(">>> Entering winSluit(m_email=%s)", m_email)
    self.close()
    maandPeriode(m_email)
    logger.debug("<<< Exiting winSluit(m_email=%s)", m_email)

def ongPeriode():
    logger.debug(">>> Entering ongPeriode()")
    msg = QMessageBox()
    logger.debug("ongPeriode(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen geldige betaalperiode opgegeven!')
    msg.setWindowTitle('Controle werkuren')
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    logger.debug("<<< Exiting ongPeriode()")
    msg.exec_()
       
def printGeg(mjrmnd):
    logger.debug(">>> Entering printGeg(mjrmnd=%s)", mjrmnd)
    if platform == 'win32':
        filename = '.\\forms\\Uren\\'+str(mjrmnd)+'.txt'
        os.startfile(filename, "print")
        logger.debug("printGeg(mjrmnd=%s): filename → %s", mjrmnd, filename)
    else:
        filename = './forms/Uren/'+str(mjrmnd)+'.txt'
        os.system('lpr '+filename)
        logger.debug("<<< Exiting printGeg(mjrmnd=%s)", mjrmnd)
        
def selectRow(index):
    logger.debug(">>> Entering selectRow(index=%s)", index)
    #print('Recordnummer is: ', index.row())
    pass
    logger.debug("<<< Exiting selectRow(index=%s)", index)
               
def toonGeg(mjrmnd):
    logger.debug(">>> Entering toonGeg(mjrmnd=%s)", mjrmnd)
    class MyWindow(QDialog):
        logger.error("Exception in toonGeg(mjrmnd=%s)", mjrmnd, exc_info=True)
        def __init__(self, data_list, header, *args):
            logger.debug(">>> Entering __init__(data_list=%s,header=%s)", data_list, header)
            QWidget.__init__(self, *args,)
            self.setGeometry(100, 50, 800, 600)
            logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font)
            logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view)
            logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_model → %s", self, data_list, header, table_model)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_view → %s", self, data_list, header, table_view)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): font → %s", self, data_list, header, font)
            self.setWindowTitle('Cluster Calculatie')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            table_model = MyTableModel(self, data_list, header)
            table_view = QTableView()
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.setModel(table_model)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.clicked.connect(selectRow)
            layout = QVBoxLayout(self)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): layout → %s", self, data_list, header, layout)
            logger.debug("__init__(data_list=%s,header=%s): layout → %s", data_list, header, layout)
            layout.addWidget(table_view)
            self.setLayout(layout)
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header)
            logger.debug(">>> Entering __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header)
            logger.debug("<<< Exiting __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header)
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.mylist → %s", self, parent, mylist, header, self.mylist)

    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.header → %s", self, parent, mylist, header, self.header)
            QAbstractTableModel.__init__(self, parent, *args)
            self.mylist = mylist
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator)
            logger.debug("__init__(parent=%s): betEdit → %s", parent, betEdit)
            logger.debug("__init__(parent=%s): self.Betaalperiode → %s", parent, self.Betaalperiode)
            logger.debug("__init__(self=%s,parent=%s): betEdit → %s", self, parent, betEdit)
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex)
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator)
            logger.debug("__init__(parent=%s): grid → %s", parent, grid)
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid)
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl)
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl)
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn)
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
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
            self.font = QFont('Arial', 10)
            logger.debug("headerData(col=%s,orientation=%s,role=%s): self.font → %s", col, orientation, role, self.font)
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self.header[col]
            logger.debug("<<< Exiting headerData(col=%s,orientation=%s,role=%s)", col, orientation, role)
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
    logger.debug(">>> Entering maandPeriode(m_email=%s)", m_email)
    import validZt
    class Widget(QDialog):
        logger.debug("<<< Exiting maandPeriode(m_email=%s)", m_email)
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
            logger.debug(">>> Entering betChanged(text=%s)", text)
            logger.debug("betChanged(self=%s,text=%s): Betaalperiode → %s", self, text, Betaalperiode)
            self.Betaalperiode.setText(text)
            logger.debug("<<< Exiting betChanged(text=%s)", text)
    
        def returnBetaalperiode(self):
            logger.debug(">>> Entering returnBetaalperiode()")
            logger.debug("<<< Exiting returnBetaalperiode()")
            return self.Betaalperiode.text()
    
        @staticmethod
        def getData(parent=None):
            logger.debug(">>> Entering getData(parent=%s)", parent)
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent)
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
    logger.debug(">>> Entering controleUren(mjrmnd=%s,m_email=%s)", mjrmnd, m_email)
    mblad = 1
    logger.debug("controleUren(mjrmnd=%s,m_email=%s): mblad → %s", mjrmnd, m_email, mblad)
    rgl = 0
    metadata = MetaData()   
    logger.debug("controleUren(mjrmnd=%s,m_email=%s): metadata → %s", mjrmnd, m_email, metadata)
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
    params = Table('params', metadata,
        Column('paramID', Integer, primary_key=True),
        Column('tarief', Float),
        Column('item', String),
        Column('lock', Boolean))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("controleUren(mjrmnd=%s,m_email=%s): engine → %s", mjrmnd, m_email, engine)
    conn = engine.connect()
    logger.debug("controleUren(mjrmnd=%s,m_email=%s): conn → %s", mjrmnd, m_email, conn)
    selwerkn = select([werknemers, accounts]).where(werknemers.c\
        .accountID == accounts.c.accountID).order_by(werknemers.c.werknemerID)
    rpwerkn = conn.execute(selwerkn)
    logger.debug("controleUren(mjrmnd=%s,m_email=%s): selwerkn → %s", mjrmnd, m_email, selwerkn)
    selpar = select([params]).where(params.c.item == mjrmnd)
    rppar = conn.execute(selpar).first()
    logger.debug("controleUren(mjrmnd=%s,m_email=%s): rpwerkn → %s", mjrmnd, m_email, rpwerkn)
    if not rppar:
          ongPeriode()
          logger.debug("controleUren(mjrmnd=%s,m_email=%s): selpar → %s", mjrmnd, m_email, selpar)
          logger.debug("controleUren(mjrmnd=%s,m_email=%s): rppar → %s", mjrmnd, m_email, rppar)
          maandPeriode(m_email)
    for record in rpwerkn:
        if rgl == 0 or rgl%57 == 0: 
            if platform == 'win32':
                filename = '.\\forms\\Uren\\'+str(mjrmnd)+'.txt'
                csvfilename = './/forms//Uren//'+str(mjrmnd)+'.csv'
            else:
                filename = './forms/Uren/'+str(mjrmnd)+'.txt'
                logger.debug("controleUren(mjrmnd=%s,m_email=%s): filename → %s", mjrmnd, m_email, filename)
                csvfilename = './forms/Uren/'+str(mjrmnd)+'.csv' 
                logger.debug("controleUren(mjrmnd=%s,m_email=%s): csvfilename → %s", mjrmnd, m_email, csvfilename)
            open (csvfilename, "w").write("")
            kop = \
    ("Controle uren tbv loonbetalingen van periode "+str(mjrmnd)+" Pagina "+str(mblad)+"\n"+
     "============================================================\n"
     "Account   Werknemer                        Uren     Gewerkt \n"
     "============================================================\n")
            open(filename, "w").write(kop)
        elif rgl%57 == 0:
            open(filename, 'a').write(kop)
            mblad += 1
        
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): selwrkwnrln → %s", mjrmnd, m_email, selwrkwnrln)
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): verlof → %s", mjrmnd, m_email, verlof)
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): feestdag → %s", mjrmnd, m_email, feestdag)
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): dokter → %s", mjrmnd, m_email, dokter)
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): ziek → %s", mjrmnd, m_email, ziek)
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): geoorlverz → %s", mjrmnd, m_email, geoorlverz)
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): extraverl → %s", mjrmnd, m_email, extraverl)
        uren100 = 0
        logger.debug("controleUren(mjrmnd=%s,m_email=%s): uren100 → %s", mjrmnd, m_email, uren100)
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
        logger.debug("controleUren(mjrmnd=%s,m_email=%s): rpwrkwnrln → %s", mjrmnd, m_email, rpwrkwnrln)
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
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): urengemaakt → %s", mjrmnd, m_email, urengemaakt)
            gegevens = str(record[2])+' '+"{:8.8}".format(record[3])+' '+"{:16.16}"\
                          .format(record[4])+"{:>12.0f}".format(rppar[1])+\
                          "{:>12.2f}".format(urengemaakt)+'\n'
            open (filename,'a').write(gegevens)
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): gegevens → %s", mjrmnd, m_email, gegevens)
            csvgegevens = str(record[2])+'|'+record[3]+'|'+record[5]\
               +'|'+record[4]+'|'+"{:>12.0f}".format(rppar[1])+'|'+\
               "{:>12.2f}".format(urengemaakt)
            logger.debug("controleUren(mjrmnd=%s,m_email=%s): csvgegevens → %s", mjrmnd, m_email, csvgegevens)
            open (csvfilename,'a').write(str(csvgegevens))
            open (csvfilename,'a').write('\n')
            rgl += 1
                            
    class Widget(QDialog):
        logger.debug("<<< Exiting controleUren(mjrmnd=%s,m_email=%s)", mjrmnd, m_email)
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