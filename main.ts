namespace SpriteKind {
    export const PowerUP = SpriteKind.create()
    export const ProjectileB = SpriteKind.create()
    export const sheild = SpriteKind.create()
    export const Boss = SpriteKind.create()
    export const Fenemy = SpriteKind.create()
    export const Benemy = SpriteKind.create()
    export const plus1 = SpriteKind.create()
}
namespace StatusBarKind {
    export const bosshealth = StatusBarKind.create()
    export const BigEnemyHealth = StatusBarKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Fenemy, function (sprite3, otherSprite3) {
    music.bigCrash.play()
    info.changeLifeBy(-1)
    enemydeath(otherSprite3)
    scene.cameraShake(4, 500)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Benemy, function (sprite22, otherSprite22) {
    sprite22.destroy()
    statusbars.getStatusBarAttachedTo(StatusBarKind.BigEnemyHealth, otherSprite22).value += -5
})
sprites.onOverlap(SpriteKind.sheild, SpriteKind.Enemy, function (sprite, otherSprite) {
    enemydeath(otherSprite)
    info.changeScoreBy(1)
    myShield.destroy()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.PowerUP, function (sprite42, otherSprite42) {
    music.beamUp.play()
    doubleshoot = sprites.create(img`
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
        `, SpriteKind.Player)
    doubleshoot.setPosition(39, 7)
    doubleshoot.lifespan = 5000
    otherSprite42.destroy()
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite7, otherSprite7) {
    sprite7.destroy()
    statusbars.getStatusBarAttachedTo(StatusBarKind.EnemyHealth, otherSprite7).value += -20
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.plus1, function (sprite4, otherSprite4) {
    music.magicWand.play()
    info.changeLifeBy(1)
    otherSprite4.destroy()
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Fenemy, function (sprite2, otherSprite2) {
    sprite2.destroy()
    statusbars.getStatusBarAttachedTo(StatusBarKind.EnemyHealth, otherSprite2).value += -20
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, Ship, 200, 0)
    music.zapped.play()
    if (doubleshoot && doubleshoot.lifespan > 0) {
        projectile = sprites.createProjectileFromSprite(img`
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
            `, Ship, 200, 0)
        projectile.y += 5
        music.zapped.stop()
        music.sonar.play()
    }
})
statusbars.onZero(StatusBarKind.EnemyHealth, function (status) {
    info.changeScoreBy(1)
    enemydeath(status.spriteAttachedTo())
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite8, otherSprite8) {
    music.bigCrash.play()
    info.changeLifeBy(-1)
    enemydeath(otherSprite8)
    scene.cameraShake(4, 500)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Benemy, function (sprite32, otherSprite32) {
    music.bigCrash.play()
    info.changeLifeBy(-2)
    enemydeath(otherSprite32)
    scene.cameraShake(4, 500)
})
function spawnFEnemy () {
    fastenemy = sprites.create(img`
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
        `, SpriteKind.Fenemy)
    fastenemy.x = scene.screenWidth()
    fastenemy.vx = 0 - fastenemyspeed
    fastenemy.y = randint(20, scene.screenHeight() - 40)
    statusbar = statusbars.create(25, 3, StatusBarKind.EnemyHealth)
    statusbar.attachToSprite(fastenemy)
    pause(FenemySpawn)
    fastenemy.setFlag(SpriteFlag.DestroyOnWall, true)
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    timer.throttle("action", 4000, function () {
        music.pewPew.play()
        myShield = sprites.create(img`
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
            `, SpriteKind.sheild)
        myShield.setPosition(Ship.x, Ship.y)
        myShield.follow(Ship)
        timer.after(2000, function () {
            myShield.destroy()
        })
    })
})
function spawnBenemy () {
    BEnemy = sprites.create(img`
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
        `, SpriteKind.Benemy)
    BEnemy.x = scene.screenWidth()
    BEnemy.vx = 0 - Benemyspeed
    BEnemy.y = randint(20, scene.screenHeight() - 40)
    statusBig = statusbars.create(40, 3, StatusBarKind.BigEnemyHealth)
    statusBig.attachToSprite(BEnemy)
    pause(BEnemySpawn)
    BEnemy.setFlag(SpriteFlag.DestroyOnWall, true)
}
statusbars.onZero(StatusBarKind.BigEnemyHealth, function (status2) {
    info.changeScoreBy(2)
    enemydeath(status2.spriteAttachedTo())
})
sprites.onOverlap(SpriteKind.sheild, SpriteKind.Benemy, function (sprite6, otherSprite6) {
    enemydeath(otherSprite6)
    info.changeScoreBy(2)
    myShield.destroy()
})
function spawnEnemy () {
    enemyalien = sprites.create(img`
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
        `, SpriteKind.Enemy)
    enemyalien.x = scene.screenWidth()
    enemyalien.vx = 0 - enemyspeed
    enemyalien.y = randint(20, scene.screenHeight() - 40)
    statusbar = statusbars.create(25, 3, StatusBarKind.EnemyHealth)
    statusbar.attachToSprite(enemyalien)
    pause(enemySpawn)
    enemyalien.setFlag(SpriteFlag.DestroyOnWall, true)
}
function enemydeath (enemy: Sprite) {
    enemy.destroy(effects.spray, 500)
    if (Math.percentChance(20)) {
        powerup = sprites.create(img`
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
            `, SpriteKind.PowerUP)
        powerup.x = enemy.x
        powerup.y = enemy.y
        powerup.lifespan = 4000
    }
    if (Math.percentChance(5)) {
        plus12 = sprites.create(img`
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
            `, SpriteKind.plus1)
        plus12.x = enemy.x
        plus12.y = enemy.y
        plus12.lifespan = 4000
    }
}
sprites.onOverlap(SpriteKind.sheild, SpriteKind.Fenemy, function (sprite5, otherSprite5) {
    enemydeath(otherSprite5)
    info.changeScoreBy(1)
    myShield.destroy()
})
let plus12: Sprite = null
let powerup: Sprite = null
let enemyalien: Sprite = null
let statusBig: StatusBarSprite = null
let BEnemy: Sprite = null
let statusbar: StatusBarSprite = null
let fastenemy: Sprite = null
let projectile: Sprite = null
let doubleshoot: Sprite = null
let myShield: Sprite = null
let Benemyspeed = 0
let BEnemySpawn = 0
let FenemySpawn = 0
let fastenemyspeed = 0
let enemySpawn = 0
let enemyspeed = 0
let Ship: Sprite = null
effects.starField.startScreenEffect()
Ship = sprites.create(img`
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
    `, SpriteKind.Player)
Ship.setPosition(8, 55)
controller.moveSprite(Ship)
Ship.setStayInScreen(true)
info.setLife(5)
enemyspeed = 20
enemySpawn = 2000
fastenemyspeed = 60
FenemySpawn = 2000
BEnemySpawn = 2000
Benemyspeed = 5
game.onUpdateInterval(5000, function () {
    enemyspeed += 5
    enemyspeed = Math.min(enemyspeed, 50)
    enemySpawn += -100
    enemySpawn = Math.max(enemyspeed, 500)
})
forever(function () {
    spawnEnemy()
    if (Math.percentChance(40)) {
        spawnFEnemy()
    }
    if (Math.percentChance(30)) {
        spawnBenemy()
    }
})
