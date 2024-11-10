from create import create_product
from read import read_products
from update import update_product
from delete import delete_product

def menu():
    while True:
        print("\nCRUD Menu:")
        print("1. Create Product")
        print("2. Read Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Enter product name: ")
            description = input("Enter product description: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            create_product(name, description, price, quantity)
        
        elif choice == "2":
            read_products()
        
        elif choice == "3":
            id = int(input("Enter product ID to update: "))
            name = input("Enter new name (or leave blank): ")
            description = input("Enter new description (or leave blank): ")
            price = input("Enter new price (or leave blank): ")
            quantity = input("Enter new quantity (or leave blank): ")
            update_product(id, name or None, description or None, float(price) if price else None, int(quantity) if quantity else None)
        
        elif choice == "4":
            id = int(input("Enter product ID to delete: "))
            delete_product(id)
        
        elif choice == "5":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
