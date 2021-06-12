def get_speed(dis,time):
    speed = dis/time
    print(f'the speed is {speed}')

#calling function
get_speed(1000,40)

distance = 200
time = 100
get_speed(distance,time)       #named arguments  

get_speed(dis=250,time=100)   # when passing argument using name we change


def pythagoeras(perpendicular:int,base:int):
    hyp = (perpendicular**2 + base**2)** .5
    print(f'p={perpendicular},b={base} => h={hyp}')

pythagoeras(1,4)
pythagoeras(23,34)    