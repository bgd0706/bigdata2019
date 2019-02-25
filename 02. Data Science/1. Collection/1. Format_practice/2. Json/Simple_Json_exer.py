import json

with open("sample.json",encoding='UTF8') as json_file:
 json_object = json.load(json_file)
 json_string = json.dumps(json_object)
 g_json_big_data = json.loads(json_string)

print(g_json_big_data)
print(g_json_big_data[0])
# json 데이터 읽기(Read)
print(g_json_big_data[0]['레벨 2-1 키'])
print(g_json_big_data[1]['레벨 2-3 키']['레벨 3-1 키'])
# json 데이터 삽입
g_json_big_data.append({"레벨 2-4 키" : "수박"})
print(g_json_big_data)
# json 데이터 수정
g_json_big_data[0]['레벨 2-1 키'] = "체리"
# json 데이터 삭제
del g_json_big_data[2] # 요소를 완전히 날림

# json 데이터 접근하는 방법 : '레벨 4-1 키"의 키를 구해라
# {"키" : 1 , "몸무게" } -> key로 접근
# [{},{},{},{}] -> 인덱스로 접근
print(g_json_big_data[1]["레벨 2-3 키"]["레벨 3-1 키"][0]["레벨 4-1 키"])
g_json_big_data[1]["레벨 2-3 키"]["레벨 3-1 키"][0]["레벨 4-1 키"] = 24 # int형은 "" 안하게
print(len(g_json_big_data))

with open('sample_modify_json', 'w', encoding='utf8') as outfile:
 readable_result = json.dumps(g_json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
 outfile.write(readable_result)
 print('sample_modify.json SAVED')