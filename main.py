@namespace
class SpriteKind:
    PowerUP = SpriteKind.create()
    ProjectileB = SpriteKind.create()
    sheild = SpriteKind.create()
    Boss = SpriteKind.create()
    Fenemy = SpriteKind.create()
    Benemy = SpriteKind.create()
    plus1 = SpriteKind.create()
@namespace
class StatusBarKind:
    bosshealth = StatusBarKind.create()
    BigEnemyHealth = StatusBarKind.create()

def on_on_overlap(sprite3, otherSprite3):
    music.big_crash.play()
    info.change_life_by(-1)
    enemydeath(otherSprite3)
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.Fenemy, on_on_overlap)

def on_on_overlap2(sprite22, otherSprite22):
    sprite22.destroy()
    statusbars.get_status_bar_attached_to(StatusBarKind.BigEnemyHealth, otherSprite22).value += -5
sprites.on_overlap(SpriteKind.projectile, SpriteKind.Benemy, on_on_overlap2)

def on_on_overlap3(sprite, otherSprite):
    enemydeath(otherSprite)
    info.change_score_by(1)
    myShield.destroy()
sprites.on_overlap(SpriteKind.sheild, SpriteKind.enemy, on_on_overlap3)

def on_on_overlap4(sprite4, otherSprite4):
    music.magic_wand.play()
    info.change_life_by(1)
    otherSprite4.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.plus1, on_on_overlap4)

def on_on_overlap5(sprite2, otherSprite2):
    sprite2.destroy()
    statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite2).value += -20
sprites.on_overlap(SpriteKind.projectile, SpriteKind.Fenemy, on_on_overlap5)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . 8 . . . . . . . . . . 
                    . . . . . 8 8 . 8 4 . . . . . . 
                    . . . . . 4 8 8 a a 2 . . . . . 
                    . . . . . 8 8 . 8 4 . . . . . . 
                    . . . . . 8 . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        Ship,
        200,
        0)
    music.zapped.play()
    if doubleshoot and doubleshoot.lifespan > 0:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 8 . . . . . . . . . . 
                            . . . . . 8 8 . 8 4 . . . . . . 
                            . . . . . 4 8 8 a a 2 . . . . . 
                            . . . . . 8 8 . 8 4 . . . . . . 
                            . . . . . 8 . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            Ship,
            200,
            0)
        projectile.y += 5
        music.zapped.stop()
        music.sonar.play()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_zero(status):
    info.change_score_by(1)
    enemydeath(status.sprite_attached_to())
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero)

def on_on_overlap6(sprite42, otherSprite42):
    global doubleshoot
    music.beam_up.play()
    doubleshoot = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 8 . . . . . . . . . . . 
                    . . . . 8 8 . 8 4 . . . . . . . 
                    . . . . 4 8 8 a a 2 . . . . . . 
                    . . . . 8 8 . 8 4 . . . . . . . 
                    . . . . 8 . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 8 . . . . . . . . . . . 
                    . . . . 8 8 . 8 4 . . . . . . . 
                    . . . . . 8 8 a a 2 . . . . . . 
                    . . . . 8 8 . 8 4 . . . . . . . 
                    . . . . 8 . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.player)
    doubleshoot.set_position(39, 7)
    doubleshoot.lifespan = 5000
    otherSprite42.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.PowerUP, on_on_overlap6)

def on_on_zero2(status2):
    info.change_score_by(2)
    enemydeath(status2.sprite_attached_to())
statusbars.on_zero(StatusBarKind.BigEnemyHealth, on_on_zero2)

def spawnFEnemy():
    global fastenemy, statusbar
    fastenemy = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . a . . . . . . . . 
                    . . . . . . a a a . . . . . . . 
                    . . . . a a a a a a a . . . . . 
                    . . . a a a a a a a a 4 4 . . . 
                    . . a f 9 9 9 a a a a a 4 4 4 . 
                    . a f f 9 a a a a a a a a a 4 4 
                    a a a a a a a a a a a a a a 5 2 
                    . a a a a a a a a a a a a a 5 2 
                    . a a 9 9 a a a a a a a a 4 4 4 
                    . . a a 9 9 9 a a a a 4 4 4 . . 
                    . . . . a a a a a a a 4 . . . . 
                    . . . . . a a a a a . . . . . . 
                    . . . . . . . a . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Fenemy)
    fastenemy.x = scene.screen_width()
    fastenemy.vx = 0 - fastenemyspeed
    fastenemy.y = randint(20, scene.screen_height() - 40)
    statusbar = statusbars.create(25, 3, StatusBarKind.enemy_health)
    statusbar.attach_to_sprite(fastenemy)
    pause(FenemySpawn)
    fastenemy.set_flag(SpriteFlag.DESTROY_ON_WALL, True)

