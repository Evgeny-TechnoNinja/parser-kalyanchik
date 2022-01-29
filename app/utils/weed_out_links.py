def weed_out_links(links: list) -> list:
    """
    Delete all duplicate product links in categories
    :param links: product link list
    :return: list of dictionaries with categories and unique product links
    """
    unique_links: list = []
    key, value = list(links[0].items())[0]
    blank = {
        key: list(set(value))
    }
    unique_links.append(blank)
    del links[0]
    for element_candidate in links:
        key_candidate, value_candidate = list(element_candidate.items())[0]
        value_candidate[:] = list(set(value_candidate))
        for idx, current_elem_candidate in enumerate(value_candidate):
            for element_accomplished in unique_links:
                value_accomplished = list(element_accomplished.values())[0]
                for current_elem_accomplished in value_accomplished:
                    if current_elem_candidate == current_elem_accomplished:
                        del value_candidate[idx]
        unique_links.append({key_candidate: value_candidate})
    return unique_links

