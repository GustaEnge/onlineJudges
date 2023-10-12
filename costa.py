import random
def readMapa(m,n,mat):
    ground = 0
    total_ground = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j]== "#":
                total_ground += 1
                if not ((i == 0 and 0 <= j < n) or (0 <= i < m and j == n-1)or (i == m-1 and 0 <= j < n) or (0 <= i < m and j == 0)):
                    if all(map(lambda x:x == "#",[mat[i][j-1],mat[i][j+1],mat[i-1][j],mat[i+1][j]])):
                        ground += 1
    return total_ground - ground

def main():
    m,n = [int(i) for i in input().split()]
    matriz = []
    for i in range(m):
        a = input()
        matriz.append(list(a))
    
    print(readMapa(m,n,matriz))
if __name__ == "__main__":
    main()


    
