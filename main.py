import os
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

# Function to generate and save spectrogram
def save_spectrogram(audio_path):
    # Load audio file
    y, sr = librosa.load(audio_path)
    
    # Generate spectrogram
    D = np.abs(librosa.stft(y))
    S = librosa.amplitude_to_db(D, ref=np.max)
    
    # Plot spectrogram
    plt.figure(figsize=(12, 8))
    librosa.display.specshow(S, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')
    plt.tight_layout()
    
    # Save spectrogram in the same folder as the audio file
    spectrogram_path = os.path.splitext(audio_path)[0] + '.png'
    plt.savefig(spectrogram_path)
    plt.close()

# Path to the folder containing subfolders with audio files
folder_path = r'path_to_folder'

# Iterate over each subfolder
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.ogg'):  # Assuming audio files are in .ogg format
            audio_path = os.path.join(root, file)
            save_spectrogram(audio_path)
            # Free up memory by closing the plots
            plt.close('all')
    print(f"Spectrograms saved for {root}")
