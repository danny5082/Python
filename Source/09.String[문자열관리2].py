# # 문자열의 변경 
# # 특정 문자 를 변경하는 기능. 
# svalue = "Visual Studio Code 를 이용한 python course"
# print(svalue.lower()) # 소문자로 변경
# print(svalue.upper()) # 대문자로 변경
# print(svalue) # lower() 나 upper() 메서드를 사용해도 원본데이터는 변하지 않는다.

# print(svalue.swapcase()) # 대 소문자를 스위칭.
# print(svalue.capitalize()) # 문자열 의 첫 영문자 만 대문자
# print(svalue.title()) # 문자열 의 문단 별로 첫 영문자 대문자(카멜롯 표기법)



# # 대 / 소문자 변경 기능의 활용
# # 로그인 기능 시 대 / 소문자 구별 하고 싶지 않을때 
# # 프로그램은 대 / 소문자를 구별하지만 사용자는 대 / 소문자를 다른 문자로 인식하지 않는다.
# # 로그인 기능 

# dbUserId = "Admin" # 데이터 베이스에 등록되어있는 사용자 아이디

# while True :
#     userid = input("사용자 ID 를 입력하세요").lower()
#     if userid.lower() == dbUserId.lower() :
#         print("admin 님 반갑습니다.")
#         break # 로그인 성공 시 종료.
#     else : 
#         print("아이디가 잘못 되었습니다.")





# # 공백 제거 
# svalue = "    Python    "
# print(svalue.lstrip(), '좋아요') # 문자열 왼쪽의 모든 공백을 제거.
# print(svalue.rstrip(), '좋아요') # 문자열 오른쪽의 모든 공백을 제거.
# print(svalue.strip(),  '좋아요') # 문자열 왼/오른쪽의 모든 공백을 제거.



# # 문자열의 분할 ***
# # split() : 특정 문자열을 기준으로 나눈 문자열을 리스트 로 반환.
# svalue = "Python C# C Java JavaScript"
# lists = svalue.split()
# print(lists) # () : 빈 공백을 기준으로 나눈다.


# # # 특정 문자 를 기준으로 나눌때 
# svalue = "Python,C#,C,Java,JavaScript"
# lists = svalue.split(',')
# print(lists) # (',') : , 기준으로 나눈다.




# # # 문자열이 개행 되는 시점으로 나뉠때 
# svalue = "안녕하세요\n반갑습니다."
# print(svalue.splitlines())




# # 문자열을 하나로 합칠때 join() <-> split()
# svalue = "Python,C#,C,Java,JavaScript"
# lists = svalue.split(',')
# print(lists) # (',') : , 기준으로 나눈다.
# print(' '.join(lists)) # 특정한 기준으로 결합.




# # 특정 문자열을 원하는 문자열로 변경 replace()
# svalue = "안녕하세요 OOO 입니다."
# print(svalue)
# print(svalue.replace("OOO","김범수"))



# # 문자열 에 공백을 추가 하여 정렬. 
# message  = "Hello Python" # 12 글자
# message2 = "VsCode" # 6글자
# print(message.ljust(30),":") # 오른쪽으로 18 공백
# print(message.rjust(30)) # 왼쪽으로 18 공백
# print(message.center(30)) # 좌 우 로 9자리 공백
# print(message2.center(30)) # 좌 우 로 12 자리 공백



#########################################################
# # 실습 
title = "안녕하세요 2023 안동대학교스마트팩토리 S/W 개발 교육과정을 이수하게 된 OOO 입니다. 즐겁고 보람찬 DIGITALTRANING 교육이 되었으면 합니다."
print(title)

# print('\n 1. OOO (대문자O) 를 본인의 이름으로 변경')
# result = title.replace("OOO","동상현")
# print(result)



# print("\n 2. S/W 위치 찾기 ")
# print(title.find("S/W"))


# print("\n 3. 시작 단어와 마지막 단어.")
# print(title[0], title[-1])



# print("\n 4. 문자의 앞 뒤에 \"-KDT-\" 출력")
# print("-KDT-",title,"-KDT-")




# print("\n 5. DIGITALTRANING 을 소문자로 표현 첫 글자만 대문자.")
# result = title.replace("DIGITALTRANING","DIGITALTRANING".capitalize())
# print(result)



# print("\n 6. 모든 공백을 삭제")
# result = title.replace(" ","")
# print(result)



# # 문단을 기준으로 데이터 나누기 
print("\n 7. 문단을 기준으로 데이터 행을 나누기.")
# result = title.split(".")
# for value in result : 
#     print(value)


# # 문단의 끝에 . 을 붙여 보기.
# result = title.split(".")
# for value in result : 
#     print(value,'.')

# # 문단 끝에 공백 없애기.
# result = title.split(".")
# for value in result : 
#     print(value,'.', sep="")


# # 두번째 문단의 불필요한 공백 없애기. 마지막 문단을 표현하면서 . 제거
# result = title.split(".")
# #for value in result[0:len(result)-1] : 
# for value in result[:-1] : 
#     print(value.lstrip(),'.', sep="")



# print("\n 8. 7에서 나눈 문단을 좌우 공백을 일정하게 두고 가운데 정렬")
# result = title.split(".")
# for value in result[:-1] : 
#     message = (value.lstrip()+'.').center(80)
#     print(message)