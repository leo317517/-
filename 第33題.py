while True:
    try:
        nums = list(map(int, input().split()))
        if not nums:
            continue
        size = len(nums)
        total_sum = sum(nums)
        avg = total_sum / size
        print(f"Size: {size}")
        print(f"Average: {avg:.3f}")


    except EOFError:
        break