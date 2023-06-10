import cv2
import matplotlib.pyplot as plt

# Load citra
img = cv2.imread('Saitama.jpg', 0)

# Aplikasikan Gaussian
blur = cv2.GaussianBlur(img, (3, 3), 0)

# Aplikasikan Laplacian
laplacian = cv2.Laplacian(blur, cv2.CV_64F)
laplacian1 = laplacian / laplacian.max()

cv2.imshow('laplacian-gaussian', laplacian1)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(laplacian1, cmap='gray')
plt.show()
