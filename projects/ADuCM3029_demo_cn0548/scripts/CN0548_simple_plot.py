# File: CN0548_simple_plot_v3.py
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

def draw_rec(x,y,x_len,y_len):
    turtle.setpos(x,y)
    turtle.down()
    for i in range(4):
        if i%2==0:
            turtle.forward(x_len)
        if i%2==1:
            turtle.forward(y_len)
        turtle.right(90)
    turtle.up()

x_init = -90
y_init = 132
x_major = 120
y_major = 96
x_minor = 30
y_minor = 24

def draw_jumpers():
    turtle.hideturtle()
    turtle.speed(0)
    turtle.up()
    style = ('Arial', 10)
    style2 = ('Arial', 20, 'bold')

    turtle.setpos(0,210)
    turtle.write('CN0548 Jumper Configuration',font=style2,align='center')

    for j in range(6):
        draw_rec(x_init+int(j/3)*x_major,y_init-(j%3)*y_major,x_major/2,y_major*(0.75))
    
        for k in range(6):
            draw_rec(x_init+int(j/3)*x_major+7+int(k/3)*x_minor,y_init-(j%3)*y_major-7-(k%3)*y_minor,x_minor*(8/15),y_minor*(5/12))
    
        if int(j/3) == 0:
            turtle.setpos(x_init+int(j/3)*x_major+x_major*0.625,y_init-(j%3)*y_major-y_major*(15/32))
        else:
            turtle.setpos(x_init+int(j/3)*x_major-x_major*0.125,y_init-(j%3)*y_major-y_major*(15/32))
    
        if j == 0:
            turtle.write('P1',font=style,align='center')
        if j == 1:
            turtle.write('P3',font=style,align='center')
        if j == 2:
            turtle.write('P10',font=style,align='center')
        if j == 3:
            turtle.write('P8',font=style,align='center')
        if j == 4:
            turtle.write('P9',font=style,align='center')
        if j == 5:
            turtle.write('P11',font=style,align='center')

    for j in range(2):
        draw_rec(x_init*(2/3)+j*0.75*x_major,-(y_init+y_minor),x_major/4,y_major*(0.75))

        for k in range(3):
            draw_rec(x_init*(2/3)+j*0.75*x_major+7+int(k/3)*x_minor,-(y_init+y_minor)-7-(k%3)*y_minor,x_minor*(8/15),y_minor*(5/12))    

        turtle.setpos(x_init*(2/3)+j*0.75*x_major+x_major*0.375-j*2*x_minor,-(y_init+y_minor)-y_major*(15/32))
        if j == 0:
            turtle.write('P13',font=style,align='center')
        else:
            turtle.write('P14',font=style,align='center')
    
    for j in range(2):
        draw_rec(-(y_init+x_minor)+j*(y_init+x_major),x_minor-y_init-y_major+18,y_major*(0.75),x_major/4)

        for k in range(3):
            draw_rec(-(y_init+x_minor)+j*(y_init+x_major)+7+int(k%3)*y_minor,x_minor-y_init-y_major+11,y_minor*(5/12),x_minor*(8/15))    

        turtle.setpos(-(y_init+x_minor)+j*(y_init+x_major)+3/2*y_minor,x_minor-y_init-y_major+x_minor/4+18)
        if j == 0:
            turtle.write('P12',font=style,align='center')
        else:
            turtle.write('P7',font=style,align='center')

def p1_neg():
    turtle.begin_fill()
    draw_rec(x_init+4,y_init-4,52,16)
    turtle.end_fill()
    
def p3_neg():
    turtle.begin_fill()
    draw_rec(x_init+4,y_init-100,52,16)
    turtle.end_fill()
    
def p10_neg():
    turtle.begin_fill()
    draw_rec(x_init+4,y_init-196,52,16)
    turtle.end_fill()
    
def p1_pos():
    turtle.begin_fill()
    draw_rec(x_init+4,y_init-28,52,16)
    turtle.end_fill()
    
def p3_pos():
    turtle.begin_fill()
    draw_rec(x_init+4,y_init-124,52,16)
    turtle.end_fill()
    
def p10_pos():
    turtle.begin_fill()
    draw_rec(x_init+4,y_init-220,52,16)
    turtle.end_fill()

def p1_open():
    turtle.begin_fill()
    draw_rec(x_init+34,y_init-4,22,40)
    turtle.end_fill()

def p3_open():
    turtle.begin_fill()
    draw_rec(x_init+34,y_init-100,22,40)
    turtle.end_fill()

