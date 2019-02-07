class Timer:
   def __init__(self,timelimit):
       self.x = timelimit
       self.y = 0

def solutioncheck():
   if int(T1.x) + int(T2.x) == 15:
       print("solved")
       exit()
   elif int(T1.x) + int(T2.y) == 15:
       print("solved")
       exit()
   elif int(T1.y) + int(T2.x) == 15:
       print("solved")
       exit()
   elif int(T1.y) + int(T2.y) == 15:
       print("solved")
       exit()
   else:
       print("keep going")

T1 = Timer(11)
T2 = Timer(13)
solution = 15

def solver():
   if T1.x > T1.y:
       T2.y = T2.x - T1.x
       T2.x = T2.x - T2.y
       T1.y = T1.x
       T1.x = 0
   elif T1.x < T1.y:
       T1.x = T1.y - T2.y
       T1.y = T1.y - T1.x
       T2.x = T2.x + T2.y
       T2.y = 0

while True:
   print("Timer 1 values: {0} & {1}".format(T1.x, T1.y))
   print("Timer 2 values: {0} & {1}".format(T2.x, T2.y))
   solutioncheck()
   solver()
   
