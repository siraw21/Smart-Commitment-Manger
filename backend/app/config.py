import os

class Config:
  SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/smart_commitment_manager"
  SQLALCHEMY_TRACK_MODIFICATIONS = False