import json

DATA_FILE = "quiz_data.json"

class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def to_dict(self):
        return {
            "question": self.question,
            "options": self.options,
            "answer": self.answer
        }

    @staticmethod
    def from_dict(data):
        return Quiz(data["question"], data["options"], data["answer"])

    def show(self):
        print(self.question)

        for index, option in enumerate(self.options, start=1):
            print(f"{index}. {option}")


class QuizGame:
    def __init__(self):
        self.running = True
        self.best_score = 0
        self.quizzes = [
            Quiz(
                "Python에서 문자열을 출력할 때 사용하는 함수는?",
                ["print()", "input()", "len()", "type()"],
                1
            ),
            Quiz(
                "리스트를 만들 때 사용하는 기호는?",
                ["{}", "[]", "()", "<>"],
                2
            ),
            Quiz(
                "조건문을 만들 때 사용하는 키워드는?",
                ["for", "while", "if", "class"],
                3
            )
        ]

        self.load_data()
        
    def show_menu(self):
        print()
        print("===== Python Quiz Game =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 퀴즈 삭제")
        print("5. 최고 점수 보기")
        print("6. 종료")

    def get_menu_choice(self):
        try:
            choice = int(input("메뉴를 선택하세요: "))
        except ValueError:
            print("숫자를 입력해주세요.")
            return None

        if choice < 1 or choice > 6:
            print("1부터 6 사이의 숫자를 입력해주세요.")
            return None

        return choice

    def run(self):
        while self.running:
            self.show_menu()
            choice = self.get_menu_choice()

            if choice is None:
                continue

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quiz_list()
            elif choice == 4:
                self.delete_quiz()
            elif choice == 5:
                self.show_best_score()
            elif choice == 6:
                self.exit_game()

    def play_quiz(self):
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0

        print()
        print("===== 퀴즈 풀기 =====")

        for index, quiz in enumerate(self.quizzes, start=1):
            print()
            print(f"[문제 {index}]")
            print(quiz.question)

            for choice_index, choice in enumerate(quiz.options, start=1):
                print(f"{choice_index}. {choice}")

            user_answer = self.get_quiz_answer(len(quiz.options))

            if user_answer == quiz.answer:
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print()
        print("===== 결과 =====")
        print(f"총 {len(self.quizzes)}문제 중 {score}문제를 맞혔습니다.")

        if score > self.best_score:
            self.best_score = score
            self.save_data()
            print("최고 점수가 갱신되었습니다!")

    def get_quiz_answer(self, choice_count):
        while True:
            try:
                answer = int(input("정답 번호를 입력하세요: "))
            except ValueError:
                print("숫자를 입력해주세요.")
                continue

            if answer < 1 or answer > choice_count:
                print(f"1부터 {choice_count} 사이의 숫자를 입력해주세요.")
                continue

            return answer

    def add_quiz(self):
        print()
        print("===== 퀴즈 추가 =====")

        question = self.get_non_empty_text("문제를 입력하세요: ")

        options = []

        for index in range(1, 5):
            option = self.get_non_empty_text(f"{index}번 보기를 입력하세요: ")
            options.append(option)

        answer = self.get_quiz_answer(len(options))

        new_quiz = Quiz(question, options, answer)
        self.quizzes.append(new_quiz)
        self.save_data()

        print("퀴즈가 추가되었습니다!")

    def get_non_empty_text(self, message):
        while True:
            text = input(message).strip()

            if text == "":
                print("빈 값은 입력할 수 없습니다.")
                continue

            return text
        
    def show_quiz_list(self):
        print()
        print("===== 퀴즈 목록 =====")

        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. {quiz.question}")

    def delete_quiz(self):
        if len(self.quizzes) == 0:
            print("삭제할 퀴즈가 없습니다.")
            return

        print()
        print("===== 퀴즈 삭제 =====")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. {quiz.question}")

        while True:
            try:
                delete_number = int(input("삭제할 퀴즈 번호를 입력하세요: "))
            except ValueError:
                print("숫자를 입력해주세요.")
                continue

            if delete_number < 1 or delete_number > len(self.quizzes):
                print(f"1부터 {len(self.quizzes)} 사이의 숫자를 입력해주세요.")
                continue

            deleted_quiz = self.quizzes.pop(delete_number - 1)
            self.save_data()

            print(f"'{deleted_quiz.question}' 퀴즈가 삭제되었습니다.")
            break
    
    def show_best_score(self):
        print()
        print("===== 최고 점수 =====")
        print(f"현재 최고 점수: {self.best_score}점")

    def exit_game(self):
        self.save_data()
        print("게임을 종료합니다.")
        self.running = False

    def save_data(self):
        data = {
            "best_score": self.best_score,
            "quizzes": [quiz.to_dict() for quiz in self.quizzes]
        }

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_data(self):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.best_score = data.get("best_score", 0)

            quizzes_data = data.get("quizzes", [])
            if len(quizzes_data) > 0:
                self.quizzes = [Quiz.from_dict(quiz_data) for quiz_data in quizzes_data]

        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("저장 파일을 읽는 중 문제가 발생했습니다. 기본 퀴즈를 사용합니다.")

if __name__ == "__main__":
    game = QuizGame()
    game.run()