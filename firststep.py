# 점수를 랜덤생성하기 위한 random 함수를 import하였다.
import random

# 숫자를 랜럼생성하여 점수를 각각의 학생정보에 입력
# 학생들을 리스트에 저장
# 학생리스트의 각 점수들을 환산하는 함수
# 순위를 매기기위해 총점으로 정렬하는 프로그램

# 각 점수를 종합 후 총점을 반환하는 함수로, 각 점수의 비율에 따라 계산한다
def total_score(list): 
# list 형식을 매개변수로 받고 이때 실제 실행에서는 students 리스트가 매개변수로 들어온다.
# 각 인덱스별 점수의 비율에 따라 계산한다. 필요한 점수는 5가지이므로 0~4까지의 인덱스가 총점계산에 사용된다.  
    return list[0]*0.1 + list[1]*0.2 + list[2]*0.2 + list[3]*0.3 + list[4]*0.2 

# 총점으로 학생들의 순위를 계산하는 함수
def rank_score(list):
# 리스트 형식의 변수를 매개변수로 받는다. 실제로는 students 리스트가 매개변수로 사용된다.
# ordering이라는 이름의 변수를 빈 리스트 형식으로 초기화 시켜준다.
    ordering = []
# for 반복문을 리스트(students)의 길이 함수 만큼 돌린다. 이때 반복문은 이중반복문을 사용한다.
    for i in range(len(list)):
# 정수 형태의 순위를 저장하는 변수 r이다. 순위는 1부터 시작하므로 r을 1로 초기화 시켜준다.
        r = 1
# 첫번째 반복문에서는 비교할 학생의 총점을 가져오기 위해 사용하였고, 
# 두번째 반복문에서는 비교대상이 될 학생의 인덱스를 가져오기 위해 사용했다. 
        for j in range(len(list)):
# 비교를 실제로 사용될 students리스트에서 students[N+1번째학생의점수리스트][학생의 점수] 라고 하였을 때
# 총점을 저장하고 있는 6번째 인덱스를 통해 두 학생의 총점 점수를 비교한다. 
# 만약 두번째 반복문을 실행시키며 j+1번째 학생이 i+1번째 학생보다 총점이 크다면 r의 값을 1 증가시키고 
# ordering 리스트에 추가를 한다. 리스트의 크기는 학생의 수와 같으며 순서는 각각 학생의 순서와 동일하다.
            if list[i][5] < list[j][5]: r += 1
        ordering.append(r)
# 학생의 순위가 모두 결정된 ordering 리스트 반환을 통해 실제로 사용가능하도록 만든다.
    return ordering

# 각 점수별 최댓값, 최솟값, 평균을 구하는 함수이다. 각 함수의 알고리즘은 동일하다.
# 매개변수로는 리스트와, 인덱스를 표현하는 정수를 받는다.
# 이때 idx는 학생리스트의 이중리스트의 인덱스로 학생별 idx번째의 점수를 가져오기 위함이다.
def max_score(list, idx):
# maxi이름의 변수를 빈 리스트로 초기화하여 생성한다.
# 이때 maxi에 들어가는 요소는 모든 학생들의 특정 항목의 점수들이다. 
    maxi = []
# 매개변수로 받는 list의 길이만큼 반복문을 돌린다. 
    for i in range(len(list)):
# i는 students리스트의 i번째 학생을 의미하고 매개변수로 받아온 idx를 통해 두번째 인덱스를 고정시켜 
# 해당 항목의 점수를 append()함수를 통해 maxi리스트에 추가한다.
        maxi.append(list[i][idx])
# 모든 학생의 idx번째 점수들을 maxi에 종합하였다면 max()함수를 통해 최댓값을 불러오고 그 값을 반환한다.
    return max(maxi)
def min_score(list, idx):
    mini = []
    for i in range(len(list)):
        mini.append(list[i][idx])
    return min(mini)    
def mean_score(list, idx):
    mean = []
    for i in range(len(list)):
        mean.append(list[i][idx])
# 알고리즘은 세 함수 모두 동일하지만, 평균을 구하는 함수에서는 maxi의 역할을 하는 mean리스트에서
# 저장된 값들을 sum()함수로 모두 더하고 mean의 길이로 나누어 평균 값을 반환한다.
    return sum(mean) / len(mean)

# 학생의 수를 입력하면 num값에 정수가 저장되며 기존 과제와 다르게 유동적으로 학생들의 수를 조절할 수 있게 하였다. 
num = int(input("학생 수를 입력하세요: "))
print("__________________________________________________________________________") # 꾸미기
# 학생들의 점수리스트를 담을 리스트 students를 빈 리스트로 초기화한다. 
# 이때 students[N]은 N+1번째 학생의 점수리스트를 나타낸다. 
# 따라서 students[]는 이중리스트이며 학생과 그 학생의 점수를 담는다.
students = []
# num에 저장된 수 만큼 반복문을 돌린다. 첫 번째 반복문의 인자인 i는 i+1번째 학생임을 나타낸다.
for i in range(num):
# students에 append()함수를 통해 빈 리스트를 추가하고 각 인덱스 별 변수가 리스트형식이 될 수 있도록 초기화시킨다.
    students.append([])
