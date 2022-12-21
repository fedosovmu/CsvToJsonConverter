from csv_to_json_converter import CsvToJsonConverter


if __name__ == '__main__':
    converter = CsvToJsonConverter()
    converter.clear_csv_from_empty_strings('translations/translations.csv')
    converter.convert('translations/translations.csv', 'translations/ru.json', 'translations/en.json')
