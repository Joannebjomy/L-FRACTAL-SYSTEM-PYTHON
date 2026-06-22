# The L-System Fractal Architect

By Joanne B. Jomy

## INTRODUCTION

My app turns a string to a fractal sounds fancy doesn't it? Don't let that scare you away it converts a string along with axioms, rules ,angle and iterations which is given by the user and turns it into a beautiful pattern .

## My journey

I started out armed with only the basics of python which I learnt in my class 12 unaware of the tkinter or turtle horror. The biggest nightmare of them all was figuring out what a root or label or canvases were, why I had to use rawturtle instead of turtle so many questions with only little answers. Even despite all these setbacks I was able to push through by learning it step by step instead of jumping straight into making an app, I started with learning how to make a window pop up then after that I had to learn on how to make small other input boxes inside the same window with a canvas on the left for the magic of the patterns to bloom and on the left the boxes which are the soul for everything.

## Features of my app

Lets now move on from those boring and miserable backstory and talk about what my app can actually do.

**Colour Gradient:**

This app doesn't just make patterns using just black but provides multiple options to the user to choose from

*Principle:*

It follows the RGB rule and additive colour mixing, let me explain it with an example, if I want to make an ombre effect from red to blue it starts from (255,0,0) and gradually becomes (0,0,255).

The rainbow colour gradient follows a sine wave to make those rainbow colours.

**Speed optimization**

Time is money and nobody likes waiting and endlessly watching the turtle slowly crawl across the screen. So in order to not test your patience the app instantly draws the pattern by turning off the screen tracker while drawing and only updating the canvas once everything is done.

**Branching using \[,]**

This feature allows the user to make more intricate patterns.

*Principle:*

Instead of drawing a pattern which can be drawn only continuously this allows the users to widen their patterns the turtle saves its position when it encounters \[ and goes back to its position when it reads ] allowing the user to make tree like patterns

## How it actually works (the logic)

**Expansion:**

You give it an axiom (starting string) and rules like `F:F+F--F+F`. The app rewrites the string over and over for however many iterations you ask for — every matching character gets replaced at the same time (that's the "parallel" part of L-systems).

**Drawing:**

Once the final string is ready, the turtle reads through it character by character:

* `F` → move forward (and pick up the next gradient color)
* `+` → turn right by your chosen angle
* `-` → turn left by your chosen angle
* `\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\[` → save current position + direction
* `]` → jump back to the last saved position + direction

## How to run it

You just need Python 3 — `tkinter` and `turtle` already come built in, no installs needed.

Then in the dashboard:

1. Type your Axiom (try `F`)
2. Type your Rules like `F:F+F--F+F`
3. Set your Angle and Iterations
4. Pick a Color Gradient
5. Hit Generate

Here are a few for you to get started:

|Fractal|Axiom|Rules|Angle|Iterations|
|-|-|-|-|-|
|Koch Snowflake|F|F:F+F--F+F|60|4|
|Sierpinski-ish|F|F:F+F-F-F+F|90|4|
|Branching Tree|F|F:FF-\[-F+F+F]+\[+F-F-F]|22|4|

## What I would have improved if I had more time

* I would have made the window look more appealing as first impressions are the best impressions it would make the user come back and use it to make more patterns
* The app right now can only be used by those who have atleast a basic idea about how the app works so I would try adding another drop down list where amateur users can easily draw a pattern with just a click making it beginner friendly.

## Output

This is a simple Koch curve

!\[Simple Koch Curve](screenshots/koch\_curve.png)

A KOCH SNOWFLAKE:

(I have changed the step from 15 to 5 for this so that the pattern will be completely visible)

!\[Koch Snowflake](screenshots/koch\_snowflake.png)

Minkowski Sausage / Quadratic Koch Island:

!\[Minkowski Sausage](screenshots/minkowski\_sausage.png)

Tree:

!\[Branching Tree](screenshots/branching\_tree.png)

