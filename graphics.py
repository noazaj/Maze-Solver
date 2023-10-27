from tkinter import Tk, BOTH, Canvas

class Window:
    """This class will be used to create the GUI or window for the user to see. 
    It will render the maze and the operations done inside of the maze."""

    def __init__(self, width, height) -> None:
        
        # Create an instance of the Tk and set it to root and have it's
        # title created
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        # Create a Canvas for the maze and have it saved. Also, pack the canvas so 
        # it is ready to be drawn 
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)

        # Create a data member to keep track of the running window. 
        # Initially set it to False
        self.__running = False
        
    def redraw(self) -> None:
        """Constantly update the rendering of the window gui"""
        self.__root.update_idletasks()
        self.__root.update()
        
    def wait_for_close(self) -> None:
        """Will continously run while the condition is True. Once the close() method
        is called, this method will stop."""
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closing...")
            
    def close(self) -> None:
        """Used to close the gui window. It will completely stop the program from running."""
        self.__running = False
        
    def draw_line(self, line, fill_color="black") -> None:
        """This will draw the line on the window canvas"""
        line.draw(self.__canvas, fill_color)
        
class Point:
    """Class used to store the x and y coordinates of a point"""
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
class Line:
    """Class will take two points as parameters. These points will come from the Point class.
    These points will be stored as data members."""
    
    def __init__(self, point1, point2) -> None:
        
        # Save the two points as data members
        self.p1 = point1
        self.p2 = point2
        
    def draw(self, canvas, fill_color="black") -> None:
        """Used to draw a line within the Canvas. It will create a line with a designated
        fill color."""
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)