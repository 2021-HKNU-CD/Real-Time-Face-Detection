import numpy as np
import cv2
import tkinter as tk
from tkinter import messagebox as msg


def AskSex():  # 얼굴인식 과정에서 성별을 판단할 수 있도록 하면 필요 없어짐  --> 참고: https://github.com/arunponnusamy/cvlib
    """
    고객의 성별을 입력받는다.
    ex) 남성인경우 : 0 여성인 경우 : 1
    :return: sex_num
    """


def DisplayHairstyle(sex_num):  # 굳이 남-녀 분리를 안해도 되나... ?
    """
    고객에게 원하는 머리스타일을 고를 수 있게 후보를 보여줌
    :return:
    """
    pass

    if sex_num == 0:
        DisplayMaleHairstyle()
    elif sex_num == 1:
        DisplayFemaleHairstyle()
    else:
        print("wrong input detected")


def DisplayMaleHairstyle():
    """
    남성 고객에게 원하는 머리스타일을 고를 수 있게 후보를 보여줌
    :return:
    """
    pass


def DisplayFemaleHairstyle():
    """
    여성 고객에게 원하는 머리스타일을 고를 수 있게 후보를 보여줌
    :return:
    """
    pass


def DisplayMaleHairDyeingColor():
    """
    남성 고객에게 원하는 머리염색 색깔을 고를 수 있게 후보를 보여줌
    :return:
    """
    pass


def DisplayMaleHairDyeingColor():
    """
    여성 고객에게 원하는 머리염색 색깔을 고를 수 있게 후보를 보여줌
    :return:
    """
    pass


def ChooseHairstyle(sex_num, wanted_hairstyle_num):  # ChooseHairDyeingColor 이것도 필요할지..
    """
    Display~~ () 안에서 실행됨 --> 고객
    :param sex_num: 고객의 성별
    :param wanted_hairstyle_num: 고객이 원하는 헤어스타일 번호
    :return: target_hairstyle_num
    """
    pass


def MakeMask(target_hairstyle_num):  # 마스크 생성 원리를 잘 몰라서 일단 앞자리에 배치...
    """
    MichiGAN에 넣을 마스크 만들기
    :return: target_hairstyle_mask
    """
    pass


def CheckUsingPersonalInformation():  # 개인정보 활용 동의 여부를 물어봅니다.
    MsgBox = msg.askquestion('개인정보 활용 동의', '카메라를 통해 얼굴을 캡처합니다. 동의하시겠습니까?')
    if MsgBox == 'no':
        msg.showinfo('개인정보 활용 동의', '프로그램을 종료합니다.')
        MsgBox.destroy()
    else:
        msg.showinfo('개인정보 활용 동의', '카메라를 통해 캡처를 시작합니다.')
        # StartCapture() <-- 이런식으로 ?


def StartFaceCapture():  # 얼굴 캡처를 시작함
    """
    영상에서 얼굴 캡처를 시작하여, origin_img를 만듬
    :return: origin_img   
    """
    # 얼굴 위치 잡을 수 있도록 해주는 xml
    xml = 'haarcascades/haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(xml)

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 노트북 웹캠을 카메라로 사용
    cap.set(3, 640)  # 너비
    cap.set(4, 480)  # 높이

    # fourcc = cv2.VideoWriter_fourcc(*'XVID') # 캡처한 영상을 저장할 때 씀
    # out = cv2.VideoWriter('result/output.mp4', fourcc, 20.0, (640, 480)) # 캡처한 영상을 저장하기 위함

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)  # 좌우 대칭
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # out.write(frame) # 캡처한 영상을 저장하기 위함

        faces = face_cascade.detectMultiScale(gray, 1.05, 5)

        if len(faces):
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x-30, y-45), (x + w + 30, y + h+30), (255, 0, 0), 1)

            cv2.imshow('result', frame)

            k = cv2.waitKey(30) & 0xff

            if k == 27:  # Esc 키를 누르면 종료
                break
            elif k == 24:  # ctrl+x 누르면 얼굴 캡처
                cv2.imwrite("FaceExample.png", frame)   # 네모 영역만 캡처가 안됨
                break

    cap.release()
    cv2.destroyAllWindows()


def GenerateImageUsingMichiGAN(origin_img, target_hairstyle_mask):
    """
    원본 이미지와, 타겟 헤어스타일 마스크를 이용해 사진 만들기
    :param origin_img: 원본 이미지
    :param target_hairstyle_mask: 타겟 마스크 (바꾸고 싶은 헤어스타일)
    :return: output_img
    """
    pass


def ShowResult(output_img):
    """
    MichiGAN으로부터 도출된 output_img을 이쁘게 보여주기 -> (원본 이미지, 변경된 이미지) 이렇게 보여준다던가..
    :param output_img: 생성된 사진
    :return: final_output_img
    """
    pass


def ShowResultTest():
    image = cv2.imread("FaceExample.png", cv2.IMREAD_COLOR)  # 저장된 사진 가져오기   -->  Timestamp + FaceExample 으로 저장해야할 지 ?

    cv2.imshow('Face', image)  # 저장된 사진 보내주기

    cv2.waitKey(0)  # 사용자 키 입력 기다림
    cv2.destroyAllWindows()


CheckUsingPersonalInformation()
StartFaceCapture()
ShowResultTest()


# 해야할 일: 사각형의 크기를 늘리고, 이를 이용하여 얼굴 사진만 저장히기 (여백 포함)

