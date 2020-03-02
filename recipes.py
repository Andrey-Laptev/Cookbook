def read_recipes(cook_b):
    with open("recipes.txt", "rt", encoding="UTF-8") as f:
        while True:
            s = f.readline()
            if not s:
                break
            if s.strip() != "":
                cook_b[s.strip()] = []
                count = int(f.readline().strip())
                for _ in range(count):
                    ingridient = f.readline().strip().split(" | ")
                    cook_b[s.strip()].append({
                        "ingridient_name": ingridient[0],
                        "quantity": int(ingridient[1]),
                        "measure": ingridient[2],
                    })

def get_shop_list_by_dishes(dishes, person_count, cook_b):
    result = {}
    for dish in dishes:
        for ing in cook_b[dish]:
            if ing["ingridient_name"] not in result.keys():
                result[ing["ingridient_name"]] = {
                    "measure": ing["measure"],
                    "quantity": ing["quantity"] * person_count,
                }
            else:
                result[ing["ingridient_name"]]["quantity"] += ing["quantity"] * person_count
    return result


def main():
    cook_book = {}
    read_recipes(cook_book)
    print()
    print("Кулинарная книга:")
    print(cook_book)
    print()
    print("Обед:")
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book))

if __name__ == "__main__":
    main()
