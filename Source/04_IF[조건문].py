##########################################################################
# # 조건문 
# # - 분기문 
# #  . 조건에 따라 로직의 흐름을 나눌수 있다. (제어, 컨트롤)
# #  . 조건의 진위(참 / 거짓) 의 여부에 따라 명령의 실행 여부 를 결정한다.
##########################################################################
# # if 의 기본 문법 
# age = 19 
# if (age < 20) :
#     print("안녕하세요")
#     print("미성년자 이시군요")


# # 비교 연산자 와 if 분기문의 사용 예시
# message = input("숫자 를 입력하세요")
# value = int(message)
# if value == 5:
#     print("5입니다.")
# if value > 5 :
#     print("5 초과합니다")
# if value < 5 :
#     print("5미만입니다.")





# # 순서상 뒤쪽으로 배치되는 문자(문자 코드) 는 큰 것으로 판단
# if "A" > "a" :
#     print("대문자 A 가 더 큽니다.")
# if "A" < "a" :
#     print("소문자 a 가 더 큽니다.")

# if "Aling" < "Beaute" :
#     print("Beaute 가 후순위에 있는 문자 입니다.")



# # != :  다르다 이고 만족하면 True 를 반환
# if 4 != 5 :
#     print("4 와 5는 다릅니다.")



# # 논리 연산자. 
# # 두개 이상의 조건을 동시에 비교할 경우 사용
# value = int(input("숫자를 입력하세요"))
# if value > 0 and value <= 10 :
#     print("1 과 10 사이에 있는 수입니다.")
# if value > 10 or value <= 0 :
#     print("1 과 10 사이에있는 수가 아닙니다.")



# # 아래 와 같이 표현 할 수있다.
# value = int(input("숫자를 입력하세요"))
# if 0 < value <= 10 :
#     print("1 과 10 사이에 있는 수입니다.")



# # 논리연산자 not 의 사용예시
# # value 가 0 일 경우 비교 연산자를 통해 True 가 되지만 not 을 만나 False 로 스위칭된다. 
# # False 조건 이므로 메세지가 출력 되지 않는다. ( C# !)
# value = int(input("숫자를 입력하세요"))
# if not value == 0:
#     print("0이 아닙니다.")










##########################################################################
# # In 과 Not In 
# # 포함되어 있는지 확인.
##########################################################################
# message = "안녕하세요"
# if "안" in message :
#     print("문자 \"안\" 은 포함되어있습니다.")
# if "." not in message :
#     print("문자 \".\" 은 포함되어있지 않습니다.")



############################################################
# # 코드 블럭 과 n 개의 분기 흐름 제어 
# # - 블럭 단위
# #   . 컴퓨터가 코드를 수행하는 단위
# #   . 분기문의 경우 해당 조건에 따른 로직이 나뉘어지고 블럭 단위의 로직을 수행하게 된다.
# #   . 파이썬 언어는 들여쓰기로 블럭을 표현한다.
#############################################################
# # 메인 코드의 흐름을 두가지 분기로 나누어 하나만 실행 할 수 있도록 제어
# number = input("번호를 입력하세요")

# if number == "12345" :
#     print("1등입니다.")
# else :
#     print("꽝 입니다.")

# print("출근준비")

# # elif 
# # 상위 분기 결과 가 False 일경우 그 나머지 경우 중 조건을 만족하는 경우의 로직을 수행하도록
# # 제어하는 기능
# number = input("번호를 입력하세요")
# if number == "12345" :
#     print("1등입니다.")
# elif number == "123456" :
#     print("2등입니다.")
# else :
#     print("꽝 입니다.")
# print("출근준비")



# # if 문의 중첩 
# # if 문 내에 분기의 흐름을 N 개 생성 할 수 있다.
# # * 너무 많은 if 문을 중첩 할 경우 코드 가 복잡해지고 가독성이 떨어질 수 있다.
# number = input("번호를 입력하세요")
# if number == "12345" :
#     print("1등입니다.")
# elif number == "123456" :
#     print("2등입니다.")
# else :
#     bonus = input("보너스 번호를 입력 : ")
#     if bonus == "123458" :
#         print("3등입니다.")
#     else : print("꽝 입니다.")
# print("출근준비")




#######################################################
# # 실습 1 : 방위 에 따른 도시 표시하기
#######################################################
# dir = input("방향을 입력 하세요")

# if dir == "동": 
#     print("독도")
# elif dir == "서": 
#     print("목포")
# elif dir == "남": 
#     print("부산")
# elif dir == "북": 
#     print("서울")
# else : 
#     print("방향을 다시 입력하세요")


    







#######################################################
# # 실습 2 : 정수 를 입력 받아 5의 배수인지 확인하는 프로그램 구현
#######################################################
# ivalue = input("정수 값을 입력 하세요 : ")
# if int(ivalue) % 5 == 0 :
#     print("5의 배수를 입력하였습니다.")
# else :
#     print("5의 배수가 아닙니다.")






#######################################################
# # 실습 3 : 우유 값의 비교 
# # 서울 1 : 2500 
# # 매일 1.8 : 4200 
# # 어떤게 더 비싸냐 ? 
#######################################################
# # 매일 우유의 1리터 가격 1.8 : 4200  =  1 : ? 
# seoul = 2500
# mail = 4200 / 1.8
# if seoul == mail :
#     print("두 우유의 가격이 같습니다.")
# elif seoul > mail :
#     print("서울우유가 더 비쌉니다. : ", seoul - mail )
# else :
#     print("매일 우유가 더 비쌉니다. : ", mail - seoul)



