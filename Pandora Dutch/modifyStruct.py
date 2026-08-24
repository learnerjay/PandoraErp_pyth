from login import hoofdMenu
import datetime
from PyQt5.QtCore import Qt, QAbstractTableModel, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon, QMovie
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QDialog, QGridLayout,\
      QMessageBox, QTableView, QVBoxLayout, QLineEdit
from sqlalchemy import (Table, Column, Integer, String, MetaData, create_engine, select, update, insert, func)
import logging
logger = logging.getLogger(__name__)

def insertReq():
    logger.debug(">>> Entering insertReq()")
    msg = QMessageBox()
    logger.debug("insertReq(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Insert data is required!')
    msg.setWindowTitle('Insert Menu Strukturen')
    logger.debug("<<< Exiting insertReq()")
    msg.exec_()

def insertOK():
    logger.debug(">>> Entering insertOK()")
    msg = QMessageBox()
    logger.debug("insertOK(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Inserting data was successful!')
    msg.setWindowTitle('Insert Menu Strukturen')
    logger.debug("<<< Exiting insertOK()")
    msg.exec_()

def errorInsert(message):
    logger.debug(">>> Entering errorInsert(message=%s)", message)
    msg = QMessageBox()
    logger.debug("errorInsert(message=%s): msg → %s", message, msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Critical)
    msg.setText('An error has occurred!\n'+message)
    msg.setWindowTitle('Insert Menu Strukturen')
    logger.debug("<<< Exiting errorInsert(message=%s)", message)
    msg.exec_()

def closeInsert(sector, m_email, self):
    logger.debug(">>> Entering closeInsert(sector=%s,m_email=%s)", sector, m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting closeInsert(sector=%s,m_email=%s)", sector, m_email)

def noChange():
    logger.debug(">>> Entering noChange()")
    msg = QMessageBox()
    logger.debug("noChange(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Critical)
    msg.setText('An error has occurred, no changes are processed!')
    msg.setWindowTitle('Modify Menu Structures')
    logger.debug("<<< Exiting noChange()")
    msg.exec_()

def changeOK():
    logger.debug(">>> Entering changeOK()")
    msg = QMessageBox()
    logger.debug("changeOK(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Changes are successful!')
    msg.setWindowTitle('Modify Menu Structures')
    logger.debug("<<< Exiting changeOK()")
    msg.exec_()

def refresh(m_email, self):
    logger.debug(">>> Entering refresh(m_email=%s)", m_email)
    self.close()
    menuStructure(m_email, self)
    logger.debug("<<< Exiting refresh(m_email=%s)", m_email)

def selectRow(index):
    logger.debug(">>> Entering selectRow(index=%s)", index)
    print('Recordnumber: ', index.row())
    logger.debug("<<< Exiting selectRow(index=%s)", index)

def menuStructure(sector, m_email):
    logger.debug(">>> Entering menuStructure(sector=%s,m_email=%s)", sector, m_email)
    metadata = MetaData()
    logger.debug("menuStructure(sector=%s,m_email=%s): metadata → %s", sector, m_email, metadata)
    cluster_structure_external = Table('cluster_structure_external', metadata,
       Column('structID', Integer(), primary_key=True),
       Column('overall_heading', String),
       Column('heading_level1', String),
       Column('line_level0', String),
       Column('line1', String),
       Column('line2', String),
       Column('line3', String),
       Column('line4', String),
       Column('line5', String),
       Column('line6', String),
       Column('line7', String),
       Column('line8', String),
       Column('line9', String),
       Column('line10', String),
       Column('line11', String),
       Column('line12', String),
       Column('line13', String),
       Column('line14', String),
       Column('line15', String))

    cluster_structure_internal = Table('cluster_structure_internal', metadata,
       Column('structID', Integer(), primary_key=True),
       Column('overall_heading', String),
       Column('heading_level1', String),
       Column('line_level0', String),
       Column('line1', String),
       Column('line2', String),
       Column('line3', String),
       Column('line4', String),
       Column('line5', String),
       Column('line6', String),
       Column('line7', String),
       Column('line8', String),
       Column('line9', String),
       Column('line10', String),
       Column('line11', String),
       Column('line12', String),
       Column('line13', String),
       Column('line14', String),
       Column('line15', String))

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("menuStructure(sector=%s,m_email=%s): engine → %s", sector, m_email, engine)
    if sector == 'external':
        con = engine.connect()
        logger.debug("menuStructure(sector=%s,m_email=%s): con → %s", sector, m_email, con)
        sel = select([cluster_structure_external]).order_by(cluster_structure_external.c.line_level0)
        logger.debug("menuStructure(sector=%s,m_email=%s): sel → %s", sector, m_email, sel)
        rpa = con1.execute(sel)
    else:
        con = engine.connect()
        sel = select([cluster_structure_internal]).order_by(cluster_structure_internal.c.line_level0)
        rpa = con.execute(sel)
        logger.debug("menuStructure(sector=%s,m_email=%s): rpa → %s", sector, m_email, rpa)
    class MyWindow(QDialog):
        logger.debug("<<< Exiting menuStructure(sector=%s,m_email=%s)", sector, m_email)
        def __init__(self, data_list, header, *args):
            logger.debug(">>> Entering __init__(data_list=%s,header=%s)", data_list, header)
            QWidget.__init__(self, *args, )
            self.setGeometry(50, 50, 1700, 900)
            self.setWindowTitle('Request account information')
            logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font)
            logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view)
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags() | Qt.WindowSystemMenuHint |
                                Qt.WindowMinMaxButtonsHint)
            table_model = MyTableModel(self, data_list, header)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_model → %s", self, data_list, header, table_model)
            logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model)
            table_view = QTableView()
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_view → %s", self, data_list, header, table_view)
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): font → %s", self, data_list, header, font)
            table_view.setFont(font)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.clicked.connect(showSelection)
            # table_view.clicked.connect(selectRow)
            layout = QVBoxLayout(self)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): layout → %s", self, data_list, header, layout)
            logger.debug("__init__(data_list=%s,header=%s): layout → %s", data_list, header, layout)
            layout.addWidget(table_view)
            self.setLayout(layout)
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header)
            logger.debug(">>> Entering __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header)
            logger.debug("<<< Exiting __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header)
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.mylist → %s", self, parent, mylist, header, self.mylist)
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.header → %s", self, parent, mylist, header, self.header)

    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            QAbstractTableModel.__init__(self, parent, *args)
            self.mylist = mylist
            self.header = header

        def rowCount(self, parent):
            logger.debug(">>> Entering rowCount(parent=%s)", parent)
            logger.debug("<<< Exiting rowCount(parent=%s)", parent)
            return len(self.mylist)

        def columnCount(self, parent):
            logger.debug(">>> Entering columnCount(parent=%s)", parent)
            try:
                logger.debug("<<< Exiting columnCount(parent=%s)", parent)
                return len(self.mylist[0])
            except:
                logger.error("Exception in columnCount(parent=%s)", parent, exc_info=True)
                noRecord()
                hoofdMenu(m_email)

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

    header = ['StructureID', 'Toplevel', 'Heading Level 1', 'Line_level0', 'Line 1', 'Line 2', 'Line 3', 'Line 4', 'Line 5',\
              'Line 6', 'Line 7', 'Line 8', 'Line 9', 'Line 10', 'Line 11', 'Line 12', 'Line 13', 'Line 14', 'Line 15']

    data_list = []
    for row in rpa:
        data_list += [row]

    def showSelection(idx):
        logger.debug(">>> Entering showSelection(idx=%s)", idx)
        if idx.column() == 0:
            structnr = idx.data()
            logger.debug("showSelection(idx=%s): structnr → %s", idx, structnr)
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showSelection(idx=%s): engine → %s", idx, engine)
            con = engine.connect()
            if sector == 'external':
                logger.debug("showSelection(idx=%s): con → %s", idx, con)
                selstruct = select([cluster_structure_external]).where(cluster_structure_external.c.structID == structnr)
                rpselstruct = con.execute(selstruct).first()
                logger.debug("showSelection(idx=%s): selstruct → %s", idx, selstruct)
                logger.debug("showSelection(idx=%s): rpselstruct → %s", idx, rpselstruct)
            else:
                selstruct = select([cluster_structure_internal]).where(cluster_structure_internal.c.structID == structnr)
                rpselstruct = con.execute(selstruct).first()
            class MainWindow(QDialog):
                logger.debug("<<< Exiting showSelection(idx=%s)", idx)
                def __init__(self):
                    QDialog.__init__(self)

                    grid = QGridLayout()
                    grid.setSpacing(20)
                    self.setWindowTitle("Modify Structure Menus Clusters")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                    self.setWindowFlags(self.windowFlags() | Qt.WindowSystemMenuHint |
                                        Qt.WindowMinMaxButtonsHint)
                    self.setFont(QFont('Arial', 10))

                    lbl1 = QLabel('Cluster Menu Structure  ID')
                    q1Edit = QLineEdit(str(rpselstruct[0]))
                    q1Edit.setFont(QFont("Arial", 10))
                    q1Edit.setFixedWidth(310)
                    q1Edit.setDisabled(True)
                    lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl1, 1, 0)
                    grid.addWidget(q1Edit, 1, 1)

                    self.q2 = QLabel()
                    lbl2 = QLabel('Overall heading')
                    q2Edit = QLineEdit(rpselstruct[1])
                    q2Edit.setFixedWidth(320)
                    q2Edit.setFont(QFont("Arial", 10))
                    q2Edit.textChanged.connect(self.q2Changed)
                    lbl2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl2, 2, 0)
                    grid.addWidget(q2Edit, 2, 1)

                    self.q3 = QLabel()
                    lbl3 = QLabel('Heading level 1')
                    q3Edit = QLineEdit(rpselstruct[2])
                    q3Edit.setFixedWidth(320)
                    q3Edit.setFont(QFont("Arial", 10))
                    q3Edit.textChanged.connect(self.q3Changed)
                    lbl3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl3, 3, 0)
                    grid.addWidget(q3Edit, 3, 1)

                    self.q4 = QLabel()
                    lbl4 = QLabel('Line level 0')
                    q4Edit = QLineEdit(rpselstruct[3])
                    q4Edit.setFixedWidth(320)
                    q4Edit.setFont(QFont("Arial", 10))
                    q4Edit.textChanged.connect(self.q4Changed)
                    lbl4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl4, 4, 0)
                    grid.addWidget(q4Edit, 4, 1)

                    self.q5 = QLabel()
                    lbl5 = QLabel('Line 1')
                    q5Edit = QLineEdit(rpselstruct[4])
                    q5Edit.setFixedWidth(320)
                    q5Edit.setFont(QFont("Arial", 10))
                    q5Edit.textChanged.connect(self.q5Changed)
                    lbl5.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl5, 5, 0)
                    grid.addWidget(q5Edit, 5, 1)

                    self.q7 = QLabel()
                    lbl7 = QLabel('Line 2')
                    q7Edit = QLineEdit(rpselstruct[5])
                    q7Edit.setFixedWidth(320)
                    q7Edit.setFont(QFont("Arial", 10))
                    q7Edit.textChanged.connect(self.q7Changed)
                    lbl7.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl7, 6, 0)
                    grid.addWidget(q7Edit, 6, 1)

                    self.q8 = QLabel()
                    lbl8 = QLabel('Line 3')
                    q8Edit = QLineEdit(rpselstruct[6])
                    q8Edit.setFixedWidth(320)
                    q8Edit.setFont(QFont("Arial", 10))
                    q8Edit.textChanged.connect(self.q8Changed)
                    lbl8.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl8, 7, 0)
                    grid.addWidget(q8Edit, 7, 1)

                    self.q9 = QLabel()
                    lbl9 = QLabel('Line 4')
                    q9Edit = QLineEdit(rpselstruct[7])
                    q9Edit.setFixedWidth(320)
                    q9Edit.setFont(QFont("Arial", 10))
                    q9Edit.textChanged.connect(self.q9Changed)
                    lbl9.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl9, 8, 0)
                    grid.addWidget(q9Edit, 8, 1)

                    self.q10 = QLabel()
                    lbl10 = QLabel('Line 5')
                    q10Edit = QLineEdit(rpselstruct[8])
                    q10Edit.setFixedWidth(320)
                    q10Edit.setFont(QFont("Arial", 10))
                    q10Edit.textChanged.connect(self.q10Changed)
                    lbl10.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl10, 9, 0)
                    grid.addWidget(q10Edit, 9, 1)

                    self.q20 = QLabel()
                    lbl20 = QLabel('Line 6')
                    q20Edit = QLineEdit(rpselstruct[9])
                    q20Edit.setFixedWidth(320)
                    q20Edit.setFont(QFont("Arial", 10))
                    q20Edit.textChanged.connect(self.q20Changed)
                    lbl20.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl20, 10, 0)
                    grid.addWidget(q20Edit, 10, 1)

                    self.q21 = QLabel()
                    lbl21 = QLabel('Line 7')
                    q21Edit = QLineEdit(rpselstruct[10])
                    q21Edit.setFixedWidth(320)
                    q21Edit.setFont(QFont("Arial", 10))
                    q21Edit.textChanged.connect(self.q21Changed)
                    lbl21.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl21, 11, 0)
                    grid.addWidget(q21Edit, 11, 1)

                    self.q22 = QLabel()
                    lbl22 = QLabel('Line 8')
                    q22Edit = QLineEdit(rpselstruct[11])
                    q22Edit.setFixedWidth(320)
                    q22Edit.setFont(QFont("Arial", 10))
                    q22Edit.textChanged.connect(self.q22Changed)
                    lbl22.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl22, 3, 2)
                    grid.addWidget(q22Edit, 3, 3)

                    self.q23 = QLabel()
                    lbl23 = QLabel('Line 9')
                    q23Edit = QLineEdit(rpselstruct[12])
                    q23Edit.setFixedWidth(320)
                    q23Edit.setFont(QFont("Arial", 10))
                    q23Edit.textChanged.connect(self.q23Changed)
                    lbl23.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl23, 4, 2)
                    grid.addWidget(q23Edit, 4, 3)

                    self.q24 = QLabel()
                    lbl24 = QLabel('Line 10')
                    q24Edit = QLineEdit(rpselstruct[13])
                    q24Edit.setFixedWidth(320)
                    q24Edit.setFont(QFont("Arial", 10))
                    q24Edit.textChanged.connect(self.q24Changed)
                    lbl24.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl24, 5, 2)
                    grid.addWidget(q24Edit, 5, 3)

                    self.q25 = QLabel()
                    lbl25 = QLabel('Line 11')
                    q25Edit = QLineEdit(rpselstruct[14])
                    q25Edit.setFixedWidth(320)
                    q25Edit.setFont(QFont("Arial", 10))
                    q25Edit.textChanged.connect(self.q25Changed)
                    lbl25.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl25, 6, 2)
                    grid.addWidget(q25Edit, 6, 3)

                    self.q26 = QLabel()
                    lbl26 = QLabel('Line 12')
                    q26Edit = QLineEdit(rpselstruct[15])
                    q26Edit.setFixedWidth(320)
                    q26Edit.setFont(QFont("Arial", 10))
                    q26Edit.textChanged.connect(self.q26Changed)
                    lbl26.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl26, 7, 2)
                    grid.addWidget(q26Edit, 7, 3)

                    self.q27 = QLabel()
                    lbl27 = QLabel('Line 13')
                    q27Edit = QLineEdit(rpselstruct[16])
                    q27Edit.setFixedWidth(320)
                    q27Edit.setFont(QFont("Arial", 10))
                    q27Edit.textChanged.connect(self.q27Changed)
                    lbl27.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl27, 8, 2)
                    grid.addWidget(q27Edit, 8, 3)

                    self.q28 = QLabel()
                    lbl28 = QLabel('Line 14')
                    q28Edit = QLineEdit(rpselstruct[17])
                    q28Edit.setFixedWidth(320)
                    q28Edit.setFont(QFont("Arial", 10))
                    q28Edit.textChanged.connect(self.q28Changed)
                    lbl28.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl28, 9, 2)
                    grid.addWidget(q28Edit, 9, 3)

                    self.q29 = QLabel()
                    lbl29 = QLabel('Line 15')
                    q29Edit = QLineEdit(rpselstruct[18])
                    q29Edit.setFixedWidth(320)
                    q29Edit.setFont(QFont("Arial", 10))
                    q29Edit.textChanged.connect(self.q29Changed)
                    lbl29.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl29, 10, 2)
                    grid.addWidget(q29Edit, 10, 3)

                    pyqt = QLabel()
                    movie = QMovie('./images/logos/pyqt.gif')
                    pyqt.setMovie(movie)
                    movie.setScaledSize(QSize(240, 80))
                    movie.start()
                    grid.addWidget(pyqt, 0, 0, 1, 2)

                    logo = QLabel()
                    pixmap = QPixmap('./images/logos/logo.jpg')
                    logo.setPixmap(pixmap)
                    grid.addWidget(logo, 0, 3, 1, 1, Qt.AlignRight)

                    grid.addWidget(QLabel('Modify Structure Menus of Clusters from '+sector+' Works'), 0, 1, 1, 4, Qt.AlignCenter)

                    applyBtn = QPushButton('Modify')
                    applyBtn.clicked.connect(self.accept)

                    grid.addWidget(applyBtn, 21, 3, 1, 1, Qt.AlignRight)
                    applyBtn.setFont(QFont("Arial", 10))
                    applyBtn.setFixedWidth(100)
                    applyBtn.setStyleSheet("color: black;  background-color: gainsboro")

                    closeBtn = QPushButton('Close')
                    closeBtn.clicked.connect(self.close)

                    grid.addWidget(closeBtn, 21, 3, 1, 1, Qt.AlignCenter)
                    closeBtn.setFont(QFont("Arial", 10))
                    closeBtn.setFixedWidth(100)
                    closeBtn.setStyleSheet("color: black;  background-color: gainsboro")

                    grid.addWidget(QLabel('                         \u00A9 2017 all rights reserved dj.jansen@casema.nl'), 22, 1, 1, 3)

                    self.setLayout(grid)
                    self.setGeometry(400, 50, 150, 150)
                    logger.debug(">>> Entering __init__()")
                    logger.debug("__init__(): grid → %s", grid)
                    logger.debug("__init__(self=%s): grid → %s", self, grid)
                    logger.debug("__init__(): q1Edit → %s", q1Edit)
                    logger.debug("__init__(): lbl1 → %s", lbl1)
                    logger.debug("__init__(self=%s): lbl1 → %s", self, lbl1)
                    logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit)
                    logger.debug("__init__(): q2Edit → %s", q2Edit)
                    logger.debug("__init__(): lbl2 → %s", lbl2)
                    logger.debug("__init__(): self.q2 → %s", self.q2)
                    logger.debug("__init__(self=%s): lbl2 → %s", self, lbl2)
                    logger.debug("__init__(self=%s): q2Edit → %s", self, q2Edit)
                    logger.debug("__init__(): q3Edit → %s", q3Edit)
                    logger.debug("__init__(): lbl3 → %s", lbl3)
                    logger.debug("__init__(): self.q3 → %s", self.q3)
                    logger.debug("__init__(self=%s): lbl3 → %s", self, lbl3)
                    logger.debug("__init__(self=%s): q3Edit → %s", self, q3Edit)
                    logger.debug("__init__(): q4Edit → %s", q4Edit)
                    logger.debug("__init__(): lbl4 → %s", lbl4)
                    logger.debug("__init__(): self.q4 → %s", self.q4)
                    logger.debug("__init__(self=%s): lbl4 → %s", self, lbl4)
                    logger.debug("__init__(self=%s): q4Edit → %s", self, q4Edit)
                    logger.debug("__init__(): q5Edit → %s", q5Edit)
                    logger.debug("__init__(): lbl5 → %s", lbl5)
                    logger.debug("__init__(): self.q5 → %s", self.q5)
                    logger.debug("__init__(self=%s): lbl5 → %s", self, lbl5)
                    logger.debug("__init__(self=%s): q5Edit → %s", self, q5Edit)
                    logger.debug("__init__(): q7Edit → %s", q7Edit)
                    logger.debug("__init__(): lbl7 → %s", lbl7)
                    logger.debug("__init__(): self.q7 → %s", self.q7)
                    logger.debug("__init__(self=%s): lbl7 → %s", self, lbl7)
                    logger.debug("__init__(self=%s): q7Edit → %s", self, q7Edit)
                    logger.debug("__init__(): q8Edit → %s", q8Edit)
                    logger.debug("__init__(): lbl8 → %s", lbl8)
                    logger.debug("__init__(): self.q8 → %s", self.q8)
                    logger.debug("__init__(self=%s): lbl8 → %s", self, lbl8)
                    logger.debug("__init__(self=%s): q8Edit → %s", self, q8Edit)
                    logger.debug("__init__(): q9Edit → %s", q9Edit)
                    logger.debug("__init__(): lbl9 → %s", lbl9)
                    logger.debug("__init__(): self.q9 → %s", self.q9)
                    logger.debug("__init__(self=%s): lbl9 → %s", self, lbl9)
                    logger.debug("__init__(self=%s): q9Edit → %s", self, q9Edit)
                    logger.debug("__init__(): q10Edit → %s", q10Edit)
                    logger.debug("__init__(): lbl10 → %s", lbl10)
                    logger.debug("__init__(): self.q10 → %s", self.q10)
                    logger.debug("__init__(self=%s): lbl10 → %s", self, lbl10)
                    logger.debug("__init__(self=%s): q10Edit → %s", self, q10Edit)
                    logger.debug("__init__(): q20Edit → %s", q20Edit)
                    logger.debug("__init__(): lbl20 → %s", lbl20)
                    logger.debug("__init__(): self.q20 → %s", self.q20)
                    logger.debug("__init__(self=%s): lbl20 → %s", self, lbl20)
                    logger.debug("__init__(self=%s): q20Edit → %s", self, q20Edit)
                    logger.debug("__init__(): q21Edit → %s", q21Edit)
                    logger.debug("__init__(): lbl21 → %s", lbl21)
                    logger.debug("__init__(): self.q21 → %s", self.q21)
                    logger.debug("__init__(self=%s): lbl21 → %s", self, lbl21)
                    logger.debug("__init__(self=%s): q21Edit → %s", self, q21Edit)
                    logger.debug("__init__(): q22Edit → %s", q22Edit)
                    logger.debug("__init__(): lbl22 → %s", lbl22)
                    logger.debug("__init__(): self.q22 → %s", self.q22)
                    logger.debug("__init__(self=%s): lbl22 → %s", self, lbl22)
                    logger.debug("__init__(self=%s): q22Edit → %s", self, q22Edit)
                    logger.debug("__init__(): q23Edit → %s", q23Edit)
                    logger.debug("__init__(): lbl23 → %s", lbl23)
                    logger.debug("__init__(): self.q23 → %s", self.q23)
                    logger.debug("__init__(self=%s): lbl23 → %s", self, lbl23)
                    logger.debug("__init__(self=%s): q23Edit → %s", self, q23Edit)
                    logger.debug("__init__(): q24Edit → %s", q24Edit)
                    logger.debug("__init__(): lbl24 → %s", lbl24)
                    logger.debug("__init__(): self.q24 → %s", self.q24)
                    logger.debug("__init__(self=%s): lbl24 → %s", self, lbl24)
                    logger.debug("__init__(self=%s): q24Edit → %s", self, q24Edit)
                    logger.debug("__init__(): q25Edit → %s", q25Edit)
                    logger.debug("__init__(): lbl25 → %s", lbl25)
                    logger.debug("__init__(): self.q25 → %s", self.q25)
                    logger.debug("__init__(self=%s): lbl25 → %s", self, lbl25)
                    logger.debug("__init__(self=%s): q25Edit → %s", self, q25Edit)
                    logger.debug("__init__(): q26Edit → %s", q26Edit)
                    logger.debug("__init__(): lbl26 → %s", lbl26)
                    logger.debug("__init__(): self.q26 → %s", self.q26)
                    logger.debug("__init__(self=%s): lbl26 → %s", self, lbl26)
                    logger.debug("__init__(self=%s): q26Edit → %s", self, q26Edit)
                    logger.debug("__init__(): q27Edit → %s", q27Edit)
                    logger.debug("__init__(): lbl27 → %s", lbl27)
                    logger.debug("__init__(): self.q27 → %s", self.q27)
                    logger.debug("__init__(self=%s): lbl27 → %s", self, lbl27)
                    logger.debug("__init__(self=%s): q27Edit → %s", self, q27Edit)
                    logger.debug("__init__(): q28Edit → %s", q28Edit)
                    logger.debug("__init__(): lbl28 → %s", lbl28)
                    logger.debug("__init__(): self.q28 → %s", self.q28)
                    logger.debug("__init__(self=%s): lbl28 → %s", self, lbl28)
                    logger.debug("__init__(self=%s): q28Edit → %s", self, q28Edit)
                    logger.debug("__init__(): q29Edit → %s", q29Edit)
                    logger.debug("__init__(): lbl29 → %s", lbl29)
                    logger.debug("__init__(): self.q29 → %s", self.q29)
                    logger.debug("__init__(self=%s): lbl29 → %s", self, lbl29)
                    logger.debug("__init__(self=%s): q29Edit → %s", self, q29Edit)
                    logger.debug("__init__(): movie → %s", movie)
                    logger.debug("__init__(): pyqt → %s", pyqt)
                    logger.debug("__init__(self=%s): pyqt → %s", self, pyqt)
                    logger.debug("__init__(self=%s): movie → %s", self, movie)
                    logger.debug("__init__(): pixmap → %s", pixmap)
                    logger.debug("__init__(): logo → %s", logo)
                    logger.debug("__init__(self=%s): logo → %s", self, logo)
                    logger.debug("__init__(self=%s): pixmap → %s", self, pixmap)
                    logger.info("__init__()=: save operation took %s ms", int((time.time() - __log_start) * 1000))
                    logger.debug("__init__(): applyBtn → %s", applyBtn)
                    logger.debug("__init__(self=%s): applyBtn → %s", self, applyBtn)
                    logger.debug("__init__(): closeBtn → %s", closeBtn)
                    logger.debug("__init__(self=%s): closeBtn → %s", self, closeBtn)
                    logger.debug("<<< Exiting __init__()")

                def q2Changed(self, text):
                    logger.debug(">>> Entering q2Changed(text=%s)", text)
                    logger.debug("q2Changed(self=%s,text=%s): q2 → %s", self, text, q2)
                    self.q2.setText(text)
                    logger.debug("<<< Exiting q2Changed(text=%s)", text)

                def q3Changed(self, text):
                    logger.debug(">>> Entering q3Changed(text=%s)", text)
                    logger.debug("q3Changed(self=%s,text=%s): q3 → %s", self, text, q3)
                    self.q3.setText(text)
                    logger.debug("<<< Exiting q3Changed(text=%s)", text)

                def q4Changed(self, text):
                    logger.debug(">>> Entering q4Changed(text=%s)", text)
                    logger.debug("q4Changed(self=%s,text=%s): q4 → %s", self, text, q4)
                    self.q4.setText(text)
                    logger.debug("<<< Exiting q4Changed(text=%s)", text)

                def q5Changed(self, text):
                    logger.debug(">>> Entering q5Changed(text=%s)", text)
                    logger.debug("q5Changed(self=%s,text=%s): q5 → %s", self, text, q5)
                    self.q5.setText(text)
                    logger.debug("<<< Exiting q5Changed(text=%s)", text)

                def q7Changed(self, text):
                    logger.debug(">>> Entering q7Changed(text=%s)", text)
                    logger.debug("q7Changed(self=%s,text=%s): q7 → %s", self, text, q7)
                    self.q7.setText(text)
                    logger.debug("<<< Exiting q7Changed(text=%s)", text)

                def q8Changed(self, text):
                    logger.debug(">>> Entering q8Changed(text=%s)", text)
                    logger.debug("q8Changed(self=%s,text=%s): q8 → %s", self, text, q8)
                    self.q8.setText(text)
                    logger.debug("<<< Exiting q8Changed(text=%s)", text)

                def q9Changed(self, text):
                    logger.debug(">>> Entering q9Changed(text=%s)", text)
                    logger.debug("q9Changed(self=%s,text=%s): q9 → %s", self, text, q9)
                    self.q9.setText(text)
                    logger.debug("<<< Exiting q9Changed(text=%s)", text)

                def q10Changed(self, text):
                    logger.debug(">>> Entering q10Changed(text=%s)", text)
                    logger.debug("q10Changed(self=%s,text=%s): q10 → %s", self, text, q10)
                    self.q10.setText(text)
                    logger.debug("<<< Exiting q10Changed(text=%s)", text)

                def q20Changed(self, text):
                    logger.debug(">>> Entering q20Changed(text=%s)", text)
                    logger.debug("q20Changed(self=%s,text=%s): q20 → %s", self, text, q20)
                    self.q20.setText(text)
                    logger.debug("<<< Exiting q20Changed(text=%s)", text)

                def q21Changed(self, text):
                    logger.debug(">>> Entering q21Changed(text=%s)", text)
                    logger.debug("q21Changed(self=%s,text=%s): q21 → %s", self, text, q21)
                    self.q21.setText(text)
                    logger.debug("<<< Exiting q21Changed(text=%s)", text)

                def q22Changed(self, text):
                    logger.debug(">>> Entering q22Changed(text=%s)", text)
                    logger.debug("q22Changed(self=%s,text=%s): q22 → %s", self, text, q22)
                    self.q22.setText(text)
                    logger.debug("<<< Exiting q22Changed(text=%s)", text)

                def q23Changed(self, text):
                    logger.debug(">>> Entering q23Changed(text=%s)", text)
                    logger.debug("q23Changed(self=%s,text=%s): q23 → %s", self, text, q23)
                    self.q23.setText(text)
                    logger.debug("<<< Exiting q23Changed(text=%s)", text)

                def q24Changed(self, text):
                    logger.debug(">>> Entering q24Changed(text=%s)", text)
                    logger.debug("q24Changed(self=%s,text=%s): q24 → %s", self, text, q24)
                    self.q24.setText(text)
                    logger.debug("<<< Exiting q24Changed(text=%s)", text)

                def q25Changed(self, text):
                    logger.debug(">>> Entering q25Changed(text=%s)", text)
                    logger.debug("q25Changed(self=%s,text=%s): q25 → %s", self, text, q25)
                    self.q25.setText(text)
                    logger.debug("<<< Exiting q25Changed(text=%s)", text)

                def q26Changed(self, text):
                    logger.debug(">>> Entering q26Changed(text=%s)", text)
                    logger.debug("q26Changed(self=%s,text=%s): q26 → %s", self, text, q26)
                    self.q26.setText(text)
                    logger.debug("<<< Exiting q26Changed(text=%s)", text)

                def q27Changed(self, text):
                    logger.debug(">>> Entering q27Changed(text=%s)", text)
                    logger.debug("q27Changed(self=%s,text=%s): q27 → %s", self, text, q27)
                    self.q27.setText(text)
                    logger.debug("<<< Exiting q27Changed(text=%s)", text)

                def q28Changed(self, text):
                    logger.debug(">>> Entering q28Changed(text=%s)", text)
                    logger.debug("q28Changed(self=%s,text=%s): q28 → %s", self, text, q28)
                    self.q28.setText(text)
                    logger.debug("<<< Exiting q28Changed(text=%s)", text)

                def q29Changed(self, text):
                    logger.debug(">>> Entering q29Changed(text=%s)", text)
                    logger.debug("q29Changed(self=%s,text=%s): q29 → %s", self, text, q29)
                    self.q29.setText(text)
                    logger.debug("<<< Exiting q29Changed(text=%s)", text)

                def returnq2(self):
                    logger.debug(">>> Entering returnq2()")
                    logger.debug("<<< Exiting returnq2()")
                    return self.q2.text()

                def returnq3(self):
                    logger.debug(">>> Entering returnq3()")
                    logger.debug("<<< Exiting returnq3()")
                    return self.q3.text()

                def returnq4(self):
                    logger.debug(">>> Entering returnq4()")
                    logger.debug("<<< Exiting returnq4()")
                    return self.q4.text()

                def returnq5(self):
                    logger.debug(">>> Entering returnq5()")
                    logger.debug("<<< Exiting returnq5()")
                    return self.q5.text()

                def returnq7(self):
                    logger.debug(">>> Entering returnq7()")
                    logger.debug("<<< Exiting returnq7()")
                    return self.q7.text()

                def returnq8(self):
                    logger.debug(">>> Entering returnq8()")
                    logger.debug("<<< Exiting returnq8()")
                    return self.q8.text()

                def returnq9(self):
                    logger.debug(">>> Entering returnq9()")
                    logger.debug("<<< Exiting returnq9()")
                    return self.q9.text()

                def returnq10(self):
                    logger.debug(">>> Entering returnq10()")
                    logger.debug("<<< Exiting returnq10()")
                    return self.q10.text()

                def returnq20(self):
                    logger.debug(">>> Entering returnq20()")
                    logger.debug("<<< Exiting returnq20()")
                    return self.q20.text()

                def returnq21(self):
                    logger.debug(">>> Entering returnq21()")
                    logger.debug("<<< Exiting returnq21()")
                    return self.q21.text()

                def returnq22(self):
                    logger.debug(">>> Entering returnq22()")
                    logger.debug("<<< Exiting returnq22()")
                    return self.q22.text()

                def returnq23(self):
                    logger.debug(">>> Entering returnq23()")
                    logger.debug("<<< Exiting returnq23()")
                    return self.q23.text()

                def returnq24(self):
                    logger.debug(">>> Entering returnq24()")
                    logger.debug("<<< Exiting returnq24()")
                    return self.q24.text()

                def returnq25(self):
                    logger.debug(">>> Entering returnq25()")
                    logger.debug("<<< Exiting returnq25()")
                    return self.q25.text()

                def returnq26(self):
                    logger.debug(">>> Entering returnq26()")
                    logger.debug("<<< Exiting returnq26()")
                    return self.q26.text()

                def returnq27(self):
                    logger.debug(">>> Entering returnq27()")
                    logger.debug("<<< Exiting returnq27()")
                    return self.q27.text()

                def returnq28(self):
                    logger.debug(">>> Entering returnq28()")
                    logger.debug("<<< Exiting returnq28()")
                    return self.q28.text()

                def returnq29(self):
                    logger.debug(">>> Entering returnq29()")
                    logger.debug("<<< Exiting returnq29()")
                    return self.q29.text()

                @staticmethod
                def getData(parent=None):
                    logger.debug(">>> Entering getData(parent=%s)", parent)
                    dialog = MainWindow()
                    logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
                    dialog.exec_()
                    logger.debug("<<< Exiting getData(parent=%s)", parent)
                    return [dialog.returnq2(), dialog.returnq3(), dialog.returnq4(), dialog.returnq5(), dialog.returnq7(),\
                            dialog.returnq8(), dialog.returnq9(), dialog.returnq10(), dialog.returnq20(), dialog.returnq21(),\
                            dialog.returnq22(), dialog.returnq23(), dialog.returnq24(), dialog.returnq25(), dialog.returnq26(),\
                            dialog.returnq27(), dialog.returnq28(), dialog.returnq29()]

            mainWin = MainWindow()
            data = mainWin.getData()

            changeflag = 0
            for k in range(0, 18):
                if data[k]:
                    changeflag = 1
            if changeflag == 0:
                return

            if data[0]:
                q2 = data[0]
            else:
                q2 = rpselstruct[1]
            if data[1]:
                q3 =data[1]
            else:
                q3 = rpselstruct[2]
            if data[2]:
                q4 = data[2]
            else:
                q4 = rpselstruct[3]
            if data[3]:
                q5 = data[3]
            else:
                q5 = rpselstruct[4]
            if data[4]:
                q7 = data[4]
            else:
                q7 = rpselstruct[5]
            if data[5]:
                q8 = data[5]
            else:
                q8 = rpselstruct[6]
            if data[6]:
                q9 = data[6]
            else:
                q9 = rpselstruct[7]
            if data[7]:
                q10 = data[7]
            else:
                q10 = rpselstruct[8]
            if data[8]:
                q20 = data[8]
            else:
                q20 = rpselstruct[9]
            if data[9]:
                q21 = data[9]
            else:
                q21 = rpselstruct[10]
            if data[10]:
                q22 = data[10]
            else:
                q22 = rpselstruct[11]
            if data[11]:
                q23 = data[11]
            else:
                q23 = rpselstruct[12]
            if data[12]:
                q24 = data[12]
            else:
                q24 = rpselstruct[13]
            if data[13]:
                q25 = data[13]
            else:
                q25 = rpselstruct[14]
            if data[14]:
                q26 = data[14]
            else:
                q26 = rpselstruct[15]
            if data[15]:
                q27 = data[15]
            else:
                q27 = rpselstruct[16]
            if data[16]:
                q28 = data[16]
            else:
                q28 = rpselstruct[17]
            if data[17]:
                q29 = data[17]
            else:
                q29 = rpselstruct[18]

            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            con = engine.connect()
            try:
                if sector == 'external':
                    updstruct = update(cluster_structure_external).where(cluster_structure_external.c.structID == structnr). \
                        values(overall_heading=q2, heading_level1=q3, line_level0=q4, line1=q5, line2=q7, line3=q8, line4=q9, line5=q10, \
                         line6=q20, line7=q21, line8=q22, line9=q23, line10=q24, line11=q25, line12=q26, line13=q27, line14=q28, line15=q29)
                    con.execute(updstruct)
                else:
                    updstruct = update(cluster_structure_internal).where(cluster_structure_internal.c.structID == structnr). \
                        values(overall_heading=q2, heading_level1=q3, line_level0=q4, line1=q5, line2=q7, line3=q8,line4=q9, line5=q10, \
                         line6=q20, line7=q21, line8=q22, line9=q23, line10=q24, line11=q25, line12=q26, line13=q27, line14=q28, line15=q29)
                    con.execute(updstruct)
                changeOK()
            except Exception:
                noChange()

    win = MyWindow(data_list, header)
    win.exec_()
    hoofdMenu(m_email)

