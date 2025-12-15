def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    # 上下左右の移動量
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                black_neighbors = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < H and 0 <= nj < W:
                        if S[ni][nj] == '#':
                            black_neighbors += 1

                if black_neighbors != 2 and black_neighbors != 4:
                    print("No")
                    return

    print("Yes")


if __name__ == "__main__":
    main()
