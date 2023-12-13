#문제1
"""
print_even 리스트 내에 있는 값 중 짝수만 화면에 출력되도록 print_score 함수를 생성 후 결과값을 출력해주세요

print_even ([1, 3, 2, 10, 12, 11, 15])
#--------------------------------------------------------------------------------------------------------------------
print_even = [1, 3, 2, 10, 12, 11, 15]
num_2 = []
def print_score(print_even):  
    for i in range(len(print_even)):
        if print_even[i]%2 == 0:
            num_2.append(print_even[i])
    return num_2
print_score(print_even)
"""
#문제2
"""
비어있는 오즈 (oz) 클래스를 "정의" 해보세요.
#--------------------------------------------------------------------------------------------------------------------
class oz:
    pass
"""
#문제3
"""
오즈(oz) 클래스의 인스턴스를 "생성" 하고 이를 coding 변수로 할당해보세요.
#--------------------------------------------------------------------------------------------------------------------
class oz:
    pass

coding = oz()
"""
#문제4
"""
오즈(oz) 클래스에 "클래스 정복"을 출력하는 기본 생성자를 추가해주세요
#--------------------------------------------------------------------------------------------------------------------
class oz:
    def __init__(self):
        print("클래스 정복")
coding = oz()
"""
#문제5
"""
오즈 (oz) 클래스에 (이름, 나이, 코딩레벨)을 받는 생성자를 추가해주세요

coding = oz("김코", 30, "A")
#--------------------------------------------------------------------------------------------------------------------
class oz:
    def __init__(self,name,age,coding_level):
        self.name = name
        self.age = age
        self.coding_level = coding_level

coding = oz("김코", 30, "A")
"""
#문제6
"""
5번 문제에서 생성한 인스턴스의 이름, 나이, 성별을 출력해주세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다 : )

출력 결과
이름 : 김코
나이 : 30
코딩레벨 : A
#----------------------------------------------------------------------------------------------------------
class oz:
    def __init__(self,name,age,coding_level):
        self.name = name
        self.age = age
        self.coding_level = coding_level
coding = oz("김코", 30, "A")
print("이름:",coding.name)
print("나이:",coding.age)
print("코딩레벨:",coding.coding_level)
"""
#문제7
"""
오즈 (oz) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하고 who()메소드를 이용해 아래 출력 결과를 만들어주세요

출력 결과 : 이름: 김코, 나이: 30, 코딩레벨: A
#--------------------------------------------------------------------------------------------------------------------
class oz:
    def __init__(self,name,age,coding_level):
        self.name = name
        self.age = age
        self.coding_level = coding_level
    def printing(self):
        print("이름:{0},나이:{1},코딩레벨:{2}".format(self.name,self.age,self.coding_level))
coding = oz("김코", 30, "A")
coding.printing()
"""
