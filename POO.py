class lamparas:
    estado = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self,palanca):
        self.palanca = palanca
    
    def apagado (self):
        self.palanca = True
        self.interructor()

    def prendido(self):
        self.palanca = False
        self.interructor()

    def interructor(self):
        if self.palanca:
            print(self.estado[0])
        else:
            print(self.estado[1])
    

def main():
    a = lamparas(palanca = False)
    b = lamparas(palanca=True)
    while True:
        tx = input("\n\nMenu \n\n 1 para prender \n\n 0 para apagar \n\n x para terminar \n\n >>> ")
        if tx == "0":
            a.interructor()
        elif tx == "1":
            b.interructor()
        else:
            break        
if __name__ =="__main__":
    main()    
