import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = 'postgres://jggkphnqehagqp:6a13df78dd9ce1e1b8ed9a76cd42e37f9b55587a3372b8ffda814f3294810d93@ec2-176-34-184-174.eu-west-1.compute.amazonaws.com:5432/dco45j4dohrfho'
    SQLALCHEMY_TRACK_MODIFICATIONS = False