import turtle as t
import random
import time

t_score = t.Turtle()#"score: " 문자를 나타냄
t_score.up()
t_score.hideturtle()
t_score.goto(170, 200)
t_score.write('score: ', False,"center",("",12))#"score"문자열의 크기는 12


t_score2 = t.Turtle()#score 기록의 숫자를 나타냄
t_score2.up()
t_score2.hideturtle()
t_score2.goto(190, 200)
score=0
t_score2.write(score)


te = t.Turtle()#악당거북이
te.shape("turtle")
te.color("red")#악당 색깔 빨강
te.speed(0)
te.up()
te.goto(0, 200)#악당 처음 위치


gold = t.Turtle()#먹이
gold.shape("circle")
gold.color("green")#먹이 색깔 초록
gold.speed(0)
gold.up()
gold.goto(0, -200)#먹이 처음 위치


def turn_right():#오른쪽 키 눌렀을 때
    t.setheading(0)#주인공 거북이 머리 방향 지정
def turn_up():
    t.setheading(90)
def turn_left():
    t.setheading(180)
def turn_down():
    t.setheading(270)


t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")#주인공 거북이
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")


def play():
    global score
    t.forward(10)#주인공 10 앞으로 감
    if random.randint(1,5)==3:#25%의 확률로 악당거북이가 주인공을 따라옴
        ang = te.towards(t.pos())
        te.setheading(ang)
    te.forward(9)#악당 거북이 9 앞으로 감
    if t.distance(gold) < 12:#주인공이 먹이에 닿으면
        score=score+1#score을 1 올린다.
        t_score2.clear()#기존의 score을 지운다.
        t_score2.write(score)#바뀐 score을 써넣는다.
        star_x = random.randint(-230, 230)#먹이의 x좌표를 랜덤으로 정함
        star_y = random.randint(-230, 230)#먹이의 y좌표를 랜덤으로 정함
        gold .goto(star_x, star_y)#먹이의 새로운 좌표
    if t.distance(te) >= 12:
        t.ontimer(play, 100)#0.1초 마다 play()함수를 실행한다.
    if t.distance(te) < 12:#주인공이 악당 거북이와 부딪히면(둘의 거리가 12이하 이면)
        text= "Score: "+str(score)
        message("Game Over",text)
        te.goto(0, 200)#악당 처음 위치
        t.goto(0,0)#주인공 처음 위치
        gold.goto(0, -200)#먹이 처음 위치
        juwelshop()


def message(m1,m2):
    t.clear()
    t.goto(0,100)
    t.write(m1,False,"center",("",20))
    t.goto(0,-100)
    t.write(m2,False,"center",("",15))



def juwelshop():#play()메소드 즉, 게임이 끝나면 실행
    global score
    print("당신의 score: ", score)
    print("당신의 score로 보석을 모으세요 \n다이아몬드:70score, 에메랄드:50score, 루비:40score, 사파이어:35score, 진주:20score, 가넷:10score \n")
    jewel={70:"다이아몬드", 50:"에메랄드",40:"루비",35:"사파이어",20:"진주",10:"가넷"}
    userjewel=[] #사용자의 쥬얼리 배열

    while(True):
        while(True):
            user=input("구입할 보석을 선택하세요 \n(다이아몬드:1, 에메랄드:2, 루비:3, 사파이어:4, 진주:5, 가넷:6, 없음:0)")#구입할 보석 선택
            if(user=='1' or user=='2' or user=='3' or user=='4' or user=='5' or user=='6' or user=='0'):
                break
            else:
                print("입력값이 잘못 되었습니다. 다시 입력 하세요")


        if(user=='1'):#다이아몬드 선택했을 때
            if(score<70):
                print("구매하기엔 score이 모자랍니다.")
            else:
                score=score-70
                userjewel.append("다이아몬드")# 사용자의 쥬얼리 배열에 쥬얼리 추가
                print("구매가 완료 되었습니다.")
                
        
        if(user=='2'):#에메랄드 선택했을 때
            if(score<50):
                print("구매하기엔 score이 모자랍니다.")
            else:
                score=score-50
                userjewel.append("에메랄드")
                print("구매가 완료 되었습니다.")
        
        if(user=='3'):#루비 선택했을 때
            if(score<40):
                print("구매하기엔 score이 모자랍니다.")
            else:
                score=score-40
                userjewel.append("루비")
                print("구매가 완료 되었습니다.")
        
        if(user=='4'):#사파이어 선택했을 때
            if(score<35):
                print("구매하기엔 score이 모자랍니다.")
            else:
                score=score-35
                userjewel.append("사파이어")
                print("구매가 완료 되었습니다.")
        
        if(user=='5'):#진주 선택했을 때
            if(score<20):
                print("구매하기엔 score이 모자랍니다.")
            else:
                score=score-20
                userjewel.append("진주")
                print("구매가 완료 되었습니다.")
        
        if(user=='6'):#가넷 선택했을 때
            if(score<10):
                print("구매하기엔 score이 모자랍니다.")
            else:
                score=score-10
                userjewel.append("가넷")
                print("구매가 완료 되었습니다.")

        if(user=='0'):#없음을 선택했을 때
            break

        print("\n남은 score: ", score) #현재 score
        print("나의 보석함: ", userjewel) #나의 보석함

        if(user=='1' or user=='2' or user=='3' or user=='4' or user=='5' or user=='6'):   
            choice=input("\n더 구매 하시겠습니까? (구매:엔터, 비구매:N)") #더 구매할건지 선택
            if(choice=="n" or choice=="N"):
                break

    rere=input("\n다시 게임을 하여 score을 모으시겠습니까? (게임다시하기:Y, 종료:N)") #더 게임 할건지 선택
    if(rere=='y' or rere=='Y'):#만약 게임한다고 선택하면 play()메소드 실행
        print("3초 안에 게임 화면을 클릭하고 게임하세요\n\n\n\n\n")
        time.sleep(3)
        t.clear()
        play()
        



t.listen()#거북이 그래픽 창이 키보드 입력을 받는다.
play()#게임 실행




