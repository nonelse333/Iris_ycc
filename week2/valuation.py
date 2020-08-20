#해당 기업명을 입력하세요
name = "삼성물산"
# 시총과 추정손익 값을 반영하세요
mkcap = 213986
ni = 11183
per = mkcap / ni

line_e = f"{name}의 PER 값은 {per}로 산정됩니다"
print(line_e)

#순자산 값을반영하세요
na = 252494
pbr = mkcap / na

line_b = f"{name} PBR 값은 {pbr}로 산정됩니다"
print(line_b)

