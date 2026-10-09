from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Products list
products = [
    {'id': 1, 'name': 'Iphone', 'price': 45000},
    {'id': 2, 'name': 'Redmi', 'price': 35000},
    {'id': 3, 'name': 'Realme', 'price': 25000},
    {'id': 4, 'name': 'Vivo', 'price': 15000},
]

# Login page
def entry_page(req):
    return render(req, 'login.html')

# Login action
def login(req):
    print(req.POST.get('username'))
    print(req.POST.get('password'))

    db_user = 'lavanya'
    db_pass = 'lav@123'

    if db_user == req.POST.get('username') and db_pass == req.POST.get('password'):
        return HttpResponse('login success!')
    else:
        return HttpResponse('invalid credentials')

# Display all products & Add product
def all_product(req):
    if req.method == 'POST':
        p_name = req.POST.get('prod_name')
        p_price = req.POST.get('price')
        p_id = len(products) + 1
        
        new_product = {
            'id': p_id,
            'name': p_name,
            'price': p_price
        }
        products.append(new_product)
        
    return render(req, 'home.html', {'products': products})

# Delete product
def delete_product(req, id):
    for product in products:
        if product['id'] == int(id):
            products.remove(product)
            break
            
    return render(req, 'home.html', {'products': products})
def update_product(req,id):
    if req.method=='POST':
        p_name=req.POST.get("name")
        p_price=req.POST.get("price")
        for product in products:
            if product.get('id')==id:
                product['name']=p_name
                product['price']=p_price
                return render(req, 'home.html', {'products': products})
    required_product=None
    for product in products:
        if(product).get('id')==id:
            required_product=product
    return render(req,'update.html',{'product':required_product})

# Display single product
def set_product(req, id):
    for product in products:
        if product['id'] == int(id):
            return JsonResponse(product)
            
    return JsonResponse({'error': 'Product not found'})
    