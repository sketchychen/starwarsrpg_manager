import jwt
from mongoengine import Document, DoesNotExist, ValidationError

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
            return self.document_cls.objects.get(pk=pk).to_mongo(), 201
        except DoesNotExist:
            return 'Document not found.', 404

    def get_many(self, **kwargs):
        try:
            return self.document_cls.objects(**kwargs).to_mongo()
        except:
            pass

    def create_one(self, **kwargs):
        try:
            return self.document_cls.objects.create(owner=auth_user, **kwargs)
        except Exception as e:
            raise e

    def update_one(self, document: Document, **kwargs):
        """
        Returns the number of updated documents (unless full_result is True)
        """
        try:
            return obj.update(**kwargs)
        except:
            pass

    def delete_one(self, document):
        try:
            return documents.delete()
        except:
            return 'Unable to delete document.', 500


class UserDAO(DAO):
    def __init__(self):
        self.document_cls = user.User

    def create_one(self, **kwargs):
        try:

            return self.document_cls.objects.create(is_admin=False, **kwargs), 201
        except ValidationError as e:
            raise e