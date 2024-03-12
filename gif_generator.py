import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import imageio

# Load the CSV file
df = pd.read_csv('./Outputs/output.csv')

# Determine the size of the matrix
max_x = df['i'].max() + 1
max_y = df['j'].max() + 1

# Initialize a blank matrix
matrix = np.zeros((4, 4))  # hay que cambiarlo para que tome un parametro

# List to hold the in-memory images
images = []

if __name__ == '__main__':

    current_step = 1
    previous_step = 1
    for _, row in df.iterrows():
        matrix[row['i'], row['j']] = 1  # Assuming top-left is (0,0) and bottom-right is (max_y-1, max_x-1)
        # "Paint" the point on the matrix
        if current_step > previous_step:
            # Create the plot
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.imshow(matrix, cmap='Greys', origin='lower')
            ax.axis('off')  # Hide axes

            print(current_step)
            # Instead of saving the image, store it in a buffer (in-memory)
            fig.canvas.draw()  # Draw the figure so we can capture it
            image = np.frombuffer(fig.canvas.buffer_rgba(), dtype='uint8')
            image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

            images.append(image)
            plt.close()

            previous_step = current_step
            matrix = np.zeros((4, 4))
        else:
            current_step = row['step']

    imageio.mimsave('my_animation.gif', images, fps=2)  # fps controls the speed of the animation
