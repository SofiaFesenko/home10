from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship, Session

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

Base = declarative_base()


class Worker(Base):
    __tablename__ = "worker"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    worker = relationship("Department", back_populates="department", cascade="all")

    def __repr__(self):
        return f"Worker(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r}"


class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True)
    name_of_department = Column(String(30))

    department = relationship("Worker", back_populates="worker")

    def __repr__(self):
        return f"Department(id={self.id!r}, name_of_department={self.name!r}"


with Session(engine) as session:
    oksanka = Department(
        name='Oksana',
        fullname='Oksanivna',
        worker=[Department(department="milk")]
    )

    serhijko = Department(
        name='Sergey',
        fullname='Sergeev',
        worker=[Department(department="milk")]
    )

    marynka = Department(
        name='Maria',
        fullname='Mariivna',
        worker=[Department(department="bread")]
    )

    maksymko = Department(
        name='Maksym',
        fullname='Maksymovicz',
        worker=[Department(department="bread")]
    )
session.add_all([oksanka, serhijko, marynka, maksymko])
session.commit()
