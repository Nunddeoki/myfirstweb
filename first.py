import streamlit as st

st.set_page_config(
    page_title = "공동교육과정"
)

menu = st.sidebar.selectbox("MENU", ["BMI 지수 계산기", "원의 넓이 계산기", "은행 이자 계산기"])

if menu == "BMI 지수 계산기":
    st.title("BMI 지수 계산기")

    키 = st.number_input("키를 입력하세요.(cm)", step = 1)
    키 = 키/100
    체중 = st.number_input("체중을 입력하세요.(kg)", step = 1)
    btn = st.button("계산하기")

    if btn:
        st.write("당신의 BMI지수는", 체중/(키*키), "입니다.")
        if 체중/(키*키) < 18.5:
            st.write("당신은 저체중 입니다.")
        elif 18.5 <= 체중/(키*키) < 24.9:
            st.write("당신은 정상 입니다.")
        elif 25 <= 체중/(키*키) < 29.9:
            st.write("당신은 과체중 입니다.")
        else:
            st.write("당신은 비만 입니다.")

elif menu == "원의 넓이 계산기":
    st.title("원의 넓이 계산기")
    #과제2. 반지름 입력시 원의 넓이를 계산

elif menu == "은행 이자 계산기":
    st.title("은행 이자 계산기")
    def calculate_interest(원금, 이자율, 기간):
        interest = 원금 * 이자율 * 기간
        total_amount = 원금 + interest

        return interest, total_amount

    원금 = st.number_input("원금을 입력하세요:")
    이자율 = st.number_input("연간 이자율을 소수로 입력하세요 (예: 10% = 0.1):")
    기간 = st.number_input("기간(년)을 입력하세요:")
    btn = st.button("계산하기")

    if btn:
        interest, total_amount = calculate_interest(원금, 이자율, 기간)
        st.write(f"{기간}년 후의 이자는 {interest}원이며, 총 반환 금액은 {total_amount}원입니다.")


