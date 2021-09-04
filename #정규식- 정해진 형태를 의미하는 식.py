#정규식- 정해진 형태를 의미하는 식
#주민등록번호처럼. 
import re
p=re.compile("ca.e")#.: 하나의 문자를 의미. case cake 처럼
#^ : 문자열의 시작을 의미
#(^de)desk, destination 등
# $: 문자열의 끝을 의미. se$이면 case, base같은 것

m=p.match("case")
print(m.group())#매치 되지 않으면 에러가 발생 

if m:
    print(m.group())
else:
    print("매칭되지 않음 ")