def on_b_pressed():
    
    def on_throttle():
        global myShield
        music.pew_pew.play()
        myShield = sprites.create(img("""
                ............229.........
                            ............9229........
                            .............9229.......
                            ..............9229......
                            ...............9229.....
                            ................9229....
                            .................9229...
                            ..................9229..
                            ..................49229.
                            ..................449229
                            ..................444922
                            ..................225459
                            ..................225459
                            ..................444922
                            ..................449229
                            ..................49229.
                            ..................9229..
                            .................9229...
                            ................9229....
                            ...............9229.....
                            ..............9229......
                            .............9229.......
                            ............9229........
                            ............229.........
            """),
            SpriteKind.sheild)
        myShield.set_position(Ship.x, Ship.y)
        myShield.follow(Ship)
        
        def on_after():
            myShield.destroy()
        timer.after(2000, on_after)
        
    timer.throttle("action", 4000, on_throttle)
    
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def spawnBenemy():
    global BEnemy, statusBig
    BEnemy = sprites.create(img("""
            ................................
                    ................................
                    ................................
                    ..........22222222222222........
                    ..........22222222222222........
                    .........22f222222222f2222......
                    .........222f2222222f22222......
                    .......222222ff222ff2222222.....
                    ......222252222222225222222.....
                    ......222255222222255222222.....
                    .....22222555222225552222222....
                    .....222225552222255522222222...
                    ....222225ff5222225ff52222222...
                    ....222225ff5222225ff52222222...
                    .....222222222222222222222222...
                    .....22222222e22e222222222222...
                    .....22222222222222222222222....
                    .......2222222222222222222......
                    .......2222222222222222222......
                    .......222ee4eeeee44e22222......
                    .......2222eeeeeeeee232222......
                    .......22232222222222322222.....
                    .......22.32..2..2...32...2.....
                    .......52.32..2..2...32...2.....
                    .......52.32..2..2...32...25....
                    .......22.32..2..2...32...25....
                    .......2..32.22..22..32...22....
                    ......22..22.25..52....2...2....
                    .....22..22..25..552...22..2....
                    .....2..23...22...52...32..2....
                    .....2..23....2...22...32..2....
                    .....2..23....2...2....32..2....
        """),
        SpriteKind.Benemy)
    BEnemy.x = scene.screen_width()
    BEnemy.vx = 0 - Benemyspeed
    BEnemy.y = randint(20, scene.screen_height() - 40)
    statusBig = statusbars.create(40, 3, StatusBarKind.BigEnemyHealth)
    statusBig.attach_to_sprite(BEnemy)
    pause(BEnemySpawn)
    BEnemy.set_flag(SpriteFlag.DESTROY_ON_WALL, True)

def on_on_overlap7(sprite5, otherSprite5):
    enemydeath(otherSprite5)
    info.change_score_by(1)
    myShield.destroy()
sprites.on_overlap(SpriteKind.sheild, SpriteKind.Fenemy, on_on_overlap7)

def spawnEnemy():
    global enemyalien, statusbar
    enemyalien = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . 7 7 7 . . . . . . . 
                    . . . . . 7 7 7 7 7 . . . . . . 
                    . . . . 7 7 2 7 2 7 7 . . . . . 
                    . . . 7 7 7 7 7 7 7 7 7 . . . . 
                    . . . 7 7 7 f f f 7 7 7 . . . . 
                    . . . . . 7 . . . 7 . . . . . . 
                    . . . . 7 7 . . . 7 7 . . . . . 
                    . . . 7 7 . . . . . 7 7 . . . . 
                    . . . 7 . . . . . . . 7 . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    enemyalien.x = scene.screen_width()
    enemyalien.vx = 0 - enemyspeed
    enemyalien.y = randint(20, scene.screen_height() - 40)
    statusbar = statusbars.create(25, 3, StatusBarKind.enemy_health)
    statusbar.attach_to_sprite(enemyalien)
    pause(enemySpawn)
    enemyalien.set_flag(SpriteFlag.DESTROY_ON_WALL, True)

def on_on_overlap8(sprite32, otherSprite32):
    music.big_crash.play()
    info.change_life_by(-2)
    enemydeath(otherSprite32)
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.Benemy, on_on_overlap8)

