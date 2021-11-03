import av
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray, label2rgb
from skimage.morphology import label, remove_small_objects
from skimage.measure import regionprops_table
import pandas as pd

# Open the video
container = av.open("Mice_short.mp4")
# Extract video stream
video = container.streams.video[0]
# Decode video frames
frames = container.decode(video)

# The column names for our DataFrame
column_names=['centroid_y', 'centroid_x', 'mouse_id', 'frame']
centroids = pd.DataFrame(columns=column_names)

# If True, recalculate centroids, otherwise read from file
recalculate = False

if recalculate:
    # Iterate through frames
    for i, f in enumerate(frames):
        # Convert to Numpy
        f = np.array(f.to_image())

        # Convert to grayscale
        im_gray = rgb2gray(f)
        # Invert and threshold
        im_inverted = 1.0-im_gray
        im_thresh = im_inverted > 0.8
        # Remove small objects left over from thresholding
        im_thresh = remove_small_objects(im_thresh, min_size=100)
        # Label connected pixels
        labels = label(im_thresh)
        # Find centroid and label of each object
        c = pd.DataFrame(regionprops_table(labels, properties=['centroid', 'label']))
        # Add frame number to row
        c['frame'] = i
        # Rename the columns to match our DataFrame
        c.columns = column_names
        # Append to our DataFrame
        centroids = centroids.append(c)

    # Save centroids to CSV
    centroids.to_csv('centroids.csv', index=False)
else:
    # Read centroids from CSV
    centroids = pd.read_csv('centroids.csv')

colors = centroids['mouse_id'].values
plt.scatter(x=centroids['centroid_x'], y=centroids['centroid_y'], c = colors, s=1)
plt.gca().invert_yaxis()
plt.show()

