# Program To Read video 
# and Extract Frames 
import cv2
from src import Frame
from PIL import Image

#List of objects that holds the data of each frame
FrameList = []


# Function to extract frames 
def FrameCapture(path): 
      
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
  
        # Saves the frames with frame-count 
        #cv2.imwrite("frame%d.jpg" % count, image) 

        #Creates an object at 
        FrameList.append(Frame.Frame(image))

        count += 1
  

# Driver Code 
if __name__ == '__main__': 
  
    # Calling the function 
    FrameCapture(r"C:\Users\chase\Desktop\TestVideoDataCapture\Sample.mp4") 

    
