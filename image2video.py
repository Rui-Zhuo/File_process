import os
import cv2
from PIL import Image

def image2video(image_dir, video_path):
    '''
    This function merges images into a video. 
    Input 
    video_path: the path of the video to be splited.
    image_dir:  the directory to save the splited images.
    '''
    # Getting image filenames
    image_names = os.listdir(image_dir)
    # Setting the writing format
    fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
    # Setting frames rate
    fps = 3
    
    # Initializing
    image = Image.open(image_dir + image_names[0])
    video_writer = cv2.VideoWriter(video_path, fourcc, fps, image.size)
    # Iterating through images
    for image_name in image_names:
        im = cv2.imread(os.path.join(image_dir, image_name))
        video_writer.write(im)
        print('Writing ', image_name, ' Done!')
    
    # Releasing video
    video_writer.release()
    print('Converting completed!')

image_dir = 'E:/Research/Work/202405_solar_storm/winding/ARTop/run_3/distribution/wind/'
video_path = 'E:/Research/Work/202405_solar_storm/winding/ARTop/run_3/distribution/wind.mp4'

image2video(image_dir, video_path)