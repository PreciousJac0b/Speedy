from app import db
from flask_login import UserMixin
from app import login
from werkzeug.security import check_password_hash, generate_password_hash

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(), index=True, nullable=False, unique=True)
  password_hash = db.Column(db.String(128))
  has_acc = db.Column(db.Integer, default=0, nullable=False)
  def __repr__(self):
    return '<User {}>'.format(self.username)
    
  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

  def associated(self):
    """This returns associated objects in the db"""
    id = self.id
    customer = Customer.query.filter_by(user_id=id).first()
    account = Account.query.filter_by(cus_id=customer.id).first()
    return [customer, account]


class Customer(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
  first_name = db.Column(db.String(140))
  last_name = db.Column(db.String(140))
  email = db.Column(db.String(120), index=True, unique=True)
  phone_number = db.Column(db.String(204), primary_key=True)
  username = db.Column(db.String(200))
  address = db.relationship('Address', backref='customer', lazy='dynamic')
  dob = db.Column(db.DateTime)
  date_created= db.Column(db.DateTime)
  bank_name = db.Column(db.String(240), default="Speedy")
  accounts = db.relationship('Account', backref='customer', lazy='dynamic')

  @classmethod
  def get(cls, param, arg):
    """Get a customer from the database based on information given"""
    if param == "id":
      customer = Customer.query.filter_by(id=arg).first()
    elif param == "email":
      customer = Customer.query.filter_by(email=arg).first()
    elif param == "phone_number":
      customer == Customer.query.filter_by(phone_number=arg).first()
    else:
      customer = None
    return customer




class Account(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  cus_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
  account_number = db.Column(db.String(100), nullable=False)
  account_pin = db.Column(db.String(4), nullable=False)
  acc_type = db.Column(db.String(240))
  balance = db.Column(db.Integer)
  bank_name = db.Column(db.String(240), default="Speedy", nullable=False)
  date_created = db.Column(db.DateTime)
  transactions = db.relationship('Transaction', backref='account', lazy='dynamic')


class Transaction(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  acc_num = db.Column(db.String(100), db.ForeignKey('account.account_number'))
  bank_name = db.Column(db.String(240), default="Speedy", nullable=False)
  transaction_type = db.Column(db.String(240))
  amount = db.Column(db.Integer)
  timestamp = db.Column(db.DateTime)

class Address(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  cus_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
  apartment_number = db.Column(db.Integer, nullable=False)
  street_number = db.Column(db.Integer, nullable=False)
  street_name = db.Column(db.String(256), nullable=False)
  city = db.Column(db.String(256), nullable=False)
  state = db.Column(db.String(256), nullable=False)
  country = db.Column(db.String(256), nullable=False)
  postal_code = db.Column(db.Integer)
  address_line_2 = db.Column(db.String(400))


@login.user_loader
def load_user(id):
  return User.query.get(int(id))