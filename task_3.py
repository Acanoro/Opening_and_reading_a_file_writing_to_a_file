import os


def get_file_path(relative_path):
    file_path = os.path.join(os.getcwd(), relative_path)
    file_list = os.listdir(file_path)

    return [os.path.join(relative_path, file_name).replace('\\', '/') for file_name in file_list]


def read_files(list_file_path):
    file_info_list = []

    for file_path in list_file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = file.read().rstrip('\n')

                file_info_list.append(
                    {
                        "file_name": file_path.split("/")[-1],
                        "number_lines": len(data.splitlines()),
                        "text": data,
                    }
                )
        except FileNotFoundError:
            print(f"Error: Файл '{file_path}' не найден.")
        except Exception as e:
            print(f"Error: {e}")

    return sorted(file_info_list, key=lambda x: x['number_lines'])


def write_file(list_data):
    try:
        with open('final_file.txt', 'w', encoding='utf-8') as f:
            for data in list_data:
                f.write(f'{data["file_name"]}\n{data["number_lines"]}\n{data["text"]}\n')
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    gfp = get_file_path('sorted')
    rf = read_files(gfp)
    wf = write_file(rf)

    print(rf)
