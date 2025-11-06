from db_setup import session, Product


def read_all_products():
    products = session.query(Product).all()
    return products

def add_product(product):
      session.add(product)
      session.commit()
      print("Product added successfully")

def search_product(id):
    employee = session.query(Product).filter_by(id = id).first()
    return employee


def update_product(id, stock):
    old_product = search_product(id)
    if old_product:
        old_product.stock = stock
        session.commit()
        print("Product updated successfully")
    else:
        print("product not found")

def delete_product(id):
    old_product = search_product(id)
    if not old_product:
        print("Product Not Found")
        return
        
    session.delete(old_product)
    session.commit()
    print("Product deleted successfully")

        