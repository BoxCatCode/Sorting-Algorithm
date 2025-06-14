import tkinter as tk
import random


n = 49
root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

class Rect():
    def __init__(self , x, rand_num):
            self.x = x
            self.rand_num = rand_num
            color = "gray25"
            self.color = color
            self.rect = canvas.create_rectangle(    
                x, #x1
                1000 - rand_num, #y1
                x+10, #x2 
                1000, #y2
                fill=self.color,
                outline="black",
                tags="my_rect"
            )
    def change_color(self, new_color):
        canvas.itemconfig(self.rect, fill=new_color)
        self.color = new_color
        

    def move_to(self, new_x):
        dx = new_x - self.x
        canvas.move(self.rect, dx, 0)
        self.x = new_x

def create_data():
    canvas.delete("my_rect")
    rectangles = []
    for i in range(n):
        x = (i+1) * 20
        rand_num = random.randint(200, 800)  # Generate a random height for the rectangle
        rectangles.append(Rect(x,rand_num))  # Append the rectangle's position and height to the list
        
    return rectangles


def createArr():
    global arr  # Make sure we overwrite the outer arr
    arr = create_data()        # Regenerate rectangles
    


##############################################################################################################################
def insertionSort(i=1):
    if i >= len(arr):
        change_color_all()
        return
    
    key_rect = arr[i]         
    key_height = key_rect.rand_num
    
    j = i - 1
    
    
    while j >= 0 and arr[j].rand_num > key_height:
        
        arr[j + 1] = arr[j]
        
        arr[j + 1].move_to((j + 2) * 20)
        
        j -= 1

    
    arr[j + 1] = key_rect
    
    arr[j + 1].move_to((j + 2) * 20)
    
    
    root.after(100, insertionSort, i + 1)
    
##############################################################################################################################

def selectionSort(i=0):
    n = len(arr)
    if i >= n - 1:
        change_color_all()
        return

    min_idx = i
    for j in range(i + 1, n):
        
        
        if arr[j].rand_num < arr[min_idx].rand_num:
            
            
            min_idx = j
    if min_idx != i:
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        arr[i].move_to((i + 1) * 20)
        
        arr[min_idx].move_to((min_idx + 1) * 20)
        
    root.after(100, selectionSort, i + 1)
    
def change_color_all(i = 0):
    if i >= n:
        return
    
    arr[i].change_color("lightgreen")
    root.after(10, change_color_all, i+1)



##############################################################################################################################

def bubbleSort(i=0, j=0):
    if i >= n - 1:
        change_color_all()
        return

    if j < n - i - 1:
        if arr[j].rand_num > arr[j+1].rand_num:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            arr[j].move_to((j+1) * 20)
            arr[j+1].move_to((j+2) * 20)
        root.after(10, bubbleSort, i, j+1)
    else:
        root.after(10, bubbleSort, i+1, 0)


##############################################################################################################################
createArr()
button = tk.Button(root, 
          text="Redo", 
          command=createArr,
          width=11,
          height=1,
          bg="gray",
          fg="black",
          font=("Arial", 12, "bold")
)
button.place(x=10, y=10)
button = tk.Button(root, 
          text="Insertion Sort", 
          command=insertionSort,
          width=11,
          height=1,
          bg="gray",
          fg="black",
          font=("Arial", 12, "bold")
)
button.place(x=140, y=10)
button = tk.Button(root, 
          text="Selection Sort", 
          command=selectionSort,
          width=11,
          height=1,
          bg="gray",
          fg="black",
          font=("Arial", 12, "bold")
)
button.place(x=270, y=10)
button = tk.Button(root, 
          text="Bubble Sort", 
          command=bubbleSort,
          width=11,
          height=1,
          bg="gray",
          fg="black",
          font=("Arial", 12, "bold")
)
button.place(x=400, y=10)
canvas.create_rectangle(0, 0, 1100, 50, fill="lightgray", outline="black")


canvas.create_text(500, 120, text="Sorting Visualizer!", font=("Times New Roman", 50), fill="black")



##############################################################################################################################

root.mainloop()