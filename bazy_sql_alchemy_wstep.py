from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Pojazd(Base):
    __tablename__ = 'pojazdy'

    id = Column(Integer, primary_key=True)
    marka = Column(String)
    model = Column(String)
    rok_produkcji = Column(Integer)
    numer_rejestracyjny = Column(String, unique=True)

    def __repr__(self):
        return f'{self.marka} {self.model}: {self.numer_rejestracyjny}'

# Tworzymy połączenie z bazą danych
# ciąg połączeniowy DSN:
# dialekt:driver://user:passwd@host:port/baza
engine = create_engine('sqlite:///baza_pojazdow.db')

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

p1 = Pojazd(marka='Toyota', model='Corolla', rok_produkcji=2010, numer_rejestracyjny='kr12345')
p2 = Pojazd(marka='Toyota', model='Supra', rok_produkcji=2020, numer_rejestracyjny='k1231235')
p3 = Pojazd(marka='BMW', model='330i', rok_produkcji=2015, numer_rejestracyjny='kasdasda')
print(session.new)
session.add(p1)
session.add(p2)
session.add(p3)
print(session.new)
session.commit()
print(session.new)
wszystkie = session.query(Pojazd).all()
print('Wszystkie:', wszystkie)
print('Pierwszy:', session.query(Pojazd).first())
# print('Ostatni:', session.query(Pojazd).last())
toyoty = session.query(Pojazd).filter(Pojazd.marka == 'Toyota').order_by(Pojazd.rok_produkcji.desc()).all()
print('Same toyoty:', toyoty)

# Chcę zmienić rok produkcji wszystkich BMW na 1999:
wszystkie_bmw = session.query(Pojazd).filter(Pojazd.marka == 'BMW')
for bmw in wszystkie_bmw:
    bmw.rok_produkcji = 1999

print(session.dirty)
session.commit()
print(session.dirty)

# skasuj wszystkie o roku produkcji >=2000
session.query(Pojazd).filter(Pojazd.rok_produkcji >= 2000).delete()
session.commit()

wszystkie = session.query(Pojazd).all()
print('Wszystkie:', wszystkie)



session.close()
