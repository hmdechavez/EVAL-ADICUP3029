# File: CN0548_simple_plot.py
# Description: CN0548 data logging and real-time plot
# Author: Harvey De Chavez (harveyjohn.dechavez@analog.com)
#
# Copyright 2020(c) Analog Devices, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#  - Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  - Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  - Neither the name of Analog Devices, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#  - The use of this software may or may not infringe the patent rights
#    of one or more patent holders.  This license does not release you
#    from the requirement that you obtain separate licenses from these
#    patent holders to use this software.
#  - Use of the software either in source or binary form, must be run
#    on or directly connected to an Analog Devices Inc. component.
#
# THIS SOFTWARE IS PROVIDED BY ANALOG DEVICES "AS IS" AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, NON-INFRINGEMENT,
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL ANALOG DEVICES BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, INTELLECTUAL PROPERTY RIGHTS, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import turtle

def draw_rec(x,y,x_len,y_len,fill):
    turtle.setpos(x,y)
    turtle.down()
    if fill == 1:
        turtle.begin_fill()
    for i in range(4):
        if i%2==0:
            turtle.forward(x_len)
        if i%2==1:
            turtle.forward(y_len)
        turtle.right(90)
    if fill == 1:
        turtle.end_fill()
    turtle.up()

unit = 24
x_init = -4 * unit
y_init = 6 * unit
style = ('Arial', 10)
style2 = ('Arial', 20, 'bold')

def draw_jumpers():
    jumper = ['P1','P3','P10','P8','P9','P11','P13','P14','P12','P7']
    turtle.hideturtle()
    turtle.speed(0)
    turtle.up()
    
    turtle.setpos(0,210)
    turtle.write('CN0548 Jumper Configuration',font=style2,align='center')

    for j in range(6):
        draw_rec(x_init+int(j/3)*(6*unit),y_init-(j%3)*(4*unit),2*unit,3*unit,0)
    
        for k in range(6):
            draw_rec(x_init+int(j/3)*(6*unit)+0.25*unit+int(k/3)*unit,y_init-(j%3)*(4*unit)-0.25*unit-(k%3)*unit,0.5*unit,0.5*unit,0)
    
        if int(j/3) == 0:
            turtle.setpos(x_init+int(j/3)*(6*unit)+(3*unit),y_init-(j%3)*(4*unit)-1.875*unit)
        else:
            turtle.setpos(x_init+int(j/3)*(6*unit)-(1*unit),y_init-(j%3)*(4*unit)-1.875*unit)
        turtle.write(jumper[j],font=style,align='center')
    
    for j in range(2):
        draw_rec(x_init+unit+j*5*unit,y_init-12*unit,unit,3*unit,0)

        for k in range(3):
            draw_rec(x_init+unit+j*5*unit+0.25*unit,y_init-12*unit-0.25*unit-k*unit,0.5*unit,0.5*unit,0)    

        turtle.setpos(x_init+unit+j*5*unit+(-3*j+2)*unit,y_init-12*unit-1.875*unit)
        turtle.write(jumper[j+6],font=style,align='center')
    
    for j in range(2):
        draw_rec(x_init-3*unit+j*11*unit,y_init-13*unit,3*unit,unit,0)

        for k in range(3):
            draw_rec(x_init-3*unit+j*11*unit+0.25*unit+k*unit,y_init-13*unit-0.25*unit,0.5*unit,0.5*unit,0)    

        turtle.setpos(x_init-1.5*unit+j*11*unit,y_init-13*unit)
        turtle.write(jumper[j+8],font=style,align='center')

