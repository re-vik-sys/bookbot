def get_count_of_words(total_of_words: str) -> int:
    total = total_of_words.split()
    return len(total)



def sort_on(param: tuple[str,int]) -> int: # helper function, used to sort in chars_dict_to_sorted_list as "key=sort_on"
    return param[1]



def chars_dict_to_sorted_list(to_sort: dict[str, int]) -> list[tuple[str,int]]:
    result: list[tuple[str, int]] = []
    for i in to_sort:
        count = to_sort[i]
        result.append((i, count))

    return sorted(result, reverse=True, key=sort_on)


def book_text_to_dict(conversions: str) -> dict[str, int]:
    result = {}
    for conversion in conversions:
        conversion = conversion.lower()

        if conversion in conversions:
            if conversion not in result:
                result[conversion] = 0

            result[conversion] += 1

    return result
