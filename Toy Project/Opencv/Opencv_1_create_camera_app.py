import glob
import random
import cv2 as cv
import numpy as np
from datetime import datetime

"""
기능 1. 특정 구간 영상으로 저장하기
기능 2. 단축키 설명창 띄우기
기능 3. 마우스로 그림 그리기
기능 4. 마우스로 사각형 그리고, 그 영역만 저장하기
기능 5. 특정 화면을 저장한 후, 내 서명을 원하는 위치에 넣어서 저장하기
기능 6. 여러가지 이모티콘 넣고 위치 조정하기
"""

### 그림 그리기 마우스 이벤트 
def draw_sign(event, x, y, flags, param):
    global i, line_point_list, cnt_line, oldx_line, oldy_line

    # 1. 마우스가 움직일 때, 왼쪽 버튼이 눌려져있으면
    if event == cv.EVENT_MOUSEMOVE:
        if flags & cv.EVENT_LBUTTONDOWN:

            if cnt_line == 0:
                oldx_line, oldy_line = x, y
                line_point_list.append([x, y])
                cnt_line += 1

            line_point_list.append([x, y])
            for i in range(len(line_point_list)-1):
                
                start = line_point_list[i]
                end = line_point_list[i+1]
                
                cv.line(frame, pt1=tuple(start), pt2=tuple(end), color=(0, int(i), int(255-i)), thickness=10)
                cv.imshow("frame", frame)
                
            i += 0.5
    
                
### 직사각형 그리기 마우스 이벤트
def draw_rectangle(event, x, y, flags, param):
    global cnt_rect, oldx_rect, oldy_rect, rect_list
    
    # 1. 마우스 왼쪽 버튼을 누르면
    if event == cv.EVENT_LBUTTONDOWN:
        rect_list.append([x, y])
        
    # 2. 마우스 왼쪽 버튼을 누르지 않으면 
    if event == cv.EVENT_LBUTTONUP:
        rect_list.append([x, y])
        cnt_rect = 0
        
    # 3. 마우스가 움직일 때, 왼쪽 버튼이 눌려져 있으면     
    if event == cv.EVENT_MOUSEMOVE:
        if flags & cv.EVENT_LBUTTONDOWN:
            
            if cnt_rect == 0:
                oldx_rect, oldy_rect = x, y
                rect_list.append([oldx_rect, oldy_rect])
                    
            if flags & cv.EVENT_FLAG_SHIFTKEY:
                cv.rectangle(frame, (oldx_rect, oldy_rect), (x, y), (255, 0, 0), thickness=2)
                cv.imshow('frame', frame)
                
                cnt_rect += 1
                
                
### 이미지에 서명 추가
def add_sign(dst_img):
    
    h, w, _ = dst_img.shape
    
    # 사인 마스크 생성
    sign_mask = np.zeros((h, w), dtype=np.uint8)
    img = cv.imread("data/mysign.png", cv.IMREAD_GRAYSCALE)
    _, threshold_img = cv.threshold(img, 120, 255, cv.THRESH_BINARY)
    threshold_img = cv.resize(~threshold_img, (120, 80), cv.INTER_LINEAR)
    sign_mask[h-80:h, w-120:w] = threshold_img
    
    # 사인의 색상은 노란색
    color_img = np.ones((h, w, 3), dtype=np.uint8)
    color_img[:, :, 1] = 255
    color_img[:, :, 2] = 255
    
    result = cv.copyTo(color_img, sign_mask, dst_img)
    
    return result


### 이미지에 이모티콘 추가
def add_emo(frame, h, w, emo_imgs):
    global mask_list
    
    # 1. 하단 바 그리기
    frame_copy = frame.copy()
    cv.rectangle(frame, (0, h-120), (w, h), color=(0, 0, 0), thickness=-1)
    frame = cv.addWeighted(frame_copy, 0.7, frame, 0.3, 0)
    
    # 2. 하단 바에 이모티콘 배치하기
    start_x = 10
    bar_emo_coordinate = []
    for i, img in enumerate(emo_imgs):
        
        frame[h-100:h-20, start_x:start_x+80] = cv.copyTo(img, ~mask_list[i], frame[h-100:h-20, start_x:start_x+80])
        bar_emo_coordinate.append([start_x, h-100])
        start_x += 90
    
    return frame, bar_emo_coordinate
    

