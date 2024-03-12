import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import imageio

# Load the CSV file
df = pd.read_csv('./Outputs/output.csv')

# Determine the size of the matrix
max_x = 4#df['i'].max() + 1
max_y = 4#df['j'].max() + 1

# Initialize a blank matrix
matrix = np.zeros((4, 4))  # hay que cambiarlo para que tome un parametro

# List to hold the in-memory images
images = []

def new_matrix():
    # Show grid lines and set minor ticks to visually separate cells
    ax.grid(which='major', color='black', linestyle='-', linewidth=2)
    ax.set_xticks(np.arange(-.5, max_x, 1), minor=True)
    ax.set_yticks(np.arange(-.5, max_y, 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=1)

    # To show x and y positions (coordinates) on the axes
    ax.set_xticks(np.arange(0, max_x, 1))
    ax.set_yticks(np.arange(0, max_y, 1))
    ax.set_xticklabels(np.arange(0, max_x, 1))
    ax.set_yticklabels(np.arange(0, max_y, 1))

    # Hide the frame
    ax.set_frame_on(False)

if __name__ == '__main__':

    current_step = 1
    previous_step = 1
    for _, row in df.iterrows():
        # "Paint" the point on the matrix
        current_step = row['step']
        if current_step > previous_step:
            # Create the plot
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.imshow(matrix, cmap='Greys', origin='lower')
            # ax.axis('on')  # Hide axes
            
            # Display the matrix; setting 'edgecolor' to visualize grid lines
            c = ax.pcolormesh(matrix, cmap='Greys', edgecolor='k')

            # Set the ticks to align with each cell
            ax.set_xticks(np.arange(max_x + 1))
            ax.set_yticks(np.arange(max_y + 1))

            # Set tick labels to show positions
            ax.set_xticklabels(np.arange(max_x + 1))
            ax.set_yticklabels(np.arange(max_y + 1))

            # Display grid
            ax.grid(True, which='both', color='k', linewidth=2)

            # Set limits to ensure the plot displays whole cells around the edges
            ax.set_xlim(0, max_x)
            ax.set_ylim(0, max_y)

            ax.invert_yaxis()  # Invert y-axis to match matrix representation

    
            # # Show grid lines and set minor ticks to visually separate cells
            # ax.grid(which='major', color='black', linestyle='-', linewidth=2)
            # ax.set_xticks(np.arange(-.5, max_x+1, 1), minor=True)
            # ax.set_yticks(np.arange(-.5, max_y+1, 1), minor=True)
            # ax.grid(which='minor', color='black', linestyle='-', linewidth=1)

            # To show x and y positions (coordinates) on the axes
            # ax.set_xticks(np.arange(0, max_x, 1))
            # ax.set_yticks(np.arange(0, max_y, 1))
            # ax.set_xticklabels(np.arange(0, max_x, 1))
            # ax.set_yticklabels(np.arange(0, max_y, 1))

            # # Hide the frame
            # ax.set_frame_on(False)





            # Instead of saving the image, store it in a buffer (in-memory)
            fig.canvas.draw()  # Draw the figure so we can capture it
            image = np.frombuffer(fig.canvas.buffer_rgba(), dtype='uint8')
            image = image.reshape(fig.canvas.get_width_height()[::-1] + (4,))

            images.append(image)
            plt.close()

            matrix = np.zeros((4, 4))

        matrix[row['i'], row['j']] = 1  # Assuming top-left is (0,0) and bottom-right is (max_y-1, max_x-1)
        previous_step = current_step
    imageio.mimsave('my_animation.gif', images, fps=2)  # fps controls the speed of the animation
