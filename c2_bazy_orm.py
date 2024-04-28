import faker
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
import datetime as dt

Base = declarative_base()


class Osoba(Base):
    __tablename__ = 'osoby'

    id = Column(Integer, primary_key=True)
    imie = Column(String)
    nazwisko = Column(String)
    wzrost = Column(Integer)
    waga = Column(Integer)
    data_urodzenia = Column(Date)


def generuj_osoby(session,
                  ile: int):
    f = faker.Faker('pl_PL')
    # wygenerowal tyle osob ile chceny z losowymi danymi wzietymi z fakera
    for _ in range(ile):
        imie = f.first_name()
        nazwisko = f.last_name()
        waga = f.pyfloat(7, 2, True, 50, 120)
        wzrost = f.pyint(140, 210)
        data_urodzenia = f.date_of_birth(minimum_age=18)
        dodaj_osobe(session, imie, nazwisko, wzrost, waga, data_urodzenia)


def dodaj_osobe(session,
                imie: str,
                nazwisko: str,
                wzrost: int,
                waga: float,
                data_urodzenia: dt.date):
    session.add(Osoba(imie=imie, nazwisko=nazwisko, wzrost=wzrost, waga=waga, data_urodzenia=data_urodzenia))
    session.commit()


def modyfikuj_osobe(session,
                    id,
                    imie: str | None = None,
                    nazwisko: str | None = None,
                    wzrost: int | None = None,
                    waga: float | None = None,
                    data_urodzenia: dt.date | None = None):
    o1 = session.query(Osoba).filter(Osoba.id == id).first()
    if imie:
        o1.imie = imie

    if nazwisko:
        o1.nazwisko = nazwisko

    if wzrost:
        o1.wzrost = wzrost

    if waga:
        o1.waga = waga

    if data_urodzenia:
        o1.data_urodzenia = data_urodzenia

    session.commit()



def usun_osobe(session, id):
    print(session.query(Osoba).filter(Osoba.id == id))
    session.query(Osoba).filter(Osoba.id == id).delete()
    session.commit()



# To use these classes with SQLAlchemy, you need to create an engine and session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    generuj_osoby(session, 20)

    # Query for all rows in the osoby table

    modyfikuj_osobe(session, 1, imie='Karol', nazwisko='Nowak')
    usun_osobe(session, 20)

    # Print the results
    osoby = session.query(Osoba).all()

    for osoba in osoby:
        print(osoba.id, osoba.imie, osoba.nazwisko, osoba.wzrost, osoba.waga)  # or any other attributes you want to print


    # Close the session
    session.close()
