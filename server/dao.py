# import jwt
from passlib.hash import bcrypt
from mongoengine import (
    Document, DoesNotExist, NotUniqueError, ValidationError
)

from .documents import user
from .permissions import Permissions


class DAO:
    """
    TODO: implement Permissions
    """
    def __init__(self, document_cls: Document):
        self.document_cls = document_cls

    def get_one(self, pk):
        try:
            result = self.document_cls.objects.get(pk=pk).to_mongo()
            return {'success': True, 'data': result}, 200
        except DoesNotExist:
            return {'success': False, 'message': 'Document not found.'}, 404

    def get_many(self, **kwargs):
        try:
            result = self.document_cls.objects(**kwargs).to_mongo()
            return {'success': True, 'data': result}, 200
        except Exception as e:
            return {'success': False, 'message': e.message}, 500

    def create_one(self, **kwargs):
        try:
            result = self.document_cls.objects.create(owner=auth_user, **kwargs)
            return result, 201
        except Exception as e:
            return {'success': False, 'message': e.message}, 400

    def update_one(self, document: Document, **kwargs):
        """
        Returns the number of updated documents (unless full_result is True)
        """
        try:
            result = obj.update(**kwargs).to_mongo()
            return {'success': True, 'data': result}, 200
        except Exception as e:
            return {'success': False, 'message': e.message}, 400

    def delete_one(self, document):
        try:
            result = document.delete()
            return {'success': True, 'data': result}, 202
        except:
            return {'success': False, 'message': 'Unable to delete document.'}, 500


class UserDAO(DAO):
    def __init__(self):
        self.document_cls = user.User

    def get_one(self, pk):
        pass

    def create_one(self, **kwargs):
        try:
            plain_pass = kwargs['passcode']
            hashed_pass = bcrypt.hash(plain_pass)
            kwargs['passcode'] = hashed_pass
            self.document_cls.objects.create(is_admin=False, **kwargs)
            return {'success': True}, 201
        except (ValidationError, NotUniqueError) as e:
            return {'success': False, 'message': e.message}, 400
