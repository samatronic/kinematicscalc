#simple kinematic calculator 
import math
def kinematics():
    g = 10
    print("Please choose what you want to calculate:")
    print("1. Final velocity (v)")
    print("2. Displacement (x)")
    print("3. Acceleration (a)")
    print("4. Time (t)")
    choice =  int(input("Enter your choice (1-4): "))

    if choice == 1:
        #v = v0 +at
        v0 = float(input('Enter the initial velocity' ))
        a = float(input('Enter the acceleration' ))
        t = float(input('Enter the time' ))
        v = v0 + a*t
        print(f"The final velocity is {v} m/s")
    elif choice == 2:
        #x= v0t - .5at^2
        v0 = float(input('Enter the initial velocity' ))
        t = float(input('Enter the time' ))
        a = float(input('Enter the acceleration' ))
        x = v0*t + .5*a*t**2
        print (f"The displacement is  {x}  m")
    elif choice == 3: 
        #v^2=v0^2 + 2ax
        v = float(input('Enter the final velocity' ))
        v0 = float(input('Enter the initial velocity' ))
        x = float(input('Enter the displacement' ))
        a = (v**2-v0**2)/(2*x)
        print(f"The acceleration is {a} m/s^2")
    elif choice == 4:
        #x= v0t - .5at^2
        v0 = float(input('Enter the initial velocity' ))
        x = float(input('Enter the displacement' ))
        a = float(input('Enter the acceleration' ))
        
        discri = (v0)**2 - (4*.5*a*-x)
        sqrtVal = math.sqrt(abs(discri))

        if discri > 0:  
            t1 = (-v0 + sqrtVal)/(2 * 0.5* a) 
            t2 = (-v0   - sqrtVal)/(2 * 0.5* a)    
            print (f"The  is time {round(t1,2)} or {round(t2,2)} s")
        elif discri == 0:  
            t3 = (-v0 / (2 * a))
            print (f"The  is time {round(t3,2)}  s")

        
kinematics()


