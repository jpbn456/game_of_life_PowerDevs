import json
import argparse

# Specify the number of cells you want
m = 4  # Change this to your desired number of cells
n = 4
alive_cells = []
output = ''
input = ''
model_name = ''


def initialize_pdm():
    global m, n
    # Initial part of the file
    return """Coupled
    {
    Type = Root
    Name = proyecto_simulacion
    Ports = 0; 0
    Description = 
    Graphic
        {
        Position = 0; 0
        Dimension = 600; 600
        Direction = Right
        Color = 15
        Icon = 
        Window = 5000; 5000; 5000; 5000
        }
    Parameters
        {
        }
    System
        {"""


x_controller = -2000
y_controller = 45
atoms_size = 200


def define_controller():
    global m, n
    # Adding controller
    return f"""    
        Atomic
            {{
            Name = Controller
            Ports = 1 ; 1
            Path = celulas/controller.h
            Description = Atomic DEVS model
            Graphic
                {{
                Position = {x_controller} ; {y_controller}
                Dimension = {atoms_size} ; {atoms_size}
                Direction = Right
                Color = 15
                Icon = None
                }}
            Parameters
                {{
                N = Str; {n}; cell id
                M = Str; {m}; value of the cell. 1 = on 0 = off
                output = Str; {output}; model output
                }}
            }}"""


x_cells = -16000
y_cells = -2010


# cells_amount #start in 2 because "1" is controller
def define_cells():
    global m, n
    # Generating cells
    pdm_content = ""
    cells_amount = 2
    for i in range(m):
        for j in range(n):
            pdm_content += define_single_cell(i, j, cells_amount)
            cells_amount += 1
    return pdm_content


def define_single_cell(x, y, cell_id):
    global m, n
    return f"""
        Atomic
            {{
            Name = Cell_{x}_{y}
            Ports = 1 ; 1
            Path = celulas/celula.h
            Description = Atomic DEVS model
            Graphic
                {{
                Position = {x_cells + (atoms_size + 200) * x} ; {y_cells + (atoms_size + 200) * y}  // Adjust position as needed
                Dimension = {atoms_size} ; {atoms_size}
                Direction = Right
                Color = 15
                Icon = None
                }}
            Parameters
                {{
                x_pos = Str;{x}; Cell Identity Number, Position x
                y_pos = Str;{y}; Cell Identity Number, Position y
                Alive = Str;{define_alive_status(x, y)}; Cell alive status
                }}
            }}"""


def define_alive_status(x, y):
    global m, n
    return 1 if (x, y) in alive_cells else 0


def define_lines():
    global m, n
    # Generating cells
    pdm_content = ""
    cells_amount = 2
    for i in range(m):
        for j in range(n):
            pdm_content += define_single_line(i, j, cells_amount)
            cells_amount += 1
    return pdm_content


def define_single_line(x, y, cell_id):
    global m, n
    return f"""
        Line
            {{
            Source = Cmp ;  {cell_id} ;  1 ; 0
            Sink = Cmp ;  1 ;  1 ; -1
            PointX = {x_cells + (atoms_size + 200) * x + atoms_size}; {x_controller}
            PointY = {y_cells + (atoms_size + 200) * y + atoms_size // 2} ; {y_controller + atoms_size // 2} 
            }}
        Line
            {{
            Source = Cmp ; 1 ;  1 ; {0}
            Sink = Cmp ; {cell_id} ;  1 ; -1
            PointX = {x_controller + atoms_size}; {x_cells + (atoms_size + 200) * x}
            PointY = {y_controller + atoms_size // 2} ; {y_cells + (atoms_size + 200) * y + atoms_size // 2} 
            }}"""


def generate_pdm_file():
    global m, n
    pdm_content = initialize_pdm()
    pdm_content += define_controller()
    pdm_content += define_cells()
    pdm_content += define_lines()
    # Write to a .pdm file
    pdm_content += """
        }
    }"""
    with open("models/" + input, 'w') as file:
        file.write(pdm_content)


def read_cfg(json_file):
    global m, n, output, input, model_name
    with open(json_file) as file:
        data = json.load(file)

    m = data['basic']['m']
    n = data['basic']['n']

    model_name = data['model_name']
    output = model_name + ".csv"
    input = model_name + ".pdm"
    for cell in data['alive_cells']:
        x = cell['x']
        y = cell['y']
        if x >= m or y >= n:
            raise ValueError("Wrong imput value")
        alive_cells.append((x, y))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create PDM file")
    parser.add_argument("json_cfg_path", help="Path to the cfg.json file.")
    args = parser.parse_args()
    read_cfg(args.json_cfg_path)
    generate_pdm_file()
