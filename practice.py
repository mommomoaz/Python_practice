#퀴즈- 랜덤라이브러리를 사용해서 날짜정하기 
# from random import*
# date=randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월"+str(date)+"일로 선정되었습니다.")
# h = 13
# s=2


# print("파이썬은 쉬워요")

# #4.2 슬라이싱
# jumin="980702-2188719"
# print("성별:"+jumin[7])
# print("연:"+jumin[0:2])
# print("월:"+jumin[2:4])
# print("생년월일:"+jumin[0:6])
# #[:6은 처음부터 6 직전까지 가져다 달라는 것]
# #뒤도 마찬가지
# # #맨 뒤에서 7번재부터 끝까지 

# #문자열 처리 함수 
# # python="python is amazing"
# # print(python.upper())
# # print(python[0].isupper())
# # print(len(python))
# # print(python.replace("python","java"))
# # index=python.index("n")
# # print(index)
# # index=python.index("n",index+ 1 )
# # print(index)
# # print(python.find("Java"))

# #문자열 포맷
# # print("나는 %d살입니다."%20)
# # print("나는 %s을 좋아해요."%"파이썬")
# # #%s 는 모든 것에 적용 가능
# # print("나는 %s색과 %s색을 좋아해요."%("파란","빨간"))

# #방법2
# # print("나는 {}살입니다.".format(20))
# #방법3
# # print("나는{age}살이며,{color}색을 좋아해요.".format(age=20,color="red"))

# #4-5탈출문자
# # print("백문이 불여일견\n백견이 불여일타")

# # \r:커서를 맨 앞으로 이동 
# # print("red apple\rpine")

# # #퀴즈
# # url = "http://naver.com"
# # my_str = url.replace("http://","") #규칙1
# # print(my_str)
# # my_str=my_str[:my_str.index(".")]
# # password=my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
# # print("{0}의 비밀번호는{1}입니다.".format(url,password))

# #리스트[]
# #insert 함수, pop 함수, append 함수
# # #같은 사람의 이름 세개
# # subway.append("유재석")
# # print(subway)
# # print(subway.count("유재석"))

# # cabinet={3:"유재석",100:"김태호"}
# # #유재석의 열쇄는 3, 김태호의 열쇄는 100
# # print(cabinet[3])
# # #3번캐비넷에는 유재석이. 
# # print(cabinet.get(3))
# # print(cabinet.get(5,"사용가능"))
# # #없는 숫자의 캐비넷은 사용가능하다는 것을 표시
# # #새손님
# # print(cabinet)
# # cabinet["c-20"]="조세호"
# # cabinet["3"]="김종국"
# # print(cabinet)
# # del cabinet["c-20"]
# # print(cabinet)

# # #튜플- 내용변경이나 추가가 불가한 리스트, 그러나 속도가 빠름
# # menu=("돈까스","치즈까스")
# # print(menu[0])
# # print(menu[1])

# #집합(set)
# #중복안됨, 순서 없음
# my_set={1,2,3,3,3}
# print(my_set)

# java= {"서지원","서혜빈","김한영"}
# python=set(["서지원","김한영"])

# #교집합
# print(java&python)
# #합집합
# print(java|python)
# #차집합
# print(java-python)
# python.add("누리아리")
# print(python)

#자료구조의 변경
#커피숍
menu={"아아","아포카토","바닐라아이스크림"}
print(menu,type(menu))

