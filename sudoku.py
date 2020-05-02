marco = [


    [7,0,0,4,0,0,1,0,0],
    [6,0,0,0,7,0,0,0,9],
    [0,0,0,6,0,0,0,0,8],
    [0,0,7,0,0,0,2,6,0],
    [0,0,1,0,0,0,0,0,0],
    [0,0,4,0,6,0,0,0,5],
    [0,7,0,0,0,0,0,1,2],
    [1,2,0,0,0,0,4,0,0],
    [0,4,9,0,0,0,0,0,7]


]

def solucion(ma):

    encontrar = encontrar_vacios(ma)
    if not encontrar:
        return True
    else:
        row, col = encontrar

    for i in range(1,10):
        if valid(ma,i, (row, col)):
            ma[row][col] = i

            if solucion(ma):
                return True
            ma[row][col] = 0

    return False



def valid(ma, num, pos):

    #chequear la fila
    for i in range (len(ma[0])):
        if ma[pos[0]][i] == num and pos[1] != i:
            return False

    #chequear columna

    for i in range(len(ma)):
        if ma[i][pos[1]] == num and pos [0] != i:
            return False

    #chequear la caja

    caja_x = pos[1] // 3
    caja_y = pos[0] // 3

    for i in range(caja_y * 3,caja_y*3 +3):
        for j in range(caja_x * 3 , caja_x*3 + 3):
            if ma [i][j] == num and (i,j) != pos:
                return False
    return True


def imprimir_marco(ma):

    for i in range(len(ma)):

        if i % 3 == 0 and i != 0:

            print("- - - - - - - - - - - - -")

        for j in range(len(ma[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(ma[i][j])
            else:
                print(str(ma[i][j]) + " ", end= "")


def encontrar_vacios(ma):
    for i in range(len(ma)):
        for j in range(len(ma[0])):
            if ma[i][j] == 0:
                return (i, j)  #row, col
    return None

imprimir_marco(marco)
solucion(marco)
print("_________________________________________")
imprimir_marco(marco)