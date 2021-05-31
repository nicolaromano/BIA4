# Biomedical Image Analysis 4 - Course plan

This is an outline of the course.

Workshops happen in class - after a brief introduction from the instructor students will go through the workshop by themselves either alone or in groups.

## Weekly structure

### Pre-course material

A selection of pre-course material will be made available for all students before the course.

These will include general Python introductory exercises, links to courses etc. **not** related to image analysis.

### Week 1 (w/b 13 September 2020)

_Introduction to image analysis._

#### Lecture 1.1

**Learning objectives:**

- Give examples of problems in image analysis.
- Describe situations where Python is useful for image analysis.
- List and descibe common Python libraries used in image analysis.

**Indicative content:**

- Introduction to the course structure and ICAs
- What is image analysis and what can we use it for
- The rationale for using Python - not as an absolute substitute for existing pieces of software
- Very cursory introduction (1-2 slides, to be used as a reference) to the tools we will be using
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

_Filters and features - week 1._

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

_Filters and features - week 2._

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

_Filters and features - week 3._

#### Lecture 5.1

**Learning objectives:**

- Describe and apply methods for detection of shapes in an image
- Describe and apply methods for particle detection
- Discuss advantages and issues with these methods

**Indicative content:**

- The Hough transform to detect lines or circles
- Particle detection (Difference of Gaussians, Laplacian of Gaussians, etc.)

**Suggested reading:**

#### ICA introductory session

**Indicative content:**

- Release of groups on Learn
- Overview of tasks (for both ICAs) and marking criteria
- Examples of possible projects
- Writing good documentation
- Suggested timeline for project

### Week 6 (Week beginning 18 October)

_Tracking._

#### Lecture 6.1

**Learning objectives:**

- Discuss the issues related to analysis of multidimensional datasets
- Describe common tracing algorithms
- Implement them in Python

**Indicative content:**

- Problems associated with analysing multidimensional datasets – stacks and videos
- Tracing algorithms (vessels, neurites, cell processes)

#### Lecture 6.2

**Learning objectives:**

- Discuss issues with tracking objects/particles in videos
- Describe common tracking algorithms
- Implement them in Python

**Indicative content:**

- Registration algorithms
- Tracking algorithms

#### Workshop 6

**Learning objectives:**

**Indicative content:**

Video registration / Particle tracking / Tracing?

### Week 7 (Week beginning 25 October)

_Segmentation._

#### Lecture 7.1

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

#### Lecture 7.2

- Something else on segmentation (TBD)

#### Workshop 7

**Learning objectives:**

**Indicative content:**

Segmantation of cells

### Week 8 (Week beginning 1 November)

_Traditional ML approaches in image analysis._

#### Lecture 8.1

**Learning objectives:**

**Indicative content:**

- Recap of ML terminology (training, validation and test set, loss function, etc)
- Trainable (random forest) segmentation
- Image classification using SVM or logistic regression

#### Lecture 8.2

**Learning objectives:**

- Describe the basic structure of an ANN
- Describe how (multi-layer) perceptrons (MLPs) work
- Discuss pros and cons of various types of activation functions
- Discuss the limitations of MLPs

**Indicative content:**

- Introduction to (shallow) neural networks
- The perceptron
- Multilayer perceptron and hidden layers
- Activation functions
- Gradient descent

#### Workshop 8

### Week 9 (Week beginning 8 November)

_Convolutional neural networks (CNNs)._

#### Lecture 9.1

- Deep networks
- General structure
- An overview of how a CNN "learns" features
- Types of network layers

#### Lecture 9.2

- Introduction to Keras and Tensorflow
- Building a simple CNN with Keras

#### Project discussion session groups 1-4

**Idea:** we are going to briefly go through the project each group is developing and discuss how they can improve on that (30 min/group)

### Week 10 (Week beginning 15 November)

_CNNs architectures._

#### Lecture 10.1

**Learning objectives:**

**Indicative content:**

- Transfer learning 
- Common CNN architectures
- AlexNet
- LeNet
- U-Net
- Inception

#### Lecture 10.2

**Learning objectives:**

**Indicative content:**

- CNN for cell segmentation in 2D and 3D
- More on U-Net
- StarDist
- YOLO

#### Project discussion session groups 5-9

**Idea:** we are going to briefly go through the project each group is developing and discuss how they can improve on that (30 min/group)

**Learning objectives:**

### Week 11 (Week beginning 22 November)

_Practical aspects of using CNNs._

#### Lecture 11.1

**Learning objectives:**

- Define hyperparameters and discuss why their choice is important
- Discuss different strategies for hyperparameter optimization

**Indicative content:**

- Hyperparameters optimization
- What are hyperparameters?
- Search strategies (Grid, HyperBand, Bayesian)
- AutoKeras

#### Lecture 11.2

**Learning objectives:**

- Describe the concept of data augmentation and discuss why it is needed
- Strategies for data augmentation in image analysis

**Indicative content:**

- Data augmentation

#### Workshop 11

Classification with CNN

**Learning objectives:**

### Week 12 (Week beginning 29 November)

_Autoencoders._

#### Lecture 12.1

**Learning objectives:**

**Indicative content:**

- What are autoencoders?
- Applications of autoencoders (denoising, anomaly detection, domain adaptation)
- Latent space

#### Lecture 12.2

**Indicative content:**

- Analysis of recent papers

#### Workshop 12

Autoencoders

**Learning objectives:**

### Week 13 (Week beginning 6 December)

_Recent topics in image analysis._

- Lecture 13.1

**Indicative content:**

Analysis of recent papers

- Lecture 13.2

**Indicative content:**

Analysis of recent papers

### Week 14 (Week beginning 13 December)

_No lectures._

- Time reserved for the finalization of the ICAs

**SUBMISSION ICA 1 - Wednesday 15 December 12 noon.**

**SUBMISSION ICA 2 - Wednesday 22 December 12 noon.**

END OF COURSE
