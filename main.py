import utime
import machine
#
ledgrün = [
machine.Pin(4, machine.Pin.OUT),
machine.Pin(5, machine.Pin.OUT),
machine.Pin(6, machine.Pin.OUT),
machine.Pin(7, machine.Pin.OUT),
machine.Pin(8, machine.Pin.OUT),
machine.Pin(9, machine.Pin.OUT),
machine.Pin(10, machine.Pin.OUT),
machine.Pin(11, machine.Pin.OUT),
machine.Pin(12, machine.Pin.OUT),
machine.Pin(13, machine.Pin.OUT),
machine.Pin(14, machine.Pin.OUT),
machine.Pin(15, machine.Pin.OUT)
]

ledrot = [
machine.Pin(0, machine.Pin.OUT),
machine.Pin(1, machine.Pin.OUT),
machine.Pin(2, machine.Pin.OUT),
machine.Pin(3, machine.Pin.OUT),
machine.Pin(26, machine.Pin.OUT),
machine.Pin(22, machine.Pin.OUT),
machine.Pin(21, machine.Pin.OUT),
machine.Pin(20, machine.Pin.OUT),
machine.Pin(19, machine.Pin.OUT),
machine.Pin(18, machine.Pin.OUT),
machine.Pin(17, machine.Pin.OUT),
machine.Pin(16, machine.Pin.OUT)
]
#
def getled(c,num,val) :
    import machine
    global ledrot
    global ledgrün
    if c == "r" :
        led = ledrot [num]
    if c == "g" :
        led = ledgrün [num]
    led.value(val)
    return ""
    

def ledscript(num,leds,c) :
    
    for i in range(leds) :
        if i == num :
            getled(c,i,1)
        else :
            getled(c,i,0)

def ledscript2(num,leds,c) :
    if y_value == 65535 or y_value > 65535 :
        ledscript(num,leds,"g")
        getled(c,num,1)
        utime.sleep(1)
        getled(c,num,0)
        utime.sleep(1)
        getled(c,num,1)
        return 
#
led = 0
check_led = 0
ledhallo = 0
#
x_axis = machine.ADC(27)
y_axis = machine.ADC(28)
#


utime.sleep(0.1) # Wait for USB to become ready
for i in range(len(ledrot)):
    ledhallo = ledrot[i]
    ledhallo.value(1)
    utime.sleep(1)
for i in range(len(ledgrün)):
    ledhallo = ledgrün[i]
    ledhallo.value(1)
    utime.sleep(1)
for i in range(len(ledgrün)):
    ledhallo = ledgrün[i]
    ledhallo.value(0)


while True :
    x_value = 66035 - x_axis.read_u16()
    y_value = 66035 - y_axis.read_u16()
    print("y:",y_value,"x :",x_value,"led :",led)
    utime.sleep(0.2)
    if x_value == 65335 or x_value > 65335 :
        led = (led-1)
        print("y:",y_value,"x :",x_value,"led :",led)


    if x_value == 500 or x_value < 500 :
        led += 1
        x_value = x_axis.read_u16()
        print("y:",y_value,"x :",x_value,"led :",led)
        
    if led < 0 :
        led = 11
    if led > 11 :
        led = 0
    #STARD LED
    ledscript(led,len(ledrot),"r")
    ledscript2(led,len(ledrot),"r")
    
    
    if check_led == led :
        print("check True")
        check_led = led
    else :
        
        getled("g",0,0)
        getled("g",1,0)
        getled("g",2,0)
        getled("g",3,0)
        getled("g",4,0)
        getled("g",5,0)
        getled("g",6,0)
        getled("g",7,0)
        getled("g",8,0)
        getled("g",9,0)
        getled("g",10,0)
        getled("g",11,0)
        check_led = led

    

    while  x_value == 65335 or x_value > 65335 or  x_value == 500 or x_value < 500 :
            print("waiting")
            utime.sleep(0.2)
            x_value = x_axis.read_u16()
            y_value = y_axis.read_u16()