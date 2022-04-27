def make_bricks(small, big, goal):
    the_goal = goal
    the_goal -= 5 * min(big, goal / 5)
    return the_goal - small <= 0

print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))