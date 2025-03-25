class EcommerceApp:
    def __init__(self):
        self.products = {
            1: {"name": "Laptop", "price": 1200},
            2: {"name": "Smartphone", "price": 800},
            3: {"name": "Headphones", "price": 150},
            4: {"name": "Smartwatch", "price": 200},
        }
        self.cart = {}

    def display_menu(self):
        print("\nWelcome to the E-Commerce App!")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

    def display_products(self):
        print("\nAvailable Products:")
        for id, product in self.products.items():
            print(f"{id}. {product['name']} - ${product['price']}")

    def add_to_cart(self):
        self.display_products()
        product_id = input("Enter the product ID to add to the cart: ")

        if product_id.isdigit():
            product_id = int(product_id)

            if product_id in self.products:
                quantity = input("Enter the quantity: ")

                if quantity.isdigit():
                    quantity = int(quantity)

                    if product_id in self.cart:
                        self.cart[product_id]["quantity"] += quantity
                    else:
                        self.cart[product_id] = {
                            "name": self.products[product_id]["name"],
                            "price": self.products[product_id]["price"],
                            "quantity": quantity,
                        }
                    print(f"Added {quantity} of {self.products[product_id]['name']} to the cart.")
                else:
                    print("Invalid quantity. Please enter a number.")
            else:
                print("Invalid product ID.")
        else:
            print("Invalid product ID. Please enter a number.")

    def view_cart(self):
        if not self.cart:
            print("\nYour cart is empty.")
        else:
            print("\nYour Cart:")
            total = 0
            for item in self.cart.values():
                subtotal = item["price"] * item["quantity"]
                total += subtotal
                print(f"{item['name']} - ${item['price']} x {item['quantity']} = ${subtotal}")
            print(f"Total: ${total}")

    def checkout(self):
        if not self.cart:
            print("\nYour cart is empty. Add items before checking out.")
        else:
            self.view_cart()
            print("\nThank you for shopping with us!")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.display_products()
            elif choice == "2":
                self.add_to_cart()
            elif choice == "3":
                self.view_cart()
            elif choice == "4":
                self.checkout()
            elif choice == "5":
                print("\nThank you for using the E-Commerce App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again!")

app = EcommerceApp()
app.run()