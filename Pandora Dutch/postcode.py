import logging
logger = logging.getLogger(__name__)
def checkpostcode(mpostcode,mhuisnr): 
      logger.warning(">>> Entering checkpostcode(mpostcode=%s,mhuisnr=%s)", mpostcode, mhuisnr, extra={"event.action": "checkpostcode", "logrite.mpostcode": mpostcode, "logrite.mhuisnr": mhuisnr})
      from sqlalchemy import create_engine, Table, Column, ForeignKey
      from sqlalchemy import Integer, String, Boolean, MetaData, and_
      from sqlalchemy.sql import select 
      postcodes = Table('postcodes', MetaData(),
             Column('van', Integer),
             Column('tem', Integer),
             Column('postcode', String),
             Column('straatID', None, ForeignKey('straat.straatID')),
             Column('soort', Boolean))
      plaats = Table('plaats', MetaData(),
             Column('plaatsID', Integer, primary_key=True),
             Column('c_plaats', String))
      straat = Table('straat', MetaData(),
             Column('straatID', Integer, primary_key=True),
             Column('c_straat', String),
             Column('plaatsID', None, ForeignKey('plaats.plaatsID')))
      engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
      logger.debug("checkpostcode(mpostcode=%s,mhuisnr=%s): engine → %s", mpostcode, mhuisnr, engine, extra={"event.action": "checkpostcode", "logrite.mpostcode": mpostcode, "logrite.mhuisnr": mhuisnr})
      con = engine.connect()
      logger.debug("checkpostcode(mpostcode=%s,mhuisnr=%s): con → %s", mpostcode, mhuisnr, con, extra={"event.action": "checkpostcode", "logrite.mpostcode": mpostcode, "logrite.mhuisnr": mhuisnr})
      s = select(['*']).\
                where(and_(postcodes.c.straatID == straat.c.straatID,
                straat.c.plaatsID == plaats.c.plaatsID,     
                postcodes.c.postcode.like(mpostcode),
                (postcodes.c.van <= mhuisnr) & (postcodes.c.tem >= mhuisnr),
                postcodes.c.soort != mhuisnr%2))
      logger.debug("checkpostcode(mpostcode=%s,mhuisnr=%s): s → %s", mpostcode, mhuisnr, s, extra={"event.action": "checkpostcode", "logrite.mpostcode": mpostcode, "logrite.mhuisnr": mhuisnr})
      result = con.execute(s).first()
      logger.debug("checkpostcode(mpostcode=%s,mhuisnr=%s): result → %s", mpostcode, mhuisnr, result, extra={"event.action": "checkpostcode", "logrite.mpostcode": mpostcode, "logrite.mhuisnr": mhuisnr})
      if result:
           mstraat = str(result[6])
           logger.debug("checkpostcode(mpostcode=%s,mhuisnr=%s): mstraat → %s", mpostcode, mhuisnr, mstraat, extra={"event.action": "checkpostcode", "logrite.mpostcode": mpostcode, "logrite.mhuisnr": mhuisnr})
           mplaats = str(result[8])
           logger.debug("checkpostcode(mpostcode=%s,mhuisnr=%s): mplaats → %s", mpostcode, mhuisnr, mplaats, extra={"event.action": "checkpostcode", "logrite.mpostcode": mpostcode, "logrite.mhuisnr": mhuisnr})
           con.close()
           return (mstraat, mplaats)
      else:
           con.close()
           logger.debug("<<< Exiting checkpostcode(mpostcode=%s,mhuisnr=%s)", mpostcode, mhuisnr, extra={"event.action": "checkpostcode", "logrite.mpostcode": mpostcode, "logrite.mhuisnr": mhuisnr})
           return('','')

