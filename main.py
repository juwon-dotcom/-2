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
    Quiz(
        question="우리 몸에서 뼈와 관절을 중심으로 몸을 지탱하고 움직이게 하는 구조는 무엇인가요?",
        choices=["소화계", "골격계", "호흡계", "순환계"],
        answer=2
    ),
    Quiz(
        question="혈액을 온몸으로 보내는 펌프 역할을 하는 기관은 무엇인가요?",
        choices=["폐", "위", "심장", "간"],
        answer=3
    ),
    Quiz(
        question="공기 중의 산소를 몸 안으로 받아들이는 데 중요한 기관은 무엇인가요?",
        choices=["폐", "신장", "대장", "췌장"],
        answer=1
    ),
    Quiz(
        question="뇌와 척수로 이루어져 몸의 여러 기능을 조절하는 계통은 무엇인가요?",
        choices=["신경계", "소화계", "배설계", "근육계"],
        answer=1
    ),
    Quiz(
        question="음식물을 잘게 분해하고 영양소를 흡수하는 데 관련된 계통은 무엇인가요?",
        choices=["호흡계", "순환계", "소화계", "감각계"],
        answer=3
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

        with open(STATE_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

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
    game.run()