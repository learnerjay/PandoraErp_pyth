from login import hoofdMenu
from PyQt5.QtWidgets import QMessageBox, QDialog
from PyQt5.QtGui import QIcon 
from sqlalchemy import (Table, Column, Integer, String, MetaData,\
                        create_engine, Float)
from sqlalchemy.sql import select, insert, delete, func, and_
import datetime
import logging
logger = logging.getLogger(__name__)

def jaarweek():
    logger.debug(">>> Entering jaarweek()")
    dt = datetime.datetime.now()
    logger.debug("jaarweek(): dt → %s", dt)
    week = str('0'+str(dt.isocalendar()[1]))[-2:]
    logger.debug("jaarweek(): week → %s", week)
    jaar = str(dt.isocalendar()[0])
    jrwk = jaar+week
    logger.debug("jaarweek(): jaar → %s", jaar)
    logger.debug("jaarweek(): jrwk → %s", jrwk)
    logger.debug("<<< Exiting jaarweek()")
    return(jrwk)

def JN(m_email):
    logger.debug(">>> Entering JN(m_email=%s)", m_email)
    msgBox=QMessageBox()
    logger.debug("JN(m_email=%s): msgBox → %s", m_email, msgBox)
    msgBox.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msgBox.setWindowTitle("Calculate Data from external Works")
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Do you want to calculate this week's financials?")
    msgBox.setStandardButtons(QMessageBox.Yes)
    msgBox.addButton(QMessageBox.No)
    msgBox.setDefaultButton(QMessageBox.Yes)
    if(msgBox.exec_() == QMessageBox.Yes):
        bereken(m_email)
    else:
        hoofdMenu(m_email) 
        logger.debug("<<< Exiting JN(m_email=%s)", m_email)
        
def geenGegevens():
    logger.debug(">>> Entering geenGegevens()")
    msgBox=QMessageBox()
    logger.debug("geenGegevens(): msgBox → %s", msgBox)
    msgBox.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msgBox.setWindowTitle("Calculate financial data from external works")
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText("No data available for this year!")
    logger.debug("<<< Exiting geenGegevens()")
    msgBox.exec_()
    
def berBestaat(jrwk, m_email):
    logger.debug(">>> Entering berBestaat(jrwk=%s,m_email=%s)", jrwk, m_email)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            msg = QMessageBox()
            logger.debug("__init__(self=%s,parent=%s): msg → %s", self, parent, msg)
            logger.debug("__init__(parent=%s): msg → %s", parent, msg)
            msg.setStyleSheet("color: black;  background-color: gainsboro")
            msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            msg.setWindowTitle("Calculation of external works")
            msg.setIcon(QMessageBox.Warning)
            msg.setText('This booking week\'s report is present\n\nDo you want to recalculate it?\n\nN.B. the existing data will be overwritten!')
            msg.setStandardButtons(QMessageBox.Yes)
            msg.addButton(QMessageBox.No)
            logger.debug("__init__(self=%s,parent=%s): resultaten → %s", self, parent, resultaten)
            msg.setDefaultButton(QMessageBox.Yes)
            if(msg.exec_() == QMessageBox.Yes):
                metadata = MetaData()
                logger.debug("__init__(self=%s,parent=%s): metadata → %s", self, parent, metadata)
                logger.debug("__init__(parent=%s): metadata → %s", parent, metadata)
                resultaten = Table('resultaten', metadata,
                   Column('resID', Integer(), primary_key=True),
                   Column('boekweek', String))  
                resultaten_status = Table('resultaten_status', metadata,
                   Column('rID', Integer(), primary_key=True),
                   Column('boekweek', String))  
                engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
                logger.debug("__init__(parent=%s): engine → %s", parent, engine)
                logger.debug("__init__(self=%s,parent=%s): engine → %s", self, parent, engine)
                con = engine.connect()
                seldel1 = delete(resultaten).where(resultaten.c.boekweek == jrwk)
                con.execute(seldel1)
                seldel2 = delete(resultaten_status).where(resultaten_status.c.boekweek == jrwk)
                con.execute(seldel2)
                logger.debug("<<< Exiting __init__(parent=%s)", parent)
                bereken(m_email)
    window = Widget()
    window.show()  
       
def berGelukt():
    logger.debug(">>> Entering berGelukt()")
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            msg = QMessageBox()
            msg.setStyleSheet("color: black;  background-color: gainsboro")
            msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            msg.setIcon(QMessageBox.Information)
            msg.setText('The calculation for '+jaarweek()+' is completed!')
            msg.setWindowTitle('Results')
            msg.exec_()
    window = Widget()
    window.show()    

