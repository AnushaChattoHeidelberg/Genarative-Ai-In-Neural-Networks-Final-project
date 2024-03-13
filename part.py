import nibabel as nib

# Load a NIfTI file (example4d.nii.gz)
example_ni1 = 'patient101_frame01_gt.nii.gz'
n1_img = nib.load(example_ni1)

# Access the image data (3D or 4D)
image_data = n1_img.get_fdata()

# Check the shape, data type, and affine matrix
print("Image shape:", image_data.shape)
print("Data type:", image_data.dtype)
print("Affine matrix:\n", n1_img.affine)

import matplotlib.pyplot as plt

# Display a slice from the 3D image
slice_index = 50
plt.imshow(image_data[:, :, slice_index], cmap='gray')
plt.title(f"Slice {slice_index}")
plt.show()
