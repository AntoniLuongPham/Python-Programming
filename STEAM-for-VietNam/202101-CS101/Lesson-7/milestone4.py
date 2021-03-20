import pygame as pg
import sys, os
pg.init()
clock = pg.time.Clock()

# Cac thong so cua chuong trinh
WIDTH = 720   # chieu dai cua so pygame
HEIGHT = 540   # chieu rong cua so pygame

FPS = 60   # So luong khung hinh moi giay

IMAGE_WIDTH = 720   # chieu dai cua
IMAGE_HEIGHT = 540
OFFSET = 100

ASSETS_PATH = './'

moves = {
    'move0': {
        'time': 1,
        'sprites': [
            '0.png'
            ]
        },
    'move1': {
        'time': 1,
        'sprites': [
            '1.1.png',
            '1.2.png',
            '1.3.png'
            ]
        },
    'move2': {
        'time': 1,
        'sprites': [
            '2.1.png',
            '2.2.png'
            ]
        },
    'move3': {
        'time': 1,
        'sprites': [
            '3.1.png',
            '3.2.png'
            ]
        },
    'move4': {
        'time': 1,
        'sprites': [
            '4.1.png',
            '4.2.png'
            ]
        },
    'move5': {
        'time': 1,
        'sprites': [
            '5.1.png',
            '5.2.png'
            ]
        },
    'move6': {
        'time': 1,
        'sprites': [
            '6.1.png',
            '6.2.png'
            ]
        },
    'move7': {
        'time': 1,
        'sprites': [
            '7.1.png',
            '7.2.png',
            '7.3.png'
            ]
        }
    }
procedure = [
    'move0'
    ]


class Dancer(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.moves = {}
        # Cac thong so dieu khien thay doi hinh anh
        self.current_move = 0
        self.current_sprite = 0
        self.frames_per_image = 0
        self.count = 0

        # Cac thong so hinh anh
        self.image = None
        self.rect = None

    ########################################
    # Khoi tao cac khung hinh anh dau tien #
    ########################################
    def init(self):
        self.load_images()
        self.draw_image(self.moves[procedure[self.current_move]]['sprites'][self.current_sprite])

    #######################################################
    # Tai cac hinh anh tu tu dien dinh nghia cac dong tac #
    #######################################################
    def load_images(self):
        count = 0
        for move in moves:
            count += 1
            sprites = []
            for sprite in moves[move]['sprites']:
                sprites.append(pg.image.load(os.path.join(ASSETS_PATH+move,sprite)))
            self.moves[move]= {
                'time': moves[move]['time'],
                'sprites': sprites
                }
    #########################################
    # Ve hinh anh nhan vat theo dung vi tri #
    #########################################
    # 
    def draw_image(self,sprite):
        self.image = sprite
        self.image = pg.transform.scale(self.image, (IMAGE_WIDTH, IMAGE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.topleft = [0,0]
      
    #############################################
    # Cap nhat tat ca cac thong so cau nhan vat #
    #############################################
    def update(self):
        number_of_moves = len(procedure)
        if self.current_move < number_of_moves:
            # So luong hinh anh trong mot dong tac
            number_of_sprites = len(self.moves[procedure[self.current_move]]['sprites'])
            # Thoi gian thuc hien mot dong tac
            time_of_move = self.moves[procedure[self.current_move]]['time']
            # Tinh so luong frames cho mot hinh anh
            self.frames_per_image = FPS*time_of_move//number_of_sprites
            
            if self.count >= self.frames_per_image:
                if self.current_sprite < number_of_sprites:
                    self.next_sprite()
                else:
                    self.next_move()
                    
            self.count += 1
            
    ############################################
    # Tai hinh anh cua tiep theo trong dong tac#
    ############################################
    def next_sprite(self):
        sprite = self.moves[procedure[self.current_move]]['sprites'][self.current_sprite]
        self.draw_image(sprite)
        self.count = 0
        self.current_sprite += 1
    
    ##################################
    # Chuyen sang dong tac tiep theo #
    ##################################
    def next_move(self):
        self.current_move += 1
        self.current_sprite = 0
    

def main():
    # khoi tao man hinh pygame
    screen = pg.display.set_mode((WIDTH,HEIGHT))
    # dat ten cho chuong trinh pygame
    pg.display.set_caption("STEAM FOR VIETNAM")
    # Khoi tao nhan vat dancer
    moving_sprites = pg.sprite.Group()
    dancer = Dancer()
    dancer.init()
    moving_sprites.add(dancer)

    # Tai nhac va choi nhac
    pg.mixer.init()
    pg.mixer.music.load(os.path.join(ASSETS_PATH,'music.wav'))
    pg.mixer.music.play(-1)
    
   
    # vong lap game
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        # cap nhat tat ca cac thong so cua cac doi tuong
        moving_sprites.update()
        moving_sprites.draw(screen)
        
        pg.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
    pg.quit()


