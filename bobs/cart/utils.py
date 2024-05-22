from django.core import serializers


def build_context(items, order):
    return {"items": items, "order": order}

def build_json_context(items, order):
    items_json = serializers.serialize('json', items)
    return {"items": items_json, "order": serializers.serialize('json', [order])}