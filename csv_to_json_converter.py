import csv, json


class CsvToJsonConverter:
    def __init__(self):
        pass

    def convert(self, path_to_csv, path_to_ru_json, path_to_en_json):
        csv_rows = self._load_csv(path_to_csv)
        ru_json_dict = self._csv_rows_to_dict(csv_rows, 'key', 'Russian')
        self._save_json(ru_json_dict, path_to_ru_json)
        en_json_dict = self._csv_rows_to_dict(csv_rows, 'key', 'English')
        self._save_json(en_json_dict, path_to_en_json)
        print('SUCCESS')

    def _load_csv(self, path_to_csv):
        with open(path_to_csv) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            return list(csv_reader)

    def _csv_rows_to_dict(self, csv_rows, key_column, value_column):
        new_dict = {}
        for row in csv_rows:
            key = row[key_column]
            value = row[value_column]
            new_dict[key] = value
        return new_dict

    def _save_json(self, json_dict, path_to_json):
        with open(path_to_json, 'w') as json_file:
            json_dump = json.dumps(json_dict, indent=2, ensure_ascii=False)
            json_file.write(str(json_dump).replace('\\\\', '\\'))