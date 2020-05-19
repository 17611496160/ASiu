from datetime import datetime

from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Notepad(Base):
    __tablename__ = 'notepad1'
    ID = Column(String(20),primary_key = True)
    cotent = Column(String(50))
    people = Column(String(20))
    leavetime = Column(String(20))
    deleteornot = Column(String(20))

connectadd = 'mysql+mysqldb://root:gloria654@localhost:3306/作业10'
engine = create_engine(connectadd, echo=True)
db_session = sessionmaker(bind = engine)

#以下为相应操作，需要一个一个执行，执行其中一个注释掉其他的
#插入记录
session = db_session()
time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
new_notepad = Notepad(ID = '10',cotent = 'good good study',people = 'Lily',leavetime = time,deleteornot = 'no')
session.add(new_notepad)
session.commit()
session.close()

#删除记录
session = db_session()
target = session.query(Notepad).filter_by(ID = 0).first()
target.deleteornot = "yes"
session.commit()
session.close()

#修改记录
session = db_session()
result = session.query(Notepad).filter_by(ID = 3).first()
result.content = "ajhgfakgsfalkgfbakhvf"
result.peole = "Cristin"
result.leavetime = datetime.now().strftime()
session.commit()
session.close()

#查询留言
session = db_session()
result = session.query(Notepad).filter().all()
for item in result:
    print(item)
session.close()

