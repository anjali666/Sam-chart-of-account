from django.db import models

# class categoryManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(asset_parent=None)
# class subcategoryManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().exclude(asset_parent=None)