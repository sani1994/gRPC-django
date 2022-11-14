"""
created at 11/13/22
"""
__author__ = "Nazmul Hasan Sani"

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(to=User,
                                   # on_delete=models.DO_NOTHING,
                                   on_delete=models.CASCADE,
                                   verbose_name="Created By",
                                   null=True,
                                   blank=True,
                                   related_name='created_%(app_label)s_%(class)s_set',
                                   db_index=True,
                                   help_text="User who created it")
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(to=User,
                                    # on_delete=models.DO_NOTHING,
                                    on_delete=models.CASCADE,
                                    verbose_name="Modified By",
                                    related_name='modified_%(app_label)s_%(class)s_set',
                                    null=True,
                                    blank=True,
                                    db_index=True,
                                    help_text="User who last modified")

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_on = datetime.now()
            # self.created_by = self.pk
        self.modified = datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
