def print_grid_line(grid_size):
    """打印一行田字格的线条，grid_size是网格的总大小（例如4表示4x4网格）"""
    print("*" * grid_size)


def print_grid_row(grid_size):
    """打印田字格的一行（除了顶部和底部），grid_size是网格的总大小"""
    row = ""
    for j in range(grid_size):
        if j % 2 == 0:  # 如果是列的开始或中间（即需要打印线条的位置）
            row += "*"
            # 在线条之间添加适当数量的空格
        row += " " * (grid_size // 2 - (j % 2))
    print(row)


def print_tianzige(grid_size):
    """打印一个grid_size x grid_size的田字格，这里grid_size应该是偶数，以便每个大格为正方形"""
    if grid_size % 2 != 0:
        print("grid_size应该是偶数")
        return

        # 打印顶部线条
    print_grid_line(grid_size)

    # 打印中间部分（除了顶部和底部线条）
    for _ in range(grid_size // 2 - 1):  # 因为顶部和底部已经打印，所以这里减1
        print_grid_row(grid_size)

        # 打印底部线条
    print_grid_line(grid_size)


# 使用函数打印4x4的田字格
print_tianzige(4)