import turtle
import array
turtle.speed(1)

cordinata3D = [[0,0,0],[1,0,0],[0,1,0],[0,0,1],[1,1,0],[0,1,1],[1,0,1],[1,1,1]]


cordinata2d = []

        



def get_cord():
    a = 0
    x = 0
    y = 0
    for i in cordinata3D:
        if cordinata3D[a][0] == 1:
            x = x + 50
            
        else:
            pass
    
        if cordinata3D[a][1] == 1:
            y = y + 50
            
        else:
            pass
 
        if cordinata3D[a][2] == 1:
            y = y + 25
            x = x + 43.30
            
        else:
            pass
        
        cordinata2d.append([x,y])
        print(cordinata2d)
        a = a + 1
        x = 0
        y = 0

def draw():
    get_cord()
    a = 1
    b = 0
    while b < 8:
        while a < 8:           
            if cordinata2d[a][0] - cordinata2d[b][0] == 0 and cordinata2d[a][1] - cordinata2d[b][1] == 50:
                turtle.up()
                turtle.setpos(cordinata2d[b][0],cordinata2d[b][1])
                turtle.down()
                turtle.setpos(cordinata2d[a][0],cordinata2d[a][1])
                turtle.up()
                turtle.setpos(0,0)
            else:
                pass
                
            
                
            if cordinata2d[a][0] - cordinata2d[b][0] == 50 and cordinata2d[a][1] - cordinata2d[b][1] == 0:
                turtle.up()
                turtle.setpos(cordinata2d[b][0],cordinata2d[b][1])
                turtle.down()
                turtle.setpos(cordinata2d[a][0],cordinata2d[a][1])
                turtle.up()
                turtle.setpos(0,0)
            else:
                pass   
            
            if cordinata2d[a][0] - cordinata2d[b][0] == 43.3 and cordinata2d[a][1] - cordinata2d[b][1] == 25:                
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
        
        

                




        

   
        

  
                
                
                
            



#def postochka(a):
    #if x[a] == 1:
     #   xco = xcor + 50
      #  yco = ycor + 0
        #turtle.setpos(xco,yco)
        

    #elif y[a] == 1:
       # xco = xcor + 0
        #yco = ycor + 50.00
        #turtle.setpos(xco,yco)

    #elif z[a] == 1:
     #   xco = xcor + 43.30
    #    yco = ycor + 25.00
   #     turtle.setpos(xco,yco)
    #    

#def tochka():
   # n = 0
   # while n < 8:
     #   zero()
   #     tochkaX(n)
    #    tochkaY(n)
      #  tochkaZ(n)
       #3 n = n + 1


        
           
        
        



        