def p10_open():
    turtle.begin_fill()
    draw_rec(x_init+34,y_init-196,22,40)
    turtle.end_fill()

def p8_pos():
    turtle.begin_fill()
    draw_rec(x_init+124,y_init-28,52,16)
    turtle.end_fill()

def p9_pos():
    turtle.begin_fill()
    draw_rec(x_init+124,y_init-124,52,16)
    turtle.end_fill()

def p11_pos():
    turtle.begin_fill()
    draw_rec(x_init+124,y_init-220,52,16)
    turtle.end_fill()

def p8_neg():
    turtle.begin_fill()
    draw_rec(x_init+124,y_init-52,52,16)
    turtle.end_fill()

def p9_neg():
    turtle.begin_fill()
    draw_rec(x_init+124,y_init-148,52,16)
    turtle.end_fill()

def p11_neg():
    turtle.begin_fill()
    draw_rec(x_init+124,y_init-244,52,16)
    turtle.end_fill()

def p8_open():
    turtle.begin_fill()
    draw_rec(x_init+124,y_init-4,22,40)
    turtle.end_fill()

def p9_open():
    turtle.begin_fill()
    draw_rec(x_init+124,y_init-100,22,40)
    turtle.end_fill()

def p11_open():
    turtle.begin_fill()
    draw_rec(x_init+124,y_init-196,22,40)
    turtle.end_fill()

def c_uni():
    turtle.begin_fill()
    draw_rec(x_init+34,y_init-292,22,40)
    turtle.end_fill()
    turtle.begin_fill()
    draw_rec(-(y_init+x_minor)+4,x_minor-y_init-y_major+14,40,22)
    turtle.end_fill()
    
def c_bi():
    turtle.begin_fill()
    draw_rec(x_init+34,y_init-316,22,40)
    turtle.end_fill()
    turtle.begin_fill()
    draw_rec(-(y_init+x_minor)+28,x_minor-y_init-y_major+14,40,22)
    turtle.end_fill()

def v_uni():
    turtle.begin_fill()
    draw_rec(x_init+124,y_init-292,22,40)
    turtle.end_fill()
    turtle.begin_fill()
    draw_rec(-(y_init+x_minor)+280,x_minor-y_init-y_major+14,40,22)
    turtle.end_fill()

def v_bi():
    turtle.begin_fill()
    draw_rec(x_init+124,y_init-316,22,40)
    turtle.end_fill()
    turtle.begin_fill()
    draw_rec(-(y_init+x_minor)+256,x_minor-y_init-y_major+14,40,22)
    turtle.end_fill()

def isint(x,lower,upper):
    try:
        val = int(x)
        if upper == 'x':
            if val >= lower:
                return 0
        else:
            if val >= lower and val <= upper:
                return 0
    except:    
        return 2

def is_y_or_n(char):
    if char == 'Y' or char == 'y' or char == 'N' or char == 'n':
        return 0
    else:
        return 2

# ------------------------------------------------------------------------------------------
# Program starts here
print("#------------------#")
print("| GENERAL REMINDER |")
print("#------------------#")
print("\nIt is important to make sure that the board will not be used for inputs that exceed the board configuration capability. For instance, even if the board can handle up to 80V but the jumper configuration is set to the 16V config, then the board should not be used to sense voltages above 16V. The node polarities should also be well noted when using the unipolar and unidirectional mode. It is advised that no inputs be fed to the board until it is properly configured. Disconnect any input attached to the board when changing jumper configurations.\n")
print("#------------------#")
print("| !!!!!!!!!!!!!!!! |")
print("#------------------#")

try:
    record = open("record.txt", "r")
    rec_value = []
    new = 0

    line_count = 0
    for line in record:
        line_count = line_count + 1
    record.close()

    if line_count < 8:
        print("Some contents of the session record file seem to have been removed. Starting new session...")
        new = 1
    else:
        line_count = 0
        record = open("record.txt", "r")
        for line in record:
            if int(line_count/7) == 0:
                rec_value.append(line.strip())
            line_count = line_count + 1
    
        new = new + isint(rec_value[0],1,2)
        new = new + isint(rec_value[1],1,5)
        new = new + isint(rec_value[2],1,2)
        new = new + is_y_or_n(rec_value[3])
        new = new + is_y_or_n(rec_value[4])
        if new == 0 and (rec_value[4] == 'Y' or rec_value[4] == 'y'):
            new = new + isint(rec_value[6],5,'x')
        new = new + isint(rec_value[5],1,5)
    
except:
    print("No session record found. Starting new session...\n\n")
    new = 1

