from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255, rotation_range= 20, horozontal_flip=True,
shear_range = 0.2, zoom_range = 0.2, validation_spilt = 0.4, fill_mode = 'wrap')

train_generator = train_datagen.flow_from_directory( base_dir, target_size =(100,150),
shuffle=True, subset='training')

validaton_generator= train_datagen.flow_from_directory( base_dir, target_size=(100,150),
subset='validation')