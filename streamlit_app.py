import streamlit as st

st.title("2025")
st.header("05.09")
st.subheader("18:17:29")

st.markdown("---")  

st.write(
    "안녕하세요. 채은입니다."
)

st.info(
    "안녕하세요. 채은입니다."
)

# st.columns(n): 화면을 n개의 수직 열로 나눕니다
col1, col2 = st.columns(2)  # 2개의 열 생성

st.image("https://item.kakaocdn.net/do/9dc14126ee3e2d16b00d0a503b592cbbfba8e3d30017c7399e19e508ee32200a")
st.image("https://media.giphy.com/media/cYZkY9HeKgofpQnOUl/giphy.gif?cid=82a1493b4vp9u76vdk9a0d8jdtwh6gg4nr9417i3ptkjhti6&ep=v1_gifs_trending&rid=giphy.gif&ct=g")

st.code("""
import streamlit as st
st.title('Hello World')
""", language="python")

st.link_button("Link", 'youtube.com')

# st.columns(n): 화면을 n개의 수직 열로 나눕니다
col1, col2 = st.columns(2)  # 2개의 열 생성

with col1:
    st.write("왼쪽 열입니다.")  # 첫 번째 열에 내용 작성
with col2:
    st.write("오른쪽 열입니다.")  # 두 번째 열에 내용 작성

# st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

with tab1:
    st.write("탭 1에 해당하는 내용입니다.")  # 첫 번째 탭에 표시할 내용
with tab2:
    st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용

name=st.text_input("학번이름을 입력하시오.")
if name=="30302 권채은":
    st.write(name+"님 반갑습니다.")
else:
    st.error("다시 입력하시오.")

st.text_area("애국가 1절")

gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.write("선택한 성별:", gender)

# 범위 내 숫자 슬라이드 선택
level = st.slider("난이도를 선택하세요", 1, 100, 1)
st.write("선택한 난이도:", level)

