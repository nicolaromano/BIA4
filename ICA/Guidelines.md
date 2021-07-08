# Biomedical Imaging Analysis 4 ICA

For this ICA, you should work in a group to create a piece of software to perform an image analysis task of your choice. You should choose one of the datasets listed below to test your software, and write a brief report on your analysis.

The software should be functional and well documented to make it easy for someone with basic programming knowledge (and markers!) to use it.

## Q&A

- **Which programming language should we use?**

    Although we ask that you write the central part of the software in Python, you can also use any language of your choice (e.g. R) to perform further analysis, draw graphs for your report etc.

    All code should be accessible through GitHub. Although we will only mark the final version, we strongly encourage you to use GitHub as a version control system rather than just using it to save your final version. If you are unsure about how to use it, have a look at this [guide to GitHub](https://guides.github.com/activities/hello-world/)!

- **Can we use pre-existent software (e.g. FIJI)?**

    In a "real-life situation", there would be no issue in using FIJI or any other pre-written software to perform a task; for this ICA we ask that you develop your own piece of software using Python.

    There are, however, exceptions. For example, you can use pre-existing software to show that your software performs as expected; you can check that the output from the two software match (or that your is better by some meaningful metric!). Or you can use another software to prepare your data in some way. If in doubt, please ask!

- **The task we want to achieve has not been mentioned in the lectures**

    Unfortunately, the course cannot cover all possible topics and techniques related to image analysis. Some of the techniques that you may end up using may be fairly new. We encourage you to explore the literature and try new approaches out independently. However, we would like to stress that **there is no requirement for using cutting-edge technology** and you will be able to get full marks even if you do not. Consider very carefully whether the time and effort needed to implement some complex technique will make a difference.

    **It is better to have a more straightforward but working approach than a complex non-functional one.**

- **Does our software need a GUI (graphical user interface)**

    Depending on what your software does, a GUI can be very helpful! There are many Python packages to create GUIs. [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/) is a good one to look at, but there is no restriction on which ones you can use.

- **How should we write documentation?**

    This is entirely up to you!
    Documentation can be as simple as a PDF, or you could generate a simple website. You can even generate some interactive examples, e.g. by creating Jupyter notebooks. You can include screenshots, videos or whatever you think is necessary. As above, start developing the content first, then you can think about the "form". A fancy website with little information is useless.

- **Can I use a different dataset from those provided?**

    As long as the dataset is publicly available and you clearly state where it can be found, that is absolutely fine.

- **I have some further questions**

    Please, use the Slack channel to ask any further questions

**TODO: focus on example projects rather than datasets**
## The datasets

Below you will find a list of datasets that you can analyse with your software. Each datasets has some "example tasks" that you could choose to perform on the images. These are not compulsory and you can choose to develop a tool to solve any meaningful question.

- ### *Drosophila melanogaster* Wings

    ***DOUBLE CHECK - LINK APPEARS NOT WORKING** (but was checked during Chinese New Year...)*

    *Description*: This dataset contains images of Drosophila wings with various genotypes.

    *Reference*: Sonnenschein et al, 2015 - An Image Database of Drosophila melanogaster Wings for Phenomic and Biometric analysis

    *Available from*: http://gigadb.org/dataset/view/id/100141

    *Data type and size*: ~7 Gb of TIFF (**double check**) files taken at 20x and 40x with different microscopes. 

    *Example tasks*: 
    - automatically detect the wing and identify the genotype of the fly
    - automate measurements of fly wings

- ### Retina scans

    *Description*: This dataset contains images of retina scans from glaucoma positive and negative patients.

    *Available from*: https://www.kaggle.com/sshikamaru/glaucoma-detection

    *Data type and size*: 650 files (~200 Mb) of jpg files. 

    *Example tasks*: 
    - classify images to detect whether glaucoma is present
    - segment blood vessels and determine their properties


