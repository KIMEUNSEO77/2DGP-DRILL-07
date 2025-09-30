from pico2d import *
import random

class Ball:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = 599
        self.small_image = load_image('ball21x21.png')
        self.big_image = load_image('ball41x41.png')


class Boy:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, 90)


class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_height, frame_width, self.x, self.y, frame_width // 2,
                             frame_height // 2)


# Game object class here
# 1. 객체를 도출 - 추상화
# 2. 객체를 도출 - 추상화
# 3. 행위를 도출
# 4. 클래스를 제작
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')  # 이 클래스를 통해 만들어지는 객체 self

    def update(self):  # 객체의 상호작용, 행위
        pass

    def draw(self):  # 객체의 모습
        self.image.draw(400, 30)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()


def reset_world():
    global running
    running = True

    global world  # 모든 게임 객체를 담을 수 있는 리스트
    world = []

    # 객체들을 생성
    grass = Grass()
    world.append(grass)

    global team
    team = [Boy() for _ in range(11)]
    world += team  # 리스트끼리 더함

    zombie = Zombie()
    world.append(zombie)


reset_world()


def update_world():
    # 객체들의 상호작용, 행위
    for game_object in world:
        game_object.update()


def render_world():
    clear_canvas()
    for game_object in world:
        game_object.draw()
    update_canvas()


reset_world()  # 아무것도 없는 세상에 객체를 생성
while running:
    handle_events()  # 사용자의 입력 처리
    update_world()  # 객체들의 상호작용을 시뮬레이션, 계산
    render_world()  # 객체들의 모습을 그린다.
    delay(0.05)

close_canvas()