from django.conf.urls import url, include

urlpatterns = [
        url(r'create_list/?$', 'shopping.views.create_list'),
        url(r'lists/?$', 'shopping.views.get_lists'),
        url(r'list/(?P<list_id>\d+)/create_item/?$', 'shopping.views.create_item_for_list'),
        url(r'list/(?P<list_id>\d+)/items/?$', 'shopping.views.get_items_for_list'),
]
