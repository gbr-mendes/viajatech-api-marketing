"""This module encopassing all the models for marketing management"""
from datetime import datetime


class EmailMarketing:
    """Model for email marketing"""
    def __init__(self, _id,subject,body, target_emails=[], viwed_by=[]):
        self._id = str(_id)
        self.target_emails = target_emails
        self.subject = subject
        self.body = body
        self.viwed_by = viwed_by
        self.created_at = datetime.now()

    def __repr__(self):
        return self.id
