from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    office = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    mobile = db.Column(db.String(80), nullable=True)

    def json(self):
        return {'id': self.id, 'firstName': self.firstName, 'lastName': self.lastName, 'office': self.office, 'email': self.email, 'mobile': self.mobile}

    def add_user(_firstName, _lastName, _office, _email, _mobile):
        new_user = User(firstName=_firstName, lastName=_lastName,
                        office=_office, email=_email, mobile=_mobile)
        db.session.add(new_user)
        db.session.commit()

    def get_all_users():
        return [User.json(user) for user in User.query.all()]

    def get_user(_id):
        return User.json(User.query.filter_by(id=_id).first())

    def update_user(_id, _firstName, _lastName, _office, _email, _mobile):
        user_to_update = User.query.filter_by(id=_id).first()
        user_to_update.firstName = _firstName
        user_to_update.lastName = _lastName
        user_to_update.office = _office
        user_to_update.email = _email
        user_to_update.mobile = _mobile
        db.session.commit()

    def delete_user(_id):
        is_successful = User.query.filter_by(id=_id).delete()
        db.session.commit()
        return bool(is_successful)

    def __repr__(self):
        user_object = {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'office': self.office,
            'email': self.email,
            'mobile': self.mobile
        }
        return json.dumps(user_object)
