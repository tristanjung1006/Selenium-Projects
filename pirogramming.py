import random


class Player:
    # 플레이어 객체를 초기화
    def __init__(self, name):
        self.name = name
        self.bingo_cnt = 0
        self.table = []

    # 객체를 문자열 표현(name)으로 반환하는 메서드
    def __str__(self) -> str:
        return f"{self.name}"


class Game:
    # 게임 객체를 초기화
    def __init__(self):
        self.players = []  # 플레이어들의 목록
        self.my_player = None  # 사용자 이름(문제 1-(1)에서 입력받음)
        self.deck = [i for i in range(1, 10)]  # 숫자 생성
        # 초기 플레이어 3명 생성
        self.players.append(Player("우보상두련"))
        self.players.append(Player("하보두련"))
        self.players.append(Player("김치련"))

    def start_game(self):
        """
        - [ 게임 시작 전 ] 초기 설정을 하고, 플레이어의 처음 빙고판을 출력하는 함수입니다.
        """
        print("=============================")
        print("      빙고게임 시작 ^_^      ")
        print("=============================")

        # TODO 1-(1): 사용자로부터 플레이어의 이름을 입력받아 플레이어들의 목록에 추가하고, 순서를 랜덤하게 섞어주세요.
        user_name = input("당신의 이름을 입력해주세요(ex. 홍길동) ")
        self.my_player = user_name
        self.players.append(Player(user_name))
        random.shuffle(self.players)

        ##### END OF TODO 1-(1) #####

        # TODO 1-(2): 각각의 플레이어들의 빙고판을 생성한 후, 출력해 주세요. (단, 각 플레이어들의 빙고판은 1부터 9까지의 숫자들이 중복없이 구성되어야 합니다.)
        for player in self.players:
            player.table = [random.sample(range(1, 10), 3) for _ in range(3)]
            print(f"플레이어 이름: {player}")
            print("===플레이어 테이블===")
            for row in player.table:
                print(row)
            print()

        ##### END OF TODO 1-(2) #####

    def set_next_player(self, round_num):
        """ 
        - [ 게임 진행 ] round_num을 매개변수로 받아서 해당 라운드의 플레이어를 지정하는 함수 입니다.
        """
        # TODO 2-(1): 리스트의 값의 개수를 초과해서 반복해도 리스트의 길이를 벗어나지 않도록 해주세요.
        next_player_index = (round_num - 1) % len(self.players)

        ##### END OF TODO 2-(1) #####

        # TODO 2-(2): 다음 순서의 플레이어 객체를 return해 주세요.
        return self.players[next_player_index]

        ##### END OF TODO 2-(2) #####

    def count_bingo(self):
        """ 
        - [ 게임 진행 ] player의 빙고 개수를 업데이트 하는 함수입니다.
        """
        for player in self.players:
            # 플레이어의 빙고 개수를 초기화합니다.
            player.bingo_cnt = 0

            # TODO 3-(1): 플레이어의 빙고판 가로를 확인해 주세요
            for row in player.table:
                if all(cell == 0 for cell in row):
                    player.bingo_cnt += 1

            ##### END OF TODO 3-(1) #####

            # TODO 3-(2): 플레이어의 빙고판 세로를 확인해 주세요
            for j in range(3):
                if all(player.table[i][j] == 0 for i in range(3)):
                    player.bingo_cnt += 1

            ##### END OF TODO 3-(2) #####

            # TODO 3-(3): 플레이어의 빙고판 대각선(좌상단 -> 우하단) 확인
            if all(player.table[i][i] == 0 for i in range(3)):
                player.bingo_cnt += 1

            ##### END OF TODO 3-(3) #####

            # TODO 3-(4): 플레이어의 빙고판 대각선(우상단 -> 좌하단) 확인
            if all(player.table[i][2 - i] == 0 for i in range(3)):
                player.bingo_cnt += 1

            ##### END OF TODO 3-(4) #####

    def do_bingo(self, picked_num):
        """ 
        - [ 게임 진행 ] 빙고판에서 선택한 숫자를 매개변수로 받아서 0으로 바꾸는 메서드입니다.
        """
        # TODO 4-(1): 플레이어들을 순회하면서 빙고!인 숫자를 숫자 0으로 바꿔주세요.
        for player in self.players:
            for i in range(3):
                for j in range(3):
                    if player.table[i][j] == picked_num:
                        player.table[i][j] = 0

        ##### END OF TODO 4-(1) #####

    def play_game(self):
        """
        - [ 게임 진행 ] 부분을 담당하는 함수 입니다.
        - 라운드를 시작하고 각 플레이어의 순서를 결정하여 게임을 진행합니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """
        print("=============================")
        print("          게임 순서          ")
        print("=============================")

        play_order = ", ".join(map(str, self.players))
        print(f"게임은 {play_order} 순으로 진행됩니다.\n")

        round_num = 0
        while True:
            round_num += 1

            print("=============================")
            print(f"       ROUND {round_num} - START")
            print("=============================")

            # 이번 라운드의 플레이어를 set_next_player를 이용하여 변수에 할당하고 출력합니다.
            next_player = self.set_next_player(round_num)
            print(f"이번은 {next_player} 차례입니다. ^_^ \n")

            # 이번 라운드 플레이어(next_player)가 사용자인 경우 -> 사용자로부터 숫자 입력받기
            # 이번 라운드 플레이어(next_player)가 다른 플레이어(안정근 | 노영진 | 민세원)인 경우 -> deck에서 랜덤하게 하나 뽑기
            if next_player.name == self.my_player:
                while True:  # 예외처리
                    try:
                        picked_num = int(input(f'당신의 차례입니다. 남은 숫자 중 하나를 입력해주세요. *남은 숫자*: {sorted(self.deck)}'))
                        if picked_num in self.deck:
                            break
                        elif picked_num > 9 or picked_num < 0:
                            print('숫자 범위를 벗어납니다. 1~9 사이의 숫자 중 뽑지 않은 숫자(남은 숫자)를 입력해주세요.')
                            continue
                        elif picked_num not in self.deck:
                            print('이미 뽑은 숫자를 입력하셨습니다. 남은 숫자 중 다시 입력해주세요.')
                    except ValueError:
                        print('정수가 아닌 숫자를 입력하셨습니다. 1~9 사이 숫자 중 뽑지 않은 숫자를 입력해주세요.')

                    except Exception as e:
                        print(e)
            # 컴퓨터는 남은 숫자 중 랜덤으로 선택합니다.
            else:
                picked_num = random.choice(self.deck)

            # 한번 뽑은 숫자를 또 뽑을 수 없기 때문에 뽑은 숫자를 deck에서 삭제해줍니다.
            self.deck.remove(picked_num)
            print(f'{next_player}(이)가 {picked_num}(을)를 선택했습니다.')

            # do_bingo함수를 이용하여 선택한 숫자 빙고판에서 0으로 바꿉니다.
            self.do_bingo(picked_num)

            # 빙고 수를 세는 부분입니다.
            self.count_bingo()

            # 빙고를 화면에 표시하는 부분입니다.
            for player in self.players:
                print(f'>> {player.name} (현재 빙고: {player.bingo_cnt})')
                for row in player.table:
                    print(row)
                print()

            print("=============================")
            print(f"       ROUND {round_num} - END")
            print("=============================")

            # 플레이어 중 3빙고 이상 달성한 플레이어 있을 경우 함수가 종료됩니다.
            for player in self.players:
                if player.bingo_cnt >= 3:
                    return
            print()

    def game_result(self):
        """
        - [게임 종료] 게임 결과를 출력하는 메서드입니다.
        - (1) 빙고 개수를 기준으로 내림차순으로 정렬하되, 만약 빙고 개수가 같다면 이름을 기준으로 오름차순으로 정렬해 주세요. (* 동점자 처리 주의!!)
        - (2) 사용자의 경우 이름 옆에 *을 붙여서 출력해주세요.(ex. *홍길동*)
        """
        print("=============================")
        print("     게임 순위 - 빙고 개수")
        print("=============================")

        # TODO 5-(1): 빙고 개수를 기준으로 내림차순 출력. 빙고 개수가 같다면 이름을 기준으로 오름차순 출력 (빙고 개수와 이름이 같은 경우는 고려하지 않습니다.)
        sorted_players = sorted(self.players, key=lambda x: (x.bingo_cnt, x.name))
        rank = 1
        for player in sorted_players:
            if player.name == self.my_player:
                print(f"{rank}. *{player.name}* - 빙고 개수: {player.bingo_cnt}")
            else:
                print(f"{rank}. {player.name} - 빙고 개수: {player.bingo_cnt}")
            rank += 1

        ##### END OF TODO 5-(1) #####

        # TODO 5-(2): 사용자의 경우 이름 옆에 *을 붙여서 출력해주세요.(ex. *홍길동*) 점수가 같으면 등수도 같도록 반드시 동점자 처리를 해주세요.

        ##### END OF TODO 5-(2) #####

    def game(self):
        """
        - 게임 운영을 위한 함수입니다.
        - 별도의 코드 작성이 필요 없습니다.
        """
        self.start_game()
        self.play_game()
        self.game_result()


if __name__ == "__main__":
    game = Game()

    game.game()
