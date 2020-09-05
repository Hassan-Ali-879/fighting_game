# 2d platform combat game
from settings import *
from sprites import *


class Game: 
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

        # ground attac
        self.attack_s_light_left = False
        self.attack_s_light_right = False
        self.attack_n_light_left = False
        self.attack_n_light_right = False
        self.attack_d_light_left = False
        self.attack_d_light_right = False

        # air attac
        self.attack_s_air_left = False
        self.attack_s_air_right = False
        self.attack_n_air = False
        self.attack_d_air = False

        # ground attac
        self.s_light_left = False
        self.s_light_right = False
        self.n_light_left = False
        self.n_light_right = False
        self.d_light_left = False
        self.d_light_right = False

        # air attac
        self.s_air_left = False
        self.s_air_right = False
        self.n_air = False
        self.d_air = False
        self.boolean = False
        self.bool = False

        # dash
        self.dash_left = False
        self.dash_right = False
        self.dash_left2 = False
        self.dash_right2 = False

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.player = Player(self)
        # all platforms
        p1 = SoftPlatform(150, HEIGHT - 140, 900, 100)
        self.all_sprites.add(p1)
        self.platforms.add(p1)
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        current_pos = self.player.vel.x
        current_pos2 = self.player.pos.x
        keys = pg.key.get_pressed()
        # Game Loop - event
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                # if w key is pressed, jump, only if the jumps are not exhausted
                if event.key == pg.K_w:
                    self.player.jump()
                isGrounded = pg.sprite.spritecollide(self.player, self.platforms, False)
                if isGrounded:
                    if event.key == pg.K_m:
                        self.player.dash_right()
                        self.player.dash_left()
                    if event.key == pg.K_n:
                        if current_pos > 0:
                            self.player.d_sig_right()
                        if current_pos < 0:
                            self.player.d_sig_left()

            # s_light_right
            if self.player.attack_timer > self.player.attack_delay_s_light:
                if keys[pg.K_d]:
                    if event.type == pg.KEYDOWN:
                        isGrounded = pg.sprite.spritecollide(self.player, self.platforms, False)
                        # if conditions are met for the specific attack, then it does that specific attack
                        if isGrounded:
                            if event.key == pg.K_b:
                                self.attack_s_light_right = True
                                self.s_light_right = True
                                self.player.s_light_right()
                                self.player.attack_timer = 0
                                # if event.key == pg.K_a and event.key == pg.K_SPACE:
                                #     self.player.move_control = False

            # s_light_left
            if self.player.attack_timer > self.player.attack_delay_s_light:
                if keys[pg.K_a]:
                    if event.type == pg.KEYDOWN:
                        isGrounded = pg.sprite.spritecollide(self.player, self.platforms, False)
                        # if conditions are met for the specific attack, then it does that specific attack
                        if isGrounded:
                            if event.key == pg.K_b:
                                self.attack_s_light_left = True
                                self.s_light_left = True
                                self.player.s_light_left()
                                self.player.attack_timer = 0
                                # if event.key == pg.K_a and event.key == pg.K_SPACE:
                                #     self.player.move_control = False

            # n_light_left
            if self.player.attack_timer > self.player.attack_delay_n_light:
                if not keys[pg.K_a] and not keys[pg.K_d] and not keys[pg.K_s]:
                    if event.type == pg.KEYDOWN:
                        isGrounded = pg.sprite.spritecollide(self.player, self.platforms, False)
                        # if conditions are met for the specific attack, then it does that specific attack
                        if isGrounded:
                            if event.key == pg.K_b:
                                if current_pos < 0:
                                    self.attack_n_light_left = True
                                    self.n_light_left = True
                                    self.player.n_light_left()
                                    self.player.attack_timer = 0
                                    # if event.key == pg.K_a and event.key == pg.K_SPACE:
                                    #     self.player.move_control = False

            # n_light_right
            if self.player.attack_timer > self.player.attack_delay_n_light:
                if not keys[pg.K_a] and not keys[pg.K_d] and not keys[pg.K_s]:
                    if event.type == pg.KEYDOWN:
                        isGrounded = pg.sprite.spritecollide(self.player, self.platforms, False)
                        # if conditions are met for the specific attack, then it does that specific attack
                        if isGrounded:
                            if event.key == pg.K_b:
                                if current_pos > 0:
                                    self.attack_n_light_right = True
                                    self.n_light_right = True
                                    self.player.n_light_right()
                                    self.player.attack_timer = 0
                                    # if event.key == pg.K_a and event.key == pg.K_SPACE:
                                    #     self.player.move_control = False

            # d_light_left
            if self.player.attack_timer > self.player.attack_delay_d_light:
                if keys[pg.K_s]:
                    if not keys[pg.K_a] and not keys[pg.K_d]:
                        if event.type == pg.KEYDOWN:
                            isGrounded = pg.sprite.spritecollide(self.player, self.platforms, False)
                            # if conditions are met for the specific attack, then it does that specific attack
                            if isGrounded:
                                if event.key == pg.K_b:
                                    if current_pos < 0:
                                        self.attack_d_light_left = True
                                        self.d_light_left = True
                                        self.player.d_light_left()
                                        self.player.attack_timer = 0
                                        # if event.key == pg.K_a and event.key == pg.K_SPACE:
                                        #     self.player.move_control = False

            # d_light_right
            if self.player.attack_timer > self.player.attack_delay_d_light:
                if keys[pg.K_s]:
                    if not keys[pg.K_a] and not keys[pg.K_d]:
                        if event.type == pg.KEYDOWN:
                            isGrounded = pg.sprite.spritecollide(self.player, self.platforms, False)
                            # if conditions are met for the specific attack, then it does that specific attack
                            if isGrounded:
                                if event.key == pg.K_b:
                                    if current_pos > 0:
                                        self.attack_d_light_right = True
                                        self.d_light_right = True
                                        self.player.d_light_right()
                                        self.player.attack_timer = 0
                                        # if event.key == pg.K_a and event.key == pg.K_SPACE:
                                        #     self.player.move_control = False

            # s_air_left
            if self.player.attack_timer > self.player.attack_delay_s_air:
                if keys[pg.K_a]:
                    if event.type == pg.KEYDOWN:
                        isGrounded = pg.sprite.spritecollide(self.player, self.platforms, False)
                        # if conditions are met for the specific attack, then it does that specific attack
                        if not isGrounded:
                            if event.key == pg.K_b:
                                self.attack_s_air_left = True
                                self.player.attack_timer = 0
                                # if event.key == pg.K_a and event.key == pg.K_SPACE:
                                #     self.player.move_control = False

            # s_air_right
            if self.player.attack_timer > self.player.attack_delay_s_air:
                if keys[pg.K_d]:
                    if event.type == pg.KEYDOWN:
                        isGrounded = pg.sprite.spritecollide(self.player, self.platforms, False)
                        # if conditions are met for the specific attack, then it does that specific attack
                        if not isGrounded:
                            if event.key == pg.K_b:
                                self.attack_s_air_right = True
                                self.player.attack_timer = 0
                                # if event.key == pg.K_a and event.key == pg.K_SPACE:
                                #     self.player.move_control = False

            # d_air
            if self.player.attack_timer > self.player.attack_delay_d_air:
                if keys[pg.K_s]:
                    if event.type == pg.KEYDOWN:
                        isGrounded = pg.sprite.spritecollide(self.player, self.platforms, False)
                        # if conditions are met for the specific attack, then it does that specific attack
                        if not isGrounded:
                            if event.key == pg.K_b:
                                self.attack_d_air = True
                                self.d_air = True
                                self.player.attack_timer = 0
                                # if event.key == pg.K_a and event.key == pg.K_SPACE:
                                #     self.player.move_control = False

            # n_air
            if self.player.attack_timer > self.player.attack_delay_n_air:
                if not keys[pg.K_a] and not keys[pg.K_d] and not keys[pg.K_s]:
                    if event.type == pg.KEYDOWN:
                        isGrounded = pg.sprite.spritecollide(self.player, self.platforms, False)
                        # if conditions are met for the specific attack, then it does that specific attack
                        if not isGrounded:
                            if event.key == pg.K_b:
                                self.attack_n_air = True
                                self.n_air = True
                                self.player.attack_timer = 0
                                # if event.key == pg.K_a and event.key == pg.K_SPACE:
                                #     self.player.move_control = False

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platform - only if falling
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if self.player.vel.y > 0:
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