def gain_config(p1,p3,p10,p8,p9,p11):
    if p1==1:
        draw_rec(x_init+4,y_init-4-unit,40,16,1)
    elif p1==2:
        draw_rec(x_init+4,y_init-4,40,16,1)
    else:
        draw_rec(x_init+4+unit,y_init-4,16,40,1)

    if p3==1:
        draw_rec(x_init+4,y_init-4-5*unit,40,16,1)
    elif p3==2:
        draw_rec(x_init+4,y_init-4-4*unit,40,16,1)
    else:
        draw_rec(x_init+4+unit,y_init-4-4*unit,16,40,1)

    if p10==1:
        draw_rec(x_init+4,y_init-4-9*unit,40,16,1)
    elif p10==2:
        draw_rec(x_init+4,y_init-4-8*unit,40,16,1)
    else:
        draw_rec(x_init+4+unit,y_init-4-8*unit,16,40,1)

    if p8==1:
        draw_rec(x_init+4+6*unit,y_init-4-1*unit,40,16,1)
    elif p8==2:
        draw_rec(x_init+4+6*unit,y_init-4-2*unit,40,16,1)
    else:
        draw_rec(x_init+4+6*unit,y_init-4,16,40,1)
    
    if p9==1:
        draw_rec(x_init+4+6*unit,y_init-4-5*unit,40,16,1)
    elif p9==2:
        draw_rec(x_init+4+6*unit,y_init-4-6*unit,40,16,1)
    else:
        draw_rec(x_init+4+6*unit,y_init-4-4*unit,16,40,1)
    
    if p11==1:
        draw_rec(x_init+4+6*unit,y_init-4-9*unit,40,16,1)
    elif p11==2:
        draw_rec(x_init+4+6*unit,y_init-4-10*unit,40,16,1)
    else:
        draw_rec(x_init+4+6*unit,y_init-4-8*unit,16,40,1)

def c_uni():
    draw_rec(x_init+4+unit,y_init-4-12*unit,16,40,1)
    draw_rec(x_init+4-3*unit,y_init-4-13*unit,40,16,1)

def c_bi():
    draw_rec(x_init+4+unit,y_init-4-13*unit,16,40,1)
    draw_rec(x_init+4-2*unit,y_init-4-13*unit,40,16,1)

def v_uni():
    draw_rec(x_init+4+6*unit,y_init-4-12*unit,16,40,1)
    draw_rec(x_init+4+9*unit,y_init-4-13*unit,40,16,1)

def v_bi():
    draw_rec(x_init+4+6*unit,y_init-4-13*unit,16,40,1)
    draw_rec(x_init+4+8*unit,y_init-4-13*unit,40,16,1)
    
def isint(x,lower,upper):
    try:
        val = int(x)
        if upper == 'x':
            if val >= lower:
                return 0
            else:
                return 1
        else:
            if val >= lower and val <= upper:
                return 0
            else:
                return 1
    except:    
        return 2

def input_int(text,lower,upper):
    x = input(text)
    if isint(x,lower,upper) == 0:
        return int(x)
    elif isint(x,lower,upper) == 1:
        print("Please input a value within the given option range")
        return 'x'
    else:
        print("Invalid response, the system is expecting an integer value within the range of options")
        return 'x'

# ----------------------------Program starts here------------------------------------------

print(" ------------------------------------------------------------------\n| EVAL-CN0548-ARDZ: Isolated High Current and High Voltage Sensing |\n ------------------------------------------------------------------\n\nGeneral Reminder:")
print("\n  > Disconnect any input until the board is properly configured.\n\n  > Note the node polarities when using the unipolar and unidirectional modes.\n\n  > Do not use the board for inputs that exceed the set configuration.\n\n  > Disconnect any input attached to the board when changing jumper configurations.\n")
input("\t\t\t\t\t\tPress the 'enter' key to proceed")
print("Starting program...")
new = 0
error = 0
try:
    rec_value = []
    line_count = 0
    
    record = open("session_record.txt", "r")
    for line in record:
        line_count = line_count + 1
    record.close()

    if line_count < 9:
        print("Some contents of the session record file seem to have been removed.\nStarting new session...")
        new = 1
    else:
        line_count = 0
        record = open("session_record.txt", "r")
        for line in record:
            part = line.split('-')
            rec_value.append(part[0].strip())
            line_count = line_count + 1
            if line_count == 9:
                break
        
        error = error + isint(rec_value[1],1,2)
        error = error + isint(rec_value[2],1,5)
        error = error + isint(rec_value[3],1,2)
        error = error + isint(rec_value[4],1,5)
        error = error + isint(rec_value[5],1,2)
        error = error + isint(rec_value[6],1,2)
        if error == 0 and rec_value[6] == '1':
            error = error + isint(rec_value[7],1,2)
            if error == 0 and rec_value[7] == '2':
                error = error + isint(rec_value[8],5,'x')
        if error > 0:
            new = 1
        
except:
    print("No session record found. Starting new session...")
    new = 1

v_rating = { 11:"16V", 12:"20V", 13:"27V", 14:"40V", 15:"80V", 21:"+/-8V", 22:"+/-10V", 23:"+/-13.5V", 24:"+/-20V", 25:"+/-40V" }
c_rating = { 1:"20A", 2:"+/-10A" }  

