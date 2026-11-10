
import sys
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import  QDialog, QTableView, QWidget, QVBoxLayout, QApplication
from sqlalchemy import create_engine, Table, Column, ForeignKey, Integer, String, Boolean, MetaData, select, and_
import logging
logger = logging.getLogger(__name__)

def zipcode():
    logger.warning(">>> Entering zipcode()", extra={"event.action": "zipcode"})
    metadata = MetaData()
    logger.debug("zipcode(): metadata → %s", metadata, extra={"event.action": "zipcode"})
    postcodes = Table('postcodes', metadata,
       Column('postcode', String),
       Column('soort', Boolean),
       Column('van', Integer),
       Column('tem', Integer),
       Column('straatID', None, ForeignKey('straat.straatID')))
    plaats = Table('plaats', MetaData(),
       Column('plaatsID', Integer, primary_key=True),
       Column('c_plaats', String))
    logger.debug("zipcode(): plaats → %s", plaats, extra={"event.action": "zipcode"})
    straat = Table('straat', MetaData(),
       Column('straatID', Integer, primary_key=True),
       Column('c_straat', String),
       Column('plaatsID', None, ForeignKey('plaats.plaatsID')))
    logger.debug("zipcode(): straat → %s", straat, extra={"event.action": "zipcode"})

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("zipcode(): engine → %s", engine, extra={"event.action": "zipcode"})
    con = engine.connect()
    logger.debug("zipcode(): con → %s", con, extra={"event.action": "zipcode"})
    selzip= select(postcodes.c.postcode, straat.c.c_straat,postcodes.c.van,postcodes.c.tem, plaats.c.c_plaats)\
        .where(and_(postcodes.c.straatID == straat.c.straatID, straat.c.plaatsID == plaats.c.plaatsID))
    logger.debug("zipcode(): selzip → %s", selzip, extra={"event.action": "zipcode"})
    rpzip = con.execute(selzip)

    logger.debug("zipcode(): rpzip → %s", rpzip, extra={"event.action": "zipcode"})
    class MyWindow(QDialog):
        logger.debug("<<< Exiting zipcode()", extra={"event.action": "zipcode"})
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args, )
            self.setGeometry(50, 50, 1500, 900)
            self.setWindowTitle('Request own sales company')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags() | Qt.WindowSystemMenuHint |
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
            table_view.setColumnWidth(0, 100)
            table_view.setColumnWidth(1, 300)
            table_view.setColumnWidth(4, 300)
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
            logger.debug("<<< Exiting rowCount(parent=%s)", parent, extra={"event.action": "rowCount"})
            return len(self.mylist)

        def columnCount(self, parent):
           logger.warning(">>> Entering columnCount(parent=%s)", parent, extra={"event.action": "columnCount"})
           logger.debug("<<< Exiting columnCount(parent=%s)", parent, extra={"event.action": "columnCount"})
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

    header = ['Zipcode', 'Streetname','Lowernr', 'Uppernr', 'Residence']

    data_list = []
    for row in rpzip:
        data_list += [row]

    win = MyWindow(data_list, header)
    win.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Windows")
    zipcode()
    app.exec_()
    sys.exit()