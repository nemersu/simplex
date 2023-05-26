class simplex:
  
    def __init__(self):
    self. table = []
    
    def  set_objective_function(self, fo: list):
    self.table.append(fo)
    
    def add_restrictions(self, sa: list):
      self.table.append(sa)
      
    def get_entry_column(self) → int:
        column_pivot = min(self.table[0])
        index = self.table[0].index(column_pivot)
        
        return index
      
     def get_exit_line(self, entry_comum: int) → int:
        results = {}
        for line in range(len(self.table)):
            if line > 0:
               if self.table[line][entry_column] > 0:
                   division = self.table[line][-1] / self.table[line][entry_column]
                   results[line] = division
        index = min(results, key=results.get)
        
        return index
