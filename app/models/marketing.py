"""This module encopassing all the models for marketing management"""


class EmailMarketing:
    """Model for email marketing"""
    def __init__(self, _id, target_emails, subject, body):
        self._id = str(_id)
        self.target_emails = target_emails
        self.subject = subject
        self.body = body

    def __repr__(self):
        return self.id