### 이모티콘 추가 마우스 이벤트
def load_emo(event, x, y, flags, param):
    global emo_imgs, bar_emo_coordinate, mask_list, frame, cur_emo_coor_list
    
    # 1. 마우스 왼쪽 버튼을 누르면
    if event == cv.EVENT_LBUTTONDOWN:
        for i in range(6):
            
            start_x = bar_emo_coordinate[i][0]
            start_y = bar_emo_coordinate[i][1]
            
            if start_x < x < start_x+80 and start_y < y < start_y+80:

                emo_x, emo_y = random.randint(0, frame.shape[1]), random.randint(0, frame.shape[0]-150)
                
                frame_copy = frame.copy()
                frame[emo_y:emo_y+80, emo_x:emo_x+80] = cv.copyTo(frame_copy[emo_y:emo_y+80, emo_x:emo_x+80], mask_list[i], emo_imgs[i])
                cur_emo_coor_list[i] = [emo_x, emo_y]
                
                cv.imshow('frame', frame)
                
    # 2. 마우스가 움직일 때, 왼쪽 버튼이 눌려져 있으면 
    elif event == cv.EVENT_MOUSEMOVE:
        if flags & cv.EVENT_LBUTTONDOWN:
            
            for i in range(6):
                
                if cur_emo_coor_list[i] == None:
                    continue
                
                emo_x = cur_emo_coor_list[i][0]
                emo_y = cur_emo_coor_list[i][1]
                
                if emo_x < x < emo_x+80 and emo_y < y < emo_y+80:
                    
                    new_x = x - 40
                    new_y = y - 40
                    cur_emo_coor_list[i][0] = new_x
                    cur_emo_coor_list[i][1] = new_y

                    frame_copy = frame.copy()
                    try:
                        frame[new_y:new_y+80, new_x:new_x+80] = cv.copyTo(frame_copy[new_y:new_y+80, new_x:new_x+80], mask_list[i], emo_imgs[i])
                    except:
                        pass
                    
                    cv.imshow("frame", frame)
                        
                      
