from db import db

class Queue(db.Model):
    __tablename__ = 'queue'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    people_count = db.Column(db.Integer, nullable=False)
    waiting_time = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Queue {self.name}>"
