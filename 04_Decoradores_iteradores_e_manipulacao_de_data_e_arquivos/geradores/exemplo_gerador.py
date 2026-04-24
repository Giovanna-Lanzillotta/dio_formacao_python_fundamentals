# Geradores


# Exemplo de código

#import requests

# def fetch_products(api_url, max_pages=100):
#     page = 1
#     while page <= max_pages:
#         response = requests.get(f"{api_url}?page={page}")
#         data = response.json()
#         for product in data['products']:
#             yield product
#         if 'next_page' not in data:
#             break
#         page += 1

#     # Uso do gerador
#     for product in fetch_products("http://api.exampke.com/products"):
#         print(product['name'])