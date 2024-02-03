class RecipeManager:
    def __init__(self, relative_path):
        self.__relative_path = relative_path

    def get_list_by_dishes(self, dishes, person_count):
        list_dishes = self._read_file(self.__relative_path).split('\n\n')
        cook_book = self._get_cook_book(list_dishes)
        list_by_dishes = self._get_shop_list_by_dishes(cook_book, dishes, person_count)

        return list_by_dishes

    def _get_shop_list_by_dishes(self, cook_book, dishes, person_count):
        ingredient_dict = {}

        for dish in dishes:
            if dish in cook_book:
                for ingredient in cook_book[dish]:
                    ingredient_dict[ingredient["ingredient_name"]] = {
                        'measure': ingredient["measure"],
                        'quantity': ingredient["quantity"] * person_count,
                    }
            else:
                print(f"Warning: Блюдо '{dish}' не найдено в книге рецептов.")
        return ingredient_dict

    def _get_cook_book(self, list_dishes):
        cook_book = {}

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

        return cook_book

    def _read_file(self, file_path):
        data = ""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = file.read().rstrip('\n')
        except FileNotFoundError:
            print(f"Error: Файл '{file_path}' не найден.")
        except Exception as e:
            print(f"Error при чтении файла '{file_path}': {e}")

        return data


if __name__ == "__main__":
    recipe = RecipeManager('recipes.txt')
    print(recipe.get_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