if new == 0:
    print("\nSession record detected.\n")
    print("Maximum rating: " + v_rating[10*int(rec_value[1])+int(rec_value[2])] + " , " + c_rating[int(rec_value[3])])

    if rec_value[4] == '1':
        print("Data sampling rate: " + rec_value[4] + " sample per second")
    else:
        print("Data sampling rate: " + rec_value[4] + " samples per second")

    if rec_value[5] == '1':
        print("Data logging enabled")
    else:
        print("Data logging disabled")
    
    if rec_value[6] == '1':
            if rec_value[7] == '1':
                print("Plot enabled in tracking mode")
            else:
                print("Plot enabled in non-tracking mode, latest " + rec_value[8] + " samples are displayed")
    else:
        print("Plot disabled")
    
    print("\nUse same setting as previous session? (1 or 2)\n\t(1) Yes\n\t(2) No")
    while True:
        response = input_int(">> ",1,2)
        if response==1:
            new = 0
            break
        elif response==2:
            new = 1
            break
        
elif error > 0:
    print("Some contents of the session record file seem to have been modified and might cause program error.\nStarting new session...")

new_record = ["Session Record:"]

if new != 0:
    print("\nCreating jumper map...\nThis will take a few seconds, do not close the jumper window")
    draw_jumpers()
    print("\nThe following prompts will help you setup the jumper configuration of the CN0548 board depending on your expected inputs. A map of the board jumpers should have appeared in another window. This map will be updated as you provide responses to the different prompts.\n\n")
    print("----- Setting up the hardware for LT1997-2 -----\n\n-Step 1 of 2: Type of voltage measurement-\n\t(1) Unipolar: The board expects non-negative readings allowing it to measure a wider range of positive voltages. Software is configured to read from 0 to Vmax.\n\t(2) Bipolar: The board expects both positive and negative readings, effective range is divided equally. Software is configured to read from -Vmax/2 to Vmax/2.\n")
while True:
    if new != 0:
        v_type = input_int("Type of measurement (1 or 2): ",1,2)
    else:
        v_type = int(rec_value[1])
    
    if v_type == 1:
        if new != 0:
            v_uni()
        break
    elif v_type == 2:
        if new != 0:
            v_bi()
        break
new_record.append(str(v_type) + " - Unipolar | Bipolar")

if new != 0:
    print("\n\n-Step 2 of 2: Voltage Range-\nThe maximum voltage range is 80V but the board can be configured to a more refined voltage range in order to produce higher resolution readings. Select your desired Vmax:\n\t(1) 16V\n\t(2) 20V\n\t(3) 27V\n\t(4) 40V\n\t(5) 80V\n")
while True:
    if new != 0:
        v_max = input_int("Range (1 to 5): ",1,5)
    else:
        v_max = int(rec_value[2])
    
    if v_max == 1:
        if new != 0:
            gain_config(3,3,1,3,3,2)
        v_gain = 0.004
        break
    elif v_max == 2:
        if new != 0:
            gain_config(3,1,3,3,2,1)    
        v_gain = 0.005
        break
    elif v_max == 3:
        if new != 0:
            gain_config(2,3,1,1,3,2)
        v_gain = (1/150)
        break
    elif v_max == 4:
        if new != 0:
            gain_config(1,3,3,2,1,1)
        v_gain = 0.01
        break
    elif v_max == 5:
        if new != 0:
            gain_config(3,2,1,3,1,2)
        v_gain = 0.02
        break
new_record.append(str(v_max) + " - 16V | 20V | 27V | 40V | 80V")

if new != 0:
    if v_type == 1:
        v_text = "Voltage measurement: Unipolar   (Effective Range: 0 to " + v_rating[10*v_type+v_max] + " )"
    else:
        v_text = "Voltage measurement: Bipolar   (Effective Range: " + v_rating[10*v_type+v_max] + " )"
    turtle.setpos(0,190)
    turtle.write(v_text,font=('Arial',10,'bold'),align='center')

i_gain = 5
if new != 0:
    print("\n\n----- Setting up the hardware for AD8410 -----\n-Step 1 of 1: Type of measurement-\n\t(1) Unidirectional: The board expects positive current flow only. Board is configured to handle 0 to 20A.\n\t(2) Bidirectional: The board expects both positive and negative current flow. Board is configured to handle -10A to 10A.\n")