def divBereken(row):
    logger.debug(">>> Entering divBereken(row=%s)", row)
    jrwk = jaarweek()
    logger.debug("divBereken(row=%s): jrwk → %s", row, jrwk)
    mstatuswk = row[12]
    metadata = MetaData()
    logger.debug("divBereken(row=%s): mstatuswk → %s", row, mstatuswk)
    resultaten = Table('resultaten', metadata,
        Column('resID', Integer(), primary_key=True),
        Column('statusweek', String),
        Column('blonen', Float),
        Column('wlonen', Float),
        Column('bmaterialen', Float),
        Column('wmaterialen', Float),
        Column('bmaterieel', Float),
        Column('wmaterieel', Float),
        Column('binhuur', Float),
        Column('winhuur', Float),
        Column('bdiensten', Float),
        Column('wdiensten', Float),
        Column('bprojectkosten', Float),
        Column('wprojectkosten', Float),
        Column('btotaal', Float),
        Column('wtotaal', Float),
        Column('betaald_bedrag', Float),
        Column('meerminderwerk', Float),
        Column('onderhandenwerk', Float),
        Column('boekweek', String),
        Column('bruto_winst', Float),
        Column('aanneemsom', Float))
      
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("divBereken(row=%s): resultaten → %s", row, resultaten)
    con = engine.connect()
    selres = select([resultaten]).where(and_(resultaten.c.statusweek == mstatuswk,\
                   resultaten.c.boekweek == jrwk))
    logger.debug("divBereken(row=%s): engine → %s", row, engine)
    rpres = con.execute(selres).first()
    mstatus = row[11]
    logger.debug("divBereken(row=%s): con → %s", row, con)
    mkosten = row[3]+row[4]+row[5]+row[6]+row[7]+row[8]+row[9]+row[10]+row[17]+\
              row[18]+row[19]+row[20]
    logger.debug("divBereken(row=%s): selres → %s", row, selres)
    logger.debug("divBereken(row=%s): rpres → %s", row, rpres)
    if mstatus == 'C':
        mwinst = row[2]/3-mkosten
    elif mstatus == 'D':
        logger.debug("divBereken(row=%s): mkosten → %s", row, mkosten)
        mwinst = row[2]/3-mkosten
        logger.debug("divBereken(row=%s): mwinst → %s", row, mwinst)
    elif mstatus == 'E':
        mwinst = row[2]*2/3-mkosten
    elif mstatus == 'F':
        mwinst = row[2]*.8667-mkosten
    elif mstatus == 'G':
       logger.debug("divBereken(row=%s): wmaterialen → %s", row, wmaterialen)
       mwinst = row[2]-mkosten
    elif mstatus == 'H':
        mwinst = row[2]+row[10]-mkosten
    else:
        logger.debug("divBereken(row=%s): blonen → %s", row, blonen)
        mwinst = 0

    if not rpres:
        try:
            mresnr = (con.execute(select([func.max(resultaten.c.resID,\
                type_=Integer)])).scalar())
            logger.debug("divBereken(row=%s): type_ → %s", row, type_)
            logger.debug("divBereken(row=%s): insres → %s", row, insres)
            mresnr += 1
        except:
            logger.error("Exception in divBereken(row=%s)", row, exc_info=True)
            mresnr = 1
        insres = insert(resultaten).values(resID = mresnr, statusweek = mstatuswk,\
          blonen=round(row[28],2), wlonen=round(row[4],2),bmaterialen=round(row[27],2),\
          wmaterialen=round(row[3],2),bmaterieel=round(row[26],2), wmaterieel=round(row[5],2),\
          binhuur=round(row[21],2), winhuur=round(row[21],2),bprojectkosten=round(row[14]+\
          row[15]+row[16]+row[22],2),wprojectkosten=round(row[6]+row[7]+row[8]+row[9],2),\
          btotaal=round(row[2],2), wtotaal=round(row[3]+row[4]+row[5]+row[6]+row[7]+row[8]\
          +row[9]+row[17]+row[18]+row[19]+row[20],2),betaald_bedrag=round(row[13],2),\
          meerminderwerk=round(row[10],2), onderhandenwerk=round(row[3]+row[4]+row[5]+\
          row[6]+row[7]+row[8]+row[9]+row[10]+row[17]+row[18]+row[19]+row[20]-row[13],2),\
          bruto_winst = round(mwinst,2), boekweek = jrwk, aanneemsom = round(row[2],2))
        logger.debug("divBereken(row=%s): btotaal → %s", row, btotaal)
        logger.debug("divBereken(row=%s): binhuur → %s", row, binhuur)
        con.execute(insres)
        logger.debug("<<< Exiting divBereken(row=%s)", row)

