##                                                                                                             
#   창의소프트웨어입문 개인과제1_로또번호 생성 프로그램                                                              
#   201821052_김규래                                                                           
#                                                                                                  
import random # 랜덤 모듈 import                                                              
rep = "y" # 게임을 여러번 진행하기 위한 반복문의 조건을 만족시키는 변수                                        
print("로또번호 자동생성 프로그램입니다.") # 프로그램 시작을 알리는 print                                        
# 게임을 여러번 진행하기 위해서 while반복문을 사용하였다.                                                 
while rep == "y" or rep == "Y":                                                      
    # number 변수에 input()함수로 입력값을 저장한다.                                     
    # input() 내용은 사용자로 하여금 어떤 값을 입력해야할지 지시할 수 있다.                    
    # input()의 입력값 자료형은 string이므로 int()로 자료형을 int로 바꾼다.                   
    number = int(input("구매할 로또의 개수를 입력하세요: "))                             
    include = input("포함하고 싶은 숫자를 입력하세요.(랜덤입력 시 일반생성됩니다.) : ")        
    # for 반복문으로 6개의 로또번호를 가진 로또를 number 값에 따라 몇 장 생성할지 정한다.                         
    for num in range(number):                                                     
        # print()함수에서 {}안의 num을 통해 몇 번째 로또인지 알려준다.                             
        # 이때 num은 0부터 시작하므로 +1을 하여 알맞은 정보를 전달한다.                              
        # print 함수의 end 매개변수는 기본값으로 개행(\n)을 가진다.                                  
        # 로또 번호가 같은 줄에 있어야 하므로 기본매개변수를 ""로 변경해주어 개행을 막는다.             
        print(f"{num+1}번 로또 : ", end="")                                       
        lotto = [] # 로또 번호를 저장하는 lotto 리스트를 생성한다.                             
        # 입력한 포함 수가 숫자가 맞는지 판단하는 조건문이다. isdigit() 숫자인지 판별해다.                 
        if include.isdigit() == True:                                                    
            # 입력한 포함수를 리스트에 추가한다.                                              
            # 이때 include는 string 자료형이므로 int()를 사용하여 숫자로 변환시켜준다.                    
            lotto.append(int(include))                                                
        # 필요한 랜덤 수는 총 6개이므로 lotto의 길이가 6이 될 때까지 while 반복문을 돌다.                  
        while len(lotto) != 6:                                                        
            # random모듈의 randiant 함수를 통해 1~45의 수 중 임의의 숫자를 L에 저장다.               
            L = random.randint(1,45)                                                 
            # lotto에 중복된 수를 막기 위한 조건문이다. L값이 존재한다면 반복문을 돌린다.                   
            if L not in lotto:                                                        
                # append()함수로 L을 lotto에 추가한다.                                   
                # 조건문을 만족시키지 않는다면 lotto의 요소가 추가되지 않으므로 반복한다.            
                lotto.append(L)                                                          
        # list.sort() 함수를 통해 사용하여 저장된 수들을 오름차순으로 정리한다.                  
        lotto.sort()                                                                 
        # 리스트에 저장된 로또 번호 6개를 for반복문을 통해 출력한다.                                          
        # 이때 lottery는 한 개의 번호로 lotto의 요소들을 한번씩 lottery에 저장한다.                            
        for lottery in lotto:                                                                  
            # 생성된 로또 번호를 lottery를 통해 접근하고 하나씩 출력한다.                                   
            # print() 함수의 end의 기본본매개변수인 개행대신 ""를 사용한다.                                 
            print(lottery, end=" ")                                                             
        print() # 개행을 위한 print                                                                
    print("로또번호가 생성 되었습니다.") # 로또번호가 생성됨을 알려준다.                                       
    # 게임을 다시 진행할지 입력을 받고 while문의 조건에 따라 반복을 하거나 게임을 종료한다.                           
    rep = input("다시 하시시려면 Y를 입력하세요. (종료를 원하시면 아무거나 입력하세요) :")                                                  
print("로또번호 자동생성 프로그램이 종료되었습니다.") # 프로그램 종료를 알리는 print       
