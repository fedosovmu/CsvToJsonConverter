from csv_to_json_converter import CsvToJsonConverter


if __name__ == '__main__':
    converter = CsvToJsonConverter()
    converter.clear_csv_from_empty_strings('data/translations.csv')
    converter.convert('data/translations.csv', 'data/ru.json', 'data/en.json')
