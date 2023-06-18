import tkinter as tk
from PIL import ImageTk, Image
'''
!   /   --------- -------\   ---------   ---------\  
!  /     !     !  !       \   !     !    !         !
!/       !-----!  !        !  !-----!    !......../
!  \     !     !  !       /   !     !    !      \
!   \    !     !  !------/    !     !    !       \
'''
def close_splash():
    window.destroy()

window = tk.Tk()
window.title("Splash Screen")
window.geometry("400x300")

# you can change onli the path of your image but please don't remove the prefix r 
image_path = r"C:\Users\ZenBook\Desktop\dual_studium\verien.png"
image = Image.open(image_path)
image = image.resize((400, 300))  # Adjust the size of the image to fit the window if needed
background_image = ImageTk.PhotoImage(image)

# Create a Label widget to display the image
background_label = tk.Label(window, image=background_image)
background_label.pack()

duration = 6000
window.after(duration, close_splash)

# Retain the reference to the image globally
window.image = background_image

window.mainloop()
