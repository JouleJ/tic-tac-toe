import grid
import minmax

def computer_step(g):
    n = g.n
    for i in range(n):
        for j in range(n):
            if g.get(i, j) == grid.CELL_EMPTY:
                g.set(i, j, grid.CELL_COMPUTER)
                result = minmax.player_wins(g)
                if not result:
                    return
                g.set(i, j, grid.CELL_EMPTY)
    for i in range(n):
        for j in range(n):
            if g.get(i, j) == grid.CELL_EMPTY:
                g.set(i, j, grid.CELL_COMPUTER)
                return

def player_step(g):
    print(g.draw())
    while True:
        i, j = list(map(int, input("Enter row and column: ").split(' ')))
        i, j = i - 1, j - 1
        if g.valid_coords(i, j) and g.get(i, j) == grid.CELL_EMPTY:
            g.set(i, j, grid.CELL_PLAYER)
            break # Внезапное прерывание, можно заменить работу цикла через флаг
        else:
            print('Invalid coordinates!')

def main():
    n = int(input("Enter grid size: ")) # naming, mb grid_size
    g = grid.Grid(n) # naming, mb grid_obj
    empty_cells = n * n
    # Внезапные прерывания - плохой тон, так как ломается идея чтения кода сверху вниз без остановок
    # Лучше использовать флаг, например isGameWork = True и вместо return делать isGameWork = False
    while True:
        computer_step(g)
        if g.who_won() == grid.COMPUTER_WON:
            print('Computer won!')
            return # внезапное прерывание
        empty_cells -= 1 # дублирование кода
        if empty_cells == 0:
            print('Neither won!')
            return # внезапное прерывание
        player_step(g)
        if g.who_won() == grid.PLAYER_WON:
            print('Player won!')
            return # внезапное прерывание
        empty_cells -= 1 # дублирование кода, работает только благодаря внезапному прерыванию,
        # если сразу избегать конструкции return в середине функции, то это тоже выпиливается
        if empty_cells == 0:
            print('Neither won!')
            return # внезапное прерывание

if __name__ == '__main__':
    main()
