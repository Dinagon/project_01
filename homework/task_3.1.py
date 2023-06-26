import pprint

class Matrix:
    
    def __init__(self,columns,rows) -> None:
        self.matrix = [[None for j in range(columns)]for i in range(rows)]
        self.columns_num = columns
        self.rows_num = rows
        # self.columns_num = columns

    def set_value(self,column,row,value):
        self.matrix[column][row] = value

    def get_value(self,column,row):
        return self.matrix[column][row]
    
    def get_columns_num(self):
        return self.columns_num
    def get_rows_num(self):
        return self.rows_num
    
       
m = Matrix(columns=10, rows= 10)
for i in range(m.get_columns_num()):
    for j in range(m.get_rows_num()):
        m.set_value(i,j,1)


pprint.pprint(m.matrix)