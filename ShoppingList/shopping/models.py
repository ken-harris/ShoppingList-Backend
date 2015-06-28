import json
from django.db import models

class ShoppingList(models.Model):
    name = models.TextField(null=False)
    items = models.ManyToManyField('Item')
    created_at = models.DateTimeField(auto_now_add=True)

    def to_json(self):
        return json.dumps({
            'name': self.name,
            'items': [i.to_dict for i in self.items.all()]
        })

class Aisle(models.Model):
    number = models.PositiveSmallIntegerField(null=False)
    description = models.TextField(null=False)

    def to_dict(self):
        return {
            'number': self.number,
            'description': self.description
        }

class Item(models.Model):
    name = models.TextField(null=False)
    quantity = models.TextField(null=True)
    user_added = models.TextField(null=False)
    aisle = models.ForeignKey(Aisle, null=True)
    added = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            'name': self.name,
            'quantity': self.quantity,
            'user_added': self.user_added,
            'aisle': self.aisle.to_dict(),
            'added': self.added.strftime('%Y-%m-%d %H:%M')
        }

