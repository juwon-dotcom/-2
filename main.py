class QuizGame:
    def __init__(self):
        self.running = True

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
        print("퀴즈 목록 보기 기능은 아직 구현 전입니다.")

    def show_best_score(self):
        print("최고 점수 보기 기능은 아직 구현 전입니다.")

    def exit_game(self):
        print("게임을 종료합니다.")
        self.running = False


if __name__ == "__main__":
    game = QuizGame()
    game.run()