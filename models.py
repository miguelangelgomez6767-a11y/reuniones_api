from sqlalchemy import Column, Integer, String, Date, Time
from database import Base


class Reunion(Base):

    __tablename__ = "reuniones"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descripcion = Column(String(300))
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    lugar = Column(String(100), nullable=False)
    responsable = Column(String(100), nullable=False)