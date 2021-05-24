# Author: Edina Do Nascimento Silva
import itertools

class Server:
  def __init__(self, val, row, column):
    self.row = row
    self.column = column
    self.top = None
    self.left = None
    self.right = None
    self.down = None
    self.value = val
    self.is_updated = True if val else False
    self.updated_moment = 0

  def __contains__(self, item):

    return item == self.value

  def __repr__(self):
    return f"<Value: {self.value} | Row: {self.row} | Column: {self.column}>"

  def update_server(self, counter):
      self.value = 1
      self.is_updated = True
      self.updated_moment = counter

  def update_near_servers(self,counter):

    #print(f"< Top: {self.top} | down: {self.down} | right: {self.right} | left: {self.left}>")

    if self.top and not self.top.is_updated:
        self.top.update_server(counter)
    if self.down and not self.down.is_updated:
        self.down.update_server(counter)
    if self.right and not self.right.is_updated:
        self.right.update_server(counter)
    if self.left and not self.left.is_updated:
        self.left.update_server(counter)



def updateServer(gridServer,counter):
    # atualizar o block se for cluster
    newgrid = []
    for server in gridServer:
        # print(f"****<Top: {server.top} | down: {server.down} | right: {server.right} | left: {server.left}>****")
        if server.is_updated:
            newgrid.append(server)

    for server in newgrid:
        server.update_near_servers(counter)

    #print(gridServer)
    for server in gridServer:
        if not server.is_updated:
            return updateServer(gridServer, counter + 1)

    return counter

    #como eu faço para mostrar o array completo aqui dentro
    #como eu faco para fazer o update do valor = 1 para essa celula e coluna que esta em uma classe
    #como eu faco para retornar os 4 vizinhos dessa celula e fazer o update?


def createServer(rows, columns, grid):
    #Como eu consigo declarar o grid em branco igual o gridServerToBeUpdate . Eu não consegui por isso precisei criar novamente dentro


    #1 LOOP TO CREATE THE LIST WITH THE CLASS SERVER
    for id_row, row in enumerate(grid):
        #print(f"<Index: {id_row}  | Row: {row}>")
        for id_col, col in enumerate(row):
            #Creating of List on each position one obj "Server" to use
            grid[id_row][id_col] = Server(col, id_row, id_col)
    # gridServerToBeUpdate = []



    #2 LOOP TO update the values inside the obj in the grid server with the neighbors's position and is_updated
    for id_row, row in enumerate(grid):
        for id_col, col in enumerate(row):
            server = grid[id_row][id_col]

            #Updating atributes in the class to exist the positions to top, down, left, right
            server.top = grid[id_row - 1][id_col] if id_row - 1 >= 0 else None
            server.down = grid[id_row + 1][id_col] if id_row + 1 < len(grid) else None
            server.right = grid[id_row][id_col + 1] if id_col + 1 < len(row) else None
            server.left = grid[id_row][id_col - 1] if id_col - 1 >= 0 else None

            # print(f"<V: {server.value} | R: {server.row} | C: {server.column} "
            #       f"| is_updated: {server.is_updated} | updated_moment: {server.updated_moment}"
            #       f"| Top: {server.top} | down: {server.down} | right: {server.right} | left: {server.left}>")
    print("*******itertools********")
    print(list(itertools.chain(*grid)))
    counter = updateServer(list(itertools.chain(*grid)), 1)


    return counter # Eu coloquei o contador aqui, poderem esta rertornando 13 que é a quantidade de linhas que tem o valor 0 para ser atualizado.



if __name__ == '__main__':
    rows = 4
    columns = 5
    # grid = (
    #     [0, 1, 1, 0, 1],
    #     [0, 1, 0, 1, 0],
    #     [0, 0, 0, 0, 0],
    #     [1, 0, 0, 0, 0],
    # )


    grid = (
        [0, 1, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0],
    )


    result = createServer(rows, columns, grid)
    print(f" *************************Valor do resultado: {result}")