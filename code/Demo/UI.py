from tkinter import *
import tkinter as tk
from tkinter import filedialog, scrolledtext
from tkVideoPlayer import TkinterVideo
import datetime
import tkinter.messagebox as msgbox
import sys

from pipeline import demo

import pickle
import time

video_loaded = False  # Ensure the variable is global

# 동영상의 총 시간 업데이트 함수
def update_duration(event):
    duration = vid_player.video_info()["duration"]
    end_time["text"] = str(datetime.timedelta(seconds=duration))
    progress_slider["to"] = duration

# 프로그레스 슬라이더 업데이트 함수
def update_scale(event):
    progress_value.set(vid_player.current_duration())


merge_datas = []
def mergedatas():
    pre_text, pre_time = datas[0]
    for i in range(len(datas)):
        cur_text, cur_time = datas[i]
        
        if(pre_text != cur_text):
            merge_datas.append([pre_text, pre_time + " - " + datas[i-1][1]])
            pre_text, pre_time = datas[i]

    merge_datas.append([pre_text, pre_time + " - " + cur_time])


datas = []

def parsing_log(log):
    time.sleep(1)
    # 영상전체 프레임 추출
    global total_frame
    total_frame = log[0]['total_frame']
    video_duration = vid_player.video_info()["duration"]
    
    # parsing 행동, 프레임  
    for i in log:
        tmp = []
        tmp.append(i['action_label'])
        
        frame = i['frame']
        sec = frame2second(frame, video_duration)
        min_sec = seconds_to_minutes_and_seconds(sec)
        tmp.append(min_sec)
        
        datas.append(tmp)
        
    mergedatas()
    
def frame2second(frame, video_duration):
    framePerSecond = total_frame / video_duration

    return round(frame / framePerSecond)


# 동영상 로딩 함수
def load_video():
    global video_loaded  # 전역 변수 사용
    file_path = filedialog.askopenfilename()

    if file_path:
        vid_player.load(file_path)
        progress_slider.config(to=0, from_=0)
        play_pause_btn["text"] = "Play"
        video_loaded = True  # Update the video loading status
        progress_value.set(0)
        play_pause()
        # log = demo(file_path)
        # with open(file='log.pickle', mode='wb') as f:
        #     pickle.dump(log, f)
        with open(file='log.pickle', mode='rb') as f:
            log=pickle.load(f)
            
        parsing_log(log)
        addButton(right_frame)

        
# 동영상 시간으로 이동 함수
def seek(value):
    vid_player.seek(int(value))

# 동영상에서 일정 시간만큼 스킵하는 함수
def skip(value: int):
    vid_player.seek(int(progress_slider.get()) + value)
    progress_value.set(progress_slider.get() + value)
    
# 재생/일시정지 토글 함수
def play_pause():
    # 동영상이 로드되었는지 확인
    if not video_loaded:
        # 동영상이 로드되지 않은 경우 알림 메시지 출력
        msgbox.showinfo("Notice", "Please load a video before playing.")
        return

    if vid_player.is_paused():
        vid_player.play()
        play_pause_btn["text"] = "Pause"
    else:
        vid_player.pause()
        play_pause_btn["text"] = "Play"

# 동영상 재생이 끝났을 때 호출되는 함수
def video_ended(event):
    progress_slider.set(progress_slider["to"])
    play_pause_btn["text"] = "Play"
    progress_slider.set(0)

# 150초가 들어올 때 2:30 과 같은 형식으로 변환
def seconds_to_minutes_and_seconds(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:01d}:{seconds:02d}"

# 2:30 - 2:45 과 같은 형식으로 분과 초가 들어올때 초로 변환
def time_to_seconds(time_str):
    try:
        time_str = time_str.split(" ")[0]
        minutes, seconds = map(int, time_str.split(":"))
        total_seconds = minutes * 60 + seconds
        return total_seconds
    except ValueError:
        print("잘못된 형식의 시간입니다.")
        return None