def on_on_overlap9(sprite6, otherSprite6):
    enemydeath(otherSprite6)
    info.change_score_by(2)
    myShield.destroy()
sprites.on_overlap(SpriteKind.sheild, SpriteKind.Benemy, on_on_overlap9)

def on_on_overlap10(sprite7, otherSprite7):
    sprite7.destroy()
    statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite7).value += -20
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap10)

def enemydeath(enemy: Sprite):
    global powerup, plus12
    enemy.destroy(effects.spray, 500)
    if Math.percent_chance(20):
        powerup = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . 3 3 3 3 3 3 3 . . . . . 
                            . . . 3 3 3 3 3 3 3 3 3 . . . . 
                            . . 3 3 3 3 3 5 5 3 3 3 3 . . . 
                            . . 3 3 3 3 5 3 3 5 3 3 3 . . . 
                            . . 3 3 3 3 3 3 3 5 3 3 3 . . . 
                            . . 3 3 3 3 3 3 5 3 3 3 3 . . . 
                            . . 3 3 3 3 3 5 3 3 3 3 3 . . . 
                            . . 3 3 3 3 3 5 3 3 3 3 3 . . . 
                            . . 3 3 3 3 3 3 3 3 3 3 3 . . . 
                            . . . 3 3 3 3 5 3 3 3 3 . . . . 
                            . . . . 3 3 3 3 3 3 3 . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.PowerUP)
        powerup.x = enemy.x
        powerup.y = enemy.y
        powerup.lifespan = 4000
    if Math.percent_chance(5):
        plus12 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . 3 3 3 3 3 3 3 . . . . . 
                            . . . 3 3 3 3 3 3 3 3 3 . . . . 
                            . . 3 3 3 3 3 3 3 3 3 3 3 . . . 
                            . . 3 3 3 3 3 3 3 7 3 3 3 . . . 
                            . . 3 3 7 3 3 3 7 7 3 3 3 . . . 
                            . . 3 7 7 7 3 3 3 7 3 3 3 . . . 
                            . . 3 3 7 3 3 3 3 7 3 3 3 . . . 
                            . . 3 3 3 3 3 3 3 7 3 3 3 . . . 
                            . . 3 3 3 3 3 3 3 3 3 3 3 . . . 
                            . . . 3 3 3 3 3 3 3 3 3 . . . . 
                            . . . . 3 3 3 3 3 3 3 . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.plus1)
        plus12.x = enemy.x
        plus12.y = enemy.y
        plus12.lifespan = 4000

def on_on_overlap11(sprite8, otherSprite8):
    music.big_crash.play()
    info.change_life_by(-1)
    enemydeath(otherSprite8)
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap11)

plus12: Sprite = None
powerup: Sprite = None
enemyalien: Sprite = None
statusBig: StatusBarSprite = None
BEnemy: Sprite = None
statusbar: StatusBarSprite = None
fastenemy: Sprite = None
doubleshoot: Sprite = None
projectile: Sprite = None
myShield: Sprite = None
Benemyspeed = 0
BEnemySpawn = 0
FenemySpawn = 0
fastenemyspeed = 0
enemySpawn = 0
enemyspeed = 0
Ship: Sprite = None
effects.star_field.start_screen_effect()
Ship = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            9 9 . . . 9 9 9 . . . . . . . . 
            8 8 8 . . a a a 9 9 . . . . . . 
            2 2 8 9 9 6 6 6 5 5 9 . . . . . 
            5 4 2 8 8 6 8 8 5 5 2 9 . . . . 
            5 4 2 8 8 6 8 8 8 8 9 . . . . . 
            2 2 8 9 9 6 6 6 8 9 9 . . . . . 
            8 8 8 . . a a a 9 9 . . . . . . 
            9 9 . . . 9 9 9 . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
Ship.set_position(8, 55)
controller.move_sprite(Ship)
Ship.set_stay_in_screen(True)
info.set_life(5)
enemyspeed = 20
enemySpawn = 2000
fastenemyspeed = 60
FenemySpawn = 2000
BEnemySpawn = 2000
Benemyspeed = 5

def on_update_interval():
    global enemyspeed, enemySpawn
    enemyspeed += 5
    enemyspeed = min(enemyspeed, 50)
    enemySpawn += -100
    enemySpawn = max(enemyspeed, 500)
game.on_update_interval(5000, on_update_interval)

def on_forever():
    spawnEnemy()
    if Math.percent_chance(40):
        spawnFEnemy()
    if Math.percent_chance(30):
        spawnBenemy()
forever(on_forever)
