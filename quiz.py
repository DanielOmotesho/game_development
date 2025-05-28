import pgzrun

WIDTH=1000
HEIGHT=900

TITLE="quiz game"

marquee_box=Rect(0,0,900,100)
question_box=Rect(0,0,400,100)
timer_box=Rect(0,0,200,100)
skip_box=Rect(0,0,100,600)
answer_box1=Rect(0,0,130,40)
answer_box2=Rect(0,0,130,40)
answer_box3=Rect(0,0,130,40)
answer_box4=Rect(0,0,130,40)

marquee_box.move_ip(0,0)
question_box.move_ip(0,150)
timer_box.move_ip(600,150)
skip_box.move_ip(600,300)
answer_box1.move_ip(0,300)
answer_box2.move_ip(180,300)
answer_box3.move_ip(0,400)
answer_box4.move_ip(180,400)
answer_boxes=[answer_box1,answer_box2,answer_box3,answer_box4]   

score=0
time_left=10
question_file_name="questions.txt"
marquee_message=" "
is_game_over=False
questions=[]
question_count=0
question_index=0


def draw():
    screen.clear()
    screen.draw.filled_rect(marquee_box,"white")
    screen.draw.filled_rect(question_box,"yellow")
    screen.draw.filled_rect(timer_box,"red")
    screen.draw.filled_rect(skip_box,"green")
    for i in answer_boxes:
        screen.draw.filled_rect(i,"orange")


pgzrun.go()