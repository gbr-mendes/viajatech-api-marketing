"""This module encopassing all the schemas for the marketing management"""
from marshmallow import post_load
from app.models.marketing import EmailMarketing
from app.config.marshmallow import MA

class EmailMarketingSchema(MA.Schema):
    class Meta:
        fields = ("_id", "target_emails", "subject", "body", "viwed_by")
    
    @post_load
    def create_email_marketing(self, data, **kwargs):
        return EmailMarketing(**data)
