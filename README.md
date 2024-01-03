# image-denoising-with-salt-and-pepper-noise

Salt-and-pepper noise is a distinct type of image noise where only a few pixels, randomly distributed, are heavily degraded, appearing either completely black (salt) or white (pepper). This program involves contaminating a clean, gray-valued image with salt-and-pepper noise and subsequently denoising the degraded image using a median filter.

**Functions** <br />

**salt_n_pepper(img, p)** <br />
This function takes an image and a probability parameter p, representing the likelihood of a pixel becoming salt/pepper. It returns a degraded version of the input image with salt-and-pepper noise. If the input is a colored image, only the red channel is kept for simplicity.

**median_filter(img, W)** <br />
The median_filter function takes a noisy 2D image and applies median filtering to it. The additional parameter W determines the width of the neighborhood window around each pixel. The function handles pixels close to the borders appropriately, considering asymmetric and non-square neighborhood windows when necessary.

**Usage** <br />

To test the functions, an image is loaded, and the salt_n_pepper function is called with different probabilities p to generate various noise levels. The denoising process is then performed using the median_filter function.

**Libraries Used:** <br />

numpy <br />
matplotlib.pyplot
