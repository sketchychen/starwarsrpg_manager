from mongoengine import Document

from .documents.user import User


class Permissions:
    """
    Permission types:
    0: Admin
    1: Editor
    2: Viewer

    TODO: replace auth_user with actual login token
    """
    auth_user = 'sketchychen'

    def __init__(self, document: Document):
        self.document = document

    @property
    def auth_user_is_owner(self):
        if isinstance(self.document, User):
            return auth_user == document.name
        else:
            return auth_user == document.owner

    @property
    def auth_user_can_edit(self):
        if user.is_admin or self.auth_user_is_owner:
            return True
        else:
            return self.auth_user in self.document.editors

    @property
    def auth_user_can_view(self):
        return True