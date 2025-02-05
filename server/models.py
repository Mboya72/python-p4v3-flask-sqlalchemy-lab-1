from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"  # This defines the table name
    
    # Define the columns
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    magnitude = db.Column(db.Float)  # Float column for magnitude
    location = db.Column(db.String)  # String column for location
    year = db.Column(db.Integer)  # Integer column for year
    
    # Define the __repr__ method
    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
