## Summarize Total revenue with reduce. 

from functools import reduce

def summarize_revenue():
    def _summarize(data):
        return reduce(lambda acc, item: acc + item['price'] * item['quantity'], data, 0.0)
    return _summarize
