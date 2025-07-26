import requests as rq

get1Url = "https://api.restful-api.dev/objects"

def callGetMethod(Url):
    try:
        response = rq.get(Url)
        if response.status_code == 200:
            data = response.json()

            #  Filter products where price > 500 using lambda
            filtered_products = list(filter(
                lambda product: product.get('data') 
                and product['data'].get('price') 
                and product['data']['price'] > 500,
                data
            ))

            print(f" Products with price > 500 ({len(filtered_products)} found):\n")
            for product in filtered_products:
                print(f" ID: {product.get('id')}")
                print(f" Price: {product['data']['price']}")
                print(f" Name: {product.get('name')}")
                print("-" * 30)
        else:
            print(f" Request failed with status code: {response.status_code}")
    except Exception as e:
        print(f" Exception occurred: {e}")

callGetMethod(get1Url)