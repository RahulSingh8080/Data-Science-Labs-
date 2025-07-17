from data_stream import stream_data 
from transformations import filter_products, apply_discount
from summary import summarize_revenue
from pipeline import transformation_engine

pipeline = [
    filter_products(min_price=200, category='Accessories'),
    apply_discount(10, key='price'),
    summarize_revenue()
]

result = transformation_engine(stream_data(), *pipeline)
print(f"Total revenue after transformation:", result)