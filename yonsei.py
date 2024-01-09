keywords = ["subjtNm", "mlgRank", "mlgReflcResnCtnt"]

with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        if any(keyword in line for keyword in keywords):
            print(line.strip())
