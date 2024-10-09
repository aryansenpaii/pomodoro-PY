from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
rep=0
my_timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global rep
    window.after_cancel(my_timer)
    heading.config(text="TIMER",fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    rep=0
    checks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep+=1
    work_seconds=WORK_MIN*60
    short_break_seconds=SHORT_BREAK_MIN*60
    long_break_seconds=LONG_BREAK_MIN*60

    if(rep%8==0):
        heading.config(text="BREAK", fg=RED)
        countDown(long_break_seconds)
    elif(rep%2==0):
        heading.config(text="BREAK",fg=PINK)
        countDown(short_break_seconds)
    else:
        heading.config(text="WORK",fg=GREEN)
        countDown(work_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):
    global my_timer
    minutes=count//60
    seconds=count%60
    if(count>=0):
        if(seconds<10):
            canvas.itemconfig(timer_text, text=f"{minutes}:0{seconds}")
        else:
            canvas.itemconfig(timer_text,text=f"{minutes}:{seconds}")
        my_timer=window.after(100,countDown,count-1)
    else:
        start_timer()
        if(rep%2==1):
            checks.config(text="✔"*(rep//2))

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro Timer")
window.config(padx=100,pady=50,bg=YELLOW)

heading=Label(text="TIMER",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
heading.grid(row=0,column=1)

canvas=Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_image=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)

startButton=Button(text="Start",command=start_timer)
startButton.grid(row=2,column=0)

resetButton=Button(text="Reset", command=reset_timer)
resetButton.grid(row=2, column=2)

checks=Label(text="",bg=YELLOW,fg=GREEN,font=(FONT_NAME,17,"bold"))
checks.grid(row=3,column=1)


window.mainloop()