### 메인 함수
def main():
    global now, frame, line_point_list, rect_list, emo_imgs, bar_emo_coordinate, mask_list, cur_emo_coor_list

    cap = cv.VideoCapture(0)
    
    if not cap.isOpened():
        raise RuntimeError('ERROR: Unable to open camera')
    
    w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    print(f'width: {w}, height: {h}')
    
    fourcc = cv.VideoWriter_fourcc(*'DIVX')
    
    # 키보드 이벤트를 위한 delay 변수 생성
    fps = cap.get(cv.CAP_PROP_FPS)
    delay = int(1000/fps)
    
    # 플래그
    press_s_before = False
    press_h_before = False
    press_r_before = False
    press_d_before = False
    press_a_before = False
    down_bottom_bar = False
    
    # 이모티콘 및 마스크 리스트 생성
    mask_list = []
    emo_imgs = [cv.imread(img) for img in glob.glob("./data/emo*.png")]
    for i, img in enumerate(emo_imgs):
        emo_imgs[i] = cv.resize(img, (80, 80), cv.INTER_LINEAR)

        mask = emo_imgs[i].copy()
        mask[mask>0] = 255
        mask = ~mask
        mask_list.append(mask)

    # While 문 시작
    while True:
        ret, frame = cap.read()
 
        if not ret:
            print("Can't read the video frame")
            break

        now = datetime.now()

        #===============================================================#
        
        ### 특정 구간 영상으로 저장하기
        # Press s
        if press_s_before:
            copy = frame.copy()
            cv.putText(frame, "Recording", (20, 50), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 5)
            cv.imshow("frame", frame)
            out.write(copy)
        else:
            cv.imshow("frame", frame)
        
        ### 단축키 설명창 띄우기    
        # Press h
        if press_h_before:
            h_explain = "H: Press H, Description of App Shortcut Key."
            p_explain = "P: Press P, Capture the current frame, Save in <screenshot> folder."
            s_explain = "S: Press S and Press S again, The section will be saved in <video> folder."
            r_explain = "R: Press R, Select ROI and Press R again, then the roi will ve saved in <screenshot> folder."
            a_explain = "A: Press A, Click Emoji to decorate the frame. Drag the emoji to where you want to place."
            esc_explain = "ESC: Press ESC, Quit this App."
            
            start_x = 10
            start_y = 30
            
            cv.rectangle(frame, (10, 10), (640, 190), color=(0, 255, 255), thickness=-1)
            cv.putText(frame, h_explain, (start_x, start_y), cv.FONT_HERSHEY_PLAIN, 0.8, (0, 0, 0), 1)
            cv.putText(frame, p_explain, (start_x, start_y+30), cv.FONT_HERSHEY_PLAIN, 0.8, (0, 0, 0), 1)
            cv.putText(frame, s_explain, (start_x, start_y+60), cv.FONT_HERSHEY_PLAIN, 0.8, (0, 0, 0), 1)
            cv.putText(frame, r_explain, (start_x, start_y+90), cv.FONT_HERSHEY_PLAIN, 0.8, (0, 0, 0), 1)
            cv.putText(frame, a_explain, (start_x, start_y+120), cv.FONT_HERSHEY_PLAIN, 0.8, (0, 0, 0), 1)
            cv.putText(frame, esc_explain, (start_x, start_y+150), cv.FONT_HERSHEY_PLAIN, 0.8, (0, 0, 0), 1)
            cv.imshow("frame", frame)
        else:
            cv.imshow("frame", frame) 
        
        ### 마우스로 그림 그리기
        # Press d
        if press_d_before:
            cv.setMouseCallback("frame", draw_sign, frame)
            for i in range(len(line_point_list)-1):
                start = line_point_list[i]
                end = line_point_list[i+1]
                cv.line(frame, pt1=tuple(start), pt2=tuple(end), color=(0, int(i), int(255-i)), thickness=10)
            cv.imshow("frame", frame)
        else:
            line_point_list = []
            cv.imshow("frame", frame)

        ### 마우스로 사각형 그리기, 그린 사각형 영역만 저장하기
        # Press r
        if press_r_before:
            cv.setMouseCallback("frame", draw_rectangle, frame)
            cv.imshow("frame", frame)    
        else:
            cv.imshow("frame", frame)
        
        ### 여러가지 이모티콘 넣고 위치 조정하기
        # Press a
        if press_a_before and down_bottom_bar:
            
            # 모든 요소가 None인 경우
            if not any(cur_emo_coor_list):
                press_a_before = False
                down_bottom_bar = False
                cv.imshow("frame", frame) 
            else:
                for i in range(6):
                    if cur_emo_coor_list[i] == None:
                        continue
                    emo_x = cur_emo_coor_list[i][0]
                    emo_y = cur_emo_coor_list[i][1]
                    
                    frame_copy = frame.copy()
                    try:
                        frame[emo_y:emo_y+80, emo_x:emo_x+80] = cv.copyTo(frame_copy[emo_y:emo_y+80, emo_x:emo_x+80], mask_list[i], emo_imgs[i])   
                    except:
                        pass
                cv.imshow("frame", frame)    
        elif press_a_before:
            frame, bar_emo_coordinate = add_emo(frame, h, w, emo_imgs)

            cv.setMouseCallback("frame", load_emo, frame)
            for i in range(6):
                if cur_emo_coor_list[i] == None:
                    continue
                emo_x = cur_emo_coor_list[i][0]
                emo_y = cur_emo_coor_list[i][1]
                
                frame_copy = frame.copy()
                try:
                    frame[emo_y:emo_y+80, emo_x:emo_x+80] = cv.copyTo(frame_copy[emo_y:emo_y+80, emo_x:emo_x+80], mask_list[i], emo_imgs[i])   
                except:
                    pass 
            cv.imshow("frame", frame)
        else:
            cur_emo_coor_list = [None] * 6
            cv.imshow("frame", frame)
            
        #===============================================================#

        ### 키보드 이벤트
        key = cv.waitKey(delay)
        # Press p     
        if key == ord('p'):
            result = add_sign(frame)
            cv.imwrite(f"screenshot/saveImage_{now.strftime('%Y-%m-%d_%H:%M:%S')}.jpg", result)
        # Press s
        elif key == ord('s'):
            if press_s_before:
                press_s_before = False
                out.release()
            else:
                press_s_before = True
                out = cv.VideoWriter(f"video/saveVideo_{now.strftime('%Y-%m-%d_%H:%M:%S')}.avi", fourcc, 20, (w, h), isColor=True)
        # Press h
        elif key == ord('h'):
            if press_h_before:
                press_h_before = False
            else:
                press_h_before = True
        # Press d
        elif key == ord('d'):
            if press_d_before:
                press_d_before = False
            else:
                press_d_before = True
        # Press r
        elif key == ord('r'):
            if press_r_before:
                press_r_before = False
                
                minx = rect_list[-2][0]
                miny = rect_list[-2][1]
                maxx = rect_list[-1][0]
                maxy = rect_list[-1][1]
                roi = frame[miny:maxy, minx:maxx]
                
                result = add_sign(roi)
                cv.imwrite(f"screenshot/saveImage_{now.strftime('%Y-%m-%d_%H:%M:%S')}.jpg", result)
            else:
                press_r_before = True
        # Press a
        elif key == ord('a'):
            if press_a_before and not down_bottom_bar:
                down_bottom_bar = True

            elif press_a_before:
                press_a_before = False
            else:
                press_a_before = True
                down_bottom_bar = False
        # Press esc
        elif key == 27:
            cv.destroyAllWindows()
            break

    cap.release()
    
    
    
if __name__=="__main__":
    
    ### 변수 초기화
    i = 0
    cnt_line = 0
    line_point_list = [] 
    oldx_line, oldy_line = None, None 
    
    cnt_rect = 0
    rect_list = []
    oldx_rect, oldy_rect = None, None
    
    cur_emo_coor_list = [None] * 6

    main()