from app.extensions import db

class Task(db.Model):
    __tablename__= "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    importance = db.Column(db.Integer, nullable=False)
    urgency = db.Column(db.Integer, nullable=False)
    estimated_time = db.Column(db.Integer, nullable=False)
    deadline = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(50), default="Pending")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))