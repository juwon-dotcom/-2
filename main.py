class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def show(self):
        print(self.question)

        for index, option in enumerate(self.options, start=1):
            print(f"{index}. {option}")


class QuizGame:
    def __init__(self):
        self.running = True
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

    def show_menu(self):
        print()
        print("===== Python Quiz Game =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 최고 점수 보기")
        print("5. 종료")

    def get_menu_choice(self):
        try:
            choice = int(input("메뉴를 선택하세요: "))
        except ValueError:
            print("숫자를 입력해주세요.")
            return None

        if choice < 1 or choice > 5:
            print("1부터 5 사이의 숫자를 입력해주세요.")
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
                self.show_best_score()
            elif choice == 5:
                self.exit_game()

    def play_quiz(self):
        print("퀴즈 풀기 기능은 아직 구현 전입니다.")

    def add_quiz(self):
        print("퀴즈 추가 기능은 아직 구현 전입니다.")

    def show_quiz_list(self):
        print()
        print("===== 퀴즈 목록 =====")

        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. {quiz.question}")

    def show_best_score(self):
        print("최고 점수 보기 기능은 아직 구현 전입니다.")

    def exit_game(self):
        print("게임을 종료합니다.")
        self.running = False


if __name__ == "__main__":
    game = QuizGame()
    game.run()