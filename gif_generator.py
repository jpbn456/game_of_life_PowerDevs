import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import imageio
import argparse
import json


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

def blank_matrix(matrix, m, n):
    for i  in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                return False
    return True

def equals_matrix(matrix_1, matrix_2, m, n):
    for i  in range(m):
        for j in range(n):
            if matrix_1[i][j] != matrix_2[i][j]:
                return False
    return True

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Generate Gif from json file")
    parser.add_argument("json_cfg_path", help="Path to the cfg.json file.")
    parser.add_argument("csv_path", help="Path to the csv file.")
    args = parser.parse_args()

    df = pd.read_csv(args.csv_path)
    with open(args.json_cfg_path, 'r') as file:
        data = json.load(file)
    file_name = data['model_name']
    max_x = data['basic']['m']
    max_y = data['basic']['n']
    matrix = np.zeros((max_x, max_y))

    images = []

    current_step = 1
    previous_step = 1
    for _, row in df.iterrows():
        # "Paint" the point on the matrix
        current_step = row['step']
        # print(current_step)
        if current_step > previous_step:
            # Create the plot
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.imshow(matrix, cmap='Greys', origin='lower')
            # ax.axis('on')  # Hide axes
            
            # Display the matrix; setting 'edge color' to visualize grid lines
            c = ax.pcolormesh(matrix, cmap='Greys', edgecolor='k')

            ax.set_title(f'Step: {previous_step}')

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

            # Instead of saving the image, store it in a buffer (in-memory)
            fig.canvas.draw()
            image = np.frombuffer(fig.canvas.buffer_rgba(), dtype='uint8')
            image = image.reshape(fig.canvas.get_width_height()[::-1] + (4,))

            images.append(image)
            plt.close()
            
            if (len(images) > 1 and equals_matrix(prev_matrix, matrix, max_x, max_y)) or blank_matrix(matrix, max_x, max_y):
                break
            prev_matrix = matrix
            matrix = np.zeros((max_x, max_y))
        matrix[row['i'], row['j']] = 1  # Assuming top-left is (0,0) and bottom-right is (max_y-1, max_x-1)
        previous_step = current_step
    imageio.mimsave(f'./animations/{file_name}.gif', images, fps=1)  # fps controls the speed of the animation
