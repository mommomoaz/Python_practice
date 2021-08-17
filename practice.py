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

# #자료구조의 변경
# #커피숍
# menu={"아아","아포카토","바닐라아이스크림"}
# print(menu,type(menu))

#분기
# weather=input("오늘 날씨는어때요?")
# if weather=="비"or weather=="눈":
#       print("우산을 챙기세요")
# elif weather=="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요없어요")
# temp=int(input("기온은 어때요?"))
# if 30<=temp:
#     print("너무더워요. 나가지마세요")
# elif 10<=temp and temp <30:
#     print("시원해용")

#for
# print("대기번호:1")
# print("대기번호:2")
# print("대기번호:3")
# print("대기번호:4")

# for waiting_no in [0,1,2,3,4,]:
#     print("대기번호:{0}".format(waiting_no))
# for waiting_no in range(2000]:
#     print("대기번호:{0}".format(waiting_no))

# #while
# customer = "한영"
# index = 5
# while index >= 1:
#     print("{0},커피가 준비 되었습니다.{1}번 남았어요".format(customer,index))p
#     index -=1
#     if index ==0:
#         print("커피는 페기처분 되었습니다.")

# customer = "토르"
# person = "unkown"

# while person!= customer:
#      print("{0},커피가 준비되었습니다.".format(customer))
#      person=input("이름이 어떻게 되세요?")

# countiue 와 break
# absent = [2,5]
# for student in range(1, 11):
#      if student in absent:
#          continue
#     print("{0}, 책을 읽어봐".format(student))

#출석번호가 1,2,3,4, 앞에 100을 붙이기로 ->101,102,103,104
# students=[1,2,3,4,5]
# print(students)
# students=[i+100 for i in students]
# print(students)

# #학생이름을 대문자로 변환
# students = ["iron man","hyebinseo"]
# students = [i.upper()for i in students]
# print(students)

#퀴즈
# from random import *
# cnt = 0 
# for i in range(1,51):
#     time = randrange(5,51)#5~50분
#     if 5<= time <=15:
#         print("[0] {0}번째 손님 (소요시간:{1}분)" .format(i,time))

# #함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# #반환값을 받는 함수#입금
# def deposit(balance,money):
#     print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
#     return balance + money

#기본값

# def profile(name, age, main_lang):
#     print("이름:{0}\t나이:{1}\주 사용언어:{2}"\
#         .format(name,age,main_lang))

# profile("서혜빈",24,"파이썬")
# profile("김한영",26,"씨언어")

#키워드값
# def profile(name,age,main_lang):
#     print(name,age,main_lang)

# profile(name="유재석"main_lang="파이썬"age=20)

#가변인자 *language> 내가 출력하고 싶은 만큼 할 수 있음. 
#서로 다른 갯수를 나타내고 싶을때

#지역변수와 전역변수 
#지역변수- 함수 호출이 될때 만들어졌다가 끝나면 없어지는 것

# gun= 10

# def checkpoint(soldiers):#경계근무
#     gun = 20 
#     gun= gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총": {0}".format(gun))

