import random
import time

# 1. 최고 기록 저장 변수
best_score = float('inf')

def show_rules():
    """게임 규칙 설명"""
    print("\n" + "="*50)
    print("📖 [ 숫자 야구 게임 규칙 ]")
    print("="*50)
    time.sleep(0.3)
    print("1. 컴퓨터가 생각한 '서로 다른 숫자 3개'를 맞히세요.")
    print("2. 숫자의 위치와 값이 모두 맞으면 👉 [스트라이크]")
    print("3. 숫자 값은 맞지만 위치가 틀리면 👉 [볼]")
    print("4. 맞는 숫자가 하나도 없으면 👉 [아웃]")
    time.sleep(0.3)
    print("\n⚠️  주의: 20번 안에 맞히지 못하면 패배합니다!")
    print("="*50)
    input("시작하려면 [Enter] 키를 누르세요...")

def play_baseball():
    """메인 게임 함수"""
    global best_score
    
    show_rules()

    numbers = list(range(10))
    random.shuffle(numbers)
    answer = numbers[:3]

    max_attempts = 20
    attempts = 0

    print("\n🚀 게임을 시작합니다! 0~9 사이의 숫자 3개를 찾아보세요.")
    
    if best_score != float('inf'):
        print(f"🏆 현재 최고 기록: {best_score}회")
    else:
        print("🏆 아직 최고 기록이 없습니다. 첫 기록에 도전하세요!")

    while attempts < max_attempts:
        print(f"\n[기회: {attempts+1}/{max_attempts}]")
        guess = input("숫자 3개 입력 (예: 123) / 종료(q): ").strip()

        if guess.lower() == 'q':
            print(f"👋 게임을 종료합니다. 정답은 {answer}였습니다.")
            return

        if len(guess) != 3 or not guess.isdigit():
            print("❌ 숫자 3개만 정확히 입력해 주세요!")
            continue
        
        guess_list = [int(n) for n in guess]
        if len(set(guess_list)) != 3:
            print("❌ 중복된 숫자는 입력할 수 없습니다!")
            continue

        attempts += 1
        strike = 0
        ball = 0

        for i in range(3):
            if guess_list[i] == answer[i]:
                strike += 1
            elif guess_list[i] in answer:
                ball += 1

        if strike == 3:
            print(f"\n🎊 홈런!!! {attempts}번 만에 맞추셨습니다!")
            if attempts < best_score:
                print(f"✨ 새로운 최고 기록 달성: {attempts}회")
                best_score = attempts
            break
        else:
            if strike == 0 and ball == 0:
                print("➡️ 결과: OUT!")
            else:
                print(f"➡️ 결과: {strike} 스트라이크 | {ball} 볼")

    if attempts >= max_attempts and strike != 3:
        print("\n☠️ 패배! 기회를 모두 소진했습니다.")
        print(f"정답은 {answer}였습니다.")

# 게임 실행 부분
if __name__ == "__main__":
    while True:
        play_baseball()
        retry = input("\n다시 플레이하시겠습니까? (y/n): ").strip().lower()
        if retry != 'y':
            print("\n⚾ 게임을 종료합니다. 즐거우셨나요?")
            break
