# Biomedical Image Analysis 4 - Course plan

This is an outline of the course.

Workshops happen in class - after a brief introduction from the instructor students will go through the workshop by themselves either alone or in groups.

## Weekly structure

### Pre-course material

A selection of pre-course material will be made available for all students before the course.

These will include general Python introductory exercises, links to courses etc. **not** related to image analysis.

### Week 1 (w/b 13 September 2020)

Basics of image analysis.

#### Lecture 1.1

**Learning objectives:**

- Give examples of problems in image analysis.
- Describe situations where Python is useful for image analysis.
- List and descibe common Python libraries used in image analysis.

**Indicative content:**

- Introduction to the course. Course structure and ICAs
- What is image analysis and what can we use it for
- The rationale for using Python - not as an absolute substitute for existing pieces of software
- Very cursory introduction (1-2 slides, to be used as a reference) to the tools we will be using (e.g. Scikit Image, OpenCV, Numpy, Pandas, Matplotlib, Napari, Scikit-Learn, Keras, ...)
- Imaging methods - Light microscopy, fluorescence, confocal, electron microscopy, X-ray, MRI, etc. and associated challenges
- Examples of problems to be solved in image analysis

#### Lecture 1.2

**Learning objectives:**

- Describe images as multidimensional arrays
- Manipulate images using Python (Numpy)

**Indicative content:**

- Images as multidimensional arrays (tensors)
- Image visualization - 2D and 3D
- Colour spaces, colour palettes, LUTs
- Basic image manipulation
  - Image cropping and scaling in 2D and 3D
  - Image histograms and their manipulations

**Further reading:**

- Harris et al. [Array programming with Numpy](https://www.nature.com/articles/s41586-020-2649-2) - *Nature*, 2020

#### Workshop 1 - Image manipulation and visualization

**Learning objectives:**

- Open and visualize images using Python
- Crop, rotate, scale images
- Save modified images
- Plot and manipulate image histograms
- Visualize videos/3D stacks/multidimensional images

### Week 2 (week beginning 20 September)

Filters and features.

*Monday 20 and Tuesday 21 holiday.*

#### Lecture 2.1

**Learning objectives:**

- Define and give examples of image features
- Explain their use in image analysis
- Define image filters and their use

**Indicative content:**

- Image features - what they are, how do we use them
- Definition of filters and related terminology (convolution, kernel size, stride, edge behaviour)
- Use cases - improving images, detecting structures of interest in images
- Traditional vs "modern" usage of filters in machine learning (more on that later in the course)
- Examples of filters
  - Non convolutional filters (mean/median/max (erosion)/min (dilation))
  - Convolutional filters (Gaussian, Sobel)

### Week 3 (week beginning 27 September)

*Friday 1 October holiday.*

#### Lecture 3.1

**Learning objectives:**

**Indicative content:**

- Image featurization
- Detecting edges (Sobel, Canny)
- Detecting corners (Harris, Shi-Tomasi)
- Texture features (Entropy, GLCM features)
- Other (SIFT and DAISY descriptors)

#### Workshop 3 - Featurization

**Learning objectives:**

- Use Python to detect edges and corners in an image
- Use Python to extract texture features from an image

### Week 4 (week beginning 4 October)

_Holiday week, no lectures!_

### Week 5 (week beginning 11 October)

Shape detection in images

#### Lecture 5.1

**Learning objectives:**

- Define the different types of segmentation
- Describe common algorithms to segment images
- Explain the challenges of segmentation

**Indicative content:**

- The Hough transform
  - Detecting lines
  - Detecting circles
  
#### ICA introductory session

**Indicative content:**

- Release of groups on Learn
- Overview of tasks (for both ICAs) and marking criteria
- Examples of possible projects
- Writing good documentation
- Suggested timeline for project

### Week 6 (Week beginning 18 October)

Segmentation

#### Lecture 6.1

**Learning objectives:**

- Define the different types of segmentation
- Describe common algorithms to segment images
- Explain the challenges of segmentation

**Indicative content:**

- Semantic vs instance segmentation
- Common issues in segmentation
- Thresholding methods (Otsu, multi-Otsu, local thresholding)
- Edge based segmentation
- k-means segmentation
- Watershed

#### Lecture 6.2
_Traditional_ ML approaches in image analysis

- Trainable (random forest) segmentation
- Image classification using SVM

#### Workshop 6

### Week 7 (Week beginning 25 October)

#### Lecture 7.1
#### Lecture 7.2

#### Workshop 7

### Week 8 (Week beginning 1 November)

#### Lecture 8.1
#### Lecture 8.2

#### Project discussion session groups 1-4

**Idea:** we are going to briefly go through the project each group is developing and discuss how they can improve on that (30 min/group)

### Week 9 (Week beginning 8 November)

#### Lecture 9.1
#### Lecture 9.2

#### Project discussion session groups 5-9

**Idea:** we are going to briefly go through the project each group is developing and discuss how they can improve on that (30 min/group)

### Week 10 (Week beginning 15 November)

#### Lecture 10.1
#### Lecture 10.2
#### Workshop 10

### Week 11 (Week beginning 22 November)

#### Lecture 11.1
#### Lecture 11.2
#### Workshop 11

### Week 12 (Week beginning 29 November)

#### Lecture 12.1
#### Lecture 12.2
#### Workshop 12

**SUBMISSION ICA 1 - Wednesday 8 December 12 noon.**

### Week 13 (Week beginning 6 December)

- Lecture 13.1
- Lecture 13.2

### Week 14 (Week beginning 13 December)

- Lecture 14.1

**SUBMISSION ICA 2 - Wednesday 22 December 12 noon.**

END OF COURSE
