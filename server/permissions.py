from mongoengine import Document

from documents.user import User

class Permissions:
    """
    Checks current_user's accessibility of a given document.

    Permission levels:
    5 Literally no one is allowed to see
        anyone's passcodes, even if it's encrypted. Absolutely no.
    4 Admin (ALL THE THINGS)
    3 Owner (GET, UPDATE, DELETE)
    2 Editor (GET, UPDATE)
    1 Private (GET,)
    0 Public (GET,)

    TODO: Determine public vs private read accessibility
    """

    def __init__(self, current_user):
        self.user_pk = current_user

    def get_level(self, document: Document):
        user = User.objects.get(pk=self.user_pk)
        if user.is_admin:
            return 4
        if self.user_pk == getattr(document, 'owner', document.pk):
            return 3
        if self.user_pk in getattr(document, 'editors', ()):
            return 2
        return 0