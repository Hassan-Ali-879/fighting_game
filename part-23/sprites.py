# sprite classes for defense game
import pygame as pg
from settings import *
from os import path
vec = pg.math.Vector2
player_pos = []


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 35))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.attack_counter = 0
        self.dt = 0.2
        self.timer = 0
        self.attack_timer = 0
        self.timer_attack_frames = 0
        self.dash_timer = 10
        self.player_movement_x = 0
        self.player_movement_y = 0
        self.current_pos = 0

        # these are the attack delays between attacks
        self.attack_delay_n_light = 60
        self.attack_delay_s_light = 25
        self.attack_delay_d_light = 45
        self.attack_delay_s_air = 30
        self.attack_delay_n_air = 30
        self.attack_delay_d_air = 30

        self.attack_delay_s_sig = 60
        self.attack_delay_n_sig = 30
        self.attack_delay_d_sig = 60
        self.attack_recovery = 30
        self.attack_ground_pound = 30

        self.dash_delay = 15

        self.move_control = False
        self.frame_counter = False
        self.right = False
        self.left = False
        self.attack_timer_boolean = False

    def jump(self):
        # jump if jump key is pressed, and triple jumps are recharged when touching platforms
        if self.timer <= 0:
            global player_jump_count
            self.rect.x += 1
            self.rect.x -= 1
            player_jump_count -= 1
            if player_jump_count > 0:
                self.vel.y = -PLAYER_JUMP
            hits = pg.sprite.spritecollide(self, self.game.platforms, False)
            if hits:
                player_jump_count = 3

    def dash_right(self):
        keys = pg.key.get_pressed()
        if not self.move_control:
            if self.dash_timer > self.dash_delay:
                if keys[pg.K_d]:
                    self.vel.x += 8

    def dash_left(self):
        keys = pg.key.get_pressed()
        if not self.move_control:
            if self.dash_timer > self.dash_delay:
                if keys[pg.K_a]:
                    self.vel.x -= 8

    def s_light_right(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.centerx + 80, self.rect.centery, 0, 0, 20, 20, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def s_light_left(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.centerx - 80, self.rect.centery, 0, 0, 20, 20, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def n_light_right(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.centerx + 70, self.rect.centery, 0, 0, 20, 20, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def n_light_left(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.centerx - 70, self.rect.centery, 0, 0, 20, 20, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def d_light_right(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.right + 15, self.rect.centery + 10.5, 0, 0, 30, 15, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def d_light_right2(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.right + 35, self.rect.centery + 10.5, 0, 0, 30, 15, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def d_light_right3(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.right + 63.3, self.rect.centery + 8.5, 0, 0, 40, 17, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def d_light_left(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.left - 15, self.rect.centery + 10.5, 0, 0, 30, 15, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def d_light_left2(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.left - 35, self.rect.centery + 10.5, 0, 0, 30, 15, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def d_light_left3(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.left - 63.3, self.rect.centery + 8.5, 0, 0, 40, 17, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def s_air_right(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.centerx + 80, self.rect.centery, 0, 0, 20, 20, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def s_air_left(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.centerx - 80, self.rect.centery, 0, 0, 20, 20, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def n_air(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.centerx + 15, self.rect.centery - 50, 0, 0, 20, 20, 0.2)
        bullet2 = Bullet(self.rect.centerx - 15, self.rect.centery - 50, 0, 0, 20, 20, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)
        self.game.all_sprites.add(bullet2)
        self.game.bullets.add(bullet2)

    def d_air(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.centerx + 15, self.rect.centery + 60, 0, 0, 20, 20, 0.2)
        bullet2 = Bullet(self.rect.centerx - 15, self.rect.centery + 60, 0, 0, 20, 20, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)
        self.game.all_sprites.add(bullet2)
        self.game.bullets.add(bullet2)

    # all attack hitboxes for s_sig_right
    def s_sig_right(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.right, self.rect.centery - 22.5, 0, 0, 20, 15, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def s_sig_right2(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.right + 12.5, self.rect.centery - 7.5, 0, 0, 25, 20, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def s_sig_right3(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.right + 15, self.rect.centery, 0, 0, 30, 30, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def s_sig_right4(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.centerx + 70, self.rect.centery, 0, 0, 20, 20, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    # all attack hitboxes for s_sig_left
    def s_sig_left(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.left, self.rect.centery - 22.5, 0, 0, 20, 15, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def s_sig_left2(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.left - 12.5, self.rect.centery - 7.5, 0, 0, 25, 20, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def s_sig_left3(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.left - 15, self.rect.centery, 0, 0, 30, 30, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def s_sig_left4(self):
        self.attack_timer = 0
        bullet = Bullet(self.rect.centerx - 70, self.rect.centery, 0, 0, 20, 20, 0.2)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

    def d_sig_left(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_s]:
            if not keys[pg.K_a] and not keys[pg.K_d]:
                if self.attack_timer > self.attack_delay_d_sig:
                    self.attack_timer = 0
                    bullet = Bullet(WIDTH + 450, self.rect.centery - 150, -16, 0, 900, 125, 30)
                    self.game.all_sprites.add(bullet)
                    self.game.bullets.add(bullet)
                    if self.game.bullets.add(bullet):
                        self.game.boolean = True

    def d_sig_right(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_s]:
            if not keys[pg.K_a] and not keys[pg.K_d]:
                if self.attack_timer > self.attack_delay_d_sig:
                    self.attack_timer = 0
                    bullet = Bullet(-450, self.rect.centery - 150, 16, 0, 900, 125, 30)
                    self.game.all_sprites.add(bullet)
                    self.game.bullets.add(bullet)
                    if self.game.bullets.add(bullet):
                        self.game.boolean = True

    def update(self):
        # print(self.right)
        # print(self.left)
        # print(self.timer)
        # print(self.attack_timer)
        # print(self.timer_attack_frames)
        self.current_pos = self.vel.x
        isGrounded = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        self.attack_timer += 1
        self.timer -= self.dt
        self.dash_timer += 1
        if not self.move_control:
            # move left
            if keys[pg.K_a]:
                self.acc.x = -PLAYER_ACC
                self.left = True
            if not keys[pg.K_a]:
                self.left = False
            # move right
            if keys[pg.K_d]:
                self.acc.x = PLAYER_ACC
                self.right = True
            if not keys[pg.K_d]:
                self.right = False
            # if not touching any platforms, fast fall if wanted key is pressed, and if not grounded
            if not isGrounded:
                if keys[pg.K_s]:
                    self.vel.y += PLAYER_GRAV * 6/8

        # if specific attack boolean is false, it makes another boolean true and does not let attacks bug out
        if not self.game.attack_s_light_left:
            self.game.bool = True
        if not self.game.attack_s_light_right:
            self.game.bool = True
        if not self.game.attack_n_light_left:
            self.game.bool = True
        if not self.game.attack_n_light_right:
            self.game.bool = True
        if not self.game.attack_d_light_left:
            self.game.bool = True
        if not self.game.attack_d_light_right:
            self.game.bool = True
        if not self.game.attack_s_sig_left:
            self.game.bool = True
        if not self.game.attack_s_sig_right:
            self.game.bool = True

        if not self.game.attack_s_air_left:
            self.game.bool = True
        if not self.game.attack_s_air_right:
            self.game.bool = True
        if not self.game.attack_n_air:
            self.game.bool = True
        if not self.game.attack_d_air:
            self.game.bool = True

        if self.game.attack_s_light_left:
            self.game.bool = False
        if self.game.attack_s_light_right:
            self.game.bool = False
        if self.game.attack_n_light_left:
            self.game.bool = False
        if self.game.attack_n_light_right:
            self.game.bool = False
        if self.game.attack_d_light_left:
            self.game.bool = False
        if self.game.attack_d_light_right:
            self.game.bool = False
        if self.game.attack_s_sig_left:
            self.game.bool = False
        if self.game.attack_s_sig_right:
            self.game.bool = False

        if self.game.attack_s_air_left:
            self.game.bool = False
        if self.game.attack_s_air_right:
            self.game.bool = False
        if self.game.attack_n_air:
            self.game.bool = False
        if self.game.attack_d_air:
            self.game.bool = False

        if self.game.bool:
            self.timer_attack_frames = 0

        if self.timer < 0:
            self.move_control = False

        # grounded attack frame by frame commands
        if self.game.s_light_left:
            if self.game.attack_s_light_left:
                self.timer_attack_frames += 1
                if self.timer_attack_frames == 2:
                    self.s_light_left()
                if self.timer_attack_frames == 3:
                    self.s_light_left()
                if self.timer_attack_frames == 4:
                    self.s_light_left()
                if self.timer_attack_frames == 5:
                    self.s_light_left()
                if self.timer_attack_frames == 6:
                    self.s_light_left()
                if self.timer_attack_frames == 7:
                    self.s_light_left()
                if self.timer_attack_frames == 8:
                    self.s_light_left()
                if self.timer_attack_frames == 9:
                    self.s_light_left()
                if self.timer_attack_frames == 10:
                    self.s_light_left()
                if self.timer_attack_frames == 11:
                    self.s_light_left()
                if self.timer_attack_frames == 12:
                    self.s_light_left()
                if self.timer_attack_frames == 13:
                    self.s_light_left()
                if self.timer_attack_frames == 14:
                    self.s_light_left()
                if self.timer_attack_frames == 15:
                    self.s_light_left()
                if self.timer_attack_frames == 16:
                    self.s_light_left()
                if self.timer_attack_frames == 17:
                    self.s_light_left()
                if self.timer_attack_frames == 18:
                    self.s_light_left()
                if self.timer_attack_frames == 19:
                    self.s_light_left()
                if self.timer_attack_frames == 20:
                    self.game.attack_s_light_left = False
                    self.game.s_light_left = False
                    self.timer_attack_frames = 0

        if self.game.s_light_right:
            if self.game.attack_s_light_right:
                self.timer_attack_frames += 1
                if self.timer_attack_frames == 2:
                    self.s_light_right()
                if self.timer_attack_frames == 3:
                    self.s_light_right()
                if self.timer_attack_frames == 4:
                    self.s_light_right()
                if self.timer_attack_frames == 5:
                    self.s_light_right()
                if self.timer_attack_frames == 6:
                    self.s_light_right()
                if self.timer_attack_frames == 7:
                    self.s_light_right()
                if self.timer_attack_frames == 8:
                    self.s_light_right()
                if self.timer_attack_frames == 9:
                    self.s_light_right()
                if self.timer_attack_frames == 10:
                    self.s_light_right()
                if self.timer_attack_frames == 11:
                    self.s_light_right()
                if self.timer_attack_frames == 12:
                    self.s_light_right()
                if self.timer_attack_frames == 13:
                    self.s_light_right()
                if self.timer_attack_frames == 14:
                    self.s_light_right()
                if self.timer_attack_frames == 15:
                    self.s_light_right()
                if self.timer_attack_frames == 16:
                    self.s_light_right()
                if self.timer_attack_frames == 17:
                    self.s_light_right()
                if self.timer_attack_frames == 18:
                    self.s_light_right()
                if self.timer_attack_frames == 19:
                    self.s_light_right()
                if self.timer_attack_frames == 20:
                    self.game.attack_s_light_right = False
                    self.game.s_light_right = False
                    self.timer_attack_frames = 0

        if self.game.n_light_left:
            self.timer_attack_frames += 1
            if self.timer_attack_frames == 2:
                self.n_light_left()
            if self.timer_attack_frames == 3:
                self.n_light_left()
            if self.timer_attack_frames == 4:
                self.n_light_left()
            if self.timer_attack_frames == 5:
                self.n_light_left()
            if self.timer_attack_frames == 6:
                self.n_light_left()
            if self.timer_attack_frames == 7:
                self.n_light_left()
            if self.timer_attack_frames == 8:
                self.n_light_left()
            if self.timer_attack_frames == 9:
                self.n_light_left()
            if self.timer_attack_frames == 10:
                self.n_light_left()
            if self.timer_attack_frames == 11:
                self.n_light_left()
            if self.timer_attack_frames == 12:
                self.n_light_left()
            if self.timer_attack_frames == 13:
                self.n_light_left()
            if self.timer_attack_frames == 14:
                self.n_light_left()
            if self.timer_attack_frames == 15:
                self.n_light_left()
            if self.timer_attack_frames == 16:
                self.n_light_left()
            if self.timer_attack_frames == 17:
                self.n_light_left()
            if self.timer_attack_frames == 18:
                self.n_light_left()
            if self.timer_attack_frames == 19:
                self.n_light_left()
            if self.timer_attack_frames == 20:
                self.n_light_left()
            if self.timer_attack_frames == 40:
                self.n_light_left()
            if self.timer_attack_frames == 41:
                self.n_light_left()
            if self.timer_attack_frames == 42:
                self.n_light_left()
            if self.timer_attack_frames == 43:
                self.n_light_left()
            if self.timer_attack_frames == 44:
                self.n_light_left()
            if self.timer_attack_frames == 45:
                self.n_light_left()
            if self.timer_attack_frames == 46:
                self.n_light_left()
            if self.timer_attack_frames == 47:
                self.n_light_left()
            if self.timer_attack_frames == 48:
                self.n_light_left()
            if self.timer_attack_frames == 49:
                self.n_light_left()
            if self.timer_attack_frames == 50:
                self.n_light_left()
            if self.timer_attack_frames == 51:
                self.n_light_left()
            if self.timer_attack_frames == 52:
                self.n_light_left()
            if self.timer_attack_frames == 53:
                self.n_light_left()
            if self.timer_attack_frames == 54:
                self.n_light_left()
            if self.timer_attack_frames == 55:
                self.n_light_left()
            if self.timer_attack_frames == 56:
                self.n_light_left()
            if self.timer_attack_frames == 57:
                self.n_light_left()
            if self.timer_attack_frames == 58:
                self.n_light_left()
            if self.timer_attack_frames == 59:
                self.n_light_left()
            if self.timer_attack_frames == 60:
                self.game.attack_n_light_left = False
                self.game.n_light_left = False
                self.timer_attack_frames = 0

        if self.game.n_light_right:
            if self.game.attack_n_light_right:
                self.timer_attack_frames += 1
                if self.timer_attack_frames == 2:
                    self.n_light_right()
                if self.timer_attack_frames == 3:
                    self.n_light_right()
                if self.timer_attack_frames == 4:
                    self.n_light_right()
                if self.timer_attack_frames == 5:
                    self.n_light_right()
                if self.timer_attack_frames == 6:
                    self.n_light_right()
                if self.timer_attack_frames == 7:
                    self.n_light_right()
                if self.timer_attack_frames == 8:
                    self.n_light_right()
                if self.timer_attack_frames == 9:
                    self.n_light_right()
                if self.timer_attack_frames == 10:
                    self.n_light_right()
                if self.timer_attack_frames == 11:
                    self.n_light_right()
                if self.timer_attack_frames == 12:
                    self.n_light_right()
                if self.timer_attack_frames == 13:
                    self.n_light_right()
                if self.timer_attack_frames == 14:
                    self.n_light_right()
                if self.timer_attack_frames == 15:
                    self.n_light_right()
                if self.timer_attack_frames == 16:
                    self.n_light_right()
                if self.timer_attack_frames == 17:
                    self.n_light_right()
                if self.timer_attack_frames == 18:
                    self.n_light_right()
                if self.timer_attack_frames == 19:
                    self.n_light_right()
                if self.timer_attack_frames == 20:
                    self.n_light_right()
                if self.timer_attack_frames == 40:
                    self.n_light_right()
                if self.timer_attack_frames == 41:
                    self.n_light_right()
                if self.timer_attack_frames == 42:
                    self.n_light_right()
                if self.timer_attack_frames == 43:
                    self.n_light_right()
                if self.timer_attack_frames == 44:
                    self.n_light_right()
                if self.timer_attack_frames == 45:
                    self.n_light_right()
                if self.timer_attack_frames == 46:
                    self.n_light_right()
                if self.timer_attack_frames == 47:
                    self.n_light_right()
                if self.timer_attack_frames == 48:
                    self.n_light_right()
                if self.timer_attack_frames == 49:
                    self.n_light_right()
                if self.timer_attack_frames == 50:
                    self.n_light_right()
                if self.timer_attack_frames == 51:
                    self.n_light_right()
                if self.timer_attack_frames == 52:
                    self.n_light_right()
                if self.timer_attack_frames == 53:
                    self.n_light_right()
                if self.timer_attack_frames == 54:
                    self.n_light_right()
                if self.timer_attack_frames == 55:
                    self.n_light_right()
                if self.timer_attack_frames == 56:
                    self.n_light_right()
                if self.timer_attack_frames == 57:
                    self.n_light_right()
                if self.timer_attack_frames == 58:
                    self.n_light_right()
                if self.timer_attack_frames == 59:
                    self.n_light_right()
                if self.timer_attack_frames == 60:
                    self.game.attack_n_light_right = False
                    self.game.n_light_right = False
                    self.timer_attack_frames = 0

        if self.game.d_light_left:
            if self.game.attack_d_light_left:
                self.timer_attack_frames += 1
                if self.timer_attack_frames == 2:
                    self.d_light_left()
                if self.timer_attack_frames == 3:
                    self.d_light_left()
                if self.timer_attack_frames == 4:
                    self.d_light_left()
                if self.timer_attack_frames == 5:
                    self.d_light_left()
                if self.timer_attack_frames == 6:
                    self.d_light_left()
                if self.timer_attack_frames == 7:
                    self.d_light_left()
                if self.timer_attack_frames == 8:
                    self.d_light_left()
                if self.timer_attack_frames == 9:
                    self.d_light_left()
                if self.timer_attack_frames == 10:
                    self.d_light_left()

                if self.timer_attack_frames == 15:
                    self.d_light_left2()
                if self.timer_attack_frames == 16:
                    self.d_light_left2()
                if self.timer_attack_frames == 17:
                    self.d_light_left2()
                if self.timer_attack_frames == 18:
                    self.d_light_left2()
                if self.timer_attack_frames == 19:
                    self.d_light_left2()
                if self.timer_attack_frames == 20:
                    self.d_light_left2()
                if self.timer_attack_frames == 21:
                    self.d_light_left2()
                if self.timer_attack_frames == 22:
                    self.d_light_left2()
                if self.timer_attack_frames == 23:
                    self.d_light_left2()
                if self.timer_attack_frames == 24:
                    self.d_light_left2()
                if self.timer_attack_frames == 25:
                    self.d_light_left2()

                if self.timer_attack_frames == 22:
                    self.d_light_left3()
                if self.timer_attack_frames == 23:
                    self.d_light_left3()
                if self.timer_attack_frames == 24:
                    self.d_light_left3()
                if self.timer_attack_frames == 25:
                    self.d_light_left3()
                if self.timer_attack_frames == 30:
                    self.d_light_left3()
                if self.timer_attack_frames == 31:
                    self.d_light_left3()
                if self.timer_attack_frames == 32:
                    self.d_light_left3()
                if self.timer_attack_frames == 33:
                    self.d_light_left3()
                if self.timer_attack_frames == 34:
                    self.d_light_left3()
                if self.timer_attack_frames == 35:
                    self.d_light_left3()
                if self.timer_attack_frames == 36:
                    self.d_light_left3()
                if self.timer_attack_frames == 37:
                    self.d_light_left3()
                if self.timer_attack_frames == 38:
                    self.d_light_left3()
                if self.timer_attack_frames == 39:
                    self.d_light_left3()
                if self.timer_attack_frames == 40:
                    self.game.attack_d_light_left = False
                    self.game.d_light_left = False
                    self.timer_attack_frames = 0

        if self.game.d_light_right:
            self.timer_attack_frames += 1
            if self.timer_attack_frames == 2:
                self.d_light_right()
            if self.timer_attack_frames == 3:
                self.d_light_right()
            if self.timer_attack_frames == 4:
                self.d_light_right()
            if self.timer_attack_frames == 5:
                self.d_light_right()
            if self.timer_attack_frames == 6:
                self.d_light_right()
            if self.timer_attack_frames == 7:
                self.d_light_right()
            if self.timer_attack_frames == 8:
                self.d_light_right()
            if self.timer_attack_frames == 9:
                self.d_light_right()
            if self.timer_attack_frames == 10:
                self.d_light_right()

            if self.timer_attack_frames == 15:
                self.d_light_right2()
            if self.timer_attack_frames == 16:
                self.d_light_right2()
            if self.timer_attack_frames == 17:
                self.d_light_right2()
            if self.timer_attack_frames == 18:
                self.d_light_right2()
            if self.timer_attack_frames == 19:
                self.d_light_right2()
            if self.timer_attack_frames == 20:
                self.d_light_right2()
            if self.timer_attack_frames == 21:
                self.d_light_right2()
            if self.timer_attack_frames == 22:
                self.d_light_right2()
            if self.timer_attack_frames == 23:
                self.d_light_right2()
            if self.timer_attack_frames == 24:
                self.d_light_right2()
            if self.timer_attack_frames == 25:
                self.d_light_right2()

            if self.timer_attack_frames == 22:
                self.d_light_right3()
            if self.timer_attack_frames == 23:
                self.d_light_right3()
            if self.timer_attack_frames == 24:
                self.d_light_right3()
            if self.timer_attack_frames == 25:
                self.d_light_right3()
            if self.timer_attack_frames == 30:
                self.d_light_right3()
            if self.timer_attack_frames == 31:
                self.d_light_right3()
            if self.timer_attack_frames == 32:
                self.d_light_right3()
            if self.timer_attack_frames == 33:
                self.d_light_right3()
            if self.timer_attack_frames == 34:
                self.d_light_right3()
            if self.timer_attack_frames == 35:
                self.d_light_right3()
            if self.timer_attack_frames == 36:
                self.d_light_right3()
            if self.timer_attack_frames == 37:
                self.d_light_right3()
            if self.timer_attack_frames == 38:
                self.d_light_right3()
            if self.timer_attack_frames == 39:
                self.d_light_right3()
            if self.timer_attack_frames == 40:
                self.game.attack_d_light_right = False
                self.game.d_light_right = False
                self.timer_attack_frames = 0

        if self.game.s_sig_left:
            if self.game.attack_s_sig_left:
                self.timer_attack_frames += 1
                if self.timer_attack_frames == 2:
                    self.s_sig_left()
                if self.timer_attack_frames == 3:
                    self.s_sig_left()
                if self.timer_attack_frames == 4:
                    self.s_sig_left()
                if self.timer_attack_frames == 5:
                    self.s_sig_left()
                if self.timer_attack_frames == 6:
                    self.s_sig_left()
                if self.timer_attack_frames == 7:
                    self.s_sig_left2()
                if self.timer_attack_frames == 8:
                    self.s_sig_left2()
                if self.timer_attack_frames == 9:
                    self.s_sig_left2()
                if self.timer_attack_frames == 10:
                    self.s_sig_left2()
                if self.timer_attack_frames == 11:
                    self.s_sig_left2()
                if self.timer_attack_frames == 12:
                    self.s_sig_left2()
                if self.timer_attack_frames == 13:
                    self.s_sig_left2()
                if self.timer_attack_frames == 14:
                    self.s_sig_left2()
                if self.timer_attack_frames == 15:
                    self.s_sig_left2()
                if self.timer_attack_frames == 16:
                    self.s_sig_left2()
                if self.timer_attack_frames == 17:
                    self.s_sig_left2()
                if self.timer_attack_frames == 18:
                    self.s_sig_left2()
                if self.timer_attack_frames == 19:
                    self.s_sig_left2()
                if self.timer_attack_frames == 20:
                    self.s_sig_left2()
                    self.s_sig_left3()
                if self.timer_attack_frames == 21:
                    self.s_sig_left3()
                if self.timer_attack_frames == 22:
                    self.s_sig_left3()
                if self.timer_attack_frames == 23:
                    self.s_sig_left3()
                if self.timer_attack_frames == 24:
                    self.s_sig_left3()
                if self.timer_attack_frames == 25:
                    self.s_sig_left3()
                if self.timer_attack_frames == 26:
                    self.s_sig_left3()
                if self.timer_attack_frames == 27:
                    self.s_sig_left3()
                if self.timer_attack_frames == 28:
                    self.s_sig_left3()
                if self.timer_attack_frames == 29:
                    self.s_sig_left3()

                if self.timer_attack_frames == 40:
                    self.s_sig_left4()
                if self.timer_attack_frames == 40:
                    self.s_sig_left4()
                if self.timer_attack_frames == 41:
                    self.s_sig_left4()
                if self.timer_attack_frames == 42:
                    self.s_sig_left4()
                if self.timer_attack_frames == 43:
                    self.s_sig_left4()
                if self.timer_attack_frames == 44:
                    self.s_sig_left4()
                if self.timer_attack_frames == 45:
                    self.s_sig_left4()
                if self.timer_attack_frames == 46:
                    self.s_sig_left4()
                if self.timer_attack_frames == 47:
                    self.s_sig_left4()
                if self.timer_attack_frames == 48:
                    self.s_sig_left4()
                if self.timer_attack_frames == 49:
                    self.s_sig_left4()
                if self.timer_attack_frames == 50:
                    self.s_sig_left4()
                if self.timer_attack_frames == 51:
                    self.s_sig_left4()
                if self.timer_attack_frames == 52:
                    self.s_sig_left4()
                if self.timer_attack_frames == 53:
                    self.s_sig_left4()
                if self.timer_attack_frames == 54:
                    self.s_sig_left4()
                if self.timer_attack_frames == 55:
                    self.s_sig_left4()
                if self.timer_attack_frames == 56:
                    self.s_sig_left4()
                if self.timer_attack_frames == 57:
                    self.s_sig_left4()
                if self.timer_attack_frames == 58:
                    self.s_sig_left4()
                if self.timer_attack_frames == 59:
                    self.s_sig_left4()
                if self.timer_attack_frames == 60:
                    self.game.attack_s_sig_left = False
                    self.game.s_sig_left = False
                    self.timer_attack_frames = 0

        if self.game.s_sig_right:
            if self.game.attack_s_sig_right:
                self.timer_attack_frames += 1
                if self.timer_attack_frames == 2:
                    self.s_sig_right()
                if self.timer_attack_frames == 3:
                    self.s_sig_right()
                if self.timer_attack_frames == 4:
                    self.s_sig_right()
                if self.timer_attack_frames == 5:
                    self.s_sig_right()
                if self.timer_attack_frames == 6:
                    self.s_sig_right()
                if self.timer_attack_frames == 7:
                    self.s_sig_right2()
                if self.timer_attack_frames == 8:
                    self.s_sig_right2()
                if self.timer_attack_frames == 9:
                    self.s_sig_right2()
                if self.timer_attack_frames == 10:
                    self.s_sig_right2()
                if self.timer_attack_frames == 11:
                    self.s_sig_right2()
                if self.timer_attack_frames == 12:
                    self.s_sig_right2()
                if self.timer_attack_frames == 13:
                    self.s_sig_right2()
                if self.timer_attack_frames == 14:
                    self.s_sig_right2()
                if self.timer_attack_frames == 15:
                    self.s_sig_right2()
                if self.timer_attack_frames == 16:
                    self.s_sig_right2()
                if self.timer_attack_frames == 17:
                    self.s_sig_right2()
                if self.timer_attack_frames == 18:
                    self.s_sig_right2()
                if self.timer_attack_frames == 19:
                    self.s_sig_right2()
                if self.timer_attack_frames == 20:
                    self.s_sig_right2()
                    self.s_sig_right3()
                if self.timer_attack_frames == 21:
                    self.s_sig_right3()
                if self.timer_attack_frames == 22:
                    self.s_sig_right3()
                if self.timer_attack_frames == 23:
                    self.s_sig_right3()
                if self.timer_attack_frames == 24:
                    self.s_sig_right3()
                if self.timer_attack_frames == 25:
                    self.s_sig_right3()
                if self.timer_attack_frames == 26:
                    self.s_sig_right3()
                if self.timer_attack_frames == 27:
                    self.s_sig_right3()
                if self.timer_attack_frames == 28:
                    self.s_sig_right3()
                if self.timer_attack_frames == 29:
                    self.s_sig_right3()

                if self.timer_attack_frames == 40:
                    self.s_sig_right4()
                if self.timer_attack_frames == 40:
                    self.s_sig_right4()
                if self.timer_attack_frames == 41:
                    self.s_sig_right4()
                if self.timer_attack_frames == 42:
                    self.s_sig_right4()
                if self.timer_attack_frames == 43:
                    self.s_sig_right4()
                if self.timer_attack_frames == 44:
                    self.s_sig_right4()
                if self.timer_attack_frames == 45:
                    self.s_sig_right4()
                if self.timer_attack_frames == 46:
                    self.s_sig_right4()
                if self.timer_attack_frames == 47:
                    self.s_sig_right4()
                if self.timer_attack_frames == 48:
                    self.s_sig_right4()
                if self.timer_attack_frames == 49:
                    self.s_sig_right4()
                if self.timer_attack_frames == 50:
                    self.s_sig_right4()
                if self.timer_attack_frames == 51:
                    self.s_sig_right4()
                if self.timer_attack_frames == 52:
                    self.s_sig_right4()
                if self.timer_attack_frames == 53:
                    self.s_sig_right4()
                if self.timer_attack_frames == 54:
                    self.s_sig_right4()
                if self.timer_attack_frames == 55:
                    self.s_sig_right4()
                if self.timer_attack_frames == 56:
                    self.s_sig_right4()
                if self.timer_attack_frames == 57:
                    self.s_sig_right4()
                if self.timer_attack_frames == 58:
                    self.s_sig_right4()
                if self.timer_attack_frames == 59:
                    self.s_sig_right4()
                if self.timer_attack_frames == 60:
                    self.game.attack_s_sig_right = False
                    self.game.s_sig_right = False
                    self.timer_attack_frames = 0

        # aerial attack frame by frame commands
        if self.game.attack_s_air_left:
            self.timer_attack_frames += 1
            if self.timer_attack_frames == 2:
                self.s_air_left()
            if self.timer_attack_frames == 3:
                self.s_air_left()
            if self.timer_attack_frames == 4:
                self.s_air_left()
            if self.timer_attack_frames == 5:
                self.s_air_left()
            if self.timer_attack_frames == 6:
                self.s_air_left()
            if self.timer_attack_frames == 7:
                self.s_air_left()
            if self.timer_attack_frames == 8:
                self.s_air_left()
            if self.timer_attack_frames == 9:
                self.s_air_left()
            if self.timer_attack_frames == 10:
                self.s_air_left()
            if self.timer_attack_frames == 11:
                self.s_air_left()
            if self.timer_attack_frames == 12:
                self.s_air_left()
            if self.timer_attack_frames == 13:
                self.s_air_left()
            if self.timer_attack_frames == 14:
                self.s_air_left()
            if self.timer_attack_frames > 14:
                self.game.attack_s_air_left = False
                self.timer_attack_frames = 0

        if self.game.attack_s_air_right:
            self.timer_attack_frames += 1
            if self.timer_attack_frames == 2:
                self.s_air_right()
            if self.timer_attack_frames == 3:
                self.s_air_right()
            if self.timer_attack_frames == 4:
                self.s_air_right()
            if self.timer_attack_frames == 5:
                self.s_air_right()
            if self.timer_attack_frames == 6:
                self.s_air_right()
            if self.timer_attack_frames == 7:
                self.s_air_right()
            if self.timer_attack_frames == 8:
                self.s_air_right()
            if self.timer_attack_frames == 9:
                self.s_air_right()
            if self.timer_attack_frames == 10:
                self.s_air_right()
            if self.timer_attack_frames == 11:
                self.s_air_right()
            if self.timer_attack_frames == 12:
                self.s_air_right()
            if self.timer_attack_frames == 13:
                self.s_air_right()
            if self.timer_attack_frames == 14:
                self.s_air_right()
            if self.timer_attack_frames > 14:
                self.game.attack_s_air_right = False
                self.timer_attack_frames = 0

        if self.game.attack_n_air:
            self.timer_attack_frames += 1
            if self.timer_attack_frames == 2:
                self.n_air()
            if self.timer_attack_frames == 3:
                self.n_air()
            if self.timer_attack_frames == 4:
                self.n_air()
            if self.timer_attack_frames == 5:
                self.n_air()
            if self.timer_attack_frames == 6:
                self.n_air()
            if self.timer_attack_frames == 7:
                self.n_air()
            if self.timer_attack_frames == 8:
                self.n_air()
            if self.timer_attack_frames == 9:
                self.n_air()
            if self.timer_attack_frames == 10:
                self.n_air()
            if self.timer_attack_frames == 11:
                self.n_air()
            if self.timer_attack_frames == 12:
                self.n_air()
            if self.timer_attack_frames == 13:
                self.n_air()
            if self.timer_attack_frames == 14:
                self.n_air()
            if self.timer_attack_frames > 14:
                self.game.attack_n_air = False
                self.game.n_air = False
                self.timer_attack_frames = 0

        if self.game.attack_d_air:
            self.timer_attack_frames += 1
            if self.timer_attack_frames == 2:
                self.d_air()
            if self.timer_attack_frames == 3:
                self.d_air()
            if self.timer_attack_frames == 4:
                self.d_air()
            if self.timer_attack_frames == 5:
                self.d_air()
            if self.timer_attack_frames == 6:
                self.d_air()
            if self.timer_attack_frames == 7:
                self.d_air()
            if self.timer_attack_frames == 8:
                self.d_air()
            if self.timer_attack_frames == 9:
                self.d_air()
            if self.timer_attack_frames == 10:
                self.d_air()
            if self.timer_attack_frames == 11:
                self.d_air()
            if self.timer_attack_frames == 12:
                self.d_air()
            if self.timer_attack_frames == 13:
                self.d_air()
            if self.timer_attack_frames == 14:
                self.d_air()
            if self.timer_attack_frames > 14:
                self.game.attack_d_air = False
                self.game.d_air = False
                self.timer_attack_frames = 0

        # this is so that the player cannot move out of the set direction they are going,
        # if they are going to move in a set direction
        if isGrounded:
            # s_light_right
            if keys[pg.K_d] and keys[pg.K_b]:
                if self.timer < 0:
                    self.timer = 4
                if self.timer > 0:
                    self.move_control = True
                    self.player_movement_x = 9
                    self.player_movement_y = 0

            # s_light_left
            if keys[pg.K_a] and keys[pg.K_b]:
                if self.timer < 0:
                    self.timer = 4
                if self.timer > 0:
                    self.move_control = True
                    self.player_movement_x = -9
                    self.player_movement_y = 0

            # n_light_right
            if self.current_pos > 0:
                if not keys[pg.K_a] and not keys[pg.K_d] and not keys[pg.K_s]:
                    if keys[pg.K_b]:
                        if self.timer < 0:
                            self.timer = 10
                        if self.timer > 0:
                            self.move_control = True
                            self.player_movement_x = 0.0001
                            self.player_movement_y = 0.0001

            # n_light_left
            if self.current_pos < 0:
                if not keys[pg.K_a] and not keys[pg.K_d] and not keys[pg.K_s]:
                    if keys[pg.K_b]:
                        if self.timer < 0:
                            self.timer = 10
                        if self.timer > 0:
                            self.move_control = True
                            self.player_movement_x = -0.0001
                            self.player_movement_y = -0.0001

            # d_light_right
            if self.current_pos > 0:
                if keys[pg.K_s]:
                    if not keys[pg.K_a] and not keys[pg.K_d]:
                        if keys[pg.K_b]:
                            if self.timer < 0:
                                self.timer = 10
                            if self.timer > 0:
                                self.move_control = True
                                self.player_movement_x = 0.0001
                                self.player_movement_y = 0.0001

        # d_light_left
            if self.current_pos < 0:
                if keys[pg.K_s]:
                    if not keys[pg.K_a] and not keys[pg.K_d]:
                        if keys[pg.K_b]:
                            if self.timer < 0:
                                self.timer = 10
                            if self.timer > 0:
                                self.move_control = True
                                self.player_movement_x = -0.0001
                                self.player_movement_y = -0.0001

        # s_sig_right
            if self.current_pos > 0:
                if keys[pg.K_d] and keys[pg.K_n]:
                    if self.timer < 0:
                        self.timer = 3
                    if self.timer > 0:
                        self.move_control = True
                        self.player_movement_x = 0.0001
                        self.player_movement_y = 0.0001

        # s_sig_left
            if self.current_pos < 0:
                if keys[pg.K_a] and keys[pg.K_n]:
                    if self.timer < 0:
                        self.timer = 3
                    if self.timer > 0:
                        self.move_control = True
                        self.player_movement_x = -0.0001
                        self.player_movement_y = -0.0001

        # d_sig_right
            if self.current_pos > 0:
                if keys[pg.K_s] and keys[pg.K_n]:
                    if not keys[pg.K_a] and not keys[pg.K_d]:
                        if self.timer < 0:
                            self.timer = 3
                        if self.timer > 0:
                            self.move_control = True
                            self.player_movement_x = 0.0001
                            self.player_movement_y = 0.0001

        # d_sig_left
            if self.current_pos < 0:
                if keys[pg.K_s] and keys[pg.K_n]:
                    if not keys[pg.K_a] and not keys[pg.K_d]:
                        if self.timer < 0:
                            self.timer = 3
                        if self.timer > 0:
                            self.move_control = True
                            self.player_movement_x = -0.0001
                            self.player_movement_y = -0.0001

        if not isGrounded:
            # s_air_right
            if keys[pg.K_d] and keys[pg.K_b]:
                if self.timer < 0:
                    self.timer = 3
                if self.timer > 0:
                    self.vel.x += PLAYER_ACC

        # s_air_left
            if keys[pg.K_a] and keys[pg.K_b]:
                if self.timer < 0:
                    self.timer = 3
                if self.timer > 0:
                    self.vel.x -= PLAYER_ACC

        if self.move_control:
            self.vel.x = self.player_movement_x
            self.vel.y = self.player_movement_y

        if not self.move_control:
            self.vel.x = self.vel.x
            self.vel.y = self.vel.y

        # if player falls farther than the bottom, player goes back to the middle of the screen
        if self.pos.y > HEIGHT + HEIGHT * 3/4:
            self.pos.x = WIDTH / 2 - 15
            self.pos.y = HEIGHT / 2

        # if player y velocity is greater than what is wanted, the player speed is capped
        if not keys[pg.K_s]:
            if self.vel.y >= 10:
                self.vel.y = 10
        if keys[pg.K_s]:
            if self.vel.y >= PLAYER_JUMP:
                self.vel.y = PLAYER_JUMP

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos


class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, x_speed, y_speed, x_size, y_size, time):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((x_size, y_size))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = x_speed
        self.speedy = y_speed
        self.dt = 0.2
        self.timer = time

    def update(self):
        self.timer -= self.dt
        if self.timer < 0:
            self.kill()
        self.rect.x += self.speedx
        self.rect.y += self.speedy


class SoftPlatform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