while True:
    if new != 0:
        c_type = input_int("Type of current measurement (1 or 2): ",1,2)
    else:
        c_type = int(rec_value[3])
    if c_type == 1:
        if new != 0:
            c_uni()
            c_text = "Current measurement: Unidirectional      (Effective range: 0 to 20A)"
        break
    elif c_type == 2:
        if new != 0:
            c_bi()
            c_text = "Current measurement: Bidirectional      (Effective range: -10A to 10A)"
        break
new_record.append(str(c_type) + " - Unidirectional | Birectional")

if new != 0:
    turtle.setpos(0,170)
    turtle.write(c_text,font=('Arial',10,'bold'),align='center')
    print("\nYou may close the jumper map window if you have configured the board jumpers")
    turtle.setpos(0,-250)
    turtle.write("You may close this window if you have configured the board jumpers",font=('Arial',10,'bold'),align='center')
    input("Press 'enter' key to proceed to connection setup and software configuration")

import sys
import time
from datetime import datetime
from typing import List
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import adi
global ad7799

while True:
    if new != 0:
        fs = input_int('\n---Software Configuration---\n\nSampling Rate: The rate at which data is collected from the board.\nSamples per second (1-5): ',1,5)
    else:
        fs = int(rec_value[4])
    if fs >= 1 and fs <= 5:
        break
new_record.append(str(fs) + " - samples per second (1-5)")

while True:
    if new != 0:
        log = input_int('\nData Logging: Records all your measurements in a csv file.\nEnable data logging?\n\t(1) Yes\n\t(2) No\n>> ',1,2)
    else:
        log = int(rec_value[5])
    if log == 1 or log == 2:
        break
new_record.append(str(log) + " - Data logging enabled | Data logging disabled")

if log == 1:
    dt_now = datetime.now()
    dt_format = dt_now.strftime("%d-%m-%Y_%H-%M")
    filename = 'CN0548_'+dt_format+'.csv'

while True:
    if new != 0:
        en = input_int('\nPlot Window: A real-time plot of the board\'s IV readings.\nNote: Sampling rate can be affected if plot is enabled\n\nEnable plot?\n\t(1) Yes\n\t(2) No\n>> ',1,2)
    else:
        en = int(rec_value[6])
    if en == 1 or en == 2:
        break
new_record.append(str(en) + " - Plot enabled | Plot disabled")

if en == 1:
    enable_plot = True
else:
    enable_plot = False

