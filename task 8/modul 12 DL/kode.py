!wget --no-check-certificate \
    https:dicodingacademy.blob.core.windows.net/picodiploma/ml_pemula_academy/rockpaperscissors.zip

import zipfile,os
local_zip = 'rockpaperscissors.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('file_extracted')
zip_ref.close()

from sklearn.model_selection import train_test_split
base_dir = 'file_extracted/rockpaperscissors/rps_cv_images'
os.listdir(base_dir)
