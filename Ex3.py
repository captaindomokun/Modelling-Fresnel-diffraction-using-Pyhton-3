#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 18:25:02 2018
"""
#
# put your "import" statements here
#



import numpy as np
import math
import matplotlib.pyplot as plt







#The function used for the composite simpsons rule
def simps(f,a_1,a_2,N):
        # 4 variables are used for the function, f being the function that will be integrated,
        #a_1 and a_2 stand for the limits of intergation for the aperture and N is the number of
        #iterations used(arbitrary)
            if N % 2 == 1:
                raise ValueError('N must be an even integer.')
            da = (a_2-a_1)/N
            #da is the spacing between the limits of intergation
            a = np.linspace(a_1,a_2,N+1)
            #list of a values
            y = f(a)
            Sum = da/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
            #y[0:-1;2] selects odd values including the beginning but not the end, y[1::2] selects all
            #the even values and y[2::2] selects the the odd values but with the end.
            return Sum
        
#Beginning of the Menu system
MyInput = '0'
while MyInput != 'q':
    MyInput = input('Enter a choice, "a" for 1-Dimensional Fresnel intergration, "b" for 2-Dimensional fresnel intergatrion or "q" to quit: ')
    print('You entered the choice: ',MyInput)

    if MyInput == 'a':
        print('You have chosen part (a)')
        Input_lambda = input('Enter the wavelength of light in nanometres')
        lmbda = float(Input_lambda)/10**9
        print(lmbda)
        
        Input_z = input('Enter the distance of the screen in centremetres')
        z = float(Input_z)/10**2
        print(z)
        
        Input_width = input('Enter the width of the aperture in micrometers')
        a_width = float(Input_width)/10**6
        print(a_width)
        
        #This Selects the range of x values used depending on the parameters used to show the 
        #Different fresnel patterns
        if z< 0.0005 and a_width > 100/10**6:
            p =0.00005
        elif z<0.0005 and a_width == 100/10**6:
            p = 0.00005
        elif z>= 0.0005 and a_width > 100/10**6:
            p = 0.0005
        elif z>= 0.0005 and a_width <= 100/10**6:
            p = 0.003
        #Constants
        x_0 = -p
        x_1 = p
        y_0 = -p
        y_1 = p
        j=complex(0,1)
        E_0 = 1
        
        #Variables
        k = (2*np.pi)/(lmbda)
        a_1 = -1 * a_width/2
        a_2 = a_width/2
        
        
    
        X = np.arange(x_0, x_1, p/100)
        I = [abs(((E_0*k)/(2*np.pi*z ) * simps(lambda a: np.exp(  (j*k)/(2*z) * (x - a)**2 ),a_1,
                   a_2,5000))**2) for x in X]
    

    
    

        plt.plot(X,I)
        plt.xlabel('Distance in metres')
        plt.ylabel('Intensity')
        plt.show()
        
        
        
        
        
        
        
        

            
       
      
    elif MyInput == 'b':
        print('You have chosen part (b)')
        
        Input_lambda = input('Enter the wavelength of light in nanometres ')
        lmbda = float(Input_lambda)/10**9
        print(lmbda)
        
        Input_z = input('Enter the distance of the screen in centremetres ')
        z = float(Input_z)/10**2
        
        print(z)
        
        Input_width = input('Enter the width of the aperture in micrometers ')
        a_width = float(Input_width)/10**6
        print(a_width)

            
        if z< 0.0005 and a_width > 100/10**6:
            p =0.00001
        elif z<0.0005 and a_width <= 100/10**6:
            p = 0.00005
        elif z>= 0.0005 and a_width > 100/10**6:
            p = 0.0005
        elif z>= 0.0005 and a_width <= 100/10**6:
            p = 0.003
        #constants
        x_0 = -p
        x_1 = p
        y_0 = -p
        y_1 = p
        l=complex(0,1)
        E_0 = 1
        
        #Variables
        k = (2*np.pi)/(lmbda)
        a_1 = -1 * a_width/2
        a_2 = a_width/2
        
        Input_shape = input("Please enter the shape of the aperture, "R" for rectangular and " )
        #Creates the intensity grid
        NumPoints = 1000
        delta =  2*p / (NumPoints - 1)
        intensity = np.zeros( (NumPoints,NumPoints) )


        #Creates the x and y values then for each point in the intensity grid, the zero is
        #Replaced with the relevant intensity value
        for i in range(NumPoints):
            x = (i * delta) - p 
            for j in range(NumPoints):
                y = (j * delta) - p
                intensity[i,j] =  - abs(((E_0*k)/(2*np.pi*z) * 
                         simps(lambda a: np.exp(  (l*k)/(2*z) * (x - a)**2 ),a_1,a_2,NumPoints) * 
                         simps(lambda a: np.exp(  (l*k)/(2*z) * (y - a)**2 ),a_1,a_2,NumPoints))**2)
           
        plt.imshow(intensity, cmap=plt.get_cmap('jet'))
        plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
        

    elif MyInput != 'q':
        print('This is not a valid choice')

print('You have chosen to finish - goodbye.')
