import numpy as np
import matplotlib.pyplot as plt

def salt_n_pepper(img, p):
    '''
    returns an image contaminated with salt-and-pepper noise 
    '''

    # converting image to grayscale (using the red channel for simplicity)
    gray_img = img[:, :, 0]

    # creating a random matrix with the same shape as the grayscale image 
    random_matrix = np.random.rand(*gray_img.shape)

    # creating masks for salt and pepper based on the random matrix and probability
    salt_mask = (random_matrix < p/2)
    pepper_mask = (random_matrix > 1 - p/2)

    # creaitng a copy of the grayscale image for adding noise 
    noisy_img = gray_img.copy()

    # appplying salt and pepper noise to the image 
    noisy_img[salt_mask] = 0
    noisy_img[pepper_mask] = 255

    # stacking the noisy channel back to the original image to get the colored noisy image 
    noisy_img_colored = np.stack([noisy_img] * 3, axis=-1)

    return noisy_img_colored

def median_filter(img, W):
    '''
    applies median filtering on a noisy image  
    '''

    # get the shape of the image 
    rows, cols, _ = img.shape

    # creating an empty array for the filtered image 
    filtered_img = np.zeros_like(img)

    # iterating over each channel in the image
    for channel in range(img.shape[2]):
        # iterating over each pixel in the image 
        for i in range(rows):
            for j in range(cols):
                # defining the neighborhood window for the current pixel
                start_row = max(0, i - W // 2)
                end_row = min(rows, i + W // 2 + 1)
                start_col = max(0, j - W // 2)
                end_col = min(cols, j + W // 2 + 1)

                # extracting the neighborhood window 
                neighborhood = img[start_row:end_row, start_col:end_col, channel].flatten()

                # applying median filter to the pixel
                filtered_img[i, j, channel] = np.median(neighborhood)

    return filtered_img

# loading the image 
img = plt.imread("Depaul.jpg")

# setting the desired probability and window size
p = 0.5
W = 5

# creating a figure for the specified probability and window size
plt.figure(figsize=(15,5))

# original image
plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title('Original')

# noisy image 
noise_img = salt_n_pepper(img,p)
plt.subplot(1, 3, 2)
plt.imshow(noise_img)
plt.title(f'Noisy (p={p})')

# denoised image
denoised_img = median_filter(noise_img, W)
plt.subplot(1, 3, 3)
plt.imshow(denoised_img)
plt.title(f'Denoised (p={p}, W={W})')

plt.tight_layout()
plt.show()
