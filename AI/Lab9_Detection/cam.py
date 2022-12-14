from matplotlib import pyplot as plt
from cv2 import VideoCapture, imread, imshow, waitKey, destroyAllWindows, CascadeClassifier, rectangle, putText, FONT_HERSHEY_SIMPLEX, LINE_4


classifier = CascadeClassifier('haarcascade_smile.xml')
# perform face detection


# define a video capture object
vid = VideoCapture(0)
while(True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    bboxes = classifier.detectMultiScale(frame)
    # Display the resulting frame
    for box in bboxes:
        # extract
        x, y, width, height = box
        x2, y2 = x + width, y + height
        if width < 200 or height < 300:
            putText(frame, 'Move forward', (50, 50),
                    FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, LINE_4)
        elif width > 300 or height > 350:
            putText(frame, 'Move Backward', (50, 50),
                    FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, LINE_4)
        else:
            putText(frame, '', (50, 50), FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 255), 2, LINE_4)
        # draw a rectangle over the pixels
        rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 1)

    imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
destroyAllWindows()



/*
from matplotlib import pyplot as plt
from cv2 import VideoCapture, imread, imshow, waitKey, destroyAllWindows, CascadeClassifier, rectangle, putText, FONT_HERSHEY_SIMPLEX, LINE_4
from mtcnn.mtcnn import MTCNN
from matplotlib.patches import Rectangle


detector = MTCNN()


# define a video capture object
vid = VideoCapture(0)

while True:
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    faces = detector.detect_faces(frame)
    ax = plt.gca()
    for result in faces:
        # get coordinates
        x, y, width, height = result['box']
        # create the shape
        rect = Rectangle((x, y), width, height, fill=False, color='red')
        # draw the box
        ax.add_patch(rect)
        # show the plot
        rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 1)
    imshow('frame', frame)

# After the loop release the cap object
vid.release()
# Destroy all the windows
destroyAllWindows()

*/
