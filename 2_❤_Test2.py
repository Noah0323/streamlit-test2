from re import A
import streamlit as st

st.title("달리 테스트 2")

# input_user_name = st.text_input(label="User Name", value="default value")
# radio_gender = st.radio(label="Gender", options=["Male", "Female"])
# check_1 = st.checkbox(label="agree", value=False)
# memo = st.text_area(label="memo", value="")

# list1 = ['연애','좋은변화','창의성','배움성장','공감','경험','공정평등',
# '믿음신앙','친구우정','성취성공','겸손','논리적임','인정받기','계획과 안정',
# '조화 균형','외모 미모','도전용기','경쟁승부','호기심','자존감','개성 다양성',
# '능력 자신감','가족에 대한 사랑','자유로운 생각','건강','정직','리더십',
# '현실감각','협동 팀워크','부자 재테크','감정 솔직함','성실 부지런함']

# list2 = ['부동산','외국어','주식','외모','게임','과학','친구','연애 사랑'
# ,'영화','미술','음악','만화','스포츠','뉴스','책','정치','경제','경영',
# '자동차','연예인','음식','공예','기계','디자인','관찰','가르치기','글쓰기'
# ,'조언','청소','놀이','가십','여행']

def list1():
    global a
    a=0
    if st.checkbox('부동산'):
        a+=1    
    if st.checkbox('외국어'):
        a+=1
    if st.checkbox('주식'):
        a+=1
    if st.checkbox('외모'):
        a+=1
    if st.checkbox('게임'):
        a+=1
    if st.checkbox('과학'):
        a+=1
    if st.checkbox('친구'):
        a+=1
    if st.checkbox('연애 사랑'):
        a+=1
    if st.checkbox('영화'):
        a+=1
    if st.checkbox('미술'):
        a+=1
    if st.checkbox('음악'):
        a+=1
    if st.checkbox('만화'):
        a+=1
    if st.checkbox('스포츠'):
        a+=1
    if st.checkbox('뉴스'):
        a+=1
    if st.checkbox('책'):
        a+=1
    if st.checkbox('정치'):
        a+=1
    if st.checkbox('경제'):
        a+=1
    if st.checkbox('경영'):
        a+=1
    if st.checkbox('자동차'):
        a+=1
    if st.checkbox('연예인'):
        a+=1
    if st.checkbox('음식'):
        a+=1
    if st.checkbox('공예'):
        a+=1
    if st.checkbox('기계'):
        a+=1
    if st.checkbox('디자인'):
        a+=1
    if st.checkbox('관찰'):
        a+=1
    if st.checkbox('가르치기'):
        a+=1
    if st.checkbox('글쓰기'):
        a+=1
    if st.checkbox('조언'):
        a+=1
    if st.checkbox('청소'):
        a+=1
    if st.checkbox('놀이'):
        a+=1        
    if st.checkbox('가십'):
        a+=1
    if st.checkbox('여행'):
        a+=1
    
list1()




if st.button("Confirm"):
    con = st.container()
    con.caption("Result")
    # con.write(f"User Name is {str(input_user_name)}")
    # con.write(str(radio_gender))
    # con.write(f"agree : {check_1}")
    # con.write(f"memo : {str(memo)}")
    if a == 3:
        con.write('다음으로')
    elif a>3:
        b=a-3
        con.write('%d개만큼 더 선택했습니다.'%b)
    else:
        c=3-a
        con.write('%d개만큼 더 선택해주세요'%c)        

from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


if st.button('End'):
    con=st.container()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.quit()