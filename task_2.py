def print_cook_book(cook_book):
    for dish, ingredients in cook_book.items():
        print(f"{dish}:")
        for ingredient in ingredients:
            print(f"  {ingredient}")
        print()


def read_recipe(file_path):
    cook_book = {}

    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            list_dishes = file.read().split('\n\n')

            for dish in list_dishes:
                dish_lines = dish.split("\n")

                name_dish = dish_lines[0]
                ingredients = []

                for ingredient_line in dish_lines[2:]:
                    ingredient_info = ingredient_line.strip().split('|')

                    ingredients.append(
                        {
                            'ingredient_name': ingredient_info[0].strip(),
                            'quantity': int(ingredient_info[1].strip()),
                            'measure': ingredient_info[2].strip()
                        }
                    )

                cook_book[name_dish] = ingredients
    except FileNotFoundError:
        print(f"Error: Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Error: {e}")

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_recipe("recipes.txt")
    ingredient_dict = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_dict[ingredient["ingredient_name"]] = {
                'measure': ingredient["measure"],
                'quantity': ingredient["quantity"] * person_count,
            }
    return ingredient_dict


if __name__ == "__main__":
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))