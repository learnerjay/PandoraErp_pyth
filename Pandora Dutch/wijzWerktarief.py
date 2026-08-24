from login import hoofdMenu
import  datetime
from PyQt5.QtWidgets import QMessageBox, QDialog
from PyQt5.QtGui import QIcon
from sqlalchemy import (Table, Column, Integer, String, Float, Boolean,\
                        MetaData, create_engine, ForeignKey, select, update)
import logging
logger = logging.getLogger(__name__)

def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)

def invoerOK():
    logger.debug(">>> Entering invoerOK()")
    msg = QMessageBox()
    logger.debug("invoerOK(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Wijzigen van verkoop_uurtarieven gelukt!')
    msg.setWindowTitle('UURTARIEVEN')
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    logger.debug("<<< Exiting invoerOK()")
    msg.exec_()
      
def winKeuze(m_email):
    logger.debug(">>> Entering winKeuze(m_email=%s)", m_email)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            msg = QMessageBox.question(self, 'Verkoop-uurtarieven aanpassen',\
             "Verkoop-uurtarieven aanpassen?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            logger.debug("__init__(parent=%s): mboekd → %s", parent, mboekd)
            logger.debug("__init__(parent=%s): selpar → %s", parent, selpar)
            logger.debug("__init__(self=%s,parent=%s): params_hours → %s", self, parent, params_hours)
            logger.debug("__init__(parent=%s): metadata → %s", parent, metadata)
            logger.debug("__init__(self=%s,parent=%s): metadata → %s", self, parent, metadata)
            if msg == QMessageBox.No:
                windowSluit(self, m_email)
                winKeuze(m_email)
            metadata = MetaData()
            params_hours = Table('params_hours', metadata,
                 Column('rateID', Integer(), primary_key=True),
                 Column('item', String),
                 Column('hourly_tariff', Float),
                 Column('wageID', None, ForeignKey('lonen.loonID')),
                 Column('travel_time', Float),
                 Column('overhead_factor', Float),
                 Column('date', String))
            lonen = Table('lonen', metadata,
                 Column('loonID', Integer(), primary_key=True),
                 Column('tabelloon', Float),
                 Column('werkuur',Float),
                 Column('reisuur', Float),
                 Column('direct', Boolean),
                 Column('maandloon', Float),
                 Column('functieomschr', String),
                 Column('boekdatum', String))

            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("__init__(self=%s,parent=%s): engine → %s", self, parent, engine)
            logger.debug("__init__(parent=%s): engine → %s", parent, engine)
            con = engine.connect()
            selpar = select([params_hours, lonen]).where(params_hours.c.rateID == lonen.c.loonID).order_by(
                lonen.c.loonID)
            logger.debug("__init__(parent=%s): updpar → %s", parent, updpar)
            rppar = con.execute(selpar)
            logger.debug("__init__(self=%s,parent=%s): rppar → %s", self, parent, rppar)
            logger.debug("__init__(parent=%s): rppar → %s", parent, rppar)
            mboekd = str(datetime.datetime.now())[0:10]
            logger.debug("__init__(self=%s,parent=%s): mboekd → %s", self, parent, mboekd)
            for row in rppar:
                updpar = update(params_hours).where(params_hours.c.rateID == row[3]).values(
                    hourly_tariff=row[8] * row[5], date=mboekd, travel_time=row[8] / 3)
                logger.debug("__init__(self=%s,parent=%s): hourly_tariff → %s", self, parent, hourly_tariff)
                con.execute(updpar)
                updlon = update(lonen).where(lonen.c.loonID == row[7]).values(werkuur=row[2])
                logger.debug("__init__(parent=%s): updlon → %s", parent, updlon)
                con.execute(updlon)
                updlon = update(lonen).where(lonen.c.loonID == row[7] - 1).values(werkuur=row[2])
                con.execute(updlon)
                updlon = update(lonen).where(lonen.c.loonID == row[7] - 2).values(werkuur=row[2])
                con.execute(updlon)
                if row[0] < 37:
                    updlon = update(lonen).where(lonen.c.loonID == row[7] - 3).values(werkuur=row[2])
                    con.execute(updlon)
            invoerOK()
            windowSluit(self, m_email)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)

    window = Widget()
    window.show()