# 두번째 반복문은 i번째 인덱스의 학생에 각 점수를 랜덤생성하여 추가한다. 위와 마찬가지로 append함수를 통해 추가시킨다. 
    for j in range(5):
# random 모듈의 randint를 통해 0부터 99사이의 수를 랜덤생성하고 값을 append()로 i번째 학생리스트에 추가시킨다.
        students[i].append(random.randint(0,99))
# 위에서 정의한 total_score를 통해 i번째 학생의 점수를 총합하여 총점을 학생점수 리스트의 마지막에 추가한다.
# 이때 들여쓰기 단계는 첫번째 반복문의 안쪽에서 진행하며 
# 두번째 반복문이 끝난 시점은 5가지 점수가 랜덤생성 후 학생리스트에 추가된 상태이다.
    students[i].append(total_score(students[i]))
# 앞서 정의한 rank_score함수의 매개변수로 students리스트를 전달하고 계산된 순위의 리스트인 ordering 반환을 통해
# 그 값을 아래 main부분에서 사용할 수 있도록 rank라는 변수에 저장한다. 이때 rank는 rank_score의 반환형인 리스트와 같다. 
rank = rank_score(students)

# 표 형식의 출력 형태에서 각 항목을 표시하는 요소들을 directory_list라는 이름의 리스트에 저장해준다.
directory_list = ["학번", "출석", "중간", "기말", "과제", "평가", "총점", "순위"]
# 리스트의 항목들을 표 출력에 앞서 출력해준다. item은 directory_list의 각 요소를 나타낸다.
for item in directory_list:
# '%-8s'%()는 print함수 안에서 사용되며 괄호안의 자료형인 문자열형식의 값을 8칸으로 맞추어 표를 더 보기 쉽게 만들었다.
# 리스트의 요소가 하나씩 출력될 때마다 칸수가 동일하게 설정되고 print()함수의 기본 종료값인 \n을 ''로 바꾸어 줄바꿈을 안하게 하였다.
    print('%-8s'%(item), end='') # s는 문자열 자료형임을 나타낸다.
print() # 표를 알맞게 출력하기 위해 줄바꿈을 사용하기 위한 print이다.
print("==========================================================================") # 꾸미기
# students의 각 요소들을 표 형식으로 출력하는 이중 반복문이다. 
for i in range(len(students)):
# 숫자 형식과 문자 형식의 차이로 10칸을 확보하도록 하였다. i는 학생의 인덱스를 나타내므로 i+1값을 출력하였다.
    print('%-10d'%(i+1), end='') # d는 정수형 자료형임을 나타낸다.
# 두번째 반복문에서는 students[i]번째의 학생의 점수를 출력한다.
    for j in range(len(students[i])):
# i번째 학생의 j번째 점수를 반복문을 통하여 출력한다. 
# 위와 마찬가지로 10칸을 맞추었고 각 점수가 소수점 1번째까지만 출력되도록 하였다. f는 실수형 자료형임을 나타낸다.
            print('%-10.1f'%(students[i][j]), end='')
# 학생별 점수가 모두 출력되었다면 위에서 학생의 순위리스트를 반환하는 함수를 통해 저장된 rank리스트에 i번째 학생의 순위를 출력한다.
    print('%-10d'%(rank[i]))
    print("--------------------------------------------------------------------------") # 꾸미기

# 모든 학생의 점수가 출력되었다면 각 점수항목별 최댓값, 최솟값, 평균값을 출력한다. 
# 각 라인의 알고리즘은 위와 같이 세 개의 항목 모두 동일하다.
# 어떤 항목인지를 출력하는 print()함수이며, end=값을 탭과 공백을 사용하여 줄바꿈을 막고 표의 가시성을 높였다.
print("최댓값", end='\t  ')
# 출력해야 하는 최댓값의 요소는 6가지 점수들이므로 6번 반복문을 반복한다.
for i in range(6):
# max_score()함수에 students리스트와 i번째 인덱스를 매개변수로 사용한다. 
# 위와 마찬가지로 10칸을 통해 칸을 맞추었고 ''를 통해 줄바꿈을 하지 않도록 한다. 
    print('%-10.1f'%(max_score(students, i)), end='')
# 모든 점수별 최댓값이 출력되었다면 다음 항목을 출력하기 위해 줄바꿈을 진행한다.
print()
print("--------------------------------------------------------------------------") # 꾸미기
print("최솟값", end='\t  ')
for i in range(6):
    print('%-10.1f'%(min_score(students, i)), end='')
print()
print("--------------------------------------------------------------------------") # 꾸미기
print("평균값", end='\t  ')
for i in range(6):
    print('%-10.1f'%(mean_score(students, i)), end='')
print()
print("--------------------------------------------------------------------------") # 꾸미기