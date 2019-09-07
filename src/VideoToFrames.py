# Program To Read video 
# and Extract Frames 
import cv2
from PIL import Image
import Frame

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

        #Creates an object for every frame with the data of that frame
        FrameList.append(Frame.Frame(image))

        count += 1

def embedData(hexaValue, frame):

    for i in range(64):
        frame.FrameData[i][0][0] = int(hexaValue[i], 16)

  
def pullData(frame):

    output = ''

    for i in range(64):
        output += str(frame.FrameData[i][0][0])

    return str(hex(int(output)))


# Driver Code 
if __name__ == '__main__': 
  
    # Calling the function 
    FrameCapture(r"C:\Users\chase\Desktop\TestVideoDataCapture\Sample.mp4") 

    embedData('6a48f82d8e828ce82b826a48f82d8e828ce82b826a48f82d8e828ce82b821234',FrameList[0])

    #print(pullData(FrameList[0]))

    #print(pullData(FrameList[0]))

    #print(FrameList[0].FrameData[0][0])


    #print(pullData(FrameList[0]))

    #img = Image.fromarray(FrameList[0].FrameData)
    #img.save('firstFrame.png')

    