if new == 0:
    print("\nSession record detected.\n")
    rating = "Maximum rating: "
    if rec_value[0] == '1':
        if rec_value[1] == '1':
            rating = rating + "16V , "
        elif rec_value[1] == '2':
            rating = rating + "20V , "
        elif rec_value[1] == '3':
            rating = rating + "27V , "
        elif rec_value[1] == '4':
            rating = rating + "40V , "
        elif rec_value[1] == '5':
            rating = rating + "80V , "
    elif rec_value[0] == '2':
        if rec_value[1] == '1':
            rating = rating + "+/-8V , "
        elif rec_value[1] == '2':
            rating = rating + "+/-10V , "
        elif rec_value[1] == '3':
            rating = rating + "+/-13.5V , "
        elif rec_value[1] == '4':
            rating = rating + "+/-20V , "
        elif rec_value[1] == '5':
            rating = rating + "+/-40V , "
    if rec_value[2] == '1':
        rating = rating + "20A"
    elif rec_value[2] == '2':
        rating = rating + "+/-10A"
    print(rating)

    if rec_value[3] == 'Y' or rec_value == 'y':
        print("Data logging enabled")
    else:
        print("Data logging disabled")
    
    if rec_value[4] == 'Y' or rec_value == 'y':
        print("Plot enabled, latest " + rec_value[6] + " samples are displayed")
    else:
        print("Plot disabled")
    
    print("Data sampling rate: " + rec_value[5] + " samples per second")
    print("\nUse same setting as previous session? (1 or 2)\n\t(1) Yes\n\t(2) No")
    while True:
        placeholder = input(">> ")
        try:
            response = int(placeholder)
            if response==1:
                new = 0
                break
            elif response==2:
                new = 1
                break
            else:
                print("Invalid response. Please choose between options 1 or 2\n")
        
        except:
            print("Invalid response. Please choose between options 1 or 2\n")

elif new == 2:
    print("Some contents of the session record file seem to have been modified. Starting new session...")

new_record = ["DO NOT EDIT THE CONTENTS OF THIS FILE"]

v_text = "Voltage measurement: "
if new != 0:
    draw_jumpers()
    print("\nThe following prompts will help you setup the jumper configuration of the CN0548 board depending on your expected inputs. A map of the board jumpers should have appeared in another window. This map will be updated as you provide responses to the different prompts.\n\n")

    print("----- Setting up the hardware for LT1997-2 -----\n\n-Step 1 of 2: Type of voltage measurement-\n\t(1) Unipolar: The board expects non-negative readings allowing it to measure a wider range of positive voltages. Software is configured to read from 0 to Vmax.\n\t(2) Bipolar: The board expects both positive and negative readings, effective range is divided equally. Software is configured to read from -Vmax/2 to Vmax/2.\n")

while True:
    if new != 0:
        placeholder = input("Type of measurement (1 or 2): ")
    else:
        placeholder = rec_value[0]
    try:
        v_type = int(placeholder)
        if v_type == 1:
            if new != 0:
                v_uni()
                v_text = v_text + "unipolar\t (Effective range: "
            break
        elif v_type == 2:
            if new != 0:
                v_bi()
                v_text = v_text + "bipolar\t (Effective range: "
            break
        else:
            print("Invalid response. Please choose between options 1 or 2\n")   
    except:
        print("Invalid response. Please choose between options 1 or 2\n")
new_record.append(v_type)

if new != 0:
    print("\n\n-Step 2 of 2: Voltage Range-\nThe maximum voltage range is 80V but the board can be configured to a more refined voltage range in order to produce higher resolution readings. Select your desired Vmax:\n\t(1) 16V\n\t(2) 20V\n\t(3) 27V\n\t(4) 40V\n\t(5) 80V\n")
