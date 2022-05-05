import functools


def transformation_name(func):
    """
    This is a decorator function
    Convert category names to the desired string form, for future use
    :param func: function name create_yml_document
    :return: object with renamed categories
    """
    @functools.wraps(func)
    def wrap(data: list):
        ASSIST = {
            "name": [("rashodniki", "Расходники"),
                     ("accessories", "Аксессуары"),
                     ("component", "Комплектующие"),
                     ("kaljany", "Кальяны")]
        }
        for current_name in ASSIST["name"]:
            for item in data:
                name: str = item["category"]["category_name"]
                if current_name[0] == name:
                    item["category"]["category_name"] = name.replace(name, current_name[1])
                    for current_product in item["goods"]:
                        goods_category_name: str = current_product["product"]["category"]
                        current_product["product"]["category"] = goods_category_name.replace(
                            goods_category_name, current_name[1])
        return func(data)
    return wrap
