from product import Product
import repo
while True:
  print("1 - Add Product")
  print("2 - Search Product")
  print("3 - Update Product")
  print("4 - Delete Product")
  print("5 - Print All Product")
  print("6 - Exit")
  choice = int(input())
  if choice == 1:
    print("Enter Id")
    id = int(input())
    print("Enter Name")
    name = input()
    print("Enter Description")
    desc = input()
    print("Enter Price:")
    price = input()
    print("Enter Stock:")
    stock = input()
    repo.add_product(Product(id=id, name=name, description = desc, price = price, stock = stock))
  elif choice == 2:
    print("Enter id to search:")
    id = int(input())
    old_product = repo.search_product(id)
    if not old_product:
       print("Product not found")
    else:
       print("Searched Employee: ", old_product)
  elif choice == 3:
    print("Enter id to update")
    id = int(input())
    print("Enter stock to update")
    stock = int(input())
    repo.update_product(id, stock)
  elif choice == 4:
    print("Enter id to delete")
    id = int(input())
    old_product = repo.search_product(id)
    if not old_product:
        print("Product not found")
    else:
        print(old_product)
        if input('Are you sure to delete(y/n)?').upper() == 'Y':
                repo.delete_product(id)

        print(f'Product deleted successfully')

  elif choice == 5:
    products = repo.read_all_products()
    if len(products) == 0:
      print('No product exist.')
    else:
      print('List of Products:')
      for product in products:
        print(product)
  elif choice == 6:
     print("Exiting program")
     break
  else:
    print("Re-enter invalid choice")
