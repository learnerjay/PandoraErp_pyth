from login import hoofdMenu
import datetime
from PyQt5.QtCore import Qt, QAbstractTableModel, QRegExp, QSize
from PyQt5.QtGui import QFont, QPixmap, QRegExpValidator, QIcon, QMovie, QColor
from PyQt5.QtWidgets import QWidget, QTableView, QDialog, QLabel, QGridLayout, QPushButton, QMessageBox, QLineEdit, QComboBox
from sqlalchemy import (Table, Column, Integer, String, Boolean, MetaData, create_engine, select, update, insert, func)
import logging
logger = logging.getLogger(__name__)

def insertReq():
    logger.debug(">>> Entering insertReq()")
    msg = QMessageBox()
    logger.debug("insertReq(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Insert data is required!')
    msg.setWindowTitle('Insert parameters')
    logger.debug("<<< Exiting insertReq()")
    msg.exec_()

def insertOK():
    logger.debug(">>> Entering insertOK()")
    msg = QMessageBox()
    logger.debug("insertOK(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Inserting data was successful!')
    msg.setWindowTitle('Insert parameters')
    logger.debug("<<< Exiting insertOK()")
    msg.exec_()

def errorInsert(message):
    logger.debug(">>> Entering errorInsert(message=%s)", message)
    msg = QMessageBox()
    logger.debug("errorInsert(message=%s): msg → %s", message, msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Critical)
    msg.setText('An error has occurred!\n'+message)
    msg.setWindowTitle('Insert parameters')
    logger.debug("<<< Exiting errorInsert(message=%s)", message)
    msg.exec_()

def closeInsert(m_email, auth_1, auth_2, auth_3, self):
    logger.debug(">>> Entering closeInsert(m_email=%s,auth_1=%s,auth_2=%s,auth_3=%s)", m_email, auth_1, auth_2, auth_3)
    self.close()
    chooseSubMenu(m_email, auth_1, auth_2, auth_3)
    logger.debug("<<< Exiting closeInsert(m_email=%s,auth_1=%s,auth_2=%s,auth_3=%s)", m_email, auth_1, auth_2, auth_3)

def noChange(message):
    logger.debug(">>> Entering noChange(message=%s)", message)
    msg = QMessageBox()
    logger.debug("noChange(message=%s): msg → %s", message, msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Critical)
    msg.setText("An critical error has occurred: \n"+message)
    msg.setWindowTitle('Modify parameters')
    logger.debug("<<< Exiting noChange(message=%s)", message)
    msg.exec_()

def changeOK():
    logger.debug(">>> Entering changeOK()")
    msg = QMessageBox()
    logger.debug("changeOK(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Changes successful!')
    msg.setWindowTitle('Modify parameters')
    logger.debug("<<< Exiting changeOK()")
    msg.exec_()

def refresh(m_email, auth_1, auth_2, auth_3, data, self):
    logger.debug(">>> Entering refresh(m_email=%s,auth_1=%s,auth_2=%s,auth_3=%s,data=%s)", m_email, auth_1, auth_2, auth_3, data)
    self.close()
    showParams(m_email, auth_1, auth_2, auth_3, data)
    logger.debug("<<< Exiting refresh(m_email=%s,auth_1=%s,auth_2=%s,auth_3=%s,data=%s)", m_email, auth_1, auth_2, auth_3, data)

def closeSubmenu(m_email, self):
    logger.debug(">>> Entering closeSubmenu(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting closeSubmenu(m_email=%s)", m_email)

def chooseSubMenu(m_email, auth_1, auth_2, auth_3):
    logger.debug(">>> Entering chooseSubMenu(m_email=%s,auth_1=%s,auth_2=%s,auth_3=%s)", m_email, auth_1, auth_2, auth_3)
    # structure Menu's
    class Widget(QDialog):
        logger.debug("<<< Exiting chooseSubMenu(m_email=%s,auth_1=%s,auth_2=%s,auth_3=%s)", m_email, auth_1, auth_2, auth_3)
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            self.setWindowTitle("Pandora ERP Periods")
            self.setWindowFlags(self.windowFlags() | Qt.WindowSystemMenuHint | Qt.WindowMinMaxButtonsHint)
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setFont(QFont('Arial', 10))
            self.setStyleSheet("background-color: #D9E1DF")

            self.k0Edit = QComboBox()
            logger.debug("__init__(parent=%s): self.k0Edit → %s", parent, self.k0Edit)
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit)
            self.k0Edit.setFixedWidth(310)
            self.k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            self.k0Edit.setFont(QFont("Arial", 10))
            self.k0Edit.setEditable(True)
            self.k0Edit.lineEdit().setFont(QFont("Arial",10))
            self.k0Edit.addItem('Submenu Parameters Periods')
            self.k0Edit.lineEdit().setReadOnly(True)
            self.k0Edit.lineEdit().setAlignment(Qt.AlignCenter)
            self.k0Edit.setItemData(0, Qt.AlignCenter, Qt.TextAlignmentRole)
            self.k0Edit.addItem('1. View params Periods')
            self.k0Edit.addItem('2. Modify params Periods')
            self.k0Edit.addItem('3. Insert new params Periods')
            logger.debug("<<< Exiting __init__(parent=%s)", parent)

            def k0Changed():
                logger.debug(">>> Entering k0Changed()")
                logger.debug("k0Changed(): k0Edit → %s", k0Edit)
                self.k0Edit.setCurrentIndex(self.k0Edit.currentIndex())
                logger.debug("<<< Exiting k0Changed()")
                self.accept()
            self.k0Edit.currentIndexChanged.connect(k0Changed)

            grid = QGridLayout()
            grid.setSpacing(20)

            lblinfo = QLabel('Parameters Periods.')
            grid.addWidget(lblinfo, 1, 0, 1, 2, Qt.AlignCenter)

            grid.addWidget(self.k0Edit, 2, 0, 1, 2, Qt.AlignCenter)

            pyqt = QLabel()
            movie = QMovie('./images/logos/pyqt.gif')
            pyqt.setMovie(movie)
            movie.setScaledSize(QSize(240, 80))
            movie.start()
            grid.addWidget(pyqt, 0, 0)

            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo, 0, 1, 1, 2, Qt.AlignRight)

            if auth_1 == 0:
                self.k0Edit.model().item(1).setEnabled(False)
                self.k0Edit.model().item(1).setForeground(QColor('darkgrey'))
                self.k0Edit.model().item(1).setBackground(QColor('gainsboro'))

            if auth_2 == 0:
                self.k0Edit.model().item(2).setEnabled(False)
                self.k0Edit.model().item(2).setForeground(QColor('darkgrey'))
                self.k0Edit.model().item(2).setBackground(QColor('gainsboro'))

            if auth_3 == 0:
                self.k0Edit.model().item(3).setEnabled(False)
                self.k0Edit.model().item(3).setForeground(QColor('darkgrey'))
                self.k0Edit.model().item(3).setBackground(QColor('gainsboro'))

            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1, 2, Qt.AlignCenter)

            self.setLayout(grid)
            self.setGeometry(600, 100, 150, 150)

            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: closeSubmenu(m_email, self))

            grid.addWidget(cancelBtn, 3, 0, 1, 2, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial", 10))
            cancelBtn.setFixedWidth(130)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")

        logger.debug(">>> Entering __init__(data_list=%s,header=%s)", data_list, header)
        logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font)
        logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view)
        logger.debug("__init__(data_list=%s,header=%s): grid → %s", data_list, header, grid)
        logger.debug("__init__(self=%s,data_list=%s,header=%s): grid → %s", self, data_list, header, grid)
        logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model)
        logger.debug("__init__(self=%s,data_list=%s,header=%s): table_model → %s", self, data_list, header, table_model)
        logger.debug("__init__(self=%s,data_list=%s,header=%s): table_view → %s", self, data_list, header, table_view)
        logger.debug("__init__(self=%s,data_list=%s,header=%s): font → %s", self, data_list, header, font)
        logger.debug("__init__(data_list=%s,header=%s): pixmap → %s", data_list, header, pixmap)
        logger.debug("__init__(data_list=%s,header=%s): lbl → %s", data_list, header, lbl)
        logger.debug("__init__(self=%s,data_list=%s,header=%s): lbl → %s", self, data_list, header, lbl)
        logger.debug("__init__(self=%s,data_list=%s,header=%s): pixmap → %s", self, data_list, header, pixmap)
        logger.debug("__init__(data_list=%s,header=%s): logo → %s", data_list, header, logo)
        logger.debug("__init__(self=%s,data_list=%s,header=%s): logo → %s", self, data_list, header, logo)
        logger.debug("__init__(data_list=%s,header=%s): freshBtn → %s", data_list, header, freshBtn)
        logger.debug("__init__(self=%s,data_list=%s,header=%s): freshBtn → %s", self, data_list, header, freshBtn)
        logger.debug("__init__(data_list=%s,header=%s): closeBtn → %s", data_list, header, closeBtn)
        logger.debug("__init__(self=%s,data_list=%s,header=%s): closeBtn → %s", self, data_list, header, closeBtn)
        logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header)
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            logger.debug(">>> Entering getData(parent=%s)", parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            logger.debug("<<< Exiting getData(parent=%s)", parent)
            return [dialog.k0Edit.currentIndex(), ]

    window = Widget()
    data = window.getData()

    if data[0] == 1 :
        showParams(m_email, auth_1, auth_2, auth_3, data)
    if data[0] == 2:
        showParams(m_email, auth_1, auth_2, auth_3, data)
    if data[0] == 3:
        insertParams(m_email, auth_1, auth_2, auth_3, data)
    chooseSubMenu(m_email, auth_1, auth_2, auth_3)

def showParams(m_email, auth_1, auth_2, auth_3, data):
    logger.debug(">>> Entering showParams(m_email=%s,auth_1=%s,auth_2=%s,auth_3=%s,data=%s)", m_email, auth_1, auth_2, auth_3, data)
    class MyWindow(QDialog):
        logger.error("Exception in showParams(m_email=%s,auth_1=%s,auth_2=%s,auth_3=%s,data=%s)", m_email, auth_1, auth_2, auth_3, data, exc_info=True)
        def __init__(self, data_list, header, *args):
            logger.debug(">>> Entering __init__(data_list=%s,header=%s)", data_list, header)
            QWidget.__init__(self, *args, )
            self.setWindowTitle('View / Change parameters Periods')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags() | Qt.WindowSystemMenuHint |
                                Qt.WindowMinMaxButtonsHint)

            self.setFont(QFont('Arial', 10))

            grid = QGridLayout()
            grid.setSpacing(20)

            table_model = MyTableModel(self, data_list, header)
            table_view = QTableView()
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            # table_view.clicked.connect(selectRow)
            if auth_2 == 1 and data[0] == 2:
                table_view.clicked.connect(showSelection)
            grid.addWidget(table_view, 0, 0, 1, 7)

            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 1, 0, 1, 2)

            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo, 1, 6, 1, 1, Qt.AlignRight)

            freshBtn = QPushButton('Refresh')
            freshBtn.clicked.connect(lambda: refresh(m_email, auth_1, auth_2, auth_3, data, self))

            freshBtn.setFont(QFont("Arial", 10))
            freshBtn.setFixedWidth(100)
            freshBtn.setStyleSheet("color: black;  background-color: gainsboro")

            grid.addWidget(freshBtn, 1, 5, 1, 1, Qt.AlignRight | Qt.AlignBottom)

            closeBtn = QPushButton('Close')
            closeBtn.clicked.connect(self.close)

            closeBtn.setFont(QFont("Arial", 10))
            closeBtn.setFixedWidth(100)
            closeBtn.setStyleSheet("color: black;  background-color: gainsboro")

            grid.addWidget(closeBtn, 1, 4, 1, 1, Qt.AlignRight | Qt.AlignBottom)

            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 1, 2, 1, 1, Qt.AlignBottom)

            self.setLayout(grid)
            self.setGeometry(300, 50, 900, 900)
            self.setLayout(grid)
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
            logger.debug(">>> Entering __init__()")
            logger.debug("__init__(): grid → %s", grid)
            logger.debug("__init__(self=%s): grid → %s", self, grid)
            logger.debug("__init__(): input_validator → %s", input_validator)
            logger.debug("__init__(): q1Edit → %s", q1Edit)
            logger.debug("__init__(): self.Period → %s", self.Period)
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit)
            logger.debug("__init__(): reg_ex → %s", reg_ex)
            logger.debug("__init__(self=%s): reg_ex → %s", self, reg_ex)
            logger.debug("__init__(self=%s): input_validator → %s", self, input_validator)
            logger.debug("__init__(): q2Edit → %s", q2Edit)
            logger.debug("__init__(): self.Hours → %s", self.Hours)
            logger.debug("__init__(self=%s): q2Edit → %s", self, q2Edit)
            logger.debug("__init__(): lblinfo → %s", lblinfo)
            logger.debug("__init__(self=%s): lblinfo → %s", self, lblinfo)
            logger.debug("__init__(): lbl1 → %s", lbl1)
            logger.debug("__init__(self=%s): lbl1 → %s", self, lbl1)
            logger.debug("__init__(): lbl2 → %s", lbl2)
            logger.debug("__init__(self=%s): lbl2 → %s", self, lbl2)
            logger.debug("__init__(): lbl3 → %s", lbl3)
            logger.debug("__init__(self=%s): lbl3 → %s", self, lbl3)
            logger.debug("__init__(): lbl4 → %s", lbl4)
            logger.debug("__init__(self=%s): lbl4 → %s", self, lbl4)
            logger.debug("__init__(): lbl5 → %s", lbl5)
            logger.debug("__init__(self=%s): lbl5 → %s", self, lbl5)
            logger.debug("__init__(): lbl0 → %s", lbl0)
            logger.debug("__init__(self=%s): lbl0 → %s", self, lbl0)
            logger.debug("__init__(): lbl7 → %s", lbl7)
            logger.debug("__init__(): lbl6 → %s", lbl6)
            logger.debug("__init__(self=%s): lbl6 → %s", self, lbl6)
            logger.debug("__init__(self=%s): lbl7 → %s", self, lbl7)
            logger.debug("__init__(): lbl8 → %s", lbl8)
            logger.debug("__init__(self=%s): lbl8 → %s", self, lbl8)
            logger.debug("__init__(): lbl9 → %s", lbl9)
            logger.debug("__init__(self=%s): lbl9 → %s", self, lbl9)
            logger.debug("__init__(): movie → %s", movie)
            logger.debug("__init__(): pyqt → %s", pyqt)
            logger.debug("__init__(self=%s): pyqt → %s", self, pyqt)
            logger.debug("__init__(self=%s): movie → %s", self, movie)
            logger.debug("__init__(): pixmap → %s", pixmap)
            logger.debug("__init__(): logo → %s", logo)
            logger.debug("__init__(self=%s): logo → %s", self, logo)
            logger.debug("__init__(self=%s): pixmap → %s", self, pixmap)
            logger.debug("__init__(): applyBtn → %s", applyBtn)
            logger.debug("__init__(self=%s): applyBtn → %s", self, applyBtn)
            logger.debug("__init__(): cancelBtn → %s", cancelBtn)
            logger.debug("__init__(self=%s): cancelBtn → %s", self, cancelBtn)
            logger.debug("<<< Exiting __init__()")

        def rowCount(self, parent):
            logger.debug(">>> Entering rowCount(parent=%s)", parent)
            logger.debug("<<< Exiting rowCount(parent=%s)", parent)
            return len(self.mylist)

        def columnCount(self, parent):
            logger.debug(">>> Entering columnCount(parent=%s)", parent)
            logger.debug("<<< Exiting columnCount(parent=%s)", parent)
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

    header = ['periodID', 'Working Period', 'Working hours per Period', 'Period Size', 'Lock Processed', 'Date']

    metadata = MetaData()
    params_periods = Table('params_periods', metadata,
       Column('periodID', Integer(), primary_key=True),
       Column('working_period', String),
       Column('working_hours_per_period', Integer),
       Column('period_size', String),
       Column('lock_processed', Boolean),
       Column('date', String))

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()

    sel = select([params_periods]).order_by(params_periods.c.periodID.asc())

    rp = con.execute(sel)

    data_list = []
    for row in rp:
        data_list += [(row)]

    def showSelection(idx):
        logger.debug(">>> Entering showSelection(idx=%s)", idx)
        periodsnr = idx.data()
        logger.debug("showSelection(idx=%s): periodsnr → %s", idx, periodsnr)
        if idx.column() == 0:
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showSelection(idx=%s): engine → %s", idx, engine)
            con = engine.connect()
            selpar = select([params_periods]).where(params_periods.c.periodID == periodsnr)
            logger.debug("showSelection(idx=%s): con → %s", idx, con)
            rppar = con.execute(selpar).first()
            class paramWindow(QDialog):
                logger.debug("showSelection(idx=%s): selpar → %s", idx, selpar)
                def __init__(self):
                    logger.debug("<<< Exiting showSelection(idx=%s)", idx)
                    QDialog.__init__(self)
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                    self.setWindowFlags(self.windowFlags() | Qt.WindowSystemMenuHint |
                                        Qt.WindowMinMaxButtonsHint)

                    grid = QGridLayout()
                    grid.setSpacing(20)

                    self.setWindowTitle("Pandora Enterprise Resource Planning")
                    self.setFont(QFont('Arial', 10))

                    self.Period = QLabel()
                    q1Edit = QLineEdit(rppar[1])
                    q1Edit.setCursorPosition(0)
                    q1Edit.setFixedWidth(300)
                    q1Edit.setFont(QFont("Arial", 10))
                    q1Edit.textChanged.connect(self.q1Changed)
                    reg_ex = QRegExp("^([12][0-9]{3})([-]{1})(0[1-9]|1[0-2])--|$")
                    input_validator = QRegExpValidator(reg_ex, q1Edit)
                    q1Edit.setValidator(input_validator)

                    self.Hours = QLabel()
                    q2Edit = QLineEdit(str(int(rppar[2])))
                    q2Edit.setFixedWidth(100)
                    q1Edit.setCursorPosition(0)
                    q2Edit.setFont(QFont("Arial", 10))
                    q2Edit.textChanged.connect(self.q2Changed)
                    reg_ex = QRegExp("^([1-9]{1}[0-9]{0,7})+$")
                    input_validator = QRegExpValidator(reg_ex, q2Edit)
                    q2Edit.setValidator(input_validator)

                    grid = QGridLayout()
                    grid.setSpacing(20)

                    lblinfo = QLabel('Modify Parameters Periods.')
                    grid.addWidget(lblinfo, 1, 0, 1, 3, Qt.AlignCenter)

                    lbl1 = QLabel('Periods ID')
                    grid.addWidget(lbl1, 2, 0)
                    lbl2 = QLabel(str(periodsnr))
                    grid.addWidget(lbl2, 2, 1)

                    lbl3 = QLabel('Period Size (YYYY-MM)')
                    grid.addWidget(lbl3, 3, 0)
                    grid.addWidget(q1Edit, 3, 1, 1, 2)

                    lbl4 = QLabel('Working Hours per Period')
                    grid.addWidget(lbl4, 4, 0)
                    grid.addWidget(q2Edit, 4, 1)

                    lbl5 = QLabel('Period Size')
                    grid.addWidget(lbl5, 5, 0)
                    lbl0 = QLabel('monthly')
                    grid.addWidget(lbl0, 5, 1, 1, 2)

                    lbl6 = QLabel('Lock Processed')
                    lbl7 = QLabel(str(rppar[4]))
                    grid.addWidget(lbl6, 6, 0)
                    grid.addWidget(lbl7, 6, 1, 1, 2)

                    lbl8 = QLabel('Modification Date')
                    grid.addWidget(lbl8, 7,0)
                    lbl9 = QLabel(rppar[5])
                    grid.addWidget(lbl9, 7, 1, 1, 2)

                    pyqt = QLabel()
                    movie = QMovie('./images/logos/pyqt.gif')
                    pyqt.setMovie(movie)
                    movie.setScaledSize(QSize(240, 80))
                    movie.start()
                    grid.addWidget(pyqt, 0, 0, 1, 2)

                    logo = QLabel()
                    pixmap = QPixmap('./images/logos/logo.jpg')
                    logo.setPixmap(pixmap)
                    grid.addWidget(logo, 0, 2, 1, 1, Qt.AlignRight)

                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 9, 0, 1, 3,
                                   Qt.AlignCenter)

                    self.setLayout(grid)
                    self.setGeometry(500, 300, 150, 150)

                    applyBtn = QPushButton('Modify')
                    applyBtn.clicked.connect(self.accept)

                    grid.addWidget(applyBtn, 8, 2, 1, 1, Qt.AlignRight)
                    applyBtn.setFont(QFont("Arial", 10))
                    applyBtn.setFixedWidth(130)
                    applyBtn.setStyleSheet("color: black;  background-color: gainsboro")

                    cancelBtn = QPushButton('Close')
                    cancelBtn.clicked.connect(self.close)

                    grid.addWidget(cancelBtn, 8, 1, Qt.AlignRight)
                    cancelBtn.setFont(QFont("Arial", 10))
                    cancelBtn.setFixedWidth(130)
                    cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")

                def q1Changed(self, text):
                    logger.debug(">>> Entering q1Changed(text=%s)", text)
                    logger.debug("q1Changed(self=%s,text=%s): Period → %s", self, text, Period)
                    self.Period.setText(text)
                    logger.debug("<<< Exiting q1Changed(text=%s)", text)

                def q2Changed(self, text):
                    logger.debug(">>> Entering q2Changed(text=%s)", text)
                    logger.debug("q2Changed(self=%s,text=%s): Hours → %s", self, text, Hours)
                    self.Hours.setText(text)
                    logger.debug("<<< Exiting q2Changed(text=%s)", text)

                def returnq1(self):
                    logger.debug(">>> Entering returnq1()")
                    logger.debug("<<< Exiting returnq1()")
                    return self.Period.text()

                def returnq2(self):
                    logger.debug(">>> Entering returnq2()")
                    logger.debug("<<< Exiting returnq2()")
                    return self.Hours.text()

                @staticmethod
                def getData(parent=None):
                    logger.debug(">>> Entering getData(parent=%s)", parent)
                    dialog = paramWindow()
                    dialog.exec_()
                    return [dialog.returnq1(), dialog.returnq2()]

            paramWin = paramWindow()
            data = paramWin.getData()

            changeflag = 0
            for k in range(0,2):
                if data[k]:
                    changeflag = 1
            if changeflag == 0:
                return

            if data[0]:
                mf0 = data[0]
            else:
                mf0 = rppar[1]
            if data[1]:
                mf1 = str(data[1])
            else:
                mf1 = rppar[2]

            dt = str(datetime.datetime.now())[0:10]

            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            con = engine.connect()
            try:
                updpar = update(params_periods).where(params_periods.c.periodID == periodsnr).values(working_period = mf0,
                                      working_hours_per_period = mf1, date = dt)
                con.execute(updpar)
                changeOK()
            except Exception as e:
                noChange(str(e))

    win = MyWindow(data_list, header)
    win.exec_()

