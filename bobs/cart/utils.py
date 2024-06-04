from typing import Any, Dict, List

from django.core.serializers import serialize
from products.models import Order, OrderItems


def build_context(items: List[OrderItems], order: Order) -> Dict[str, Any]:
    return {"items": items, "order": order}

def build_json_context(i: List[OrderItems], o: Order) -> Dict[str, Any]:
    i_json = serialize('json', i)
    o_json = serialize('json', [o])
    return {"items": i_json, "order": o_json}