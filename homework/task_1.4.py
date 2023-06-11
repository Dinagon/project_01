titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',  # словарь кодов товаров
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}
store = {          # словарь с количеством и ценой по коду товара
    '100000110': [{'quantity': 31, 'price': 1637}],   
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}
for i in titles:
    q=0
    s=0
    for j in store[titles[i]]:
        q+=j['quantity']       
        s+=j['quantity'] * j['price']
    print(i,'-',q,'шт, стоимость',s,'руб')  # суммарная стоимость каждого товара  