from peewee import *
from configs.db import db
from playhouse.shortcuts import ThreadSafeDatabaseMetadata

class BModel(Model):
    class Meta:
       database = db
       # Instruct peewee to use our thread-safe metadata implementation.
       model_metadata_class = ThreadSafeDatabaseMetadata