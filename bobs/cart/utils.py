from typing import Any, Dict, List

from django.core.serializers import serialize
from products.models import Order, OrderItems


def build_context(items: List[OrderItems], order: Order) -> Dict[str, Any]:
    return {"items": items, "order": order}

def build_json_context(items: List[OrderItems], order: Order) -> Dict[str, Any]:
    items_json = serialize('json', items)
    return {"items": items_json, "order": serialize('json', [order])}