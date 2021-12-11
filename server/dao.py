# import jwt
from passlib.hash import bcrypt
from mongoengine import (
    Document, DoesNotExist, NotUniqueError, ValidationError
)

from permissions import Permissions
from documents.user import User


class DAO:
    def __init__(self, document_cls: Document):
        """
        TODO: replace current_user with actual login token
        """
        self.current_user = 'sketchychen'
        self.document_cls = document_cls
        self.user_perms = Permissions(current_user=self.current_user)

    def get_allowed_fields(self, document: Document):
        perm_level = self.user_perms.get_level(document)
        return tuple(
            k
            for k,v
            in self.document_cls._fields.items()
            if perm_level >= getattr(v, 'perm_level', 0)
        )

    def get_one(self, pk):
        try:
            documents = self.document_cls.objects(pk=pk)
            allowed_fields = self.get_allowed_fields(documents.first())
            print(allowed_fields)
            result = documents.only(*allowed_fields).first().to_mongo()
            return result
        except DoesNotExist as e:
            return e.message, 404

    def get_many(self, **kwargs):
        """
        When creating a new DAO, override this method
        to filter queryset and fields as appropriate for the current user.
        """
        try:
            documents = self.document_cls.objects(**kwargs)
            result = documents.to_mongo()
            return result
        except Exception as e:
            return e.message, 500

    def create_one(self, **kwargs):
        try:
            result = self.document_cls.objects.create(owner=current_user, **kwargs)
            return result, 201
        except (ValidationError, NotUniqueError) as e:
            if isinstance(e, ValidationError):
                return e.message, 400
            elif isinstance(e, NotUniqueError):
                return e.message, 409

    def update_one(self, update_with, pk=None, document: Document = None):
        if pk is not None and document is None:
            document = self.get_one(pk)

        if self.user_perms.get_level(document) > 2:
            return 'User cannot edit document', 403

        try:
            result = document.update(**update_with).to_mongo()
            return result
        except Exception as e:
            return e.message, 400


    def delete_one(self, pk = None, document: Document = None):
        if pk is not None and document is None:
            document = self.get_one(pk)

        if self.user_perms.get_level(document) > 1:
            return 'User cannot delete document', 403

        try:
            result = document.delete()
            return result, 202
        except:
            return 'Server unable to delete document. Try again later.', 500


class UserDAO(DAO):
    def __init__(self):
        """
        TODO: replace current_user with actual login token
        """
        self.current_user = 'sketchychen'
        self.document_cls = User
        self.user_perms = Permissions(current_user=self.current_user)

    def create_one(self, **kwargs):
        try:
            plain_pass = kwargs['passcode']
            hashed_pass = bcrypt.hash(plain_pass)
            kwargs['passcode'] = hashed_pass
            document = self.document_cls.objects.create(is_admin=False, **kwargs)
            return '', 201
        except (ValidationError, NotUniqueError) as e:
            if isinstance(e, ValidationError):
                return e.message, 400
            elif isinstance(e, NotUniqueError):
                return 'User name or email is already in use.', 409