while True:
    if new != 0:
        placeholder = input("Range (1 to 5): ")
    else:
        placeholder = rec_value[1]
    try:
        v_max = int(placeholder)
        if v_max == 1:
            if new != 0:
                p1_open()
                p3_open()
                p10_pos()
                p8_open()
                p9_open()
                p11_neg()
            if v_type==1:
                title_text = "CN0548 Maximum Rating: 16V "
                v_text = v_text + "0 to 16V)"
            else:
                v_text = v_text + "-8V to 8V)"
                title_text = "CN0548 Maximum Rating: +/-8V "
            v_gain = 0.004
            break
        elif v_max == 2:
            if new != 0:
                p1_open()
                p3_pos()
                p10_open()
                p8_open()
                p9_neg()
                p11_pos()
            if v_type==1:
                v_text = v_text + "0 to 20V)"
                title_text = "CN0548 Maximum Rating: 20V "
            else:
                v_text = v_text + "-10V to 10V)"
                title_text = "CN0548 Maximum Rating: +/-10V "
            v_gain = 0.005
            break
        elif v_max == 3:
            if new != 0:
                p1_neg()
                p3_open()
                p10_pos()
                p8_pos()
                p9_open()
                p11_neg()
            if v_type==1:
                v_text = v_text + "0 to 27V)"
                title_text = "CN0548 Maximum Rating: 27V "
            else:
                v_text = v_text + "-13.5V to 13.5V)"
                title_text = "CN0548 Maximum Rating: +/-13.5V "
            v_gain = (1/150)
            break
        elif v_max == 4:
            if new != 0:
                p1_pos()
                p3_open()
                p10_open()
                p8_neg()
                p9_open()
                p11_open()
            if v_type==1:
                v_text = v_text + "0 to 40V)"
                title_text = "CN0548 Maximum Rating: 40V "
            else:
                v_text = v_text + "-20V to 20V)"
                title_text = "CN0548 Maximum Rating: +/-20V "
            v_gain = 0.01
            break
        elif v_max == 5:
            if new != 0:
                p1_open()
                p3_neg()
                p10_pos()
                p8_open()
                p9_pos()
                p11_neg()
            if v_type==1:
                v_text = v_text + "0 to 80V)"
                title_text = "CN0548 Maximum Rating: 80V "
            else:
                v_text = v_text + "-40V to 40V)"
                title_text = "CN0548 Maximum Rating: +/-40V "
            v_gain = 0.02
            break
        else:
            print("Invalid response. Please choose between options 1 to 5\n")   
    except:
        print("Invalid response. Please choose between options 1 or 2\n")
new_record.append(v_max)

if new != 0:
    turtle.setpos(0,190)
    turtle.write(v_text,font=('Arial',10,'bold'),align='center')

i_gain = 5
c_text = "Current measurement: "
if new != 0:
    print("\n\n----- Setting up the hardware for AD8410 -----\n-Step 1 of 1: Type of measurement-\n\t(1) Unidirectional: The board expects positive current flow only. Board is configured to handle 0 to 20A.\n\t(2) Bidirectional: The board expects both positive and negative current flow. Board is configured to handle -10A to 10A.\n")
while True:
    if new != 0:
        placeholder = input("Type of current measurement (1 or 2): ")
    else:
        placeholder = rec_value[2]
    try:
        c_type = int(placeholder)
        if c_type == 1:
            if new != 0:
                c_uni()
                c_text = c_text + "unidirectional\t (Effective range: 0 to 20A)"
            title_text = title_text + ", 20A"
            break
        elif c_type == 2:
            if new != 0:
                c_bi()
                c_text = c_text + "bidirectional\t (Effective range: -10A to 10A)"
            title_text = title_text + ", +/-10A"
            break
        else:
            print("Invalid response. Please choose between options 1 or 2\n")   
    except:
        print("Invalid response. Please choose between options 1 or 2\n")
new_record.append(c_type)

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
import numpy as np
import adi

global ad7799
print("\n\n\n\n-Connection setup-\n")
while True:
    port = input('Input Serial line (e.g. if ADICUP3029 is connected to COM7, input \'COM7\' )\nSerial line: ')

    try:
        context = "serial:" + port + ",115200"
        ad7799 = adi.ad7799(uri=context)
        print("\nCN0548 board detected.\nBegin setup query:\n")
        break
    except:
        print("Port not found\n")

global log
while True:
    if new != 0:
        log = input('Log data? (Y/N): ')
    else:
        log = rec_value[3]
    if log == 'Y' or log == 'N' or log == 'y' or log == 'n':
        break
    else:
        print("'Y' or 'N' only")
new_record.append(log)

if log == 'Y' or log == 'y':
    global filename
    dt_now = datetime.now()
    dt_format = dt_now.strftime("%d-%m-%Y_%H-%M")
    filename = 'LVHC_'+dt_format+'.csv'

global fs
while True:
    if new != 0:
        fs = input('\nSamples per second? (1-5): ')
    else:
        fs = rec_value[5]
    try:
        fs = int(fs)
    except:
        print('Please input an integer within the specified range')
        continue
    if fs < 1 or fs > 5:
        print('Please input an integer within the specified range')
    else:
        break
new_record.append(fs)

while True:
    if new != 0:
        en = input('\nEnable plot? (Y/N): ')
    else:
        en = rec_value[4]
    if en == 'Y' or en == 'N' or en == 'y' or en == 'n':
        break
    else:
        print("'Y' or 'N' only")
