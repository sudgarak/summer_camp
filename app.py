import streamlit as st
import openai

#openai api key
openai.api_key = st.secrets["api_key"]

#페이지 레이아웃 설정
st.set_page_config(layout="wide")

#페이지의 메인 이름
st.title("0814 여름학교 ChatGPT API 실습")

# #가로 줄
st.divider()

# #헤더 
st.header("예시 자료")

# #텍스트 출력하기
text = '''
조선의 제4대 국왕으로 태종과 원경왕후의 아들이다. 형인 양녕대군이 폐세자가 되자 세자에 책봉되었으며 태종의 양위를 받아 즉위하였다.[2]
세종은 과학 기술, 예술, 문화, 국방 등 여러 분야에서 다양한 업적을 남겼다. 백성들에게 농사에 관한 책을 펴내었지만 글을 몰라 이해하지 못하는 모습을 보고 누구나 쉽게 배울 수 있는 효율적이고 과학적인 문자 체계인 훈민정음(訓民正音)을 창제하였다. 훈민정음은 언문으로 불리며 왕실과 민간에서 사용되다가 20세기 주시경이 한글로 발전시켜 오늘날 대한민국의 공식 문자로서 널리 쓰이고 있다.
과학 기술에도 두루 관심을 기울여 혼천의, 앙부일구, 자격루, 측우기 등의 발명을 전폭적으로 지원했고 신분을 뛰어넘어 장영실, 최해산 등의 학자들을 후원하였다.
국방에 있어서는 이종무를 파견하여 왜구를 토벌하고 대마도를 정벌하였으며 이징옥, 최윤덕, 김종서 등을 북방으로 보내 평안도와 함길도에 출몰하는 여진족을 국경 밖으로 몰아내고 4군 6진을 개척하여 압록강과 두만강 유역으로 국경을 확장하였고 백성들을 옮겨 살게 하는 사민정책(徙民政策)을 실시하여 국토의 균형 발전을 위해서도 노력하였다.
정치면에서는 황희와 맹사성, 윤회, 김종서 등을 등용하여 정무를 주관하였는데 이 통치 체제는 일종의 내각중심 정치제도인 의정부서사제의 효시가 되었다. 이 밖에도 법전과 문물을 정비하였고 전분 6등법과 연분 9등법 등의 공법(貢法)을 제정하여 조세 제도의 확립에도 업적을 남겼다.
'''
st.write(text)
# # st.write("~~~") 의 형태로도 출력 가능

# #링크 넣기
st.markdown("[위키피디아 링크](https://ko.wikipedia.org/wiki/%EC%84%B8%EC%A2%85)")

# #학생들이 텍스트 입력하는 곳 만들기
# #조사한 자료를 research에 저장
research = st.text_input("조사해온 자료를 입력해주세요 : ")

st.write(research)

st.divider()

# #ChatGPT API 활용하기 response를 불러오는 함수 만들기
@st.cache_data #반복 수행을 막아줌
def gptapi(persona, user):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content" : persona},
        {"role": "user", "content": user}
    ],
    max_tokens = 200,
    temperature = 1
    )
    return response["choices"][0]["message"]["content"]

# #prompt 설정하기
persona_prompt1 = '''
너는 역사선생님이야. 세종대왕에 대해 학생들에게 가르쳤어. 학생들이 조사해온 자료를 50자 이내로 요약해줘
'''

persona_prompt2 = '''
    너는 역사선생님이야. 학생들이 조사해온 자료를 요악한 내용을 보고, 문제를 2개 만들어줘
    '''

# #클릭해야 실행되도록 버튼 만들기
if st.button("요약본 보고 질문받기"): 
    #복잡한 단계는 나누어 진행하기
    step1 = gptapi(persona_prompt1, research)
    st.write(step1)

    step2 = gptapi(persona_prompt2, step1)
    st.write(step2)