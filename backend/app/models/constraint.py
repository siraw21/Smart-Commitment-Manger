from app.extensions import db

class Constraint(db.Model):
    __tablename__ = "constraints"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)  # e.g., "Class", "Work"

    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))