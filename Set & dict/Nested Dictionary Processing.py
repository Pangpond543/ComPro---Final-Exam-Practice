def inventory_summary(inven) :
    
    data2 = {}
    
    for i in inven:
        if i["category"] not in data2:
            data2[i["category"]] = i["price"] * i["quantity"]
        else:
            data2[i["category"]] += i["price"] * i["quantity"]
             
    data1 = {}
    
    for i in inven:
        for k, v in i.items():
            if k == "name":
                if v not in data1:
                    data1[v] = i["price"] * i["quantity"]
                else:
                    data1[v] += i["price"] * i["quantity"]
                    
    return {'category_totals' : data2 , 'most_valuable_product' : max(data1, key=data1.get)}


#==============================

def inventory_summary2(inven) :
    cat_total_dict = {}
    product_max_dict = {}
    
    for i in inven:
        Name = i["name"]
        cat = i["category"]
        price_total = i["price"] * i["quantity"]
        
        if cat not in cat_total_dict:
            cat_total_dict[cat] = price_total
        else:
            cat_total_dict[cat] += price_total
        
        product_max_dict[Name] = price_total
        
        maximum_pro = max(product_max_dict, key=product_max_dict.get)
        
    return {'category_totals': cat_total_dict, 'most_valuable_product': maximum_pro}
        
    
inventory = [
    {"name": "Laptop", "category": "Electronics", "price": 25000, "quantity": 2},
    {"name": "Mouse", "category": "Electronics", "price": 500, "quantity": 10},
    {"name": "Chair", "category": "Furniture", "price": 3000, "quantity": 4},
    {"name": "Desk", "category": "Furniture", "price": 7000, "quantity": 2},
]

# print(inventory_summary(inventory))
print(inventory_summary2(inventory))


# output = {
#     'category_totals': {'Electronics': 55000, 'Furniture': 26000},
#     'most_valuable_product': 'Laptop'
# }
    