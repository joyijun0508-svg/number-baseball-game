import random
import streamlit as st

# 1. 웹 페이지 제목 및 기본 설정
st.set_page_config(page_title="숫자 야구 게임", page_icon="⚾")
st.title("⚾ 숫자 야구 게임")

# 2. 최고 기록 및 게임 상태 세션 초기화 (Streamlit은 새로고침되면 변수가 리셋되므로 session_state 사용)
if 'best_score' not in st.session_state:
    st.session_state.best_score = float('inf')

if 'answer' not in st.session_state:
    numbers = list(range(10))
    random.shuffle(numbers)
    st.session_state.answer = numbers[:3]
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.history = []

# 3. 사이드바 - 게임 규칙 설명
with st.sidebar:
    st.header("📖 게임 규칙")
    st.write("1. 컴퓨터가 생각한 **서로 다른 숫자 3개**를 맞히세요.")
    st.write("2. 숫자의 위치와 값이 모두 맞으면 👉 **[스트라이크]**")
    st.write("3. 숫자 값은 맞지만 위치가 틀리면 👉 **[볼]**")
    st.write("4. 맞는 숫자가 하나도 없으면 👉 **[아웃]**")
    st.warning("⚠️ 주의: 20번 안에 맞히지 못하면 패배합니다!")
    
    st.markdown("---")
    # 최고 기록 표시
    if st.session_state.best_score != float('inf'):
        st.success(f"🏆 현재 최고 기록: {st.session_state.best_score}회")
    else:
        st.info("🏆 아직 최고 기록이 없습니다. 첫 기록에 도전하세요!")

# 4. 게임 리셋 함수
def reset_game():
    numbers = list(range(10))
    random.shuffle(numbers)
    st.session_state.answer = numbers[:3]
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.history = []

# 새 게임 시작 버튼
if st.button("🔄 새 게임 시작하기"):
    reset_game()
    st.rerun()

# 5. 메인 게임 로직
max_attempts = 20

st.write(f"### 🚀 현재 기회: {st.session_state.attempts} / {max_attempts}")

# 입력창 및 버튼 구성을 위한 폼
with st.form(key='baseball_form', clear_on_submit=True):
    user_guess = st.text_input("0~9 사이의 서로 다른 숫자 3개를 입력하세요 (예: 123):", max_chars=3)
    submit_button = st.form_submit_button(label='입력 완료')

if submit_button and not st.session_state.game_over:
    guess = user_guess.strip()
    
    # 예외 처리
    if len(guess) != 3 or not guess.isdigit():
        st.error("❌ 숫자 3개만 정확히 입력해 주세요!")
    elif len(set(guess)) != 3:
        st.error("❌ 중복된 숫자는 입력할 수 없습니다!")
    else:
        # 판정 시작
        st.session_state.attempts += 1
        guess_list = [int(n) for n in guess]
        answer = st.session_state.answer
        
        strike = 0
        ball = 0
        
        for i in range(3):
            if guess_list[i] == answer[i]:
                strike += 1
            elif guess_list[i] in
