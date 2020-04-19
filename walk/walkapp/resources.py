from import_export import resources
from walkapp.models import Wts_table
from django.contrib.auth.models import User
from django.db import models

class Wtsresource(resources.ModelResource):
    class Meta:
        model = Wts_table
        # exclude = 'updatedby'
