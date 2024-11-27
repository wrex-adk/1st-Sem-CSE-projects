def create_word_search(grid, words):
    def search_word(word):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == word[0]:
                    if check_directions(word, i, j):
                        return True
        return False

    def check_directions(word, x, y):
        directions = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]
        for dx, dy in directions:
            if check_word(word, x, y, dx, dy):
                return True
        return False

    def check_word(word, x, y, dx, dy):
        for k in range(len(word)):
            nx, ny = x + k * dx, y + k * dy
            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != word[k]:
                return False
        return True

    found_words = []
    for word in words:
        if search_word(word):
            found_words.append(word)
    return found_words

grid = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P']
]

words = ['ABCD', 'FG', 'JKL', 'NOP', 'XYZ']
found_words = create_word_search(grid, words)
print(found_words)