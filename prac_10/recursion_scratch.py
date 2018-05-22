def pyramid_block_counter(rows):
    if rows <= 0:
        return 0
    return rows + pyramid_block_counter(rows - 1)


print(pyramid_block_counter(6))