def bereken(m_email):
    logger.debug(">>> Entering bereken(m_email=%s)", m_email)
    jrwk = jaarweek()
    logger.debug("bereken(m_email=%s): jrwk → %s", m_email, jrwk)
    jr = jrwk[0:4]
    metadata = MetaData()
    logger.debug("bereken(m_email=%s): metadata → %s", m_email, metadata)
    resultaten = Table('resultaten', metadata,
        Column('resID', Integer(), primary_key=True),
        Column('boekweek', String))
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("bereken(m_email=%s): resultaten → %s", m_email, resultaten)
    con = engine.connect()
    selc = select([resultaten]).where(resultaten.c.boekweek == jrwk)
    logger.debug("bereken(m_email=%s): engine → %s", m_email, engine)
    rpc = con.execute(selc).first()
    if rpc:
        logger.debug("bereken(m_email=%s): con → %s", m_email, con)
        berBestaat(jrwk, m_email)
    metadata = MetaData()
    logger.debug("bereken(m_email=%s): selc → %s", m_email, selc)
    werken = Table('werken', metadata,
        Column('werknummerID', Integer(), primary_key=True),
        Column('werkomschrijving', String),
        Column('aanneemsom', Float),
        Column('kosten_materialen', Float),
        Column('kosten_lonen', Float),
        Column('kosten_materieel', Float),
        Column('kosten_leiding', Float),
        Column('kosten_huisv', Float),
        Column('kosten_overig', Float),
        Column('kosten_vervoer', Float),
        Column('meerminderwerk', Float),
        Column('voortgangstatus', String),
        Column('statusweek',  String),
        Column('betaald_bedrag', Float),
        Column('begr_huisv', Float),
        Column('begr_leiding', Float),
        Column('begr_overig', Float),
        Column('kosten_inhuur', Float),
        Column('beton_bvl', Float),
        Column('kabelwerk', Float),
        Column('grondverzet', Float),
        Column('begr_inhuur', Float),
        Column('begr_vervoer', Float),
        Column('begr_beton_bvl', Float),
        Column('begr_kabelwerk', Float),
        Column('begr_grondverzet', Float),
        Column('begr_materieel',Float),
        Column('begr_materialen', Float),
        Column('begr_lonen', Float),
        Column('startweek', String))
          
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
     
    logger.debug("bereken(m_email=%s): werken → %s", m_email, werken)
    sel = select([werken]).where(werken.c.statusweek.like(jr+'%')).order_by(werken.c.statusweek)
    if con.execute(sel).first():
        rpwerken = con.execute(sel)
    else:
        geenGegevens()
        logger.debug("bereken(m_email=%s): sel → %s", m_email, sel)
        hoofdMenu(m_email)
         
        logger.debug("bereken(m_email=%s): rpwerken → %s", m_email, rpwerken)
    msomA,msomB,msomC,msomD,msomE,msomF,msomG,msomH,mkosttot,mbetaald,mmeerwerk = (0,)*11
    mkostB,mkostC,mkostD,mkostE,mkostF,mkostG,mkostH = (0,)*7
    mwinstC, mwinstD, mwinstE, mwinstF, mwinstG, mwinstH = (0,)*6
    mohwC, mohwD, mohwE, mohwF, mohwG, mohwH = (0,)*6
    maantA,maantB,maantC,maantD,maantE,maantF,maantG,maantH = (0,)*8
    mbetaaldB, mbetaaldC, mbetaaldD, mbetaaldE, mbetaaldF, mbetaaldG, mbetaaldH = (0,)*7
    mmeerwB, mmeerwC, mmeerwD, mmeerwE, mmeerwF, mmeerwG, mmeerwH = (0,)*7
    for row in rpwerken:
        #mwerknr = row[0]
        #mwerkomschr = row[1]
        mktotal=row[3]+row[4]+row[5]+row[6]+row[7]+row[8]+row[9]+row[17]+row[20]
        logger.debug("bereken(m_email=%s): mktotal → %s", m_email, mktotal)
        mmeerwerk = mmeerwerk+row[10]
        logger.debug("bereken(m_email=%s): mmeerwerk → %s", m_email, mmeerwerk)
        mkosttot = mkosttot+mktotal
        logger.debug("bereken(m_email=%s): mkosttot → %s", m_email, mkosttot)
        mbetaald = mbetaald+row[13]
        logger.debug("bereken(m_email=%s): mbetaald → %s", m_email, mbetaald)
        mvgangst = row[11]
        if mvgangst == 'A' and row[12][0:4] == jaarweek()[0:4]:
            msomA = msomA+row[2]
            logger.debug("bereken(m_email=%s): msomA → %s", m_email, msomA)
            maantA = maantA+1
            logger.debug("bereken(m_email=%s): maantA → %s", m_email, maantA)
        elif mvgangst == 'B':
            msomB = msomB+row[2]
            logger.debug("bereken(m_email=%s): msomB → %s", m_email, msomB)
            mkostB = mkostB+row[3]+row[4]+row[5]+row[6]+row[7]+row[8]+row[9]+row[10]+\
                row[17]+row[18]+row[19]+row[20]
            logger.debug("bereken(m_email=%s): aanneemsom → %s", m_email, aanneemsom)
            logger.debug("bereken(m_email=%s): mkostB → %s", m_email, mkostB)
            logger.debug("bereken(m_email=%s): msomC → %s", m_email, msomC)
            maantB = maantB+1
            logger.debug("bereken(m_email=%s): maantB → %s", m_email, maantB)
            mbetaaldB = mbetaaldB+row[13]
            logger.debug("bereken(m_email=%s): mbetaaldB → %s", m_email, mbetaaldB)
            mmeerwB = mmeerwB+row[10]
            logger.debug("bereken(m_email=%s): mmeerwB → %s", m_email, mmeerwB)
        elif mvgangst == 'C' and row[12][0:4] == jaarweek()[0:4]:
            msomC = msomC+row[2]
            mkostC = mkostC+row[3]+row[4]+row[5]+row[6]+row[7]+row[8]+row[9]+row[10]+\
                row[17]+row[18]+row[19]+row[20]
            logger.debug("bereken(m_email=%s): mkostC → %s", m_email, mkostC)
            maantC = maantC+1
            logger.debug("bereken(m_email=%s): maantC → %s", m_email, maantC)
            mbetaaldC = mbetaaldC+row[13]
            logger.debug("bereken(m_email=%s): mbetaaldC → %s", m_email, mbetaaldC)
            mmeerwC = mmeerwC+row[10]
            logger.debug("bereken(m_email=%s): mmeerwC → %s", m_email, mmeerwC)
            mmeerwerk = mmeerwerk+row[10]
            mwinstC = mwinstC+row[2]/3-mkostC
            logger.debug("bereken(m_email=%s): mwinstC → %s", m_email, mwinstC)
            mohwC =  mohwC+mkostC-mbetaaldC
            logger.debug("bereken(m_email=%s): mohwC → %s", m_email, mohwC)
        elif mvgangst == 'D' and row[12][0:4] == jaarweek()[0:4]:
            msomD = msomD+row[2]
            logger.debug("bereken(m_email=%s): msomD → %s", m_email, msomD)
            mkostD = row[3]+row[4]+row[5]+row[6]+row[7]+row[8]+row[9]+row[10]+\
                row[17]+row[18]+row[19]+row[20]
            logger.debug("bereken(m_email=%s): mkostD → %s", m_email, mkostD)
            mkostD += mkostD
            maantD = maantD+1
            logger.debug("bereken(m_email=%s): maantD → %s", m_email, maantD)
            mbetaaldD += mbetaaldD+row[13]
            mmeerwD += mmeerwD+row[10]
            mwinstD = mwinstD+row[2]/3-mkostD
            logger.debug("bereken(m_email=%s): mwinstD → %s", m_email, mwinstD)
            mohwD =  mohwD+mkostD-mbetaaldD
            logger.debug("bereken(m_email=%s): mohwD → %s", m_email, mohwD)
        elif mvgangst == 'E' and row[12][0:4] == jaarweek()[0:4]:
            msomE = msomE+row[2]
            logger.debug("bereken(m_email=%s): msomE → %s", m_email, msomE)
            mkostE = mkostE+row[3]+row[4]+row[5]+row[6]+row[7]+row[8]+row[9]+row[10]+\
                row[17]+row[18]+row[19]+row[20]
            logger.debug("bereken(m_email=%s): mkostE → %s", m_email, mkostE)
            maantE = maantE+1
            logger.debug("bereken(m_email=%s): maantE → %s", m_email, maantE)
            mbetaaldE += mbetaaldE+row[13]
            mmeerwE += mmeerwE+row[10]
            mwinstE = mwinstE+row[2]*2/3-mkostE
            logger.debug("bereken(m_email=%s): mwinstE → %s", m_email, mwinstE)
            mohwE =  mohwE+mkostE-mbetaaldE
            logger.debug("bereken(m_email=%s): mohwE → %s", m_email, mohwE)
        elif mvgangst == 'F' and row[12][0:4] == jaarweek()[0:4]:
            msomF = msomF+row[2]
            logger.debug("bereken(m_email=%s): msomF → %s", m_email, msomF)
            mkostF = mkostF+row[3]+row[4]+row[5]+row[6]+row[7]+row[8]+row[9]+row[10]+\
                row[17]+row[18]+row[19]+row[20]
            logger.debug("bereken(m_email=%s): mkostF → %s", m_email, mkostF)
            maantF = maantF+1
            logger.debug("bereken(m_email=%s): maantF → %s", m_email, maantF)
            mbetaaldF += mbetaaldF+row[13]
            mmeerwF += mmeerwF+row[10]
            mwinstF = mwinstF+row[2]*.8666-mkostF
            logger.debug("bereken(m_email=%s): mwinstF → %s", m_email, mwinstF)
            mohwF =  mohwF+mkostF-mbetaaldF
            logger.debug("bereken(m_email=%s): mohwF → %s", m_email, mohwF)
        elif mvgangst == 'G' and row[12][0:4] == jaarweek()[0:4]:
            msomG = msomG+row[2]
            logger.debug("bereken(m_email=%s): msomG → %s", m_email, msomG)
            mkostG = mkostG+row[3]+row[4]+row[5]+row[6]+row[7]+row[8]+row[9]+row[10]+\
                row[17]+row[18]+row[19]+row[20]
            logger.debug("bereken(m_email=%s): mkostG → %s", m_email, mkostG)
            maantG = maantG+1
            logger.debug("bereken(m_email=%s): maantG → %s", m_email, maantG)
            mbetaaldG += mbetaaldG+row[13]
            mmeerwG += mmeerwG+row[10]
            mwinstG= mwinstG+row[2]-mkostG
            logger.debug("bereken(m_email=%s): mwinstG → %s", m_email, mwinstG)
            mohwG =  mohwG+mkostG-mbetaaldG
            logger.debug("bereken(m_email=%s): mohwG → %s", m_email, mohwG)
        elif mvgangst == 'H' and row[12][0:4] == jaarweek()[0:4]:
            msomH = msomH+row[2]
            logger.debug("bereken(m_email=%s): msomH → %s", m_email, msomH)
            mkostH = mkostH+row[3]+row[4]+row[5]+row[6]+row[7]+row[8]+row[9]+row[10]+\
                row[17]+row[18]+row[19]+row[20]
            logger.debug("bereken(m_email=%s): mkostH → %s", m_email, mkostH)
            maantH = maantH+1
            logger.debug("bereken(m_email=%s): maantH → %s", m_email, maantH)
            mbetaaldH += mbetaaldH+row[13]
            mmeerwH = mmeerwH+row[10]
            logger.debug("bereken(m_email=%s): mmeerwH → %s", m_email, mmeerwH)
            mwinstH = mwinstH+row[2]+mmeerwH-mkostH
            logger.debug("bereken(m_email=%s): mwinstH → %s", m_email, mwinstH)
            mohwH =  mohwH+mkostH-mbetaaldH
            logger.debug("bereken(m_email=%s): mohwH → %s", m_email, mohwH)
            
        divBereken(row)
        logger.debug("bereken(m_email=%s): resultaten_status → %s", m_email, resultaten_status)
   
    metadata = MetaData()      
    resultaten_status = Table('resultaten_status', metadata,
        Column('rID', Integer, primary_key=True),
        Column('status', String),
        Column('aanneemsom', Float),
        Column('kosten', Float),
        Column('aantal', Integer),
        Column('boekweek', String),
        Column('betaald', Float),
        Column('meerminderwerk', Float))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    
    selr = select([resultaten_status]).where(resultaten_status.c.boekweek == jrwk)
    logger.debug("bereken(m_email=%s): selr → %s", m_email, selr)
    logger.debug("bereken(m_email=%s): insres → %s", m_email, insres)
    rpr = con.execute(selr).first()
    logger.debug("bereken(m_email=%s): rpr → %s", m_email, rpr)
    
    if not rpr: 
        try:
            mrnr = (con.execute(select([func.max(resultaten_status.c.rID,\
             type_=Integer)])).scalar())
            logger.debug("bereken(m_email=%s): type_ → %s", m_email, type_)
            mrnr += 1
            logger.error("Exception in bereken(m_email=%s)", m_email, exc_info=True)
        except:
            mrnr = 1
        insres = insert(resultaten_status).values(rID = mrnr, status = 'A',\
            aanneemsom = round(msomA,2), aantal = maantA, boekweek = jrwk)
        con.execute(insres)
        try:
            mrnr = (con.execute(select([func.max(resultaten_status.c.rID,\
              type_=Integer)])).scalar())
            mrnr += 1
        except:
            mrnr = 1
        insres = insert(resultaten_status).values(rID = mrnr, status = 'B',\
            aanneemsom = round(msomB,2), kosten = round(mkostB,2), aantal = maantB,\
            betaald = mbetaaldB, boekweek = jrwk, meerminderwerk = mmeerwB)
        logger.debug("bereken(m_email=%s): betaald → %s", m_email, betaald)
        con.execute(insres)
        try:
            mrnr = (con.execute(select([func.max(resultaten_status.c.rID,\
               type_=Integer)])).scalar())
            mrnr += 1
        except:
            mrnr = 1
        insres = insert(resultaten_status).values(rID = mrnr, status = 'C',\
            aanneemsom = round(msomC,2), kosten = round(mkostC,2), aantal = maantC,\
            betaald = mbetaaldC, boekweek = jrwk, meerminderwerk = mmeerwC)
        con.execute(insres)
        try:
            mrnr = (con.execute(select([func.max(resultaten_status.c.rID,\
              type_=Integer)])).scalar())
            mrnr += 1
        except:
            mrnr = 1
        insres = insert(resultaten_status).values(rID = mrnr, status = 'D',\
            aanneemsom = round(msomD,2), kosten = round(mkostD,2), aantal = maantD,\
            betaald = mbetaaldD, boekweek = jrwk, meerminderwerk = mmeerwD)
        con.execute(insres)
        try:
            mrnr = (con.execute(select([func.max(resultaten_status.c.rID,\
               type_=Integer)])).scalar())
            mrnr += 1
        except:
            mrnr = 1
        insres = insert(resultaten_status).values(rID = mrnr, status = 'E',\
            aanneemsom = round(msomE,2), kosten = round(mkostE,2), aantal = maantE,\
            betaald = mbetaaldE, boekweek = jrwk, meerminderwerk = mmeerwE)
        con.execute(insres)
        try:
            mrnr = (con.execute(select([func.max(resultaten_status.c.rID,\
              type_=Integer)])).scalar())
            mrnr += 1
        except:
            mrnr = 1
        insres = insert(resultaten_status).values(rID = mrnr, status = 'F',\
            aanneemsom = round(msomF,2), kosten = round(mkostF,2), aantal = maantF,\
            betaald = mbetaaldF, boekweek = jrwk, meerminderwerk = mmeerwF)
        con.execute(insres)
        try:
            mrnr = (con.execute(select([func.max(resultaten_status.c.rID,\
               type_=Integer)])).scalar())
            mrnr += 1
        except:
            mrnr = 1
        insres = insert(resultaten_status).values(rID = mrnr, status = 'G',\
            aanneemsom = round(msomG,2), kosten = round(mkostG,2), aantal = maantG,\
            betaald = mbetaaldG, boekweek = jrwk, meerminderwerk = mmeerwG)
        con.execute(insres)
        try:
            mrnr = (con.execute(select([func.max(resultaten_status.c.rID,\
               type_=Integer)])).scalar())
            mrnr += 1
        except:
            mrnr = 1
        insres = insert(resultaten_status).values(rID = mrnr, status = 'H',\
            aanneemsom = round(msomH,2), kosten = round(mkostH,2), aantal = maantH,\
            betaald = mbetaaldH, boekweek = jrwk, meerminderwerk = mmeerwH)
        con.execute(insres)
        berGelukt() 
        logger.debug("<<< Exiting bereken(m_email=%s)", m_email)
        hoofdMenu(m_email)