def insertParams(m_email, auth_1, auth_2, auth_3, data):
    logger.debug(">>> Entering insertParams(m_email=%s,auth_1=%s,auth_2=%s,auth_3=%s,data=%s)", m_email, auth_1, auth_2, auth_3, data)
    metadata = MetaData()
    logger.debug("insertParams(m_email=%s,auth_1=%s,auth_2=%s,auth_3=%s,data=%s): metadata → %s", m_email, auth_1, auth_2, auth_3, data, metadata)
    params_periods = Table('params_periods', metadata,
       Column('periodID', Integer(), primary_key=True),
       Column('working_period', String),
       Column('working_hours_per_period', Integer),
       Column('period_size', String),
       Column('lock_processed', Boolean),
       Column('date', String))

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("insertParams(m_email=%s,auth_1=%s,auth_2=%s,auth_3=%s,data=%s): engine → %s", m_email, auth_1, auth_2, auth_3, data, engine)
    con = engine.connect()
    try:
       logger.debug("insertParams(m_email=%s,auth_1=%s,auth_2=%s,auth_3=%s,data=%s): con → %s", m_email, auth_1, auth_2, auth_3, data, con)
       periodsnr = (con.execute(select([func.max(params_periods.c.periodID, \
                                               type_=Integer)])).scalar())
       periodsnr += 1
       logger.debug("insertParams(m_email=%s,auth_1=%s,auth_2=%s,auth_3=%s,data=%s): periodsnr → %s", m_email, auth_1, auth_2, auth_3, data, periodsnr)
       logger.debug("insertParams(m_email=%s,auth_1=%s,auth_2=%s,auth_3=%s,data=%s): type_ → %s", m_email, auth_1, auth_2, auth_3, data, type_)
    except:
       periodsnr = 1

    class parWindow(QDialog):
        logger.debug("<<< Exiting insertParams(m_email=%s,auth_1=%s,auth_2=%s,auth_3=%s,data=%s)", m_email, auth_1, auth_2, auth_3, data)
        def __init__(self):
            QDialog.__init__(self)
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags() | Qt.WindowSystemMenuHint |
                                Qt.WindowMinMaxButtonsHint)

            grid = QGridLayout()
            grid.setSpacing(20)

            self.setWindowTitle("Pandora Enterprise Resource Planning")
            self.setFont(QFont('Arial', 10))

            dt = str(datetime.datetime.now())[0:10]

            self.Period = QLabel()
            q1Edit = QLineEdit('')
            q1Edit.setCursorPosition(0)
            q1Edit.setFixedWidth(100)
            q1Edit.setFont(QFont("Arial", 10))
            q1Edit.textChanged.connect(self.q1Changed)
            reg_ex = QRegExp("^([12][0-9]{3})([-]{1})(0[1-9]|1[0-2])--|$")

            input_validator = QRegExpValidator(reg_ex, q1Edit)
            q1Edit.setValidator(input_validator)

            self.Hours = QLabel()
            q2Edit = QLineEdit('')
            q2Edit.setFixedWidth(100)
            q2Edit.setCursorPosition(0)
            q2Edit.setFont(QFont("Arial", 10))
            q2Edit.textChanged.connect(self.q2Changed)
            reg_ex = QRegExp("^([1-9]{1}[0-9]{0,7})+$")
            input_validator = QRegExpValidator(reg_ex, q2Edit)
            q2Edit.setValidator(input_validator)

            lblinfo = QLabel('Insert Parameters Periods.')
            grid.addWidget(lblinfo, 1, 0, 1, 3, Qt.AlignCenter)

            lbl1 = QLabel('Periods ID')
            grid.addWidget(lbl1, 2, 0)
            lbl2 = QLabel(str(periodsnr))
            grid.addWidget(lbl2, 2, 1)

            lbl3 = QLabel('Period Wages')
            grid.addWidget(lbl3, 3, 0)
            grid.addWidget(q1Edit, 3, 1, 1, 2)

            lbl4 = QLabel('Working Hours per  Period')
            grid.addWidget(lbl4, 4, 0)
            grid.addWidget(q2Edit, 4, 1)

            lbl5 = QLabel('Period Size (YYYY-MM)')
            lbl0 = QLabel('monthly')
            grid.addWidget(lbl5, 5, 0)
            grid.addWidget(lbl0, 5, 1, 1, 2)

            lbl6 = QLabel('Lock Processed')
            lbl7 = QLabel(str('False'))
            grid.addWidget(lbl6, 6, 0)
            grid.addWidget(lbl7, 6, 1, 1, 2)

            lbl8 = QLabel('Modification Date')
            grid.addWidget(lbl8,7, 0)
            lbl9 = QLabel(dt)
            grid.addWidget(lbl9, 7, 1, 1, 2)

            pyqt = QLabel()
            movie = QMovie('./images/logos/pyqt.gif')
            pyqt.setMovie(movie)
            movie.setScaledSize(QSize(240, 80))
            movie.start()
            grid.addWidget(pyqt, 0, 0, 1, 2)

            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo, 0, 2, 1, 1, Qt.AlignRight)

            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 9, 0, 1, 3,
                           Qt.AlignCenter)

            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)

            applyBtn = QPushButton('Insert')
            applyBtn.clicked.connect(self.accept)

            grid.addWidget(applyBtn, 8, 2, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial", 10))
            applyBtn.setFixedWidth(130)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")

            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: closeInsert(m_email, auth_1, auth_2, auth_3, self))

            grid.addWidget(cancelBtn, 8, 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial", 10))
            cancelBtn.setFixedWidth(130)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")

        def q1Changed(self, text):
            self.Period.setText(text)

        def q2Changed(self, text):
            self.Hours.setText(text)

        def returnq1(self):
            return self.Period.text()

        def returnq2(self):
            return self.Hours.text()

        @staticmethod
        def getData(parent=None):
            dialog = parWindow()
            dialog.exec_()
            return [dialog.returnq1(), dialog.returnq2()]

    parWin = parWindow()
    data = parWin.getData()
    if data[0]:
        mf0 = data[0]
    else:
        insertReq()
        insertParams(m_email, auth_1, auth_2, auth_3, data)
    if data[1]:
        mf1 = int(data[1])
    else:
        insertReq()
        insertParams(m_email, auth_1, auth_2, auth_3, data)

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    try:
        inspar = insert(params_periods).values(periodID = periodsnr, working_period = mf0, working_hours_per_period = mf1)
        con.execute(inspar)
        insertOK()
        insertParams(m_email, auth_1, auth_2, auth_3, data)
    except Exception as e:
        errorInsert(str(e))
        insertParams(m_email, auth_1, auth_2, auth_3, data)




