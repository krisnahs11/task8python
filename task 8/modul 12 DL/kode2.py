import tensorflow as tf 
model= tf.keras.models.sequential([
    tf.keras,layers.Conv2D(16, (3,3), activation='relu', input_shape=(100,150,3)),
    tf.keras,layers.MaxPolling2D(2,2),
    tf.keras,layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras,layers.MaxPolling2D(2,2),
    tf.keras,layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras,layers.MaxPolling2D(2,2),
    tf.keras,layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras,layers.MaxPolling2D(2,2),
    tf.keras,layers.Flattern(),
    tf.keras,layers.Dense(512, activation='relu'),
    tf.keras,layers.Dense(3, activation='softmax')
])

model.compile(loss-'categorical_crossentropy',optimizer=tf.optimizers.Adam(),metrics=['accuracy'])

model.fit(train_generator, steps_per_epoch=16, epochs=15, validation_data=validation_spilt, validation_steps=4, verbose=2)