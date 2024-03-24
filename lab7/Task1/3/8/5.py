def sum67(nums):
    total = 0
    skip_section = False

    for num in nums:
        if num == 6:
            skip_section = True
        elif not skip_section:
            total += num
        elif num == 7:
            skip_section = False

    return total