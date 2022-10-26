from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np

digits = load_digits()
print(digits.images.shape)

# # Plot 16 random images
# # Get some random ids
# ids = np.random.randint(0, len(digits.images), 16)

# fig, ax = plt.subplots(4, 4, figsize=(1.5, 1.5))
# for i, a in enumerate(ax.ravel()):
#     a.imshow(digits.images[ids[i]], cmap='gray')
#     a.axis('off')
# plt.show()

tsne = TSNE(n_components=2, random_state=0).fit_transform(digits.data)
pca = PCA(n_components=2, random_state=0).fit_transform(digits.data)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].scatter(x=tsne[:, 0], y=tsne[:, 1], c=digits.target, alpha=0.5, s=10)
ax[0].set_xlabel('t-SNE 1')
ax[0].set_ylabel('t-SNE 2')

ax[1].scatter(x=pca[:, 0], y=pca[:, 1], c=digits.target, alpha=0.5, s=10)
ax[1].set_xlabel('PCA 1')
ax[1].set_ylabel('PCA 2')

ids = np.random.randint(0, len(digits.images), 50)
# Plot the corresponding images on top of the tsne
for i in ids:
    x, y = tsne[i, 0], tsne[i, 1]
    inset = ax[0].inset_axes([x, y, 6, 6], transform=ax[0].transData)
    inset.axis('off')
    inset.imshow(digits.images[i], cmap='gray')

plt.show()