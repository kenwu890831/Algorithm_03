#演算法分析機側
#學號 : 10724128
#姓名 : 吳宇哲
#中原大學資訊工程系
import time
class RiverCross :
 def __init__(self,wolf_num,sheep_num):
    self.total_wolf_num = wolf_num
    self.total_sheep_num = sheep_num
    self.west_wolf_num = wolf_num
    self.west_sheep_num = sheep_num
    self.east_wolf_num = 0
    self.east_sheep_num = 0
    self.boat_place = 0 # 0 west 1 east
    self.first = True
    self.temp = []

 def toEast(self, path,west_wolf_num,west_sheep_num,east_wolf_num,east_sheep_num, pos) :
    if  ( (self.first == False) and ( self.testError(west_wolf_num,west_sheep_num,east_wolf_num,east_sheep_num,path,0) == True )):
        return
    else :
       self.first = False 
       nowTemp = [west_wolf_num,west_sheep_num,"W"]
       path1 = path[:]
       path1.append( nowTemp)
       if (pos != 1) :
        self.toWest( path1,west_wolf_num-2,west_sheep_num,east_wolf_num+2,east_sheep_num, 1)
       if (pos != 3):
         self.toWest( path1,west_wolf_num-1,west_sheep_num,east_wolf_num+1,east_sheep_num, 3)
       if (pos != 4) :
         self.toWest( path1,west_wolf_num,west_sheep_num-1,east_wolf_num,east_sheep_num+1, 4)
       if (pos != 5) :
         self.toWest( path1,west_wolf_num,west_sheep_num-2,east_wolf_num,east_sheep_num+2, 5)
         

 def toWest(self, path,west_wolf_num,west_sheep_num,east_wolf_num,east_sheep_num, pos) :
    if (west_wolf_num == 0 ) and (west_sheep_num == 0) : # done
       self.temp.append(path)
       return 
    elif  ( self.testError(west_wolf_num,west_sheep_num,east_wolf_num,east_sheep_num,path,1) == True):
       return
    else :
       nowTemp = [west_wolf_num,west_sheep_num,"E"]
       path1 = path[:]
       path1.append( nowTemp)
       
       if (((west_wolf_num>=west_sheep_num)and ( west_sheep_num != 0)) or ((east_wolf_num>=east_sheep_num)and ( west_sheep_num != 0)))and (east_sheep_num != 0) and (east_wolf_num != 0) :
          return 
       if (pos != 1) :
         self.toEast( path1,west_wolf_num+2,west_sheep_num,east_wolf_num-2,east_sheep_num,1)
       #if (pos != 2) :
       #   
       if (pos != 3) :
          self.toEast( path1,west_wolf_num+1,west_sheep_num,east_wolf_num-1,east_sheep_num,3)
       if (pos != 4) :
          self.toEast( path1,west_wolf_num,west_sheep_num+1,east_wolf_num,east_sheep_num-1,4)
       if (pos != 5) :
          self.toEast( path1,west_wolf_num,west_sheep_num+2,east_wolf_num,east_sheep_num-2,5)
       #self.toEast( path,west_wolf_num,west_sheep_num,east_wolf_num,east_sheep_num,2)

 def testError(self,west_wolf_num,west_sheep_num,east_wolf_num,east_sheep_num,path,place) :
      for i in range(len(path)) :
        if (( path[i][0] == west_wolf_num ) and ( path[i][1] == west_sheep_num )) :
          if ( place == 0 ) :
            if ( i % 2 == 0 ) :
              return True

      if (east_wolf_num < 0) or (east_sheep_num< 0) or (west_sheep_num< 0)or (west_wolf_num< 0) : # too low
       return True 
      elif (((west_wolf_num>=west_sheep_num)and (west_sheep_num != 0)) or ((east_wolf_num>=east_sheep_num) and (east_sheep_num != 0))): # 會被吃
       return True
      elif ( west_sheep_num > self.total_sheep_num) or (east_sheep_num > self.total_sheep_num) or ( west_wolf_num > self.total_wolf_num) or ( east_wolf_num > self.total_wolf_num) : # too much
       return True
      elif ((west_wolf_num==self.total_wolf_num) and (west_sheep_num==self.total_sheep_num)): # first
       return True
      return False

 def riverCross(self) :
    self.first = True
    path = []
    self.toEast(path,self.west_wolf_num,self.west_sheep_num,self.east_wolf_num,self.east_sheep_num,0)
    if ( len(self.temp)!=0) :
      self.printResult()
    else :
      print("not have result")
 def printResult(self) :
    max = 0
    place = 0
    nowTemp = [0,0,"E"]
    
    for i in range( len(self.temp)) :
      if max < len(self.temp[i]) :
        max = len(self.temp[i])
        place = i

    self.temp[place].append(nowTemp)
    print(self.temp[place])
       




print("渡河問題(River Crossing Problem)")

wolf_num, sheep_num = map( int , input("請輸入數量 : ").split())
while True :
   if ( wolf_num == 0) & ( sheep_num == 0) :
     break
   start_time = time.time()
   r1 = RiverCross(wolf_num,sheep_num)
   r1.riverCross() 
   total_time = time.time() - start_time
   print ( "run time : ",total_time )
   wolf_num, sheep_num = map( int , input("請輸入數量 : ").split())
"""
2 2
0 0
( 2 2 W )
( 0 2 E )
( 1 2 W )
( 1 0 E )
( 2 0 W )
( 0 0 E )
"""