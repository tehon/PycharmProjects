i = [[['순위','1'],['영화','닥터스트레인지']],[["순위","2"],["영화","닥터이상한"]],[["순위","3"],["영화","이상한의사"]]]

for a in i:
    print(a[0])
    print(a[1])

# 오류
# i = {{{"순위","1"},{"영화","닥터스트레인지"}},{{"순위","2"},{"영화","닥터이상한"}},{{"순위","3"},{"영화","이상한의사"}}}
# 처음에 파이썬 리스트가 아닌 자바 배열을 만들어버려서 오류가 났었다...