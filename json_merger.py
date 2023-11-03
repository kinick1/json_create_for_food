import json

# JSON 파일 리스트
json_files = ['Kimchi_Fried_Rice.json', 'Chicken_Noodle.json']

merged_data = []

# 각 JSON 파일을 읽고 데이터를 병합
for json_file in json_files:
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        merged_data.append(data)

# 병합된 데이터를 새로운 JSON 파일에 저장
with open('Food_recipe.json', 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, ensure_ascii=False, indent=4)