if enable_plot:
    datalog = []
    while True: 
        if new != 0:
            mode = input_int('\nPlot Mode:\n (1) Tracking: All data points will be displayesd in the plot\n (2) Non-tracking: Only the recent x samples will be displayed\n\n>> ',1,2)
        else:
            mode = int(rec_value[7])
        if mode != 'x':
            break    
    new_record.append(str(mode) + " - Tracking | Non-tracking")
    
    if mode == 2:
        while True: 
            if new != 0:
                samples = input_int('\nInput number of samples to retain within the plot (>=5).\nSamples to retain: ',5,'x')
            else:
                samples = int(rec_value[8])
            if samples != 'x':
                break
        new_record.append(str(samples) + " - samples to retain (>=5)")

    # Create figure for plotting
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    xs: List[float] = []
    ys: List[float] = []
    if mode ==2:
        for i in range(samples):
            xs.append(0)
            ys.append(0)
    
    print("\n-Connection setup-\n")
    while True:
        port = input('Input Serial line (e.g. if ADICUP3029 is connected to COM7, input \'COM7\' )\nSerial line: ')
        try:
            context = "serial:" + port + ",115200"
            ad7799 = adi.ad7799(uri=context)
            input("\nCN0548 board detected.\nPress 'enter' key to start board operation\n")
            break
        except:
            print("Port not found\n")
    print("Voltage readings are in volts (V) while current readings are in milliamperes (mA).")
    

    def animate(i,volt, curr):      # function for animation
        v_reading = v_gain*ad7799.channel[2].value # get new voltage reading
        i_reading = i_gain*ad7799.channel[0].value # get new current reading
        volt.append(v_reading)  
        curr.append(i_reading)  
        print('Voltage reading: ' + str(v_reading) + '\t\t\t' + 'Current reading: ' + str(i_reading))
        if log == 1:
            datalog.append(str(v_reading) + ',' + str(i_reading)+'\n')
              
    # number of recent samples to be retained
        if mode == 2:
            volt = volt[-samples:]
            curr = curr[-samples:]
    #initialize/clear
        lower = 0
        upper = 0
    # Plot config
        ax1.clear()
        span = max(volt) - min(volt)
        if span != 0:
            lower = min(volt) - span/16
            upper = max(volt) + span/16
        else:
            lower = min(volt) - 0.001
            upper = max(volt) + 0.001
        ax1.set_ylim([lower,upper])
        color = 'tab:orange'
        ax1.plot(volt, label="Voltage Reading", linewidth=2.0,color=color)
        if mode == 1:
            ax1.set_xlabel("Latest "+str(len(volt)) + " samples" , labelpad=10)
        else:
            ax1.set_xlabel("Latest "+str(samples) + " samples" , labelpad=10)
        ax1.set_ylabel("Volts (V)",color=color)
        ax1.tick_params(axis="x", which="both", bottom=True, top=False, labelbottom=False)
        ax1.legend(bbox_to_anchor=[0.1, -0.1], ncol=2, loc="upper left", frameon=False)
        
        ax2.clear()
        span = max(curr) - min(curr)
        if span != 0:
            lower = min(curr) - span/16
            upper = max(curr) + span/16
        else:
            lower = min(curr) - 0.5
            upper = max(curr) + 0.5
        ax2.set_ylim([lower,upper])
        color = 'tab:blue'
        ax2.plot(curr, label="Current Reading", linewidth=2.0,color=color)
        ax2.set_ylabel("Milliamperes (mA)",color=color)
        ax2.tick_params(axis="x", which="both", bottom=True, top=False, labelbottom=False)
        ax2.legend(bbox_to_anchor=[0.9, -0.1], ncol=2, loc="upper right", frameon=False)
        # ax2.set_xlabel("Latest "+str(samples) + " samples",labelpad=10)
        title_text = "CN0548 Maximum Rating: " + v_rating[10*v_type+v_max] + " , " + c_rating[c_type]
        plt.title(title_text, fontweight="bold")
        plt.subplots_adjust(bottom=0.30)
        if log == 1:
            ax2.text(0,-0.3,"Your data will be logged upon closing the plot window.",size="small",transform=ax2.transAxes)
            ax2.text(0,-0.35,"Premature termination of the program by closing the terminal will result to loss of data.",size="small",transform=ax2.transAxes)
        
    if mode == 1:
        new_record.append('x - samples to retain')
    record = open("session_record.txt","w")
    for i in range(9):
        record.write(str(new_record[i]))
        if i != 8:
            record.write("\n")
    record.close()

    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=(1000/fs))
    plt.show()
    
    if log == 1:
        output = open(filename,'w')
        output.write("Voltage Reading (V),Current Reading (mA)\n")
        for i in range(len(datalog)):
            output.write(datalog[i])
        output.close()
        input("\n\nData has been sucessfully logged!\n\n")
    
else:
    new_record.append('x - Tracking | Non-tracking')
    new_record.append('x - samples to retain')
    record = open("session_record.txt",'w')
    for i in range(9):
        record.write(str(new_record[i]))
        if i != 8:
            record.write("\n")
    record.close()

    while True:
        port = input('Input Serial line (e.g. if ADICUP3029 is connected to COM7, input \'COM7\' )\nSerial line: ')
        try:
            context = "serial:" + port + ",115200"
            ad7799 = adi.ad7799(uri=context)
            input("\nCN0548 board detected.\nPress 'enter' key to start board operation\n")
            break
        except:
            print("Port not found\n")

    print("Voltage reading is in terms of volts (V) and current reading is in terms of milliamperes (mA).")
    if log == 1:
            output = open(filename,'a')
            output.write("Voltage Reading (V),Current Reading (mA)\n")
            output.close()
    while True:
        v_reading = v_gain*ad7799.channel[2].value # get new voltage reading
        i_reading = i_gain*ad7799.channel[0].value # get new current reading
        print('Voltage reading: ' + str(v_reading) + '\t\t\t' + 'Current reading: ' + str(i_reading) )
        time.sleep(1/fs)
        if log == 1:
            output = open(filename,'a')
            output.write(str(v_reading)+","+str(i_reading)+"\n")
            output.close()
            
del ad7799
