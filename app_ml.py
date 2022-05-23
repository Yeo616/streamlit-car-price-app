import streamlit as st
import joblib
import numpy as np

def run_ml():
    st.subheader('자동차 구매 가능 금액 예측')
    
    print(sklearn.__version)
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
    worth = st.number_input('자산 입력',0)

    if st.button('자동차 구매 금액 예측'):
        # 학습은 웹대시보드에서 시키는 것이 아니다. 
        # 1. 신규 고객의 정보를 넘파이 어레이로 만들어준다.
        new_data = np.array([gender,age,salary,deb, worth])

        # 2. 학습할때 사용한 X의 피처 스케일러를 이용해서, 피처스케일링한다.
        # 먼저, 데이터를 2차원으로 만들어준다.
        new_data = new_data.reshape(1,5)
        # 1행: 한명의 사람 정보, 5열: gender,age,salary,deb,worth
        new_data = scaler_X.transform(new_data)

        # 3. 인공지능에게 예측해달라고 한다.
        y_pred = regressor.predict(new_data)

        # 4. 예측한 값을, 원상복구 시킨다.
        y_pred = scaler_y.inverse_transform(y_pred)

        y_pred = round(y_pred[0,0])

        st.write('이 사람의 구매 가능 금액은' + str(y_pred) + '달러 입니다.')
    
        