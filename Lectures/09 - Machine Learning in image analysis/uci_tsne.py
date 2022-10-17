from sklearn.datasets import load_digits
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np

digits = load_digits()
print(digits.images.shape)

# # Plot 16 random images
# # Get some random ids
ids = np.random.randint(0, len(digits.images), 16)

fig, ax = plt.subplots(4, 4, figsize=(1.5, 1.5))
for i, a in enumerate(ax.ravel()):
    a.imshow(digits.images[ids[i]], cmap='gray')
    a.axis('off')
plt.show()

tsne = TSNE(n_components=2, random_state=0).fit_transform(digits.data)

# Plot the result, color by digit
fig, ax = plt.subplots(figsize=(6, 6))

ax.scatter(x=tsne[:, 0], y=tsne[:, 1], c=digits.target, alpha=0.5, s=10)
ax.set_xlabel('t-SNE 1')
ax.set_ylabel('t-SNE 2')

# Write the labels of 100 random digits on the plot
ids = np.random.randint(0, len(digits.images), 100)

for i in ids:
    ax.text(tsne[i, 0], tsne[i, 1], str(digits.target[i]), color='black', fontsize=10)

plt.show()

