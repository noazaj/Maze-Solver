from tkinter import Tk, BOTH, Canvas

class Window:
    """This class will be used to create the GUI or window for the user to see. 
    It will render the maze and the operations done inside of the maze."""

    def __init__(self, width, height):
        # Use the width and height parameters to create the pixel window
        self.width = width
        self.height = height

        # Create an instance of the Tk and set it to root and have it's
        # title created
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        # Create a Canvas for the maze and have it saved. Also, pack the canvas so 
        # it is ready to be drawn 
        self.canvas = Canvas()
        self.canvas.pack

        # Create a data member to keep track of the running window. 
        # Initially set it to False
        self.running = False
        
    def redraw(self):
        # self.root.update_idletasks()
        self.__root.update()
        
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
            
    def close(self):
        self.running = False
        
        

def main():
    win = Window(800, 800)
    win.wait_for_close()


if __name__ == '__main__':
    main()