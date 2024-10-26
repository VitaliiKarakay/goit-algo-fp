import turtle


def draw_branch(t, branch_length, level):
    if level == 0:
        return
    t.forward(branch_length)
    t.left(45)
    draw_branch(t, branch_length * 0.6, level - 1)
    t.right(90)
    draw_branch(t, branch_length * 0.6, level - 1)
    t.left(45)
    t.backward(branch_length)


def draw_pythagoras_tree(level):
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    draw_branch(t, 200, level)
    window.mainloop()


if __name__ == "__main__":
    level = int(input("Enter the recursion level: "))
    draw_pythagoras_tree(level)
