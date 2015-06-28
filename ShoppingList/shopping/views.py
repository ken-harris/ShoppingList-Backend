import json

from django.http import HttpResponse

from shopping.models import ShoppingList, Item


def create_list(request):
    shopping_list = ShoppingList.objects.create(name=json.loads(request.body.decode('utf-8')).get('name'))

    return HttpResponse(shopping_list.to_json(), status=200, content_type='application/json')

def get_lists(request):
    shopping_lists = list(ShoppingList.objects.all())
    return HttpResponse(json.dumps(shopping_lists), status=200, content_type='application/json')

def create_item_for_list(request, list_id):
    try:
        shopping_list = ShoppingList.objects.get(pk=list_id)
    except ShoppingList.DoesNotExist:
        return HttpResponse(json.dumps({'error': "Shopping list does not exist."}), status=400, content_type='application/json')
    item_data = json.loads(request.body.decode('utf-8'))
    item = Item.objects.create(**item_data)
    shopping_list.items.add(item)
    return HttpResponse(status=200)

def get_items_for_list(request, list_id):
    try:
        shopping_list = ShoppingList.objects.get(pk=list_id)
    except ShoppingList.DoesNotExist:
        return HttpResponse(json.dumps({'error': "Shopping list does not exist."}), status=400, content_type='application/json')
    return HttpResponse(json.dumps([i.to_dict() for i in shopping_list.items]), status=200, content_type='application/json')

