from django.db import models
from .utils import decrypt_data,encrypt_data
from django.contrib.auth.models import User
# Create your models here.

class EncryptedBodyText(models.CharField):
  description = "EncryptedBodyText"
  def __init__(self, *args, **kwargs):
    kwargs['max_length'] = 255
    kwargs['blank'] = True
    kwargs['null'] = True
    super().__init__(*args, **kwargs)
  def deconstruct(self):
    name, path, args, kwargs = super().deconstruct()
    del kwargs["max_length"]
    del kwargs["blank"]
    del kwargs["null"]
    return name, path, args, kwargs
  def get_prep_value(self, value):
    # encrypt data with your own function
    return encrypt_data(value) 
  
  def from_db_value(self, value, expression, connection):
    if value is None:
      return value
    # decrypt data with your own function
    return decrypt_data(value)



class Notes(models.Model):
    title = models.CharField(max_length=60)
    update_date = models.DateField(auto_now_add=True)
    body_text = EncryptedBodyText(max_length=400,editable=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title