def insertStruct(sector, m_email):
    logger.debug(">>> Entering insertStruct(sector=%s,m_email=%s)", sector, m_email)
    metadata = MetaData()
    logger.debug("insertStruct(sector=%s,m_email=%s): metadata → %s", sector, m_email, metadata)
    cluster_structure_external = Table('cluster_structure_external', metadata,
           Column('structID', Integer(), primary_key=True),
           Column('overall_heading', String),
           Column('heading_level1', String),
           Column('line_level0', String),
           Column('line1', String),
           Column('line2', String),
           Column('line3', String),
           Column('line4', String),
           Column('line5', String),
           Column('line6', String),
           Column('line7', String),
           Column('line8', String),
           Column('line9', String),
           Column('line10', String),
           Column('line11', String),
           Column('line12', String),
           Column('line13', String),
           Column('line14', String),
           Column('line15', String))

    cluster_structure_internal = Table('cluster_structure_internal', metadata,
           Column('structID', Integer(), primary_key=True),
           Column('overall_heading', String),
           Column('heading_level1', String),
           Column('line_level0', String),
           Column('line1', String),
           Column('line2', String),
           Column('line3', String),
           Column('line4', String),
           Column('line5', String),
           Column('line6', String),
           Column('line7', String),
           Column('line8', String),
           Column('line9', String),
           Column('line10', String),
           Column('line11', String),
           Column('line12', String),
           Column('line13', String),
           Column('line14', String),
           Column('line15', String))

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("insertStruct(sector=%s,m_email=%s): engine → %s", sector, m_email, engine)
    con = engine.connect()
    logger.debug("insertStruct(sector=%s,m_email=%s): con → %s", sector, m_email, con)

    if sector == 'external':
        try:
            structnr = (con.execute(select([func.max(cluster_structure_external.c.structID, \
                                                       type_=Integer)])).scalar())
            logger.debug("insertStruct(sector=%s,m_email=%s): type_ → %s", sector, m_email, type_)
            structnr += 1
        except:
            logger.error("Exception in insertStruct(sector=%s,m_email=%s)", sector, m_email, exc_info=True)
            structnr = 1
    if sector == 'internal':
        try:
            structnr = (con.execute(select([func.max(cluster_structure_internal.c.structID, \
                                                 type_=Integer)])).scalar())
            structnr += 1
        except:
            structnr = 1
    class insWindow(QDialog):
        logger.debug("<<< Exiting insertStruct(sector=%s,m_email=%s)", sector, m_email)
        def __init__(self, *args):
            logger.debug(">>> Entering __init__()")
            QWidget.__init__(self, *args, )
            self.setGeometry(50, 50, 1700, 900)
            self.setWindowTitle('Request account information')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags() | Qt.WindowSystemMenuHint |
                                Qt.WindowMinMaxButtonsHint)

            grid = QGridLayout()
            grid.setSpacing(20)
            self.setWindowTitle("Insert Structure Menus Clusters")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags() | Qt.WindowSystemMenuHint |
                                Qt.WindowMinMaxButtonsHint)
            self.setFont(QFont('Arial', 10))

            lbl1 = QLabel('Cluster Menu Structure  ID')
            q1Edit = QLineEdit(str(structnr))
            q1Edit.setFont(QFont("Arial", 10))
            q1Edit.setFixedWidth(310)
            q1Edit.setDisabled(True)
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 1, 0)
            grid.addWidget(q1Edit, 1, 1)

            self.q2 = QLabel()
            lbl2 = QLabel('Overall heading')
            q2Edit = QLineEdit('')
            q2Edit.setFixedWidth(320)
            q2Edit.setFont(QFont("Arial", 10))
            q2Edit.textChanged.connect(self.q2Changed)
            lbl2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl2, 2, 0)
            grid.addWidget(q2Edit, 2, 1)

            self.q3 = QLabel()
            lbl3 = QLabel('Heading level 1')
            q3Edit = QLineEdit('')
            q3Edit.setFixedWidth(320)
            q3Edit.setFont(QFont("Arial", 10))
            q3Edit.textChanged.connect(self.q3Changed)
            lbl3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl3, 3, 0)
            grid.addWidget(q3Edit, 3, 1)

            self.q4 = QLabel()
            lbl4 = QLabel('Line level 0')
            q4Edit = QLineEdit('')
            q4Edit.setFixedWidth(320)
            q4Edit.setFont(QFont("Arial", 10))
            q4Edit.textChanged.connect(self.q4Changed)
            lbl4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl4, 4, 0)
            grid.addWidget(q4Edit, 4, 1)

            self.q5 = QLabel()
            lbl5 = QLabel('Line 1')
            q5Edit = QLineEdit('')
            q5Edit.setFixedWidth(320)
            q5Edit.setFont(QFont("Arial", 10))
            q5Edit.textChanged.connect(self.q5Changed)
            lbl5.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl5, 5, 0)
            grid.addWidget(q5Edit, 5, 1)

            self.q7 = QLabel()
            lbl7 = QLabel('Line 2')
            q7Edit = QLineEdit('')
            q7Edit.setFixedWidth(320)
            q7Edit.setFont(QFont("Arial", 10))
            q7Edit.textChanged.connect(self.q7Changed)
            lbl7.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl7, 6, 0)
            grid.addWidget(q7Edit, 6, 1)

            self.q8 = QLabel()
            lbl8 = QLabel('Line 3')
            q8Edit = QLineEdit('')
            q8Edit.setFixedWidth(320)
            q8Edit.setFont(QFont("Arial", 10))
            q8Edit.textChanged.connect(self.q8Changed)
            lbl8.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl8, 7, 0)
            grid.addWidget(q8Edit, 7, 1)

            self.q9 = QLabel()
            lbl9 = QLabel('Line 4')
            q9Edit = QLineEdit('')
            q9Edit.setFixedWidth(320)
            q9Edit.setFont(QFont("Arial", 10))
            q9Edit.textChanged.connect(self.q9Changed)
            lbl9.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl9, 8, 0)
            grid.addWidget(q9Edit, 8, 1)

            self.q10 = QLabel()
            lbl10 = QLabel('Line 5')
            q10Edit = QLineEdit('')
            q10Edit.setFixedWidth(320)
            q10Edit.setFont(QFont("Arial", 10))
            q10Edit.textChanged.connect(self.q10Changed)
            lbl10.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl10, 9, 0)
            grid.addWidget(q10Edit, 9, 1)

            self.q20 = QLabel()
            lbl20 = QLabel('Line 6')
            q20Edit = QLineEdit('')
            q20Edit.setFixedWidth(320)
            q20Edit.setFont(QFont("Arial", 10))
            q20Edit.textChanged.connect(self.q20Changed)
            lbl20.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl20, 10, 0)
            grid.addWidget(q20Edit, 10, 1)

            self.q21 = QLabel()
            lbl21 = QLabel('Line 7')
            q21Edit = QLineEdit('')
            q21Edit.setFixedWidth(320)
            q21Edit.setFont(QFont("Arial", 10))
            q21Edit.textChanged.connect(self.q21Changed)
            lbl21.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl21, 11, 0)
            grid.addWidget(q21Edit, 11, 1)

            self.q22 = QLabel()
            lbl22 = QLabel('Line 8')
            q22Edit = QLineEdit('')
            q22Edit.setFixedWidth(320)
            q22Edit.setFont(QFont("Arial", 10))
            q22Edit.textChanged.connect(self.q22Changed)
            lbl22.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl22, 3, 2)
            grid.addWidget(q22Edit, 3, 3)

            self.q23 = QLabel()
            lbl23 = QLabel('Line 9')
            q23Edit = QLineEdit('')
            q23Edit.setFixedWidth(320)
            q23Edit.setFont(QFont("Arial", 10))
            q23Edit.textChanged.connect(self.q23Changed)
            lbl23.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl23, 4, 2)
            grid.addWidget(q23Edit, 4, 3)

            self.q24 = QLabel()
            lbl24 = QLabel('Line 10')
            q24Edit = QLineEdit('')
            q24Edit.setFixedWidth(320)
            q24Edit.setFont(QFont("Arial", 10))
            q24Edit.textChanged.connect(self.q24Changed)
            lbl24.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl24, 5, 2)
            grid.addWidget(q24Edit, 5, 3)

            self.q25 = QLabel()
            lbl25 = QLabel('Line 11')
            q25Edit = QLineEdit('')
            q25Edit.setFixedWidth(320)
            q25Edit.setFont(QFont("Arial", 10))
            q25Edit.textChanged.connect(self.q25Changed)
            lbl25.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl25, 6, 2)
            grid.addWidget(q25Edit, 6, 3)

            self.q26 = QLabel()
            lbl26 = QLabel('Line 12')
            q26Edit = QLineEdit('')
            q26Edit.setFixedWidth(320)
            q26Edit.setFont(QFont("Arial", 10))
            q26Edit.textChanged.connect(self.q26Changed)
            lbl26.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl26, 7, 2)
            grid.addWidget(q26Edit, 7, 3)

            self.q27 = QLabel()
            lbl27 = QLabel('Line 13')
            q27Edit = QLineEdit('')
            q27Edit.setFixedWidth(320)
            q27Edit.setFont(QFont("Arial", 10))
            q27Edit.textChanged.connect(self.q27Changed)
            lbl27.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl27, 8, 2)
            grid.addWidget(q27Edit, 8, 3)

            self.q28 = QLabel()
            lbl28 = QLabel('Line 14')
            q28Edit = QLineEdit('')
            q28Edit.setFixedWidth(320)
            q28Edit.setFont(QFont("Arial", 10))
            q28Edit.textChanged.connect(self.q28Changed)
            lbl28.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl28, 9, 2)
            grid.addWidget(q28Edit, 9, 3)

            self.q29 = QLabel()
            lbl29 = QLabel('Line 15')
            q29Edit = QLineEdit('')
            q29Edit.setFixedWidth(320)
            q29Edit.setFont(QFont("Arial", 10))
            q29Edit.textChanged.connect(self.q29Changed)
            lbl29.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl29, 10, 2)
            grid.addWidget(q29Edit, 10, 3)

            pyqt = QLabel()
            movie = QMovie('./images/logos/pyqt.gif')
            pyqt.setMovie(movie)
            movie.setScaledSize(QSize(240, 80))
            movie.start()
            grid.addWidget(pyqt, 0, 0, 1, 2)

            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo, 0, 3, 1, 1, Qt.AlignRight)

            grid.addWidget(QLabel('Insert Structure Menus of Clusters from '+sector+' Works'), 0, 1, 1, 4, Qt.AlignCenter)
            logger.info("__init__()=: save operation took %s ms", int((time.time() - __log_start) * 1000))

            applyBtn = QPushButton('Insert')
            applyBtn.clicked.connect(self.accept)

            grid.addWidget(applyBtn, 21, 3, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial", 10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")

            closeBtn = QPushButton('Close')
            closeBtn.clicked.connect(lambda: closeInsert(sector, m_email, self))

            grid.addWidget(closeBtn, 21, 3, 1, 1, Qt.AlignCenter)
            closeBtn.setFont(QFont("Arial", 10))
            closeBtn.setFixedWidth(100)
            closeBtn.setStyleSheet("color: black;  background-color: gainsboro")

            grid.addWidget(QLabel('                         \u00A9 2017 all rights reserved dj.jansen@casema.nl'), 22, 1, 1, 3)

            self.setLayout(grid)
            self.setGeometry(400, 50, 150, 150)
            logger.debug("<<< Exiting __init__()")


        def q2Changed(self, text):
            self.q2.setText(text)

        def q3Changed(self, text):
            self.q3.setText(text)

        def q4Changed(self, text):
            self.q4.setText(text)

        def q5Changed(self, text):
            self.q5.setText(text)

        def q7Changed(self, text):
            self.q7.setText(text)

        def q8Changed(self, text):
            self.q8.setText(text)

        def q9Changed(self, text):
            self.q9.setText(text)

        def q10Changed(self, text):
            self.q10.setText(text)

        def q20Changed(self, text):
            self.q20.setText(text)

        def q21Changed(self, text):
            self.q21.setText(text)

        def q22Changed(self, text):
            self.q22.setText(text)

        def q23Changed(self, text):
            self.q23.setText(text)

        def q24Changed(self, text):
            self.q24.setText(text)

        def q25Changed(self, text):
            self.q25.setText(text)

        def q26Changed(self, text):
            self.q26.setText(text)

        def q27Changed(self, text):
            self.q27.setText(text)

        def q28Changed(self, text):
            self.q28.setText(text)

        def q29Changed(self, text):
            self.q29.setText(text)

        def returnq2(self):
            return self.q2.text()

        def returnq3(self):
            return self.q3.text()

        def returnq4(self):
            return self.q4.text()

        def returnq5(self):
            return self.q5.text()

        def returnq7(self):
            return self.q7.text()

        def returnq8(self):
            return self.q8.text()

        def returnq9(self):
            return self.q9.text()

        def returnq10(self):
            return self.q10.text()

        def returnq20(self):
            return self.q20.text()

        def returnq21(self):
            return self.q21.text()

        def returnq22(self):
            return self.q22.text()

        def returnq23(self):
            return self.q23.text()

        def returnq24(self):
            return self.q24.text()

        def returnq25(self):
            return self.q25.text()

        def returnq26(self):
            return self.q26.text()

        def returnq27(self):
            return self.q27.text()

        def returnq28(self):
            return self.q28.text()

        def returnq29(self):
            return self.q29.text()

        @staticmethod
        def getData(parent=None):
            dialog = insWindow()
            dialog.exec_()
            return [dialog.returnq2(), dialog.returnq3(), dialog.returnq4(), dialog.returnq5(), dialog.returnq7(),\
                    dialog.returnq8(), dialog.returnq9(), dialog.returnq10(), dialog.returnq20(), dialog.returnq21(),\
                    dialog.returnq22(), dialog.returnq23(), dialog.returnq24(), dialog.returnq25(), dialog.returnq26(),\
                    dialog.returnq27(), dialog.returnq28(), dialog.returnq29()]

    insWin = insWindow()
    data = insWin.getData()

    if data[0]:
        q2 = data[0]
    else:
        insertReq()
        insertStruct(sector, m_email)
    if data[1]:
        q3 =data[1]
    else:
        insertReq()
        insertStruct(sector, m_email)
    if data[2]:
        q4 = data[2]
    else:
        insertReq()
        insertStruct(sector, m_email)
    if data[3]:
        q5 = data[3]
    else:
        insertReq()
        insertStruct(sector, m_email)
    if data[4]:
        q7 = data[4]
    else:
        insertReq()
        insertStruct(sector, m_email)
    if data[5]:
        q8 = data[5]
    else:
        insertReq()
        insertStruct(sector, m_email)
    if data[6]:
        q9 = data[6]
    else:
        insertReq()
        insertStruct(sector, m_email)
    if data[7]:
        q10 = data[7]
    else:
        insertReq()
        insertStruct(sector, m_email)
    if data[8]:
        q20 = data[8]
    else:
        insertReq()
        insertStruct(sector, m_email)
    if data[9]:
        q21 = data[9]
    else:
        insertReq()
        insertStruct(sector, m_email)
    if data[10]:
        q22 = data[10]
    else:
        insertReq()
        insertStruct(sector, m_email)
    if data[11]:
        q23 = data[11]
    else:
        insertReq()
        insertStruct(sector, m_email)
    if data[12]:
        q24 = data[12]
    else:
        insertReq()
        insertStruct(sector, m_email)
    if data[13]:
        q25 = data[13]
    else:
        insertReq()
        insertStruct(sector, m_email)
    if data[14]:
        q26 = data[14]
    else:
        insertReq()
        insertStruct(sector, m_email)
    if data[15]:
        q27 = data[15]
    else:
        insertReq()
        insertStruct(sector, m_email)
    if data[16]:
        q28 = data[16]
    else:
        insertReq()
        insertStruct(sector, m_email)
    if data[17]:
        q29 = data[17]
    else:
        insertReq()
        insertStruct(sector, m_email)

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    try:
        if sector == 'external':
            instruct = insert(cluster_structure_external).values(structID = structnr, overall_heading=q2, heading_level1=q3,\
                            line_level0=q4, line1=q5, line2=q7, line3=q8, line4=q9, line5=q10, line6=q20, line7=q21,\
                            line8=q22, line9=q23, line10=q24, line11=q25, line12=q26, line13=q27, line14=q28, line15=q29)
            con.execute(instruct)
            insertOK()
            insertStruct(sector, m_email)
        else:
            instruct = insert(cluster_structure_internal).values(structID = structnr, overall_heading=q2, heading_level1=q3,\
                            line_level0=q4, line1=q5, line2=q7, line3=q8, line4=q9, line5=q10, line6=q20, line7=q21,\
                            line8=q22, line9=q23, line10=q24, line11=q25, line12=q26, line13=q27, line14=q28, line15=q29)
            con.execute(instruct)
            insertOK()
            insertStruct(sector, m_email)
    except Exception as e:
        errorInsert(str(e))
        insertStruct(sector, m_email)