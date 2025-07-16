import streamlit as st

# --- Product and Customer Classes (same as yours) ---
class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock_quantity = stock_quantity

    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock_quantity

    def update_stock(self, quantity):
        if quantity <= self.__stock_quantity:
            self.__stock_quantity -= quantity
            return True
        return False

    def __str__(self):
        return f"{self.__name} (ID: {self.__product_id}) - ₹{self.__price}, Stock: {self.__stock_quantity}"


class Customer:
    def __init__(self, customer_id, name):
        self.__customer_id = customer_id
        self.__name = name
        self.__cart = []

    def add_to_cart(self, product, quantity):
        if product.update_stock(quantity):
            self.__cart.append({'product': product, 'quantity': quantity})
            return True
        return False

    def calculate_total(self):
        total = 0
        for item in self.__cart:
            total += item['product'].get_price() * item['quantity']
        return total

    def display_summary(self):
        summary = f"\nPurchase Summary for {self.__name}:\n"
        for item in self.__cart:
            pname = item['product'].get_name()
            qty = item['quantity']
            price = item['product'].get_price()
            summary += f"- {pname} x{qty} = ₹{price * qty}\n"
        summary += f"Total Bill: ₹{self.calculate_total()}"
        return summary

    def get_cart(self):
        return self.__cart

    def get_name(self):
        return self.__name


class PremiumCustomer(Customer):
    def __init__(self, customer_id, name, discount_percent):
        super().__init__(customer_id, name)
        self.__discount_percent = discount_percent

    def calculate_total(self):
        total = super().calculate_total()
        discount = total * self.__discount_percent / 100
        return total - discount

    def display_summary(self):
        summary = f"\n(Premium) Purchase Summary for {self.get_name()}:\n"
        for item in self.get_cart():
            pname = item['product'].get_name()
            qty = item['quantity']
            price = item['product'].get_price()
            summary += f"- {pname} x{qty} = ₹{price * qty}\n"
        original_total = super().calculate_total()
        summary += f"Original Bill: ₹{original_total}\n"
        summary += f"Discount Applied: {self.__discount_percent}%\n"
        summary += f"Discounted Bill: ₹{self.calculate_total()}"
        return summary


# --- Initialize Products in Session State ---
if 'products' not in st.session_state:
    st.session_state.products = {
        1: Product(1, "Laptop", 60000, 10),
        2: Product(2, "Mouse", 500, 50),
        3: Product(3, "Keyboard", 1000, 30),
        4: Product(4, "Monitor", 12000, 15),
    }

# --- Initialize Customer in Session State ---
if 'customer' not in st.session_state:
    st.session_state.customer = None


# --- UI Section ---
st.title("Retail Store Calculator (OOP + Streamlit)")

name = st.text_input("Enter Customer Name")
customer_type = st.selectbox("Customer Type", ["Regular", "Premium"])
discount = 10 if customer_type == "Premium" else 0

if name and st.session_state.customer is None:
    if customer_type == "Regular":
        st.session_state.customer = Customer(1, name)
    else:
        st.session_state.customer = PremiumCustomer(1, name, discount)
    st.success(f"{customer_type} Customer Created: {name}")

product_names = {p.get_id(): f"{p.get_name()} (₹{p.get_price()} | Stock: {p.get_stock()})"
                 for p in st.session_state.products.values()}
product_id = st.selectbox("Select Product", options=list(product_names.keys()), format_func=lambda x: product_names[x])
quantity = st.number_input("Enter Quantity", min_value=1, step=1)

if st.button("Add to Cart"):
    product = st.session_state.products[product_id]
    success = st.session_state.customer.add_to_cart(product, quantity)
    if success:
        st.success(f"{quantity} x {product.get_name()} added to cart.")
    else:
        st.error(f"Not enough stock for {product.get_name()}.")

# --- Display Cart Summary ---
if st.button("Show Bill Summary"):
    st.subheader("Bill Summary")
    st.text(st.session_state.customer.display_summary())