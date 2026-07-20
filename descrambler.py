import cv2
import numpy as np


def decrypt():

    # Load Saved Complex FFT Data
    scrambled_freq = np.load("scrambled_freq.npy")

    # Load Phase Mask
    random_phase = np.load("phase_mask.npy")

    # Undo Scrambling
    restored_freq = scrambled_freq / random_phase

    # Inverse Fast Fourier Transform (IFFT)
    inverse_shift = np.fft.ifftshift(restored_freq)

    complex_image = np.fft.ifft2(inverse_shift)

    # Convert Back To Real Image
    real_image = np.real(complex_image)

    normalized_image = cv2.normalize(
        real_image,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    ).astype(np.uint8)

    cv2.imwrite("restored.png", normalized_image)

    print("Decryption complete.")