# 특정 시간으로 동영상을 로딩하고 이동하는 함수
def load_video_at_time(seconds):
    seconds = time_to_seconds(seconds)
    vid_player.seek(seconds)

def frame(d, x, y, p, bgc):
    fr = Frame(d, width=x, height=y, bg=bgc)
    fr.pack(side=p, fill='both', padx=5, pady=5, expand=True)
    return fr

def addButton(right_frame):
    # 특정 시간으로 이동하는 버튼들
    time_buttons = []
    for data in merge_datas:
        btn = tk.Button(right_frame, text=f"%-20s: {data[1]}" % data[0], command=lambda s=data[1]: load_video_at_time(s), width=60, height=2)
        btn.pack(side="top")
        time_buttons.append(btn)


class ConsoleRedirector:
    def __init__(self, console):
        self.console = console

    def write(self, message):
        self.console.insert(tk.END, message)
        self.console.see(tk.END)  # 스크롤하여 가장 최근의 내용을 보여줌

    def flush(self):
        pass

if __name__ == '__main__':
    root = Tk()
    root.title("URIGHT Demo.")
    root.config(bg='grey17')
    root.geometry("1400x800")
    root.resizable(0, 0) 

    left_frame = frame(root, 200, 400, 'left', 'grey10')
    right_frame = frame(root, 500, 300, 'right', 'grey17')

    Label(left_frame, text="Presentation VIDEO", font="Arial", foreground="white", background='grey10').pack(side='top', padx=5, pady=7)
    Label(right_frame, text="VIDEO TIME TABLE", font="Arial", foreground="white", background='grey17').pack(side='top', padx=5, pady=7)
    
    
    # 이미지 로드
    logo_image = tk.PhotoImage(file=r"code\Demo\resorce\Upright_logo.png")

    # 이미지를 표시할 프레임 생성
    img_frame = Frame(left_frame, height=200)
    img_frame.pack(fill="both", expand=True)  # img_frame이 left_frame을 채우도록 패킹

    # 내용에 따라 크기를 조정하지 않도록 함
    img_frame.pack_propagate(0)

    # 이미지를 표시할 라벨 생성
    imglabel = Label(img_frame, image=logo_image)
    imglabel.pack(fill="both", expand=True)  # imglabel이 img_frame을 채우도록 패킹

    # TkinterVideo 객체 생성 및 설정
    vid_player = TkinterVideo(scaled=True, master=imglabel)
    vid_player.pack(expand=True)

    tool_frame = Frame(left_frame,background="black")
    tool_frame.pack(side="top",fill="both")

    # 재생/일시정지 버튼
    play_pause_btn = tk.Button(tool_frame, text="PLAY",font="Fixedsys",background="white", command=play_pause)
    play_pause_btn.pack(side="left", fill="y")

    # 동영상 로딩 버튼
    load_btn = tk.Button(tool_frame, text="Load Video",font="Fixedsys",background="white", command=load_video)
    load_btn.pack(side="left", fill="y")

    # 프로그레스 슬라이더
    progress_value = tk.IntVar(tool_frame)
    progress_slider = tk.Scale(tool_frame, variable=progress_value, from_=0, to=0, orient="horizontal", command=seek)
    progress_slider.pack(side="left", fill="both", expand=True)

    # 현재 재생 시간 표시 레이블
    start_time = Label(tool_frame, text="",font="system")
    start_time.pack(fill="both", expand=True)

    # 총 재생 시간 표시 레이블
    end_time = tk.Label(tool_frame, text=str(datetime.timedelta(seconds=0)), font="system")
    end_time.pack(fill="both",expand=True)

    # 이벤트 바인딩
    vid_player.bind("<<Duration>>", update_duration)
    vid_player.bind("<<SecondChanged>>", update_scale)
    vid_player.bind("<<Ended>>", video_ended)

    root.mainloop()