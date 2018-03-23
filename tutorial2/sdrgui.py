"""
Sound Card Test
"""
import tkinter

class MainWindow:

    def __init__(self):
        self.top = tkinter.Tk()
        self.top.title("SDR Test Tool")
        self.canvas = LineChart(self.top, "white", 250, 300)
        self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    def start(self):
        self.top.mainloop()

    def get_ratio_position(self, min, max, value, dimension):
        if (max == min):
            return 0
        ratio = (max - value) / (max - min)
        position = int(dimension * ratio)
        return position
    
    def setData(self, data):
        self.canvas.setData(data)

class LineChart(tkinter.Canvas):

    def __init__(self, parent, background, h, w):
        super().__init__(parent, bg=background, height=h, width=w)
        self.BORDER = 10
        self.y_axis = self.create_line(self.BORDER, self.BORDER, self.BORDER, self.BORDER)
        self.x_axis = self.create_line(self.BORDER, 0, self.BORDER, self.BORDER)
        self.lines = []
        for n in range(0, 255):
            self.lines.append(self.create_line(0,0,0,0))

    def get_ratio_position(self, min, max, value, dimension):
        if (max == min):
            return 0
        ratio = (max - value) / (max - min)
        position = int(dimension * ratio)
        return position
    
    def setData(self, data):
        maxValue = -99999
        minValue = 99999
        height = self.winfo_height()
        width = self.winfo_width()*2
        
        for n in data:
            if (n > maxValue):
                maxValue = n
            if (n < minValue):
                minValue = n
                
        self.coords(self.y_axis, self.BORDER, self.BORDER, self.BORDER, height-self.BORDER)
        
        #The zero point is the middle of the canvas.  We have aqn equal BORDER top and bottom.
        zeroPoint = height/2
        self.coords(self.x_axis, self.BORDER, zeroPoint, width-self.BORDER, zeroPoint)

        step = int(len(data) / 16) # plot 16 labels
        lastx = self.BORDER
        lasty = zeroPoint

        p = 0
        for n in data:
            # We have values from -1 to 1.  We want to scale them so that +1 is the top of the 
            # TkCanvas and -1 is the bottom.  The top is at x position BORDER.  The bottom is at 
            # X position getHeight()-BORDER
            y = self.get_ratio_position(minValue, maxValue, n, height-self.BORDER*2)
            x = self.get_ratio_position(len(data),0,p,width-self.BORDER*2)
            x = x + self.BORDER
            self.coords(self.lines[p], lastx, lasty, x, y)
            lastx = x
            lasty = y
            p=p+1
            #if (n % step == 0):
            #g2.drawString(""+n, x, zeroPoint+15)

        
