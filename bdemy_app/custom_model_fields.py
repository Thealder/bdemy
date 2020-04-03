from django.db import models


class FAQ(models.Field):


	def db_type(self, connection):
        return 'custom_type'