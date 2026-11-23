from products import Product
from store import Store

def start(store_obj: Store):
    """
    Displays an interactive menu for the store management system
    and handles user choices.
    """
    while True:
        print("\n--- Store Menu ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":

            print("------")
            active_products = store_obj.get_active_products()
            if not active_products:
                print("No products available.")
            else:
                for idx, p in enumerate(active_products, start=1):
                    print(f"{idx}. ", end="")
                    p.show()

            print("------")

        elif choice == "2":
            total_qty = store_obj.get_total_quantity()
            print(f"Total of items in store: {total_qty}")

        elif choice == "3":
            print("\n--- Make an Order ---")
            active_products = store_obj.get_active_products()
            if not active_products:
                print("No products available to order.")
                continue

            for idx, p in enumerate(active_products, start=1):
                print(f"{idx}. {p.name} — Price: ${p.price}, Stock: {p.quantity}")

            try:
                prod_idx = int(input("Select product number to buy: ")) - 1
                if 0 <= prod_idx < len(active_products):
                    chosen_product = active_products[prod_idx]
                    quantity = int(input(f"Enter quantity of {chosen_product.name} to buy: "))

                    order_list = [(chosen_product, quantity)]
                    total_cost = store_obj.order(order_list)
                    print(f"✅ Order successful! Total cost: ${total_cost}")
                else:
                    print("❌ Invalid product number selected.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


def main():
    # Setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = Store(product_list)

    # Start the interactive menu loop
    start(best_buy)


if __name__ == "__main__":
    main()
