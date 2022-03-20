import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("D:\\Data\\rawdata.csv",encoding='latin1')
header = list(df.columns.values)

df1=df[df.ignition_status==1]



Plotstatus = 1
while (Plotstatus == 1):

    Plotsel = int(input("Enter the plot type\n 1. Histogram\
                        \n 2. Scatter plot \n 3. Line chart\
                        \n 4. Bar chart\n 5. Pie chart\n"))
    
    if Plotsel == 1:
    
        inputparam = input("Enter the parameter:")
        Param = df1[inputparam]
        
        n_bins = int(input("Enter the no of bins"))
        colorst = int(input("Do you want to input color?\n 1 Yes \n 0 No \n"))
        if colorst == 1:
            colorip = int(input("Choose the color\n 1. Red \n 2. Blue\
                                \n 3. Green \n 4. Yellow \n 5. Pink\n"))
            if colorip == 1:
                colorset= 'red'
            elif colorip == 2:
                colorset= 'blue'
            elif colorip == 3:
                colorset= 'green'
            elif colorip == 4:
                colorset= 'yellow'
            elif colorip == 5:
                colorset= 'pink'
        maxminst = int(input("Do you want to set max min range? \n 1 Yes \n 2 No\n"))
        if maxminst == 1:
            maxval = int(input("Enter the max limit"))
            minval = int(input("Enter the min limit"))
        plt.hist(Param, bins=n_bins,color= colorset)
        plt.xlabel(inputparam)
        plt.title("Histogram plot of {}".format(inputparam),fontsize=15)
        #plt.ylim(minval,maxval)
        plt.show()
        Plotstatus = int(input("Do you want to plot more? \n 1. Yes \n 2. No \n"))
    elif Plotsel == 2:
        inputparam1 = input("Enter the first parameter:")
        inputparam2 = input("Enter the second parameter:")
        Param1 = df1[inputparam1]
        Param2 = df1[inputparam2]
        #print("Parameter1",Param1)
        #print("Parameter2",Param2)
        colorst = int(input("Do you want to input color?\n 1 Yes \n 0 No \n"))
        if colorst == 1:
            colorip1 = int(input("Choose the color for Parameter\n 1. Red \n 2. Blue\
                                \n 3. Green \n 4. Yellow \n 5. Pink\n"))
            if colorip1 == 1:
                colorset= 'red'
            elif colorip1 == 2:
                colorset= 'blue'
            elif colorip1 == 3:
                colorset= 'green'
            elif colorip1 == 4:
                colorset= 'yellow'
            elif colorip1 == 5:
                colorset= 'pink'
        maxminst = int(input("Do you want to set max min range? \n 1 Yes \n 2 No\n"))
        if maxminst == 1:
            maxval = int(input("Enter the max limit"))
            minval = int(input("Enter the min limit"))    
        plt.ylim(minval,maxval)
        plt.scatter(Param1,Param2,color=colorset)
        plt.title("Scatter plot of {} vs {}".format(inputparam1,inputparam2),fontsize=12)
        plt.xlabel(inputparam1)
        plt.ylabel(inputparam2)
        
        plt.show()
        Plotstatus = int(input("Do you want to plot more? \n 1. Yes \n 2. No \n"))
    elif Plotsel == 3:
        Paramcount = int(input("Enter the number of parameters to be plotted:(Max 2)"))
        if Paramcount==1:
            lineinputparam1 = input("Enter the parameter:")
            LineParam1 = df1[lineinputparam1]
            colorst = int(input("Do you want to input color?\n 1 Yes \n 0 No \n"))
            if colorst == 1:
                colorip1 = int(input("Choose the color for Parameter\n 1. Red \n 2. Blue\
                                    \n 3. Green \n 4. Yellow \n 5. Pink\n"))
                if colorip1 == 1:
                    colorset= 'red'
                elif colorip1 == 2:
                    colorset= 'blue'
                elif colorip1 == 3:
                    colorset= 'green'
                elif colorip1 == 4:
                    colorset= 'yellow'
                elif colorip1 == 5:
                    colorset= 'pink'
            maxminst = int(input("Do you want to set max min range? \n 1 Yes \n 2 No\n"))
            if maxminst == 1:
                maxval = int(input("Enter the max limit"))
                minval = int(input("Enter the min limit"))    
            plt.ylim(minval,maxval)
            plt.plot(LineParam1,color=colorset)
            plt.title("Line plot of {}".format(lineinputparam1),fontsize=15)
            plt.legend(lineinputparam1,loc="upper left")
            plt.ylabel(lineinputparam1)
            plt.show()
        elif Paramcount==2:
            lineinputparam1 = input("Enter the first parameter:")
            lineinputparam2 = input("Enter the second parameter:")
        
            LineParam1 = df1[lineinputparam1]
            LineParam2 = df1[lineinputparam2]
            
            colorst = int(input("Do you want to input color?\n 1 Yes \n 0 No \n"))
            if colorst == 1:
                colorip1 = int(input("Choose the color for Parameter1\n 1. Red \n 2. Blue\
                                    \n 3. Green \n 4. Yellow \n 5. Pink\n"))
                if colorip1 == 1:
                    colorset= 'red'
                elif colorip1 == 2:
                    colorset= 'blue'
                elif colorip1 == 3:
                    colorset= 'green'
                elif colorip1 == 4:
                    colorset= 'yellow'
                elif colorip1 == 5:
                    colorset= 'pink'
                colorip2 = int(input("Choose the color for Parameter2\n 1. Red \n 2. Blue\
                                    \n 3. Green \n 4. Yellow \n 5. Pink\n"))
                if colorip2 == 1:
                    colorset1= 'red'
                elif colorip2 == 2:
                    colorset1= 'blue'
                elif colorip2 == 3:
                    colorset1= 'green'
                elif colorip2 == 4:
                    colorset1= 'yellow'
                elif colorip2 == 5:
                    colorset1= 'pink'
            fig, ax1 = plt.subplots()
            ax1.plot(LineParam1,label=lineinputparam1,color= colorset)
            ax1.set_ylabel(lineinputparam1)
            ax1.legend(lineinputparam1,loc="upper left")
            
            ax2 = ax1.twinx()
            ax2.plot(LineParam2, label=lineinputparam2,color= colorset1)
            ax2.set_ylabel(lineinputparam2)
            ax2.legend(lineinputparam2,loc="lower left")
            plt.title("Line plot of {} & {}".format(lineinputparam1,lineinputparam2),fontsize=15)
            #plt.legend([lineinputparam1,lineinputparam2],loc="upper left")
            plt.show()
            Plotstatus = int(input("Do you want to plot more? \n 1. Yes \n 2. No \n"))
            
    elif Plotsel == 4:
#       Paramcount = int(input("Enter the number of parameters to be plotted:(Max 2)"))
#       if Paramcount == 1:
        barinputparam1 = input("Enter the parameter:")
        BarParam1 = df1[barinputparam1]
        print("parameter selected is",BarParam1)
        barstart = int(input("Enter the start value:"))
        barend = int(input("Enter the end value:"))
        barbin = int(input("Enter the bin value:"))
        i =1
        max = int(((barend-barstart)/barbin)+1)
        print ("max is", max)
        BarParam2 = [0]*max
        while (i<max):
            print ("entered")
            BarParam2[0] = barstart
            print("firstvalue:",BarParam2[0])
            BarParam2[i]= barbin+ BarParam2[i-1]
            print("Parameter 2",BarParam2[i])
            i = i+1
            print("i is",i)
        
        colorst = int(input("Do you want to input color?\n 1 Yes \n 0 No \n"))
        if colorst == 1:
            colorip1 = int(input("Choose the color for Parameter\n 1. Red \n 2. Blue\
                                \n 3. Green \n 4. Yellow \n 5. Pink\n"))
            if colorip1 == 1:
                colorset= 'red'
            elif colorip1 == 2:
                colorset= 'blue'
            elif colorip1 == 3:
                colorset= 'green'
            elif colorip1 == 4:
                colorset= 'yellow'
            elif colorip1 == 5:
                colorset= 'pink'
        plt.title("Bar chart of {}".format(barinputparam1),fontsize=15)
        plt.hist(BarParam1,bins=BarParam2,color= colorset)
        
        plt.show()
        Plotstatus = int(input("Do you want to plot more? \n 1. Yes \n 2. No \n"))
                
    elif Plotsel == 5:
        pieinputparam = input("Enter the parameter:")
        PieParam = df1[pieinputparam] 
        #count= Counter(PieParam)
        count= pd.Series(PieParam).value_counts()
        length = len(count)
        sumarray= sum(count)
        print("Length of the array is",length)
        i=0
        Pieparamplot = [0]*length
        label = [0]*length
        while (i<length):
            Pieparamplot[i]= (count[i]/sumarray)*100
            
            print("label is",label[i])
            print("Pieparam",Pieparamplot[i])
            i = i+1
        
        #print("Headers",headers)
        plt.title("Pie chart of {}".format(pieinputparam),fontsize=15)
        plt.pie(Pieparamplot)
        plt.show()
        
        Plotstatus = int(input("Do you want to plot more? \n 1. Yes \n 2. No \n"))