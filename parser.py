import requests


class AuchanParsing:
    @staticmethod
    def get_shops(region_id):
        list_shop_id = []
        params = {
            'regionId': region_id
        }
        response = requests.get(url='https://www.auchan.ru/v1/shops', params=params)
        response_json = response.json()
        for shop in response_json['shops']:
            list_shop_id.append(shop['merchant_id'])
        return list_shop_id

    @staticmethod
    def get_products(list_shop_id):
        list_products = []
        list_product_id = []
        for shop in list_shop_id:
            params = {
                'merchantId': shop,
                'perPage': 1000
            }
            body = {
                "filter": {"category": "molochnye_kokteyli_napitki", "promo_only": False, "active_only": False, "cashback_only": False}
            }
            print(f"Получаем список товаров из магазина {shop}")
            response = requests.get(url='https://www.auchan.ru/v1/catalog/products', params=params, json=body)
            response_json = response.json()

            for product in response_json['items']:
                if product['stock']['qty'] > 0 and product['productId'] not in list_product_id:
                    list_product_id.append(product['productId'])
                    list_products.append(dict(
                        id=product['productId'],
                        title=product['title'],
                        url=f'https://www.auchan.ru/product/{product["code"]}/',
                        regular_price=product['oldPrice']['value'] if product['oldPrice'] is not None else product['price']["value"],
                        promo_price=product['price']["value"],
                        brand=product['brand']['name']))

        return list_products, list_product_id




