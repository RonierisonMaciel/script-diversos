import re
import json

class DisplayNameExtractor:
    def __init__(self, input_files):
        self.input_files = input_files

    def extract_display_names(self):
        display_names = []
        for input_file in self.input_files:
            with open(input_file, 'r', encoding='utf-8') as file:
                content = file.read()

            pattern = r"@DisplayName\(\"(.*?)\"\)"
            matches = re.findall(pattern, content, re.DOTALL)
            display_names.extend(matches)

        return display_names

    def convert_to_json(self, display_names):
        output = []

        for display_name in display_names:
            item = {
                "description": display_name,
                "bonus": False
            }
            output.append(item)

        return output

    def write_to_json_file(self, data, output_file):
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def run(self, output_file):
        display_names = self.extract_display_names()
        json_data = self.convert_to_json(display_names)
        self.write_to_json_file(json_data, output_file)

if __name__ == "__main__":
    files = ['file1.java', 'file2.java', 'file3.java']
    extractor = DisplayNameExtractor(files)
    extractor.run('output.json')
