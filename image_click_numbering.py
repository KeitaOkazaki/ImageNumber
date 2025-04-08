import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont

class ImageApp:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Image Click Numbering")
        self.root.geometry("600x700")
        
        self.image = Image.open(image_path)
        self.tk_image = ImageTk.PhotoImage(self.image)
        
        self.canvas = tk.Canvas(self.root, width=self.image.width, height=self.image.height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
        
        self.canvas.bind("<Button-1>", self.add_number)
        
        self.number = 1
        self.draw = ImageDraw.Draw(self.image)
        
        try:
            self.font = ImageFont.truetype("Arial.ttf", 30)
        except IOError:
            self.font = ImageFont.load_default()

    def add_number(self, event):
        x, y = event.x, event.y
        r = 15  # Radius of the circle
        
        # Draw circle and text on the Tkinter canvas
        self.canvas.create_oval(x-r, y-r, x+r, y+r, outline="red", width=1, fill="red")
        self.canvas.create_text(x, y, text=str(self.number), fill="white", font=("Arial", 30))

        # Draw circle and text on the PIL image
        self.draw.ellipse((x-r, y-r, x+r, y+r), outline="red", width=1, fill="red")
        
        # Center text in the circle
        self.draw.text((x, y), str(self.number), fill="white", font=self.font, anchor="mm")

        self.number += 1

    def save_image(self, output_path):
        self.image.save(output_path, format="PNG")
        
if __name__ == "__main__":
    root = tk.Tk()
    
    # 編集したい画像のpathを入力
    app = ImageApp(root, "/Users/okazakikeita/Desktop/imageNumber/resize_image/resize_image.png")
    
    def on_closing():
        output_path = "/Users/okazakikeita/Desktop/imageNumber/output_images/output_image.png"
        app.save_image(output_path)
        img = Image.open(output_path)
        root.destroy()
        img.show()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()