import json

from parser import AuchanParsing


def get_product_all():
    print("Получам Id списков магазинов по регионам Мск и СПб")
    list_shop_msk = AuchanParsing.get_shops(1)
    list_shop_spb = AuchanParsing.get_shops(2)

    print("Получаем список уникальных продуктов в наличии для каждого региона")
    list_products_msk, list_product_id_msk = AuchanParsing.get_products(list_shop_msk)
    list_products_spb, list_product_id_spb = AuchanParsing.get_products(list_shop_spb)

    print("Формируем список товаров")
    unique_list_product_id_msk = set(list_product_id_msk)
    unique_list_product_id_spb = set(list_product_id_spb)
    unique_list_product_id_all = unique_list_product_id_msk.intersection(unique_list_product_id_spb)

    filter_list_products = list(filter(lambda product: product['id'] in unique_list_product_id_all, list_products_msk))[:100]

    file = open('products.json', 'w', encoding="utf-8")
    json.dump(filter_list_products, file, ensure_ascii=False)
    file.close()


if __name__ == "__main__":
    get_product_all()
