"""This module encopassing all the models for marketing management"""


class EmailMarketing:
    """Model for email marketing"""
    def __init__(self, _id,subject,body, target_emails=[], viwed_by=[]):
        self._id = str(_id)
        self.target_emails = target_emails
        self.subject = subject
        self.body = body
        self.viwed_by = viwed_by

    def __repr__(self):
        return self.id
