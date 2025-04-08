from graphics import GraphWin, Rectangle, Point
import time

CANVAS_WIDTH: int = 400
CANVAS_HEIGHT: int = 400

CELL_SIZE: int = 40
ERASER_SIZE: int = 20

def erase_objects(win, eraser, cells):
    """Erase objects in contact with the eraser"""
    eraser_left_x = eraser.getP1().getX()
    eraser_top_y = eraser.getP1().getY()
    eraser_right_x = eraser_left_x + ERASER_SIZE
    eraser_bottom_y = eraser_top_y + ERASER_SIZE
    
    # Check each cell in the list to see if it overlaps with the eraser
    for cell in cells:
        p1 = cell.getP1()  # Top-left corner
        p2 = cell.getP2()  # Bottom-right corner
        x1, y1 = p1.getX(), p1.getY()
        x2, y2 = p2.getX(), p2.getY()
        
        # Check if the cell overlaps with the eraser
        if (x1 < eraser_right_x and x2 > eraser_left_x and y1 < eraser_bottom_y and y2 > eraser_top_y):
            cell.setFill('white')  # Change the color to white (erased)

def main():
    win = GraphWin("Canvas", CANVAS_WIDTH, CANVAS_HEIGHT)
    
    num_rows = CANVAS_HEIGHT // CELL_SIZE  # Figure out how many rows of cells we need
    num_cols = CANVAS_WIDTH // CELL_SIZE   # Figure out how many columns of cells we need
    
    cells = []  # List to track the created cells
    
    # Make a grid of squares based on the number of rows and columns.
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE   # The right coordinate of the cell
            bottom_y = top_y + CELL_SIZE   # The bottom coordinate of the cell
            
            # Create a single cell in the grid
            cell = Rectangle(Point(left_x, top_y), Point(right_x, bottom_y))
            cell.setFill('blue')
            cell.draw(win)
            
            # Add the created cell to the list
            cells.append(cell)
    
    win.getMouse()  # Wait for the user to click before creating the eraser
    
    last_click = win.getMouse()  # Get the starting location for the eraser
    last_click_x, last_click_y = last_click.getX(), last_click.getY()
    
    # Create our eraser
    eraser = Rectangle(Point(last_click_x, last_click_y), Point(last_click_x + ERASER_SIZE, last_click_y + ERASER_SIZE))
    eraser.setFill('pink')
    eraser.draw(win)
    
    # Move the eraser, and erase what it's touching
    while True:
        # Get where our mouse is and move the eraser to there
        mouse_click = win.getMouse()  # Get the mouse click position for the new eraser position
        mouse_x, mouse_y = mouse_click.getX(), mouse_click.getY()
        eraser.move(mouse_x - last_click_x, mouse_y - last_click_y)
        last_click_x, last_click_y = mouse_x, mouse_y
        
        # Erase anything touching the eraser
        erase_objects(win, eraser, cells) 
        
        time.sleep(0.05)

if __name__ == '__main__':
    main()
