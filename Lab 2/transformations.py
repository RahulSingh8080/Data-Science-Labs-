## Filter products baed on rules.
def filter_products(*, min_price=None, category=None, **kwargs):
    def _filter(data):
        return filter(lambda item:
                      (min_price is None or item['price'] >= min_price) and
                      (category is None or item['category'] == category),
            data)
    return _filter 

def apply_discount(discount, /, *, key='price'):
    return lambda data:map(lambda item: {**item, key: round(item[key] * (1 - discount/100),2)}, data)
