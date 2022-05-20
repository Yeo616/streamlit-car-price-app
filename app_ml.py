import streamlit as st
import joblib

def run_ml():
    st.subheader('자동차 구매 가능 금액 예측')
    
    # 예측하기 위해서 필요한 파일들을 불러와야 된다.
    # 이 예에서는, 인공지능 파일, X 스케일러 파일, y 스케일러 파일
    # 3개를 불러와야 한다. 

    regressor = joblib.load('data/regressor.pkl')
    # 변수이름도 같게 해준다. 헷갈리지 않게. 
    scaler_X = joblib.load('data/scaler_X.pkl')
    scaler_y = joblib.load('data/scaler_y.pkl')

    # 유저가 앱을 통해서 데이터를 입력했습니다.
    # 이 사람은 얼마정도의 차를 구매할 수 있을지 예측해서, 그 사람에게 맞는 차를 보여주려 합니다.
    # 여자이고, 나이는 38살, 연봉은 78,000달러, 카드 빚은 15,000달러이고, 
    # 자산은 480,000달러입니다. 

    # 성별, 나이, 연봉, 카드빚, 자산을 입력받도록 만드세요
    gender_list = ['남자','여자']
    gender = st.radio('성별입력',gender_list)
    if gender == '여자':
        gender = 0
    else:
        gender = 1

    # age = st.slider('나이',15,120)
    age = st.number_input('나이',0,120)
    salary = st.number_input('연봉 입력',0)
    deb = st.number_input('빚 입력',0)
    total = st.number_input('자산 입력',0)

    customer = [gender,age,salary,deb,total]

    # 다음에는 입력받은 값으로 예측하는 걸 진행해 볼것.
    # 진행한 값으로 AWS에 업로드 할 것.
    