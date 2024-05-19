def apply_discount(products, minimum_price, discount_rate):
    # 割引を適用するラムダ関数
    discount = lambda price: price * (1 - discount_rate / 100)
    
    # リスト内包表記でフィルタリングと割引適用
    discounted_products = [
        (product["name"], discount(product["price"]))
        for product in products
        if product["price"] >= minimum_price
    ]
    
    return discounted_products

# 入力と出力の例
products1 = [
    {"name": "Laptop", "category": "Electronics", "price": 1200},
    {"name": "Bread", "category": "Food", "price": 2},
    {"name": "Jacket", "category": "Apparel", "price": 100}
]
minimum_price1 = 50
discount_rate1 = 10
output1 = apply_discount(products1, minimum_price1, discount_rate1)
print(output1)  # [("Laptop", 1080.0), ("Jacket", 90.0)]

products2 = [
    {"name": "Smartphone", "category": "Electronics", "price": 800},
    {"name": "Sneakers", "category": "Footwear", "price": 120},
    {"name": "Coffee", "category": "Beverage", "price": 5}
]
minimum_price2 = 100
discount_rate2 = 15
output2 = apply_discount(products2, minimum_price2, discount_rate2)
print(output2)  # [("Smartphone", 680.0), ("Sneakers", 102.0)]