new_record.append(en)

if en == 'Y' or en == 'y':
    enable_plot = True
else:
    enable_plot = False

if enable_plot:
    global samples
    while True: 
        if new != 0:
            samples = input('\nInput number of samples to retain within the plot (>=5).\n***Note that this can affect the sampling rate of the device\nSamples to retain: ')
        else:
            samples = rec_value[6]
        try:
            samples = int(samples)
        except:
            print('Please input an integer within the specified range')
            continue
        if samples < 5:
            print('Please input an integer within the specified range')
        else:
            break
    new_record.append(samples)

    # Create figure for plotting
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    xs: List[float] = []
    ys: List[float] = []
    for i in range(samples):
        xs.append(0)
        ys.append(0)

    def animate(i,volt, curr):      # function for animation
    # Continuously adding streams of x and y to lists
        v_reading = round(v_gain*ad7799.channel[2].value,3) # get new voltage reading (mV)
        i_reading = round(i_gain*ad7799.channel[0].value,3) # get new current reading
        flag = len(volt)
        volt.append(v_reading)  
        curr.append(i_reading)  
        print('Voltage reading: ' + str(v_reading) + '\t\t\t' + 'Current reading: ' + str(i_reading))
        if log == 'Y' or log == 'y':
            output = open(filename,'a')
            output.write('Voltage reading:,' + str(v_reading) + ',' + 'Current reading:,' + str(i_reading)+'\n')
            output.close()  

    # number of recent samples to be retained
        volt = volt[-samples:]
        curr = curr[-samples:]
    #initialize/clear
        lower = 0
        upper = 0
    # Plot config
        ax1.clear()
        minimum = min(volt)
        if minimum >= 0:
            lower = int(minimum)
        else:
            lower = int(minimum) - 1
        maximum = max(volt)
        if maximum >= 0:
            upper = int(maximum)
        else:
            upper = int(maximum) - 1
        ax1.set_ylim([lower,(upper+1)])
        color = 'tab:orange'
        ax1.plot(volt, label="Voltage Reading", linewidth=2.0,color=color)
        ax1.set_ylabel("Volts (V)",color=color)
        ax1.tick_params(axis="x", which="both", bottom=True, top=False, labelbottom=False)
        ax1.legend(bbox_to_anchor=[0.5, -0.1], ncol=2, loc="upper left", frameon=False)
        
        ax2.clear()
        minimum = min(curr)
        if minimum >= 0:
            lower = int(minimum/50)
        else:
            lower = int(minimum/50) - 1
        maximum = max(curr)
        if maximum >= 0:
            upper = int(maximum/50)
        else:
            upper = int(maximum/50) - 1
        ax2.set_ylim([lower*50,(upper+1)*50])
        color = 'tab:blue'
        ax2.plot(curr, label="Current Reading", linewidth=2.0,color=color)
        ax2.set_ylabel("Milliamperes (mA)",color=color)
        ax2.tick_params(axis="x", which="both", bottom=True, top=False, labelbottom=True)
        ax2.legend(bbox_to_anchor=[0.5, -0.1], ncol=2, loc="upper right", frameon=False)
        
        # plt.title("Voltage and Current Sensing of CN0548", fontweight="bold")
        plt.title(title_text, fontweight="bold")
        plt.subplots_adjust(bottom=0.30)

    print(new_record)
    record = open("record.txt","w")
    for i in range(7):
        record.write(str(new_record[i+1])+"\n")
    record.write(new_record[0])
    record.close()

    # begin animation
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=(1000/fs))
    plt.show()
    
else:
    new_record.append('-')
    record = open("record.txt","w")
    for i in range(7):
        record.write(str(new_record[i+1])+"\n")
    record.write(new_record[0])
    record.close()

    print("Voltage reading is in terms of volts (V) and current reading is in terms of milliamperes (mA).")
    while True:
        v_reading = round(v_gain*ad7799.channel[2].value,3) # get new voltage reading
        i_reading = round(i_gain*ad7799.channel[0].value,3) # get new current reading  
        print('Voltage reading: ' + str(v_reading) + '\t\t\t' + 'Current reading: ' + str(i_reading) )
        time.sleep(1/fs)
        if log == 'Y' or log == 'y':
            output = open(filename,'a')
            output.write('Voltage reading:,' + str(v_reading) + ',' + 'Current reading:,' + str(i_reading)+'\n')
            output.close()

del ad7799

input("Press 'enter' key to exit program")
