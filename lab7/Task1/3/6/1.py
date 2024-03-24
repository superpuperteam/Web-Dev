def make_bricks(small, big, goal):
    max_big_bricks = goal // 5
    if max_big_bricks > big:
        max_big_bricks = big

    remaining_goal = goal - max_big_bricks * 5

    return small >= remaining_goal