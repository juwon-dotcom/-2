import json
import os
from dataclasses import dataclass, asdict


STATE_FILE = "state.json"


@dataclass
class Quiz:
    question: str
    choices: list
    answer: int


DEFAULT_QUIZZES = [
# 기본 퀴즈 5개: state.json이 없거나 손상된 경우 사용
    Quiz(
        question="운동역학에서 힘의 단위로 알맞은 것은?",
        choices=["kg", "N", "m/s", "J"],
        answer=2
    ),
    Quiz(
        question="뉴턴의 제2법칙을 올바르게 나타낸 식은?",
        choices=["F = ma", "v = s/t", "P = W/t", "E = mc²"],
        answer=1
    ),
    Quiz(
        question="물체가 회전하려는 효과를 나타내는 운동역학 개념은?",
        choices=["속도", "가속도", "토크", "질량"],
        answer=3
    ),
    Quiz(
        question="인체가 균형을 잘 유지하기 위한 조건으로 가장 적절한 것은?",
        choices=["무게중심이 높고 기저면이 좁다", "무게중심이 낮고 기저면이 넓다", "마찰력이 항상 0이다", "질량이 작을수록 항상 안정하다"],
        answer=2
    ),
    Quiz(
        question="운동량을 나타내는 식으로 알맞은 것은?",
        choices=["질량 × 속도", "힘 × 거리", "일 ÷ 시간", "질량 × 가속도"],
        answer=1
    ),
]


class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.high_score = 0
        self.load_state()

    def load_state(self):
        """state.json에서 퀴즈 데이터와 최고 점수를 불러옵니다."""
        if not os.path.exists(STATE_FILE):
            self.quizzes = DEFAULT_QUIZZES.copy()
            self.high_score = 0
            self.save_state()
            return

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.high_score = data.get("high_score", 0)

            quiz_data = data.get("quizzes", [])
            self.quizzes = [
                Quiz(
                    question=item["question"],
                    choices=item["choices"],
                    answer=item["answer"]
                )
                for item in quiz_data
            ]

            if not self.quizzes:
                self.quizzes = DEFAULT_QUIZZES.copy()
                self.save_state()

        except (json.JSONDecodeError, KeyError, TypeError):
            print("state.json 파일을 읽는 중 문제가 발생했습니다.")
            print("기본 퀴즈 데이터로 다시 시작합니다.")
            self.quizzes = DEFAULT_QUIZZES.copy()
            self.high_score = 0
            self.save_state()

    def save_state(self):
        """퀴즈 데이터와 최고 점수를 state.json에 UTF-8로 저장합니다."""
        data = {
            "high_score": self.high_score,
            "quizzes": [asdict(quiz) for quiz in self.quizzes]
        }

        try:
            with open(STATE_FILE, "w", encoding="utf-8") as file:
               json.dump(data, file, ensure_ascii=False, indent=2)
        except OSError:
            print("파일 저장 중 오류가 발생했습니다.")
    
    def input_number(self, message, min_value, max_value):
        """정해진 범위 안의 숫자를 입력받습니다."""
        while True:
            user_input = input(message).strip()

            try:
                number = int(user_input)
            except ValueError:
                print("숫자를 입력해주세요.")
                continue

            if min_value <= number <= max_value:
                return number

            print(f"{min_value}부터 {max_value} 사이의 숫자를 입력해주세요.")

    def show_menu(self):
        print("\n===== Python Quiz Game =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 퀴즈 삭제")
        print("5. 최고 점수 보기")
        print("6. 종료")

    def solve_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0

        print("\n[퀴즈 시작]")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n문제 {index}. {quiz.question}")

            for choice_index, choice in enumerate(quiz.choices, start=1):
                print(f"{choice_index}. {choice}")

            user_answer = self.input_number("정답 번호를 입력하세요: ", 1, len(quiz.choices))

            if user_answer == quiz.answer:
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print(f"\n최종 점수: {score} / {len(self.quizzes)}")

        if score > self.high_score:
            self.high_score = score
            self.save_state()
            print("최고 점수가 갱신되었습니다!")

    def add_quiz(self):
        print("\n[퀴즈 추가]")

        question = input("문제를 입력하세요: ").strip()

        if not question:
            print("문제 내용은 비워둘 수 없습니다.")
            return

        choices = []

        for i in range(1, 5):
            choice = input(f"{i}번 선택지를 입력하세요: ").strip()

            if not choice:
                print("선택지는 비워둘 수 없습니다.")
                return

            choices.append(choice)

        answer = self.input_number("정답 번호를 입력하세요(1~4): ", 1, 4)

        new_quiz = Quiz(question=question, choices=choices, answer=answer)
        self.quizzes.append(new_quiz)
        self.save_state()

        print("퀴즈가 추가되었습니다.")

    def show_quiz_list(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print("\n[퀴즈 목록]")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n{index}. {quiz.question}")

            for choice_index, choice in enumerate(quiz.choices, start=1):
                print(f"   {choice_index}. {choice}")

            print(f"   정답: {quiz.answer}번")

    def delete_quiz(self):
        if not self.quizzes:
            print("삭제할 퀴즈가 없습니다.")
            return

        self.show_quiz_list()

        quiz_number = self.input_number(
            "\n삭제할 퀴즈 번호를 입력하세요: ",
            1,
            len(self.quizzes)
        )

        deleted_quiz = self.quizzes.pop(quiz_number - 1)
        self.save_state()

        print(f"삭제된 퀴즈: {deleted_quiz.question}")

    def show_high_score(self):
        print(f"\n현재 최고 점수: {self.high_score}점")

    def run(self):
        while True:
            self.show_menu()
            menu = self.input_number("메뉴를 선택하세요: ", 1, 6)

            if menu == 1:
                self.solve_quiz()
            elif menu == 2:
                self.add_quiz()
            elif menu == 3:
                self.show_quiz_list()
            elif menu == 4:
                self.delete_quiz()
            elif menu == 5:
                self.show_high_score()
            elif menu == 6:
                print("프로그램을 종료합니다.")
                break


if __name__ == "__main__":
    game = QuizGame()

    try:
        game.run()
    except KeyboardInterrupt:
        print("\n프로그램이 사용자에 의해 중단되었습니다.")
        game.save_state()
    except EOFError:
        print("\n입력이 종료되었습니다.")
        game.save_state()