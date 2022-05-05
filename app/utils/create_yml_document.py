from yattag import Doc, indent
from config import XML_VERSION, DATA_HEADER_YML, DATA_CURRENCY_YML, FILE_TARGET  # noqa
from settings_ui import DIALOGUE  # noqa
from datetime import datetime
from .transformation_name import transformation_name


@transformation_name
def create_yml_document(data: list):
    """
    Creates xml document in yml standard
    :param data: goods object
    :return: An object with the quantity of goods,
    the name of the created file, a message about the work done
    """
    assist = {
        "characters": ["\n", "●", "⚜"]
    }
    result = {
        "total_products": 0,
        "filename": "",
        "msg": ""
    }
    goods: list = data
    doc, tag, text = Doc().tagtext()
    doc.asis(XML_VERSION)
    with tag("yml_catalog", data=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))):
        with tag("shop"):
            # header
            for key, value in DATA_HEADER_YML.items():
                with tag(key):
                    text(value)
            with tag("currencies"):
                doc.stag("currency", id=DATA_CURRENCY_YML[0], rate=DATA_CURRENCY_YML[1])
            with tag("categories"):
                counter_id = 0
                goods_categories = []
                for item in goods:
                    category, category_id = item[list(item.keys())[0]].values()
                    goods_categories.append((category, str(category_id + counter_id)))
                    counter_id += 1
                for items in goods_categories:
                    item_name, item_id = items
                    with tag("category", id=item_id):
                        text(item_name)
            # body
            with tag("offers"):
                for item in goods:
                    all_current_products = item[list(item.keys())[1]]
                    result["total_products"] += len(all_current_products)
                    product_content_keys = list(item["goods"][0]["product"].keys())
                    for products in all_current_products:
                        for current_product in products.values():
                            with tag("offer", id=current_product.get(product_content_keys[0]),
                                     available=current_product.get(product_content_keys[1])):
                                with tag("url"):
                                    text(current_product.get(product_content_keys[2]))
                                with tag("price"):
                                    text(current_product.get(product_content_keys[3]))
                                with tag("currencyId"):
                                    text(current_product.get(product_content_keys[4]))
                                with tag("categoryId"):
                                    current_category = current_product.get(product_content_keys[-1])
                                    for elements in goods_categories:
                                        if elements[0] == current_category:
                                            text(elements[1])
                                for picture in current_product.get(product_content_keys[5]):
                                    if picture:
                                        with tag("picture"):
                                            text(picture)
                                with tag("name"):
                                    text(current_product.get(product_content_keys[6]))
                                description = current_product.get(product_content_keys[7])
                                if description:
                                    with tag("description"):
                                        for num in range(3):
                                            description = description.replace(assist["characters"][num], "", len(description)) # noqa
                                        text(description)
                                parameters = current_product.get(product_content_keys[8])
                                if parameters:
                                    for current_parameter in parameters:
                                        for current_key, current_value in current_parameter.items():
                                            if current_value:
                                                with tag("param", name=current_key):
                                                    text(current_value)
    with open(FILE_TARGET, "w") as f:
        for line in indent(doc.getvalue()):
            f.write(line)
        result["msg"] = DIALOGUE["ready_yml"]
    result["filename"] = FILE_TARGET
    return result
