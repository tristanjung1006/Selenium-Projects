from openpyxl import load_workbook

# 엑셀 파일 열기
workbook = load_workbook('test.xlsx')

# 시트 선택
sheet = workbook['test']

# 특정 셀의 값 추출
value = sheet['A1'].value

# 추출한 값 출력
print(value)
