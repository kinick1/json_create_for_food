# json_create_for_food
만개의 레시피에서 데이터를 크롤링해서 json파일로 변경하여 데이터를 저장하는 코드
54번째 줄의 recipe_data = PageCrawler("URL") 코드에서 URL부분만 레시피 사이트의 코드를 가져오면 사용가능
55번째 줄의 save_to_json(recipe_data, 'name.json') 는 name에 저장할 json 파일의 이름을 입력하여 실행하면 해당이름의 json 파일이 저장됨

*사용시 필요사항*
vscode라는 프로그램을 이용해 작성했으며 해당 코드의 파이썬 버전은 3.12.0, pip를 이용해 
pip install beautifulsoup4
pip install requests
위 두개의 라이브러리를 cmd(명령프롬프트)에서 인스톨해야 사용이 가능함
