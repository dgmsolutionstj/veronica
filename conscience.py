import tensorflow
from keras.layers import Input, Dense
from keras.models import Model

def create_autoencoder(input_size, encoding_dim):
    # Input layer
    input_data = Input(shape=(input_size,))
    
    # Encoding layer
    encoded = Dense(encoding_dim, activation='relu')(input_data)
    
    # Decoding layer
    decoded = Dense(input_size, activation='sigmoid')(encoded)
    
    # Autoencoder model
    autoencoder = Model(input_data, decoded)
    
    # Encoder model (for feature extraction)
    encoder = Model(input_data, encoded)
    
    # Compile the autoencoder
    autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

    return autoencoder, encoder

def train_autoencoder(autoencoder, data, epochs=50, batch_size=32):
    autoencoder.fit(data, data, epochs=epochs, batch_size=batch_size, shuffle=True)

# Example usage
if __name__ == "__main__":
    # Replace these values with the size of your input data and desired encoding dimension
    input_size = 100
    encoding_dim = 10

    # Create autoencoder
    autoencoder, encoder = create_autoencoder(input_size, encoding_dim)

    # Replace 'data' with your actual input data for training
    data = ...  # Your input data here

    # Train the autoencoder
    train_autoencoder(autoencoder, data)
