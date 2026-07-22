import cv2
import numpy as np


def encrypt():
    image = cv2.imread("Image.png", cv2.IMREAD_GRAYSCALE)

    if image is None:
        raise ValueError("Could not load image.")

    # Fast Fourier Transform (FFT)
    fourier_transform = np.fft.fft2(image)
    fourier_shift = np.fft.fftshift(fourier_transform)

    rows, cols = image.shape

    # Random Phase Mask
    random_phase = np.exp(
        1j * np.random.uniform(0, 2 * np.pi, (rows, cols))
    )

    # Scramble
    scrambled_freq = fourier_shift * random_phase

    # Save Complex Data
    np.save("scrambled_freq.npy", scrambled_freq)

    # Save Phase Mask
    np.save("phase_mask.npy", random_phase)

    # Visualization
    magnitude_log = np.log(
        1 + np.abs(scrambled_freq)
    )

    magnitude = cv2.normalize(
        magnitude_log,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    ).astype(np.uint8)

    cv2.imwrite("scrambled_visual.png", magnitude)

    print("Encryption complete.")
