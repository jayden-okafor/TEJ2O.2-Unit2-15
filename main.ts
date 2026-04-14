/* Copyright (c) 2026 MTHS All rights reserved
 *
 * Created by: Jayden Okafor
 * Created on: Apr 2026
 * This program creates a circle loop using the sprite engine
*/

// variables
let sprite: game.LedSprite = null
let sides: number = 0
let steps: number = 0

// show happy face
basic.clearScreen()
basic.showIcon(IconNames.Happy)

// when button "A" is pressed
input.onButtonPressed(Button.A, function () {
    // create the sprite at the beginning and wait for 0.1 seconds
    basic.clearScreen()
    sprite = game.createSprite(0, 0)
    sides = 0
    basic.pause(100)

    // if its not back to the position it started then continue code
    while (sides < 4) {
        // reset the steps to 0 so the sprite can move to the 4th coordinate before stopping
        steps = 0
        // if its not in the last pixel then move 1 step forward and wait for 0.1 seconds
        while (steps < 4) {
            sprite.move(1)
            basic.pause(100)
            steps++
        }
        // turn right when it reaches the end
        sprite.turn(Direction.Right, 90)
        sides++
    }

    // delete sprite and show happy face
    sprite.delete()
    basic.clearScreen()
    basic.showIcon(IconNames.Happy)
})

// when button "B" is pressed
input.onButtonPressed(Button.B, function () {
    // create the sprite at the beginning and wait for 0.1 seconds
    basic.clearScreen()
    sprite = game.createSprite(0, 0)
    basic.pause(100)
    sides = 0

    // make the sprite face down before starting
    sprite.turn(Direction.Right, 90)

    // if its not back to the position it started then continue code
    while (sides < 4) {
        // reset the steps to 0 so the sprite can move to the 4th coordinate before stopping
        steps = 0
        // if its not in the last pixel then move 1 step forward and wait for 0.1 seconds
        while (steps < 4) {
            sprite.move(1)
            basic.pause(100)
            steps++
        }
        // turn left when it reaches the end
        sprite.turn(Direction.Left, 90)
        sides++
    }

    // delete sprite and show happy face
    sprite.delete()
    basic.clearScreen()
    basic.showIcon(IconNames.Happy)
})
