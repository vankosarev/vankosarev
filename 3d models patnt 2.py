import turtle
import array

cordinata3D = [[0,0,0],[1,0,0],[0,1,0],[0,0,1],[1,1,0],[0,1,1],[1,0,1],[1,1,1]]

cordinata2d = []

#angleX

#def opredelenie_proekt():
    
    



def get_cord():
    a = 0
    x = 0
    y = 0
    for i in cordinata3D:
        if cordinata3D[a][0] == 1:
            y = y - 25
            x = x - 43.30
            
        else:
            pass
    
        if cordinata3D[a][1] == 1:
            y = y + 50
            
        else:
            pass
 
        if cordinata3D[a][2] == 1:
            y = y - 25
            x = x + 43.30
            
        else:
            pass
        
        cordinata2d.append([x,y])
        
        a = a + 1
        x = 0
        y = 0
    print(cordinata2d)

def draw():
    get_cord()
    a = 1
    b = 0
    while b < 8:
        while a < 8:           
            if cordinata2d[a][0] - cordinata2d[b][0] == cordinata2d[1][0] and cordinata2d[a][1] - cordinata2d[b][1] == cordinata2d[1][1]:
                turtle.up()
                turtle.setpos(cordinata2d[b][0],cordinata2d[b][1])
                turtle.down()
                turtle.setpos(cordinata2d[a][0],cordinata2d[a][1])
                turtle.up()
                turtle.setpos(0,0)
            else:
                pass
                
            
                
            if cordinata2d[a][0] - cordinata2d[b][0] == cordinata2d[2][0] and cordinata2d[a][1] - cordinata2d[b][1] == cordinata2d[2][1]:
                turtle.up()
                turtle.setpos(cordinata2d[b][0],cordinata2d[b][1])
                turtle.down()
                turtle.setpos(cordinata2d[a][0],cordinata2d[a][1])
                turtle.up()
                turtle.setpos(0,0)
            else:
                pass   
            
            if cordinata2d[a][0] - cordinata2d[b][0] == cordinata2d[3][0] and cordinata2d[a][1] - cordinata2d[b][1] == cordinata2d[3][1]:                
                turtle.up()
                turtle.setpos(cordinata2d[b][0],cordinata2d[b][1])
                turtle.down()
                turtle.setpos(cordinata2d[a][0],cordinata2d[a][1])
                turtle.up()
                turtle.setpos(0,0)
                
            else:
                pass
            
            
            
                
            a = a + 1
        b = b + 1
        a = a - 7
        
        

        

        
        

draw()
