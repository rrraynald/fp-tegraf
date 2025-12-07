import matplotlib.pyplot as plt


dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def isSafe(x, y, n, board):
    return x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1

def knightTourUtil(x, y, step, n, board):
    if step == n * n:
        return True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if isSafe(nx, ny, n, board):
            board[nx][ny] = step

            if knightTourUtil(nx, ny, step + 1, n, board):
                return True

            board[nx][ny] = -1

    return False

def knightTour(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]

    board[0][0] = 0

    if knightTourUtil(0, 0, 1, n, board):
        return board

    return None

def visualize_tour(n, board):
    if board is None:
        print("Solusi tidak ditemukan!")
        return

    path = [None] * (n * n)
    for r in range(n):
        for c in range(n):
            step_num = board[r][c]
            path[step_num] = (r, c)

    plt.figure(figsize=(8, 8))
    
    plt.gca().invert_yaxis() 
    plt.tick_params(axis='both', which='both', bottom=False, top=True, labelbottom=False, labeltop=True)

    plt.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
    plt.xticks(range(n))
    plt.yticks(range(n))

    y_coords = [p[0] for p in path]
    x_coords = [p[1] for p in path]

    plt.plot(x_coords, y_coords, marker='o', color='black', linewidth=1.5, markersize=8)

    plt.plot(x_coords[0], y_coords[0], 'go', markersize=15, label='Start (0)')
    plt.plot(x_coords[-1], y_coords[-1], 'ro', markersize=15, label=f'End ({n*n-1})')

    for i, (r, c) in enumerate(path):
        plt.text(c, r, str(i), color='white', ha='center', va='center', fontsize=9, fontweight='bold')

    plt.title(f"Knight's Tour (N={n})")
    plt.legend()
    plt.show()

if __name__=="__main__":
    n = 8
    print(f"Menghitung solusi untuk N={n}...")
    
    res = knightTour(n)

    if res:
        print("\nMatriks Langkah:")
        for row in res:
            for val in row:
                print(f"{val:2}", end=" ")
            print()
        
        print("\nMenampilkan visualisasi...")
        visualize_tour(n, res)
    else:
        print("Solusi tidak ditemukan.")