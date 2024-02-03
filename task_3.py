import os


class FileMerger:
    def __init__(self, relative_path, name_new_file):
        self.__list_file_path = self._get_file_path(relative_path)
        self.__name_new_file = name_new_file

    def merge_files(self):
        info_list = self._get_info_list()
        self._write_file(info_list)

    def read_merged_file(self):
        print(self._read_file(self.__name_new_file))

    def _get_file_path(self, relative_path):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)
        file_list = os.listdir(file_path)

        return [os.path.join(relative_path, file_name).replace('\\', '/') for file_name in file_list]

    def _get_info_list(self):
        file_info_list = []

        for file_path in self.__list_file_path:
            rf = self._read_file(file_path)

            file_info_list.append(
                {
                    "file_name": file_path.split("/")[-1],
                    "number_lines": len(rf.splitlines()),
                    "text": rf,
                }
            )

        return sorted(file_info_list, key=lambda x: x['number_lines'])

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

    def _write_file(self, list_data):
        try:
            with open(self.__name_new_file, 'w', encoding='utf-8') as f:
                for data in list_data:
                    f.write(f'{data["file_name"]}\n{data["number_lines"]}\n{data["text"]}\n')
        except Exception as e:
            print(f"Error при записи в файл '{self.__name_new_file}': {e}")


if __name__ == "__main__":
    merger = FileMerger('sorted', 'final_file.txt')
    merger.merge_files()
    merger.read_merged_file()
