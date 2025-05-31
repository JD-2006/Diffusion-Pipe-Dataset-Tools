**Diffusion-Pipe_Dataset_Folder_Bucket_Stats.py**\
    Asks user to input a folder location containing video clips or images. Creates a txt file for use in adding 
section 'size_buckets' to your dataset.toml file. It lists every file that was in alphabetical order, 
their dimensions and frames. In the format:


size_buckets = [
    [480, 640, 59],
    [480, 640, 60],
    [480, 640, 60],
    [480, 640, 89],
    [480, 640, 60],
    [480, 640, 60],
    [480, 640, 74],
    [368, 640, 58],
]


**Diffusion-Pipe_Dataset_Folder_Resolution_Stats.py**\
  Asks user to input a folder location containing video clips or images. Creates a txt file for use in adding 
section 'resolutions' to your dataset.toml file. It lists every file that was in alphabetical order, 
their dimensions. In the format:

resolutions = [
    [480, 640],
    [480, 640],
    [480, 640],
    [480, 640],
    [480, 640],
    [480, 640],
    [480, 640],
    [368, 640],
]



**Diffusion-Pipe_Dataset_Folder_Resolution_Stats2.py**\
  Asks user to input a folder location containing video clips or images. Creates a txt file for use in adding 
section 'resolutions' to your dataset.toml file. It lists only the unique resolutions. In the format:


resolutions = [
    [272, 360],
    [368, 640],
    [400, 720],
    [480, 640],
]


**Text_Search_and_Replace.py**\
  Asks user for a folder location of txt files, then asks for a word to search and replace every
instance of in every file with a new word.
 


 **Video_Folder_Stats.py**\
   Asks users to input a folder location of video files and returns a txt file:
 cats-b.mp4, 368x640, 30.00 fps, 58 frames
 kittens6-d.mp4, 272x360, 15.00 fps, 60 frames
