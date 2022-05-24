import pandas as pd
import streamlit as st
import seaborn as sb
import matplotlib.pyplot as plt

def run_eda():
    st.subheader('데이터 분석')
    
    st.text('기본적인 데이터 분석입니다.')

    car_df = pd.read_csv('data/Car_Purchasing_Data.csv',encoding = 'ISO-8859-1')

    ## 라디오버튼을 이용해서, 데이터프레임과, 통계치를 선택해서
    # 보여줄수 있도록 만든다.

    radio_menu = ['데이터프레임','통계치']
    selected = st.radio('선택하세요', radio_menu)
    # 선택한 것이 해당 변수에 저장이 된다. 

    if selected == radio_menu[0]:
        st.dataframe(car_df)
    elif selected == radio_menu[1]:
        st.dataframe(car_df.describe())

    # 컬럼명을 보여주고, 컬럼을 선택하면,
    # 해당 컬럼의 최대값 데이터와, 최소값 데이터를 보여준다.

    car_list = car_df.columns[4:]
    selected_col = st.selectbox('최소값/최대값', car_list)
    
    # 연봉 제일 높은 사람
    # car_df.loc[car_df['Annual Salary'] == car_df['Annual Salary'].max(),]

    df_max = car_df.loc[car_df[selected_col] == car_df[selected_col].max(),]
    df_min = car_df.loc[car_df[selected_col] == car_df[selected_col].min(),]

    st.text('{}컬럼의 최대값에 해당하는 데이터.'.format(selected_col))
    st.dataframe(df_max)

    st.text('{}컬럼의 최소값에 해당하는 데이터.'.format(selected_col))
    st.dataframe(df_min)

    # 유저가 선택한 컬럼들만, pairplot 그리고 그 아래, 상관계수를 보여준다. 

    selected_col2 = st.multiselect('상관계수 컬럼선택', car_list)
   
    if len(selected_col2) > 1:
        st.text('선택하신 컬럼끼리의 상관계수입니다.')
        st.dataframe(car_df[selected_col2].corr())
       
        fig1 = sb.pairplot(data = car_df[selected_col2])
        st.pyplot(fig1)

        fig2 = plt.figure() # 영역 잡아주고
        sb.heatmap(data = car_df[selected_col2].corr(),annot = True, fmt = '.2f', 
           vmin = -1, vmax =1, cmap = 'coolwarm', linewidths = 0.5)
        st.pyplot(fig2)

    elif len(selected_col2) == 1:
        st.text('두 개이상의 컬럼을 선택해주세요.')
    else:
        st.text('컬럼을 선택해주십쇼')


    ## 고객 이름 컬럼을 검색할 수 있도록 만듭니다.
    ## he라고 넣으면, he가 이름에 들어가있는 고개들의 데이터를 가져옵니다.

    # 1. 유저한테 검색어를 입력받는다. 
    word = st.text_input('이름을 검색할 단어를 입력하세요.')

    # 2. 검색어를 고객이름 컬럼에 들어있는 데이터 가져온다.
    result = car_df.loc[car_df['Customer Name'].str.lower().str.contains(word.lower()), ]

    # 3. 화면에 보여준다. 
    st.dataframe(result)



